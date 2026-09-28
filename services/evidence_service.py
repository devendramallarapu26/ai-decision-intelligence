def create_evidence(
    source: str,
    claim: str,
    relevance: float
) -> dict:
    return {
        "source": source,
        "claim": claim,
        "relevance": relevance
    }