import torch
import torch.nn as nn
import torch.nn.functional as F


class GroupedQueryAttention(nn.Module):
    def __init__(self, d_model, num_heads, num_kv_heads, dropout=0.0):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads  # Q的头数 (Query heads)
        self.num_kv_heads = num_kv_heads  # K和V的头数 (KV heads)

        # Q的头数必须是KV头数的整数倍
        assert num_heads % num_kv_heads == 0, "num_heads 必须能被 num_kv_heads 整除"

        # 每个 KV 头对应多少个 Q 头 (即分组大小 Group size)
        self.num_queries_per_kv = num_heads // num_kv_heads

        # 每个头的维度
        self.head_dim = d_model // num_heads

        # 定义线性投影层
        self.q_proj = nn.Linear(d_model, num_heads * self.head_dim, bias=False)
        self.k_proj = nn.Linear(d_model, num_kv_heads * self.head_dim, bias=False)
        self.v_proj = nn.Linear(d_model, num_kv_heads * self.head_dim, bias=False)
        self.o_proj = nn.Linear(num_heads * self.head_dim, d_model, bias=False)

        self.dropout = dropout

    def forward(self, x, attention_mask=None, is_causal=False):
        batch_size, seq_len, _ = x.shape

        # 1. 线性投影
        q = self.q_proj(x)  # (B, L, num_heads * head_dim)
        k = self.k_proj(x)  # (B, L, num_kv_heads * head_dim)
        v = self.v_proj(x)  # (B, L, num_kv_heads * head_dim)

        # 2. Reshape 并转置为 (Batch, Heads, Seq_len, Head_dim)
        q = q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        k = k.view(batch_size, seq_len, self.num_kv_heads, self.head_dim).transpose(
            1, 2
        )
        v = v.view(batch_size, seq_len, self.num_kv_heads, self.head_dim).transpose(
            1, 2
        )

        # 3. 复制 K 和 V 的头，使其数量与 Q 的头数对齐
        # K, V 形状变换: (B, num_kv_heads, L, head_dim) -> (B, num_heads, L, head_dim)
        k = self.repeat_kv(k, self.num_queries_per_kv)
        v = self.repeat_kv(v, self.num_queries_per_kv)

        # 4. 计算 Scaled Dot-Product Attention
        # PyTorch 2.0+ 原生支持，如果可用会自动调用 FlashAttention 进行加速
        attn_output = F.scaled_dot_product_attention(
            q,
            k,
            v,
            attn_mask=attention_mask,
            dropout_p=self.dropout if self.training else 0.0,
            is_causal=is_causal,
        )

        # 5. 合并所有的头并输出
        # (B, num_heads, L, head_dim) -> (B, L, num_heads, head_dim)
        attn_output = attn_output.transpose(1, 2).contiguous()

        # (B, L, num_heads, head_dim) -> (B, L, d_model)
        attn_output = attn_output.view(batch_size, seq_len, self.d_model)

        # 输出投影
        out = self.o_proj(attn_output)
        return out

    def repeat_kv(self, x, num_repeats):
        """
        这个函数用于将 K 和 V 的头复制多次，以匹配 Q 的头数。
        输入维度: (batch, num_kv_heads, seq_len, head_dim)
        输出维度: (batch, num_heads, seq_len, head_dim)
        """
        if num_repeats == 1:
            return x

        batch, num_kv_heads, seq_len, head_dim = x.shape

        # 扩展维度: (B, num_kv_heads, 1, L, head_dim)
        # expand 只是创建视图，不消耗额外内存
        x = x[:, :, None, :, :].expand(
            batch, num_kv_heads, num_repeats, seq_len, head_dim
        )

        # 将重复的组展平，合并到 Heads 维度: (B, num_kv_heads * num_repeats, L, head_dim)
        # 也就是 (B, num_heads, L, head_dim)
        return x.reshape(batch, num_kv_heads * num_repeats, seq_len, head_dim)


# ================== 测试代码 ==================
if __name__ == "__main__":
    batch_size = 2
    seq_len = 10
    d_model = 512
    num_heads = 8  # 8个Query头
    num_kv_heads = 2  # 2个KV头 -> 这意味着每 4 个 Q 头共享 1 个 KV 头 (Group Size = 4)

    # 初始化模型
    gqa = GroupedQueryAttention(
        d_model=d_model, num_heads=num_heads, num_kv_heads=num_kv_heads
    )

    # 随机生成输入
    x = torch.randn(batch_size, seq_len, d_model)

    # 前向传播 (Causal模式，常用于GPT这种自回归模型)
    output = gqa(x, is_causal=True)

    print(f"输入形状: {x.shape}")
    print(f"输出形状: {output.shape}")
