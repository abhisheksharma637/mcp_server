# RAG Search MCP Server

A Model Context Protocol (MCP) server that provides RAG (Retrieval-Augmented Generation) search capabilities for the "Attention Is All You Need" paper using LlamaIndex and OpenAI.

## Overview

This server creates a searchable knowledge base from the seminal Transformer paper "Attention Is All You Need" and exposes it through an MCP tool. It allows you to query the paper's content about transformer architecture and attention mechanisms.

## Features

- **RAG Search**: Query the "Attention Is All You Need" paper using natural language
- **Vector Store Index**: Uses LlamaIndex to create efficient vector embeddings
- **MCP Integration**: Seamlessly integrates with MCP-compatible clients
- **OpenAI Integration**: Leverages OpenAI's models for search and retrieval

## Prerequisites

- Python 3.8+
- OpenAI API key
- The "Attention Is All You Need" PDF file

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd rag-search-mcp-server
```

2. Install dependencies:
```bash
pip install fastmcp python-dotenv llama-index
```

3. Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**: The `.env` file should be placed in the same directory as your `custom_mcp_server_rag_tool.py` file. This file stores your sensitive API credentials and should never be committed to version control. Add `.env` to your `.gitignore` file.

4. Download the "Attention Is All You Need" paper and place it at:
```
C:\Users\spacecat\Downloads\attention_is_all_you_need.pdf
```
Or update the path in `custom_mcp_server_rag_tool.py` to match your file location.

## Usage

### Starting the Server

Run the server:
```bash
python custom_mcp_server_rag_tool.py
```

The server will:
1. Load the PDF document
2. Create a vector store index from the document content
3. Start the MCP server with the RAG search tool available

### Connecting to Claude Desktop

To use this MCP server with Claude Desktop:

1. **Configure Claude Desktop**: Add the server to your Claude Desktop configuration file:

   **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. **Add server configuration**:
   ```json
   {
     "mcpServers": {
       "rag-search": {
         "command": "python",
         "args": ["path/to/your/custom_mcp_server_rag_tool.py"],
         "env": {
           "OPENAI_API_KEY": "your_openai_api_key_here"
         }
       }
     }
   }
   ```

   **Alternative (using .env file)**:
   ```json
   {
     "mcpServers": {
       "rag-search": {
         "command": "python",
         "args": ["path/to/your/custom_mcp_server_rag_tool.py"]
       }
     }
   }
   ```
   *(Make sure your .env file is in the same directory as the Python script)*

3. **Restart Claude Desktop** for the changes to take effect.

4. **Verify connection**: You should see the RAG search tool available in Claude Desktop's interface.

### Using the RAG Search Tool

Once connected to an MCP client, you can use the `search_rag` tool to query the paper:

**Example queries:**
- "What is attention mechanism?"
- "How does multi-head attention work?"
- "Explain the transformer architecture"
- "What are the advantages of self-attention?"

## Code Structure

```
custom_mcp_server_rag_tool.py
├── Environment Setup (OpenAI API key)
├── AppContext (Data class for storing the index)
├── Lifespan Manager (Loads PDF and creates index)
├── MCP Server Setup
└── RAG Search Tool (Query interface)
```

## Key Components

- **FastMCP**: The MCP server framework
- **SimpleDirectoryReader**: Loads PDF documents
- **VectorStoreIndex**: Creates searchable vector embeddings
- **Query Engine**: Processes natural language queries

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for embeddings and LLM | Yes |

### File Paths

Update the PDF file path in the `lifespan` function:
```python
documents = SimpleDirectoryReader(input_files=["path/to/your/pdf"]).load_data()
```

## API Reference

### Tools

#### `search_rag`
- **Description**: Search content in the PDF about transformer and attention methodology
- **Parameters**: 
  - `message` (string): The search query
- **Returns**: String response with relevant information from the paper

## Dependencies

- `fastmcp`: MCP server framework
- `python-dotenv`: Environment variable management
- `llama-index`: RAG and vector search capabilities
- `openai`: OpenAI API integration (via llama-index)

## Troubleshooting

### Common Issues

1. **Missing OpenAI API Key**
   - Ensure your `.env` file contains a valid `OPENAI_API_KEY`
   - Check that the key has sufficient credits
   - If using Claude Desktop config, verify the API key is correctly set in the JSON

2. **PDF File Not Found**
   - Verify the PDF path in the `lifespan` function
   - Ensure the file exists and is readable

3. **Import Errors**
   - Install all required dependencies: `pip install fastmcp python-dotenv llama-index`

4. **Claude Desktop Connection Issues**
   - Verify the path to `custom_mcp_server_rag_tool.py` is correct in the config
   - Ensure Python is in your system PATH
   - Check Claude Desktop logs for error messages
   - Restart Claude Desktop after configuration changes

5. **Server Not Starting**
   - Make sure all dependencies are installed
   - Check that the PDF file path is accessible
   - Verify OpenAI API key is valid and has credits

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original "Attention Is All You Need" paper by Vaswani et al.
- LlamaIndex for RAG capabilities
- FastMCP for the MCP server framework
