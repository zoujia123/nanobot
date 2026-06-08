# Chinese Markdown Digest Format

Use this format for the default answer.

```markdown
# 最近 N 天 arXiv 论文雷达：<topic>

范围：<categories>，时间：最近 <N> 天  
筛选标准：只保留和 <topic> 直接相关、具有系统贡献的论文。

## 总览

- 抓取候选论文：<candidate_count> 篇
- 筛选相关论文：<relevant_count> 篇
- 主要方向：<top_tags>

## 论文列表

### 1. <paper title>

- 链接：<arxiv link>
- 标签：`serving` `offloading`
- 相关性：一句话说明为什么它属于该主题。
- 中文 TL;DR：用 2-3 句话说明问题、方法和结果。如果摘要没有量化结果，明确写“摘要中未给出量化结果”。

## 值得优先读

1. <title>：一句话理由。
2. <title>：一句话理由。
```

Keep the digest concise. Prefer accurate summaries over broad claims.
