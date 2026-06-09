# 🤝 贡献指南

感谢你愿意为 **AI Neural Networks Visualized** 出一份力！这里有 107 篇经典论文的动画 SVG 可视化，欢迎你提建议、修 bug、加新论文。

## 📂 仓库结构

```
.
├── index.html              # 首页（107 张论文卡片）
├── cnn.html / gnn.html / gat.html / groupnorm.html
│                           # 4 个独立深度可视化（核心架构详解）
├── papers/<slug>.html      # 每篇论文一个独立的 HTML 页面（107 个）
├── .github/
│   ├── ISSUE_TEMPLATE/     # 提名新论文 / 报告 bug / 提问模板
│   └── workflows/          # CI：自动校验论文数量
├── README.md
└── CONTRIBUTING.md (本文件)
```

每个 paper 页面是**单文件 HTML**：自带样式 + 内嵌 SVG + SMIL 动画，**不依赖任何外部资源**（除 Google Fonts）。

## 🆕 提名新论文

最轻量的方式：[开一个 issue](../issues/new?template=propose-paper.md)，填好"提名新论文"模板。

如果你想**直接实现一个 paper 页面**，请按以下步骤：

### 1. Fork 并 Clone

```bash
git clone https://github.com/<you>/ai-neural-networks.git
cd ai-neural-networks
```

### 2. 创建分支

```bash
git checkout -b paper/<slug>-name
# slug 命名参考 papers/ 现有文件：小写、连字符，例如
# neural-turing-machines.html / mixtral.html / deepseek-r1.html
```

### 3. 复制模板

```bash
cp papers/transformer.html papers/<your-slug>.html
```

### 4. 修改以下字段

| 位置 | 含义 |
|------|------|
| `<title>` | 论文标题 + 论文名（中文译名） |
| `<meta name="description">` | 一句话中文介绍（≤ 80 字） |
| `paper-hero` 块 | 论文标题、作者、年份、发表会议 |
| `key-innovations` 块 | 3-5 条核心创新点 |
| SVG 区域 | 动画演示（参考 cnn.html / gnn.html 的 SMIL 写法） |
| 论文原文链接 | arXiv / DOI |

### 5. 关联到首页

在 `index.html` 里找到合适的主题分组（按 `data-category` 或 class），复制一张已有卡片，修改：

- `href` 指向 `papers/<your-slug>.html`
- 标题、年份、简介

### 6. 本地校验

```bash
# 数字应该等于 papers/*.html 文件数
ls papers/*.html | wc -l
grep -E "Total Papers" README.md
```

如果不等，CI 会失败（参见 `.github/workflows/check-paper-count.yml`）。

### 7. 提交 PR

```bash
git add papers/<your-slug>.html index.html
git commit -m "Add <论文名> paper visualization"
git push origin paper/<slug>-name
```

然后在 GitHub 上开 PR，标题格式：`Add <论文名> paper visualization`。

## 🐞 报告 Bug

用 [bug 报告模板](../issues/new?template=bug-report.md)。请附：

- 浏览器 + 版本
- 操作系统
- 触发步骤
- Console 错误（如有）

## 🎨 可视化设计原则

为了让 107 个页面风格统一，建议遵循：

1. **深色主题**：`--dark-bg: #0a0a0f`，文字 `#e0e0e0`
2. **霓虹色板**：`--neon-indigo / --neon-purple / --neon-blue / --neon-amber`
3. **SMIL 动画**：用 `<animate>` / `<animateMotion>`，避免 JS 库依赖
4. **动画时长**：单个动作 0.3-2s，整组 4-8s，循环 or `fill="freeze"`
5. **响应式**：在 viewport < 768px 时让 SVG 等比缩放

参考 `papers/transformer.html` 即可看到完整样板。

## 📜 许可

贡献的代码视为 MIT License（与仓库一致）。如果你引用了第三方资源（论文截图、公式图等），请确保来源标注在页面里。

## 💬 联系方式

- Issue 区留言（最推荐）
- 或开 Discussion（如果启用了）

---

再次感谢你的贡献 ✨
