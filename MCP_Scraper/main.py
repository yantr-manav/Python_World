from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
import asyncio



# Load environment variables from .env
load_dotenv()

# ✅ Initialize Ollama model (change "mistral" if you want another)
model = ChatOllama(model="mistral")

# ✅ MCP tool connection setup  
server_params = StdioServerParameters(
    command="npx",
    env={
        "API_TOKEN": os.getenv("API_TOKEN"),
        "BROWSER": os.getenv("BROWSER_AUTH"),
        "WEB_UNLOCKER_ZONE": os.getenv("WEB_UNLOCKER_ZONE"),
    },
    args=["@brightdata/mcp"],
)

async def chat_with_agent():
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await load_mcp_tools(session)
                agent = create_react_agent(model, tools)

                messages = [
                            {
                            "role": "system",
                            "content": (
                                "You are an AI assistant with access to tools like `search_engine` and `scrape_as_markdown`."
                                " Always use tools to answer questions that require real-time or factual data (like YouTube tutorials)."
                                " Do not guess or fabricate results. Do not explain what you will do—just do it and return results."
                            )
                            }


                ]

                print("Type 'exit' or 'quit' to end the conversation.")

                while True:
                    user_input = input("\nYou: ")
                    if user_input.strip().lower() in {"exit", "quit"}:
                        print("Goodbye!")
                        break

                    messages.append({"role": "user", "content": user_input})

                    try:
                        agent_response = await agent.ainvoke({"messages": messages})
                        ai_message = agent_response["messages"][-1].content
                        print(f"Agent: {ai_message}")
                    except Exception as e:
                        print(f"[Error] Failed to get agent response: {e}")
    except Exception as e:
        print(f"[Error] Failed to connect to MCP server: {e}")

if __name__ == "__main__":
    asyncio.run(chat_with_agent())
