
from astracompass import evaluate_exact_match


def test_exact_match_success():
    result = evaluate_exact_match("Hello", "Hello")
    assert result.passed is True


def test_exact_match_failure():
    result = evaluate_exact_match("Hello", "World")
    assert result.passed is False
