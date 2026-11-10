# AIGC 驱动的跨境电商智能运营中枢

一个集成了多模型混合调度、智能客服（RAG）与一键商品主图生成的 B 端 AI 营销系统。全栈独立开发。

## ✨ 核心亮点
- **多模型混合编排**：按业务分发调度，文本调用 DeepSeek，图像调用智谱 GLM-4V / CogView，兼顾效果与 API 成本。
- **商品主图 AIGC 闭环**：Rembg 本地高精度抠图 -> AI 生成背景 -> Pillow 边缘阴影与多语言文字排版，保证商品 100% 还原。
- **轻量级 RAG 防幻觉**：手写本地 FAQ 检索，利用 Jieba 分词 + TF-IDF 相似度匹配，配合阈值过滤，防止大模型胡编乱造。
- **工程健壮性与安全**：并发锁防 CPU 打满、大文件上传防断连（Broken pipe）、使用 Cryptography 加密存储敏感 API Key。

## 🛠️ 技术栈
- **后端**：Python, FastAPI, SQLite
- **前端**：原生 HTML/JS
- **AI 生态 & 图像处理**：DeepSeek API, 智谱 (GLM-4V / CogView), Rembg, Pillow, Jieba

## 🚀 本地部署与运行环境

**⚠️ 运行环境要求：Linux (推荐 Ubuntu 20.04+)**
由于本项目使用了 Rembg 进行本地高精度抠图，部分底层图像处理依赖在 Windows 下容易出现兼容性问题，建议在 Linux 环境下部署运行。

1. 安装依赖：
**pip install -r requirements.txt**

2. 配置环境变量：
复制 **.env.example** 为 **.env**，并填入你的 API Keys（DeepSeek 和智谱）。

3. 启动服务：
**uvicorn main:app --reload**
