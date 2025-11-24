from app.models import build_ds_llm
from langchain_core.messages import SystemMessage


def ontology_agent(state):
    """
    简单DS Agent
    :param state:
    :return:
    """
    llm = build_ds_llm(model_name="deepseek-reasoner", temperature=0)
    messages = [SystemMessage(content="你是智能问答助手，简洁回答用户问题。")] + state["messages"]
    # 调用llm
    response = llm.invoke(messages)
    return {"messages": [response]}
