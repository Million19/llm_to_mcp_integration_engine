"""Registry for tool adapters."""

from typing import Dict, Any, Optional, Type, Callable
from .logging import logger
from abc import ABC, abstractmethod
import asyncio

# --- Abstract Base Class for Tool Adapters ---
class ToolAdapter(ABC):
    """Abstract base class for all tool adapters."""

    @abstractmethod
    async def run(self, **kwargs: Any) -> Any:
        """Execute the tool with the given parameters."""
        pass

    # Optional: Add methods for validation, schema definition, etc.
    # def get_schema(self) -> List[ToolParam]:
    #     """Return the parameter schema for this tool."""
    #     raise NotImplementedError


# --- Registry Implementation ---

# Global registry dictionary: maps tool_name -> adapter_instance or adapter_class
_tool_registry: Dict[str, Union[ToolAdapter, Type[ToolAdapter]]] = {}


def register_tool(tool_name: str, adapter: Union[ToolAdapter, Type[ToolAdapter]]):
    """
    Registers a tool adapter instance or class with the registry.

    Args:
        tool_name: The unique name of the tool.
        adapter: An instance of a ToolAdapter subclass or the class itself.
                 If a class is provided, an instance might be created on first use
                 or it might be expected to have static/class methods (adjust as needed).
                 For simplicity, let's assume instances are registered for now.
    """
    if tool_name in _tool_registry:
        logger.warning(f"Tool '{tool_name}' is already registered. Overwriting.")
    if not isinstance(adapter, ToolAdapter) and not (isinstance(adapter, type) and issubclass(adapter, ToolAdapter)):
         raise TypeError(f"Adapter for tool '{tool_name}' must be an instance or subclass of ToolAdapter.")

    _tool_registry[tool_name] = adapter
    logger.info(f"Tool '{tool_name}' registered with adapter {adapter.__class__.__name__}.")


def get_tool_adapter(tool_name: str) -> Optional[ToolAdapter]:
    """
    Retrieves a tool adapter instance from the registry.

    Args:
        tool_name: The name of the tool.

    Returns:
        The registered ToolAdapter instance, or None if not found.
        Handles potential class registration by instantiating (basic example).
    """
    adapter_entry = _tool_registry.get(tool_name)
    if adapter_entry is None:
        logger.error(f"Tool adapter for '{tool_name}' not found in registry.")
        return None

    if isinstance(adapter_entry, ToolAdapter):
        # Already an instance
        return adapter_entry
    elif isinstance(adapter_entry, type) and issubclass(adapter_entry, ToolAdapter):
        # It's a class, try to instantiate it (requires default constructor)
        try:
            logger.debug(f"Instantiating adapter class {adapter_entry.__name__} for tool '{tool_name}'.")
            instance = adapter_entry()
            # Optional: Cache the instance back into the registry?
            # _tool_registry[tool_name] = instance
            return instance
        except Exception as e:
            logger.error(f"Failed to instantiate adapter class {adapter_entry.__name__} for tool '{tool_name}': {e}")
            return None
    else:
        # Should not happen due to registration validation
        logger.error(f"Invalid entry in registry for tool '{tool_name}': {adapter_entry}")
        return None


def get_registered_tools() -> List[str]:
    """Returns a list of names of all registered tools."""
    return list(_tool_registry.keys())


# --- Example Usage (Optional - for demonstration or testing) ---

# class ExampleWeatherAdapter(ToolAdapter):
#     async def run(self, location: str, unit: str = "C") -> str:
#         logger.info(f"Simulating weather lookup for {location} in {unit}")
#         await asyncio.sleep(0.1) # Simulate async work
#         return f"It's sunny in {location} ({unit})"

# class ExampleCalculatorAdapter(ToolAdapter):
#     async def run(self, expression: str) -> float:
#         logger.info(f"Simulating calculation for: {expression}")
#         await asyncio.sleep(0.05)
#         try:
#             # WARNING: eval is unsafe with untrusted input! Use a safe parser in real code.
#             result = eval(expression, {"__builtins__": {}}, {})
#             return float(result)
#         except Exception as e:
#             logger.error(f"Calculation error for '{expression}': {e}")
#             raise ValueError(f"Invalid expression: {expression}") from e

# # Register instances
# register_tool("get_weather", ExampleWeatherAdapter())
# register_tool("calculator", ExampleCalculatorAdapter())

# # Register a class (will be instantiated on first get)
# class ExampleEmailAdapter(ToolAdapter):
#      async def run(self, to: str, subject: str, body: str) -> str:
#          logger.info(f"Simulating sending email to {to} with subject '{subject}'")
#          await asyncio.sleep(0.2)
#          return f"Email sent to {to}"

# register_tool("send_email", ExampleEmailAdapter) # Register the class

# logger.info(f"Registered tools: {get_registered_tools()}")
