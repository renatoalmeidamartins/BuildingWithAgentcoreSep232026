from strands import Agent
from strands_tools import generate_image
# Bedrock is the default, so no model object is needed.
agent = Agent(tools=[generate_image])
agent("Create a salvador dali style image of a chicken and a cow")

# Output model and provider details
# model ID is gonna come empty due to the lazy initialization (even if we look it up after invoking the agent)
# the default model varies based on multiple settings (region, account, quotas, ...)
# my example had (from the propmt logging output), global.anthropic.claude-sonnet-4-6
model_id = getattr(agent.model, "model_id", "Unknown model_id")
provider_name = type(agent.model).__name__
provider_module = type(agent.model).__module__

print(f"Model ID: {model_id}")
print(f"Provider Class: {provider_name}")
print(f"Provider Module: {provider_module}")
