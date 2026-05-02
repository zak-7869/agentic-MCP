import asyncio
from mcp.server.fastmcp import FastMCP
from langchain_community.tools import DuckDuckGoSearchRun

mcp = FastMCP("research-agent")

search = DuckDuckGoSearchRun()

@mcp.tool()
async def research_topic(topic: str) -> str:
    """Research a given topic using web search and returns key findings."""
    return await asyncio.to_thread(search.run, topic)


if __name__ == "__main__":
    mcp.run(transport="stdio")