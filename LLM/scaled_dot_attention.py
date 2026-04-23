import torch
import torch.nn.functional as F


def scaled_dot_product_attention(
    query, key, value, attn_mask=None, dropout_p=0.0, is_causal=False
):
    """
    计算缩放点积注意力 (Scaled Dot-Product Attention)

    参数:
        query: 形状为 (..., L_q, d_k) 的张量
        key: 形状为 (..., L_k, d_k) 的张量
        value: 形状为 (..., L_k, d_v) 的张量
        attn_mask: 形状为 (..., L_q, L_k) 的掩码（布尔值或浮点数）
        dropout_p: Dropout 概率
        is_causal: 是否使用因果掩码 (Causal Mask)

    返回:
        output: 注意力计算结果 (..., L_q, d_v)
        attn_weights: 注意力权重矩阵 (..., L_q, L_k)
    """
    # 获取序列长度和缩放因子 d_k (即每个头的维度)
    L_q = query.size(-2)
    L_k = key.size(-2)
    d_k = query.size(-1)

    # 1. 点积 (Dot Product): Q * K^T
    # query 形状: (..., L_q, d_k)
    # key.transpose 形状: (..., d_k, L_k)
    # scores 形状: (..., L_q, L_k)
    scores = torch.matmul(query, key.transpose(-2, -1))

    # 2. 缩放 (Scale): 除以 sqrt(d_k)
    # 这一步是为了防止点积结果过大，导致 Softmax 梯度消失
    scores = scores / torch.sqrt(
        torch.tensor(d_k, dtype=torch.float32, device=query.device)
    )

    # 3. 因果掩码 (Causal Mask) - 用于 GPT 等自回归模型
    if is_causal:
        # 生成下三角矩阵，右上角为 0 (False)，表示不能看到未来的 token
        causal_mask = torch.ones(L_q, L_k, dtype=torch.bool, device=query.device).tril()
        # 将不允许看的位置替换为 负无穷大 (-inf)
        scores = scores.masked_fill(~causal_mask, float("-inf"))

    # 4. 自定义掩码 (Attention Mask) - 用于 Padding 或其他特殊 Mask
    if attn_mask is not None:
        if attn_mask.dtype == torch.bool:
            # 如果传入的是布尔值：True 表示允许关注，False 表示遮蔽
            scores = scores.masked_fill(~attn_mask, float("-inf"))
        else:
            # 如果传入的是浮点数（通常遮蔽处已经是极小值如 -1e9），直接相加
            scores = scores + attn_mask

    # 5. Softmax 归一化，得到注意力权重 (Attention Weights)
    attn_weights = F.softmax(scores, dim=-1)

    # 6. Dropout (仅在 dropout_p > 0 且处于训练状态时需要)
    if dropout_p > 0.0:
        attn_weights = F.dropout(attn_weights, p=dropout_p)

    # 7. 与 Value 相乘: Weights * V
    # attn_weights 形状: (..., L_q, L_k)
    # value 形状: (..., L_k, d_v)
    # output 形状: (..., L_q, d_v)
    output = torch.matmul(attn_weights, value)

    return output, attn_weights


# ================== 测试代码 ==================
if __name__ == "__main__":
    batch_size = 2
    num_heads = 8
    seq_len = 5
    head_dim = 64

    # 随机初始化 Q, K, V
    Q = torch.randn(batch_size, num_heads, seq_len, head_dim)
    K = torch.randn(batch_size, num_heads, seq_len, head_dim)
    V = torch.randn(batch_size, num_heads, seq_len, head_dim)

    # 1. 测试因果注意力 (Causal Attention)
    out_causal, weights_causal = scaled_dot_product_attention(Q, K, V, is_causal=True)
    print("Causal Attention Output Shape:", out_causal.shape)

    # 打印权重矩阵看看是不是下三角矩阵 (右上角应为 0)
    print("Causal Weights (Batch 0, Head 0):\n", weights_causal[0, 0].round(decimals=3))

    # 2. 与 PyTorch 官方 API 的对比
    out_official = F.scaled_dot_product_attention(Q, K, V, is_causal=True)

    # 检查两者结果是否几乎一致
    diff = torch.max(torch.abs(out_causal - out_official))
    print(f"\n与 PyTorch 官方 API 的最大差异: {diff.item():.6e}")
