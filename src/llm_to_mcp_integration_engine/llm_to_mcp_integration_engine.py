from typing import Union

from .core.integrator import (
    integration_advance as _advance,
)


def llm_to_mcp_integration_advance(
    tools_list: dict,
    llm_response: Union[str, dict],
    json_validation: bool,
    no_tools_selected: bool,
    multi_stage_tools_select: bool,
):
    """
    Validate and execute an LLM response (JSON or not) according to the
    SELECTED_TOOLS / SELECTED_TOOL / NO_TOOLS_SELECTED protocol.
    """
    return _advance(
        tools_list=tools_list,
        llm_response=llm_response,
        json_validation=json_validation,
        no_tools_selected=no_tools_selected,
        multi_stage_tools_select=multi_stage_tools_select,
    )


# Stub out default and custom signatures (just forward to the same core with different defaults).
def llm_to_mcp_integration_default():
    raise NotImplementedError

def llm_to_mcp_integration_custom():
    raise NotImplementedError
