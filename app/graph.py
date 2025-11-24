from langgraph.graph import StateGraph, MessagesState, END

from app.agent import ontology_agent


def build_graph():
    graph = StateGraph(MessagesState)
    # 添加Agent
    graph.add_node("agent", ontology_agent)
    # 调用添加Agent
    graph.add_edge("agent", END)

    # 设置入口
    graph.set_entry_point("agent")
    return graph
