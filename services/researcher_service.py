from services.evidence_service import create_evidence 
def research_sub_question(sub_question: str) -> dict:
    evidence = create_evidence(
        source="Example Source",
        claim=f"Evidence related to: {sub_question}",
        relevance=0.5
    )

    return {
        "question": sub_question,
        "answer": f"Research answer for: {sub_question}",
        "sources": [evidence]
    }


def research_all(sub_questions: list[str]) -> list[dict]:
    results = []

    for question in sub_questions:
        result = research_sub_question(question)
        results.append(result)

    return results
