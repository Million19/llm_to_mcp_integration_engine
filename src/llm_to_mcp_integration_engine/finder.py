from typing import Union, Tuple, Literal

def is_response_json(llm_resp: Union[str, dict]) -> bool:
    """Check if the LLM response is a JSON."""
    # TODO: Implement logic to check if the response is JSON
    return False


def find_tools_in_json(response: dict) -> Literal["SELECTED_TOOLS", "SELECTED_TOOL", "NO_TOOLS_SELECTED"]:
    """Find tools in JSON response."""
    # TODO: Implement logic to find tools in JSON
    return "NO_TOOLS_SELECTED"


def find_tools_in_text(text: str) -> Tuple[Literal["SELECTED_TOOLS", "SELECTED_TOOL", "NO_TOOLS_SELECTED"], dict]:
    """Regex-extract JSON fragment."""
    # TODO: Implement logic to extract JSON from text
    return "NO_TOOLS_SELECTED", {}
