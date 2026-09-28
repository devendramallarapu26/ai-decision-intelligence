from exceptions.research_exceptions import EmptyQuestionError
from services.planner_service import create_research_plan
from services.researcher_service import research_all
from services.evidence_service import create_evidence
def process_research(question: str) -> dict:
    question = question.strip()

    if not question:
        raise EmptyQuestionError("Question Cannot be Empty")

    if len(question) < 10:
        raise EmptyQuestionError(
            "Question Must be More than 10 Characters"
        )
    plan = create_research_plan(question)
    research_results = research_all(plan["sub_questions"])
    return {
        "question": question,
        "message": "Research processing started",
        "status" : "processing",
            "result": {
        "summary": "Research is being processed",
        "confidence": 0.0
    },
        'plan':plan,
        "research": research_results
        
        
    }