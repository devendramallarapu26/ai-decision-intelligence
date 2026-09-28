from services.planner_service import create_research_plan


def test_create_research_plan():
    result = create_research_plan(
        "Should we launch a food delivery business?"
    )

    assert result["question"] == "Should we launch a food delivery business?"
    assert "sub_questions" in result
    assert len(result["sub_questions"]) == 5