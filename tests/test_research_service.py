from services.research_service import process_research;
from exceptions.research_exceptions import EmptyQuestionError;
import pytest;
def test_process_research_valid_question():
    result = process_research("Should we launch a food business?")
    assert result["question"] == "Should we launch a food business?"
    assert result["message"] == "Research processing started"
    
def test_process_research_empty_question():
    with pytest.raises(EmptyQuestionError):
        process_research("")
def test_process_research_short_question():
    with pytest.raises(EmptyQuestionError):
        process_research("Hello")