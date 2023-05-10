from typing import Any, Callable, Dict


def rule_response(
    rule_func: Callable[..., Dict[str, Any]]
) -> Callable[[Any, str], dict[str, Any]]:
    def get_response(cls, sentence: str) -> Dict[str, Any]:
        response = {}
        result = rule_func(cls, sentence)
        if result:
            response.update(is_returned=True, value=result.get("value"))

        return response

    return get_response
