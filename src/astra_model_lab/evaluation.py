
from dataclasses import dataclass


@dataclass
class EvaluationResult:
    expected: str
    actual: str
    passed: bool


def evaluate_exact_match(
    expected: str,
    actual: str,
) -> EvaluationResult:
    """Evaluate a response using exact text matching."""

    return EvaluationResult(
        expected=expected,
        actual=actual,
        passed=expected.strip() == actual.strip(),
    )
