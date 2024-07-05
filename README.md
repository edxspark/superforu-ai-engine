
## SuperforuAIEngine
***
SuperforuAIEngine is a data engine for your LLM application. 
Building with SuperforuAIEngine typically involves working with LLM、Memory、knowledge and tools. 

![architecture](./docs/images/superforu-architecture.png)

## Why use SuperforuAIEngine?
***
Langchain/LlamaIndex provide easy to use abstractions that can be used for quick experimentation and prototyping. 
But, when things move to production, there are constraints like the External knowledge base integration, 
complex text parsing, precise knowledge extraction, tool custom routing encapsulation, response custom encapsulation etc. 

## Introduction
SuperforuAIEngine is an open-source data engine to organize your RAG codebase along with a frontend to play around with different RAG customizations. 
It provides a simple way to organize your codebase so that it becomes easy to test it locally while also being able to deploy it in a production ready environment. 

## 🧑‍💻Technical selection
### 1. Data processing:
- Local services: OmniParse a platform that ingests and parses any unstructured data into structured, actionable data optimized for GenAI (LLM) applications. Whether you are working with documents, tables, images, videos, audio files, or web pages, OmniParse prepares your data to be clean, structured, and ready for AI applications such as RAG, fine-tuning, and more.
- Cloud services: Moonshot OCR services、Google OCR、Baidu OCR、Moonshot etc.

### 2. Data storage and management: 
- Elasticsearch: Version 8.X+ A low latency architecture optimized for AI, with native vector database functionality. Supports full-text retrieval and reciprocal Rank Fusion (RRF).
- Nocodb: NocoDB is a no-code database platform that allows teams to collaborate and build applications with ease of a familiar and intuitive spreadsheet interface. This allows even non-developers.

### 3. Data embedding
- Ollama: nomic-embed-text

### Development framework
- Python
- LlamaIndex
- Langchain
- Flask

## API Services
- Data processing
- Data retrieval
- Chat (stream or no)

