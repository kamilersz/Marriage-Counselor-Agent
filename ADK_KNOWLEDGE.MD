# Google Agent Development Kit (ADK) - Knowledge Base

## Overview

The Google Agent Development Kit (ADK) is a comprehensive framework for building powerful multi-agent systems. It provides a structured approach to creating AI agents that can handle complex tasks through tool usage, multi-agent orchestration, and sophisticated state management.

---

## Core Concepts

### 1. Agent Types

| Agent Type | Description | Use Case |
|------------|-------------|----------|
| **LLM Agents** | Language model-based agents with tool capabilities | Conversational agents, task automation |
| **Workflow Agents** | Sequential, loop, or parallel agent orchestration | Multi-step processes, complex pipelines |
| **Custom Agents** | User-defined agent implementations | Specialized behaviors |

### 2. Supported Languages

- **Python** (Primary focus, most examples)
- **TypeScript/JavaScript**
- **Go**
- **Java**

---

## Agent Architecture

### Basic Agent Structure

```python
from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    model='gemini-2.5-pro',           # LLM model to use
    name='agent_name',                 # Unique identifier
    description='Agent description',   # What the agent does
    instruction='System prompt',       # Behavior instructions
    tools=[tool1, tool2],              # Available tools
    output_key='result_key',           # State key for output
)
```

### Key Agent Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | str | The Gemini model to use (e.g., 'gemini-2.5-pro', 'gemini-2.0-flash') |
| `name` | str | Unique identifier for the agent |
| `description` | str | Description of agent's purpose (used for delegation) |
| `instruction` | str | System prompt defining agent behavior |
| `global_instruction` | str | Instructions applied across all agents |
| `tools` | list | List of tool functions/objects available to agent |
| `input_schema` | BaseModel | Pydantic schema for input validation |
| `output_schema` | BaseModel | Pydantic schema for structured output |
| `output_key` | str | Session state key for storing results |
| `before_agent_callback` | callable | Hook before agent execution |
| `before_tool_callback` | callable | Hook before tool execution |
| `after_tool_callback` | callable | Hook after tool execution |
| `before_model_callback` | callable | Hook before LLM call |

---

## Tools

### Tool Definition

Tools are functions that agents can call to perform actions or retrieve information:

```python
def tool_name(param1: str, param2: int) -> dict:
    """Tool description (seen by LLM)."""
    # Tool implementation
    return {"result": "value"}

root_agent = LlmAgent(
    model='gemini-2.5-pro',
    name='agent',
    tools=[tool_name],  # Pass tools as functions
)
```

### Tool Categories

| Category | Examples |
|----------|----------|
| **Built-in** | Code Execution, Computer Use, Google Search |
| **Google Cloud** | BigQuery, Cloud Spanner, Vertex AI Search, RAG Engine |
| **Third-party** | GitHub, Notion, Slack, PayPal, Qdrant |
| **Custom Function Tools** | User-defined Python functions |
| **MCP Tools** | Model Context Protocol integrations |
| **OpenAPI Tools** | REST API wrappers |

---

## Multi-Agent Systems

### Agent Team Pattern

Create specialized agents that work together using `AgentTool`:

```python
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

# Sub-agents
data_analyst = LlmAgent(
    name="data_analyst",
    model="gemini-2.5-pro",
    description="Analyzes market data and trends",
    instruction="You are a data analyst...",
)

trading_analyst = LlmAgent(
    name="trading_analyst",
    model="gemini-2.5-pro",
    description="Develops trading strategies",
    instruction="You are a trading analyst...",
)

# Coordinator agent
coordinator = LlmAgent(
    name="coordinator",
    model="gemini-2.5-pro",
    description="Orchestrates specialist agents",
    instruction="Guide users through the process...",
    tools=[
        AgentTool(agent=data_analyst),
        AgentTool(agent=trading_analyst),
    ],
)
```

### Multi-Agent Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| **Sequential** | Agents execute in sequence | Data Analyst → Strategy Developer |
| **Parallel** | Agents execute simultaneously | Multiple analysts working on different aspects |
| **Hierarchical** | Coordinator delegates to specialists | Financial Advisor pattern |

---

## Session Management

### Session Service

```python
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()

# Create session
session = await session_service.create_session(
    app_name="my_app",
    user_id="user_123",
    session_id="session_456"
)

# Access session state
state = session.state
result = state.get("output_key")
```

### Session State

Session state persists information across interactions:

```python
# Store data in state
session.state["analysis_result"] = analysis_data

# Retrieve data from state
result = session.state.get("analysis_result")
```

---

## Callbacks and Hooks

### Available Callbacks

```python
def before_agent_callback(agent, invocation_context):
    """Called before agent processes message."""
    pass

def before_tool_callback(tool, tool_args, invocation_context):
    """Called before tool execution."""
    pass

def after_tool_callback(tool, tool_args, tool_result, invocation_context):
    """Called after tool execution."""
    pass

def before_model_callback(model invocation_context):
    """Called before LLM call."""
    pass
```

### Safety Callbacks Pattern

For implementing guardrails:

```python
def safety_filter(content):
    """Filter unsafe content."""
    if is_unsafe(content):
        return "Content removed for safety reasons."
    return content
```

---

## Runner

### Running Agents

```python
from google.adk.runners import Runner

runner = Runner(
    agent=root_agent,
    app_name="my_app",
    session_service=session_service,
)

# Run agent
async for event in runner.run_async(
    user_id="user_123",
    session_id="session_456",
    new_message=user_message,
):
    if event.is_final_response():
        print(event.content)
```

### Event Types

| Event Type | Description |
|------------|-------------|
| `is_final_response()` | Agent's final response to user |
| `is_partial_response()` | Streaming response chunk |
| `is_tool_call()` | Agent calling a tool |

---

## Input/Output Schemas

### Structured Input

```python
from pydantic import BaseModel, Field

class UserInput(BaseModel):
    country: str = Field(description="The country to analyze")
    include_history: bool = Field(default=False)

agent = LlmAgent(
    model="gemini-2.5-pro",
    input_schema=UserInput,
)
```

### Structured Output

```python
class AnalysisOutput(BaseModel):
    capital: str = Field(description="Capital city")
    population: int = Field(description="Estimated population")

agent = LlmAgent(
    model="gemini-2.5-pro",
    output_schema=AnalysisOutput,
    output_key="analysis_result",
)
```

**Note**: When using `output_schema`, tools cannot be used simultaneously.

---

## Configuration

### Environment Variables

```bash
# Google Cloud / Vertex AI
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1

# Or for Gemini API directly
export GOOGLE_API_KEY=your-api-key
```

### Configuration Class Pattern

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    model: str = "gemini-2.5-pro"
    name: str = "agent"
    temperature: float = 0.7
```

---

## Development Workflow

### 1. Create Project

```bash
# Create new agent project
adk create my_agent

cd my_agent
```

### 2. Run Locally

```bash
# Command-line interface
adk run my_agent

# Web interface (development only)
adk web
```

### 3. Deploy to Agent Engine

```bash
# Build wheel
uv build --wheel --out-dir deployment

# Deploy
cd deployment
uv run python deploy.py
```

---

## Key Samples Reference

### Customer Service Agent

**Location**: `python/agents/customer-service/`

**Key Features**:
- Single agent with multiple tools
- Mocked backend integration
- Session state for customer context
- Video input support (Call Companion)
- Cart management tools

**Architecture**:
```
root_agent (Customer Service)
    ├── send_call_companion_link
    ├── approve_discount
    ├── access_cart_information
    ├── modify_cart
    ├── get_product_recommendations
    ├── schedule_planting_service
    └── send_care_instructions
```

### Financial Advisor

**Location**: `python/agents/financial-advisor/`

**Key Features**:
- Multi-agent coordination
- Specialized sub-agents
- Sequential workflow
- Risk assessment

**Architecture**:
```
financial_coordinator (Root)
    ├── data_analyst_agent (Market analysis)
    ├── trading_analyst_agent (Strategy development)
    ├── execution_analyst_agent (Execution planning)
    └── risk_analyst_agent (Risk evaluation)
```

### Safety Plugins

**Location**: `python/agents/safety-plugins/`

**Key Features**:
- Agent-agnostic safety guardrails
- LLM-as-judge pattern
- Model Armor API integration
- Session poisoning prevention
- Hook-based filtering

**Hooks Used**:
- `on_user_message_callback`
- `before_tool_callback`
- `after_tool_callback`
- `after_model_callback`

---

## Best Practices

### 1. Agent Design

- **Single Responsibility**: Each agent should have a clear, focused purpose
- **Clear Descriptions**: Agent descriptions are used for delegation decisions
- **Structured Instructions**: Use clear, detailed system prompts

### 2. Tool Design

- **Descriptive Names**: Tool names should be self-explanatory
- **Type Hints**: Always include type annotations
- **Docstrings**: Describe what the tool does (LLM reads this)
- **Error Handling**: Return meaningful error messages

### 3. Multi-Agent Systems

- **Coordinator Pattern**: Use a coordinator agent for complex workflows
- **State Passing**: Use `output_key` to pass results between agents
- **Specialization**: Create specialized agents for different domains

### 4. Safety

- **Input Validation**: Use schemas for input validation
- **Output Filtering**: Implement callbacks for safety checks
- **Rate Limiting**: Use callbacks to prevent abuse

### 5. Session Management

- **State Keys**: Use descriptive, unique state keys
- **Session Isolation**: One session per user/conversation
- **State Cleanup**: Clear sensitive data when no longer needed

---

## Models

### Available Gemini Models

| Model | Use Case | Speed |
|-------|----------|-------|
| `gemini-2.5-pro` | Complex reasoning, multi-agent | Slower |
| `gemini-2.5-flash` | Fast responses, simple tasks | Faster |
| `gemini-2.0-flash` | Quick interactions | Fastest |
| `gemini-2.5-flash-lite` | LLM-as-judge, safety | Very Fast |

### Model Selection

```python
# For complex reasoning
model = "gemini-2.5-pro"

# For fast responses
model = "gemini-2.5-flash"

# For safety filtering
model = "gemini-2.5-flash-lite"
```

---

## Testing and Evaluation

### Unit Tests

```bash
uv run pytest tests/unit
```

### Evaluation Tests

```bash
uv run pytest eval
```

### Evaluation Pattern

```python
from google.adk.testing import AgentEvaluator

evaluator = AgentEvaluator(agent=root_agent)

results = evaluator.evaluate(
    test_cases=[
        {"input": "test query", "expected": "expected outcome"},
    ]
)
```

---

## Deployment Options

### 1. Agent Engine (Vertex AI)

```bash
uv run deployment/deploy.py
```

### 2. Cloud Run

Containerized deployment with REST API

### 3. Agent Starter Pack

```bash
pip install agent-starter-pack
agent-starter-pack create my-agent -a adk@template
```

---

## Common Patterns

### Pattern 1: Tool-Using Agent

```python
from google.adk import Agent

def my_tool(param: str) -> str:
    """Tool description."""
    return f"Result: {param}"

root_agent = Agent(
    model="gemini-2.5-pro",
    name="tool_agent",
    instruction="Use the tool to answer questions.",
    tools=[my_tool],
)
```

### Pattern 2: Multi-Agent Coordinator

```python
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

sub_agent = LlmAgent(
    name="specialist",
    model="gemini-2.5-pro",
    description="Specializes in X",
)

coordinator = LlmAgent(
    name="coordinator",
    model="gemini-2.5-pro",
    tools=[AgentTool(agent=sub_agent)],
)
```

### Pattern 3: Structured Output

```python
from pydantic import BaseModel

class Output(BaseModel):
    result: str

agent = LlmAgent(
    model="gemini-2.5-pro",
    output_schema=Output,
    output_key="structured_output",
)
```

---

## Resources

- **Documentation**: https://google.github.io/adk-docs/
- **Samples**: https://github.com/google/adk-samples
- **Agent Starter Pack**: https://goo.gle/agent-starter-pack

---

*Last Updated: 2025-03-08*
