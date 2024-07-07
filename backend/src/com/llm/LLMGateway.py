import os
import dotenv

from enum import Enum
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms.ollama import Ollama
from langchain_community.llms.openai import AzureOpenAI

dotenv.load_dotenv()


class LLMGateway(object):
    def __init__(self, llm_name: str, model_name: str, temperature=0.3):
        self.llm_name = llm_name
        self.model_name = model_name
        self.temperature = temperature

        # LLM config
        if LlmNameEnum.DEEP_SEEK.value == llm_name:
            self.base_url = os.getenv("DS_BASE_URL")
            self.api_key = os.getenv("DS_API_KEY")
        elif LlmNameEnum.AZURE_OPENAI.value == llm_name:
            self.base_url = os.getenv("AZURE_BASE_URL")
            self.api_key = os.getenv("AZURE_API_KEY")
            self.api_version = os.getenv("AZURE_VERSION")
        elif LlmNameEnum.OLLAMA.value == llm_name:
            self.base_url = os.getenv("OLLAMA_BASE_URL")
        else:
            self.base_url = os.getenv("OPENAI_BASE_URL")
            self.api_key = os.getenv("OPENAI_API_KEY")

    # Create LLM
    def llm(self):
        llm = None
        if LlmNameEnum.AZURE_OPENAI.value == self.llm_name:
            llm = AzureOpenAI(
                azure_endpoint=self.base_url,
                deployment_name=self.model_name,
                openai_api_version=self.api_version,
                openai_api_key=self.api_key
            )
        elif LlmNameEnum.OLLAMA.value == self.llm_name:
            llm = Ollama(
                model=self.model_name
            )
        else:
            llm = ChatOpenAI(
                api_base=self.base_url,
                api_key=self.api_key,
                model=self.model_name,
                temperature=self.temperature
            )
        return llm


class LlmNameEnum(Enum):
    DEEP_SEEK = "DEEP_SEEK"
    AZURE_OPENAI = "AZURE_OPENAI"
    OPEN_AI = "OPEN_AI"
    OLLAMA = "OLLAMA"
