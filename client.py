import asyncio
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


async def main():
    # 1. Initialize the Multi-Server Client
    client = MultiServerMCPClient(
        {
            "research-agent": {
                "command": "python",
                "args": ["ResearchAgent.py"],
                "transport": "stdio",
            },
            "summarizer-agent": {
                "command": "python",
                "args": ["SummarizerAgent.py"],
                "transport": "stdio",
            },
        }
    )

    # 2. Get tools
    tools = await client.get_tools()

    # 3. Setup Model and Agent
    model = ChatGroq(model="openai/gpt-oss-20b")
    agent = create_agent(model, tools)

    

    # 1. Run the research task
    research_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the latest news in india?"}]}
    )

    # 2. Extract the text correctly
    research_text = research_response["messages"][-1].content

    # 3. Pass that text to the next step
    summarizer_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": f"Summarize this: {research_text}"}]}
    )

    print(summarizer_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
