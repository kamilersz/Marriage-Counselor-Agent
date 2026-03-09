# Marriage Counselor Agent

A multi-agent marriage counseling support system built with Google's Agent Development Kit (ADK).

## Overview

The Marriage Counselor Agent is a responsible AI system designed to provide support for individuals and couples navigating relationship challenges. It uses a multi-agent architecture with specialized sub-agents for active listening, emotion analysis, resource provision, and many more.

## Why?

While general-purpose Large Language Models (LLMs) can provide basic advice, relationship counseling requires a level of nuance, long-term context, and structured analysis that a single-prompt interface simply cannot deliver.

Asking a standard LLM for marriage advice often results in generic, one-size-fits-all platitudes, and the model tends to exhibit "sycophancy"—agreeing with the user who is prompting it, rather than remaining an objective mediator.

The **Marriage Counselor Agent** solves this by leveraging a structured, multi-agent framework:

* **Separation of Concerns (Specialized Agents):** Instead of relying on one model to do everything, this system delegates tasks. An *Active Listening Agent* validates emotions, an *Emotion Analyzer* reads subtext and detects communication breakdowns, and a *Resource Provider* queries a dedicated knowledge management system for proven relationship frameworks (e.g., conflict resolution techniques).
* **Objective Mediation:** Standard LLMs inherently bias toward the user writing the prompt. A multi-agent system can process inputs from both partners simultaneously, cross-reference them, and provide a neutral, balanced perspective without taking sides.
* **Contextual Continuity:** Relationship dynamics are complex and historical. This system is designed to maintain structured memory and context across multiple sessions, recognizing patterns in behavior or recurring arguments that a stateless LLM would forget.
* **Responsible AI Guardrails:** Built with safety in mind. The system includes strict monitoring agents that detect when a situation escalates beyond the scope of AI assistance (e.g., signs of abuse or severe psychological distress) and automatically provides routing to human professionals.

In short, the Marriage Counselor Agent transforms a simple Q&A chatbot into a comprehensive, analytical, and objective support system for relationship management.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Counseling Coordinator                      │
│                   (Root Agent - Orchestrator)                   │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│    Active    │    │  Emotion    │    │  Resource   │
│  Listening   │    │  Analysis   │    │  Provider   │
│    Agent     │    │    Agent    │    │    Agent    │
└──────────────┘    └──────────────┘    └──────────────┘
```

## Features

- **Active Listening**: Empathetic reflection and validation
- **Emotion Analysis**: Pattern recognition and insight
- **Resource Provision**: Communication exercises and coping strategies
- **Crisis Detection**: Immediate resource provision for urgent situations
- **Safety First**: Professional referral recommendations

## Prerequisites

- Python 3.10 or later
- Google Cloud Project (for Vertex AI) or Gemini API key
- pip or uv for package management

## Installation

### Using pip

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

### Using uv (recommended)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

### Configuration

Create a `.env` file in the project root:

```bash
# For Gemini API (direct)
GEMINI_API_KEY=your-api-key-here

# OR for Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

## Running the Agent

### Command Line Interface

```bash
# Using ADK CLI
adk run marriage_counselor

# Or using Python directly
python -m marriage_counselor.agent
```

### Web Interface (Development)

```bash
# Start the web UI
adk web

# Then open http://localhost:8000 in your browser
```

### Test Script

```bash
# Run interactive test
python deployment/test_deployment.py --local
```

## Testing

```bash
# Run unit tests
pytest tests/unit

# Run evaluation tests
pytest tests/eval

# Run all tests
pytest
```

## Safety and Ethics

### Important Disclaimer

This agent is an AI assistant, not a licensed mental health professional. This service is for educational and support purposes only.

### Crisis Resources

If users indicate they are experiencing:
- Abuse or violence
- Thoughts of self-harm or suicide
- Severe mental health symptoms

The agent will immediately provide:
- Suicide & Crisis Lifeline: 988
- National Domestic Violence Hotline: 1-800-799-7233
- Crisis Text Line: Text HOME to 741741

## Project Structure

```
marriage-counselor-agent/
├── marriage_counselor/
│   ├── __init__.py
│   ├── agent.py                 # Root agent
│   ├── config.py                # Configuration
│   ├── prompts.py               # System prompts
│   ├── sub_agents/              # Specialist agents
│   ├── tools/                   # Agent tools
│   ├── callbacks/               # Safety callbacks
│   └── schemas/                 # Input/output schemas
├── tests/
│   ├── unit/                    # Unit tests
│   └── eval/                    # Evaluation tests
├── deployment/                  # Deployment files
├── .env.example                 # Example environment file
├── pyproject.toml               # Project dependencies
└── README.md
```

## Deployment

### Agent Engine (Vertex AI)

```bash
# Build wheel
uv build --wheel --out-dir deployment

# Deploy (requires Google Cloud setup)
cd deployment
python deploy.py --create
```

### Agent Starter Pack

```bash
# Install Agent Starter Pack
pip install agent-starter-pack

# Create deployment project
agent-starter-pack create my-counselor -a adk@marriage_counselor
```

## Development

### Adding New Tools

1. Define the tool function in `marriage_counselor/tools/`
2. Add type hints and docstrings
3. Import in `tools/__init__.py`
4. Add to agent's `tools` list

### Adding New Sub-Agents

1. Create agent file in `marriage_counselor/sub_agents/`
2. Define agent with LlmAgent
3. Import in `sub_agents/__init__.py`
4. Add as AgentTool to coordinator

## License

Copyright 2025 Google LLC

Apache License 2.0

## Support

For issues and questions:
- Review the ADK documentation: https://google.github.io/adk-docs/
- Check samples: https://github.com/google/adk-samples
