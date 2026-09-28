from services.evidence_service import create_evidence


def test_create_evidence():
    result = create_evidence(
        "Example Source",
        "Food delivery demand is growing.",
        0.9
    )

    assert result["source"] == "Example Source"
    assert result["claim"] == "Food delivery demand is growing."
    assert result["relevance"] == 0.9