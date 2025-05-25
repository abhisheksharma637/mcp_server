# server.py
from mcp.server.fastmcp import FastMCP,Context
from dotenv import load_dotenv
load_dotenv()
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
import os
from dataclasses import dataclass
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

#################
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#################################



#########################

@dataclass
class Appcontext:
    index: VectorStoreIndex

@asynccontextmanager
async def lifespan(app: FastMCP):
    documents = SimpleDirectoryReader(input_files=["YOUR FILE LOCATION"]).load_data()
    index = VectorStoreIndex.from_documents(documents)
    yield Appcontext(index=index)
    
 # Create an MCP server
mcp = FastMCP("RAG_SEARCH",dependencies=["dotenv", "llama-index"],lifespan=lifespan)
 
 # Add an addition tool
@mcp.tool()
def search_rag(ctx:Context,message:str) -> str:
    """Use this tool to search content in the pdf about transformer and attention methadology
    """
    
    idx = ctx.request_context.lifespan_context.index
    query_engine = idx.as_query_engine()
    response = query_engine.query(message)
    return str(response)


