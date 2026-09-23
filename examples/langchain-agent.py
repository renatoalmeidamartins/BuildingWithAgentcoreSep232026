from langchain.agents import create_agent
from langchain_core.utils.uuid import uuid7

agent = create_agent(model= "bedrock_converse:global.amazon.nova-2-lite-v1:0", 
                    tools=[])

config = {"configurable": {"thread_id": str(uuid7())}}
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]},
    config=config,
)
print (result)