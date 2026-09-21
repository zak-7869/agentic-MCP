import os
import asyncio
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from langchain_core.documents import Document
from langchain_groq import ChatGroq
# Use standard langchain unless you specifically need the legacy 'classic' package
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("summarizer-agent")

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

# Initialize LLM (Ensure GROQ_API_KEY is in your .env)
llm = ChatGroq(model="openai/gpt-oss-120b")

@mcp.tool()
async def summarize_text(content: str) -> str:
    """Summarizes a block of text using Groq. 
    Uses map_reduce for long text by splitting it into chunks first.
    """
    try:
        # 1. Split text into chunks if it's long
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.create_documents([content])

        # 2. Choose chain type based on length
        # 'stuff' is faster for short text; 'map_reduce' handles long documents
        chain_type = "map_reduce" if len(docs) > 1 else "stuff"
        chain = load_summarize_chain(llm, chain_type=chain_type)

        # 3. Run in executor to prevent blocking the async event loop
        loop = asyncio.get_running_loop()
        summary = await loop.run_in_executor(None, lambda: chain.invoke({"input_documents": docs}))

        return summary["output_text"]
    
    except Exception as e:
        return f"Error during summarization: {str(e)}"

if __name__ == "__main__":
    # FastMCP uses 'stdio' by default if no arguments are passed
    mcp.run()
