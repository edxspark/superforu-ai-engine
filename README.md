
# superforu-ai-engine
***
## AI数据引擎
快速构建高性能可持续的AI应用，如：RAG、智能体、客服机器人、写作助手、阅读助手、合同助手、论文助手等。 
提供的API服务，外部应用可快速集成AI能力，如: 知识库管理、OCR、Embedding、Chat服务。

Langchain/LlamaIndex提供了易于使用的抽象，但在实际生产中存在了限制，不利于针对业务的微调和扩展。

## 系统架构
> 架构增强：精准提取内容、上下文过大处理、问题模糊、长期记忆等问题  
> 价值参考：llamaindex、phidata、cognita

![architecture](./docs/images/superforu-architecture.png)

在线应用案例: http://www.superforu.com

⚠️ 系统代码正在持续迭代上传中  

## 功能一览
- 知识管理：通过可视化管理知识并记录知识处理状态
- 智能体: 自定义Agent
- LLM对话: 直接与LLM对话
- 与知识库对话：RAG检索增强生成对话

## 接口一览
- 文档向量化：通过接收文档，解析分段后进行向量化，保存到索引库和向量库中
- 删除文档：移除已处理的文档
- 获取相关文档内容: 获取与问题相关的文档内容
- 聊天: 通过发送问题，响应生成内容，支持一次性返回和流式返回

## 技术选型
- OCR
  - 本地化: OmniParse (需要至少T4显卡)
  - 云服务: Moonshot OCR或其他
- Embedding: 
  - 本地化: Ollama (nomic-embed-text)
  - 云服务: ChatGLM (embedding)
- LLM: 
  - 本地化: Ollama (qwen2:7b)
  - 云服务: Deepseek
- 索引库向量库:
  - elasticsearch 8.X
- 元数据管理：
  - nocodb: 知识库管理、元数据管理
- 基础框架: 
  - python
  - fastapi
  - langchain
- 前端应用:
  - chatgpt-next-web-ui

# 🚀 本地开发指南
## 环境准备: docker、docker compose、conda、ollama
- 安装 [docker](https://www.docker.com/)
- 安装 [docker compose](https://docs.docker.com/compose/)
- 安装 [miniconda](https://docs.anaconda.com/miniconda)
- 安装 [Ollama](https://ollama.com/)

```shell
# 创建python环境
conda create --name superforu-ai-engine python=3.11
conda activate superforu-ai-engine

# 安装依赖
pip install -r requirements.txt

# 本地安装embedding模型
ollama pull nomic-embed-text

# 启动程序
python backend/src/App.py
```


