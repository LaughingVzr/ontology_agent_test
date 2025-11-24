import os

from langchain_openai import ChatOpenAI

def build_ds_llm(model_name="deepseek-reasoner", temperature=0):
    """
    返回一个DS LLM的
    :param model_name:
    :param temperature:
    :return:
    """
    api_key=os.getenv("DEEPSEEK_API_KEY")
    base_url=os.getenv("DEEPSEEK_BASE_URL")
    llm = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        base_url=base_url,
        temperature=temperature
    )
    return llm
