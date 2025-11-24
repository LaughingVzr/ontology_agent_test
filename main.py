from dotenv import load_dotenv

from app.graph import build_graph
from langchain_core.messages import HumanMessage


def main():
    print("Hello from ontology-agent-test!")
    load_dotenv()
    app = build_graph()
    app = app.compile()
    result = app.invoke({"messages": [HumanMessage(content="请用DeepSeeK模型简单介绍 LangGraph")]})
    print(result)


if __name__ == "__main__":
    main()
