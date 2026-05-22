# Agentic MCP (Model Context Protocol)

A Python-based implementation of AI agents with Model Context Protocol (MCP) support, featuring host client and server architecture.

## Overview

This project implements an agentic system using the Model Context Protocol. It provides a framework for building AI agents that can communicate via client-server architecture, enabling distributed and scalable AI agent deployments.

## Project Structure

- `ResearchAgent.py` - Agent implementation for research tasks
- `SummarizerAgent.py` - Agent implementation for summarization tasks
- `client.py` - Client-side implementation for connecting to the MCP server

## Features

- **AI Agents** - Modular agent implementations for various tasks
- **Model Context Protocol (MCP)** - Standardized communication protocol
- **Client-Server Architecture** - Distributed agent deployment
- **Research Agent** - Specialized agent for research operations
- **Summarizer Agent** - Specialized agent for content summarization
- **Extensible Design** - Easy to add new agent types

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required dependencies (see requirements below)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/zak-7869/agentic-MCP.git
```

2. Navigate to the repository directory:
```bash
cd agentic-MCP
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Running the MCP Server

```bash
python server.py
```

#### Running the Client

```bash
python client.py
```

#### Using Research Agent

```python
from ResearchAgent import ResearchAgent

agent = ResearchAgent()
# Use agent for research tasks
```

#### Using Summarizer Agent

```python
from SummarizerAgent import SummarizerAgent

agent = SummarizerAgent()
# Use agent for summarization tasks
```

## Architecture

### Client-Server Model

- **Server**: Hosts the MCP implementation and agent services
- **Client**: Connects to the server to interact with agents
- **Protocol**: Model Context Protocol (MCP) for standardized communication

### Agent Types

1. **ResearchAgent** - Handles research-related operations
2. **SummarizerAgent** - Processes and summarizes content

## Technologies Used

- **Python** - Programming language
- **Model Context Protocol (MCP)** - Communication protocol
- **Agents Framework** - AI agent implementation

## Project Structure

```
agentic-MCP/
├── ResearchAgent.py       # Research agent implementation
├── SummarizerAgent.py     # Summarizer agent implementation
├── client.py              # Client-side code
├── server.py              # Server implementation (if available)
└── README.md              # This file
```

## Development

To extend this project with new agents:

1. Create a new agent class inheriting from the base agent structure
2. Implement required methods for your specific use case
3. Register the agent with the MCP server
4. Update this README with usage examples

## Contributing

Contributions are welcome! Please feel free to:
- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Commit your changes (`git commit -m 'Add amazing feature'`)
- Push to the branch (`git push origin feature/amazing-feature`)
- Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

Created by [zak-7869](https://github.com/zak-7869)

---

For more information about Model Context Protocol, visit the [MCP Documentation](https://modelcontextprotocol.io/).
