def create_research_plan(question: str) -> dict:
    return {
        "question": question,
        "sub_questions": [
            "What is the market demand?",
            "Who are the major competitors?",
            "What are the potential opportunities?",
            "What are the major risks?",
            "What are the expected costs?"
        ]
    }