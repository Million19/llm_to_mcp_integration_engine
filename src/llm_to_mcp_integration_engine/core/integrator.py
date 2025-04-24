from ..finder import is_response_json, find_tools_in_json, find_tools_in_text
from ..core.json_handler import parse_selected_tools
from ..core.non_json_handler import extract_json_fragment
from ..validators import validate_tools_list, validate_json_structure, validate_parameters
from ..cot_verifier import verify_chain_of_thought
from ..retry import RetryHandler
from .executor import execute_tool
from ..exceptions import IntegrationError, RetryLimitExceededError

def integration_advance(
    tools_list, llm_response, json_validation, no_tools_selected, multi_stage_tools_select
):
    retry = RetryHandler()
    for attempt in retry:
        try:
            is_json = is_response_json(llm_response)
            if is_json:
                directive = find_tools_in_json(llm_response)
            else:
                fragment = extract_json_fragment(llm_response)
                directive = find_tools_in_text(fragment)
            # validate directive and CoT
            # parse steps
            # steps = parse_selected_tools(llm_response)  # or other
            # execute all steps in order
            # results = []
            # for step in steps:
            #     result = execute_tool(step.name, step.params)
            #     results.append(result)
            return {"success": True, "results": []}
        except IntegrationError as e:
            if not retry.should_retry(e):
                raise
            llm_response = retry.build_retry_prompt(llm_response, "Please try again.")  # or ask LLM again
    raise RetryLimitExceededError
