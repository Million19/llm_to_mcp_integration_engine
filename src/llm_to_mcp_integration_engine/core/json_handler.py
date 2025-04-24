from typing import List

from ..schema import StepDef


def parse_selected_tools(response: dict) -> List[StepDef]:
    """Parse the selected tools from the JSON response."""
    # TODO: Implement logic to parse selected tools
    return []


def parse_selected_tool(response: dict) -> StepDef:
    """Parse the selected tool from the JSON response."""
    # TODO: Implement logic to parse selected tool
    return StepDef(step_name="", tool_name="", parameters={})


def parse_no_tools(response: dict) -> None:
    """Parse the no tools selected from the JSON response."""
    # TODO: Implement logic to parse no tools selected
    return None
