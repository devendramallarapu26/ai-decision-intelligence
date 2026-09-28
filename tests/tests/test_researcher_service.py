from services.researcher_service import research_sub_question
from services.researcher_service import (
    research_sub_question,
    research_all
)

def test_research_sub_question():
    result = research_sub_question("What is the market demand?")

    assert result["question"] == "What is the market demand?"
    assert "answer" in result
    assert "sources" in result
def test_research_all():
    questions = [
        "What is the market demand?",
        "Who are the competitors?"
    ]

    results = research_all(questions)

    assert len(results) == 2
    assert results[0]["question"] == "What is the market demand?"
    assert results[1]["question"] == "Who are the competitors?"