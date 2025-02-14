import importlib
import pkgutil
import inspect
from backend.agents.base_agent import BaseAgent 

package = "backend.agents" 

def load_agents():
    """Dynamically loads all AI agents from the 'backend/agents/' folder."""
    agents_dict = {}

    for _, module_name, _ in pkgutil.iter_modules(["backend/agents"]):
        module = importlib.import_module(f"{package}.{module_name}")

        for class_name, cls in inspect.getmembers(module, inspect.isclass):
            if issubclass(cls, BaseAgent) and cls.__module__ == module.__name__:
                try:
                    agent_instance = cls(name=module_name, category=module_name.replace("_agent", ""))  
                    agents_dict[module_name] = agent_instance
                    print(f"✅ Loaded agent: {module_name} -> {agent_instance}")
                except TypeError as e:
                    print(f"⚠️ Error loading agent {class_name}: {e}")

    return agents_dict

AGENT_REGISTRY = load_agents()

print(" Registered Agents:", list(AGENT_REGISTRY.keys()))