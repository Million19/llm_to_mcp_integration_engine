from typing import Union

from .core.integrator import integration_advance


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
    return integration_advance(
        tools_list=tools_list,
        llm_response=llm_response,
        json_validation=json_validation,
        no_tools_selected=no_tools_selected,
        multi_stage_tools_select=multi_stage_tools_select,
    )


def llm_to_mcp_integration_default(
    tools_list: dict,
    llm_response: Union[str, dict],
    json_validation: bool
):
    return integration_advance(
        tools_list=tools_list,
        llm_response=llm_response,
        json_validation=json_validation,
        no_tools_selected=False,  # disabled
        multi_stage_tools_select=False  # disabled
    )


def llm_to_mcp_integration_custom(
    tools_list: dict,
    llm_response: Union[str, dict],
    json_validation: bool
):
    """
    This function is for agentic/custom behaviors.
    It allows raw JSON fragments to be processed differently.
    It lets users override tool param parsing (e.g. parse a mini-language or special DSL).
    It may also allow function-based callbacks instead of HTTP-based tools in the future.
    """
    return integration_advance(
        tools_list=tools_list,
        llm_response=llm_response,
        json_validation=json_validation,
        no_tools_selected=True,  # enable this if agent might not call tools
        multi_stage_tools_select=True  # allow multi-step behaviors
    )
    # TODO: Add a custom parsing/validation plugin in the future.
