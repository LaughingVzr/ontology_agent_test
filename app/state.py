from typing_extensions import TypedDict, Literal


class EmailClassification(TypedDict):
    intent: Literal["question", "bug", "billing", "feature", "complex"]
    urgency: Literal["high", "medium", "low", "critical"]
    topic: str
    summary: str


class EmailAgentState(TypedDict):
    # Raw email data
    email_content: str
    sender_email: str
    email_id: str

    # Classification result
    classification: EmailClassification | None

    # Bug tracking
    ticket_id: str | None

    # Raw search results
    search_results: list[str] | None
    customer_history: dict | None

    # Generated content
    draft_response: str | None
