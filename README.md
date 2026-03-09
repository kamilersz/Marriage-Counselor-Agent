# Marriage Counselor Agent

A comprehensive multi-agent marriage counseling support system built with Google's Agent Development Kit (ADK).

## Overview

The Marriage Counselor Agent is a responsible AI system designed to provide holistic support for individuals and couples navigating relationship challenges. It uses a sophisticated multi-agent architecture with **11 specialized sub-agents** covering every aspect of relationship health, from assessment and goal setting to conflict resolution, intimacy building, and crisis intervention.

## Why?

While general-purpose Large Language Models (LLMs) can provide basic advice, relationship counseling requires a level of nuance, long-term context, and structured analysis that a single-prompt interface simply cannot deliver.

Asking a standard LLM for marriage advice often results in generic, one-size-fits-all platitudes, and the model tends to exhibit "sycophancy"—agreeing with the user who is prompting it, rather than remaining an objective mediator.

The **Marriage Counselor Agent** solves this by leveraging a structured, multi-agent framework with 31 specialized tools:

* **Specialist Agents:** Instead of relying on one model to do everything, this system delegates to 11 expert agents:
  - **Active Listening Agent** - Validates emotions with empathy
  - **Emotion Analysis Agent** - Detects patterns and subtext
  - **Resource Provider Agent** - Proven frameworks and strategies
  - **Relationship Assessment Agent** - Evaluates 10 dimensions of health
  - **Goal Setting Agent** - SMART goals and shared vision
  - **Conflict Resolution Agent** - Pattern analysis and de-escalation
  - **Values Alignment Agent** - Finds common ground in differences
  - **Repair & Healing Agent** - Apologies, forgiveness, trust rebuilding
  - **Intimacy Specialist Agent** - Emotional and physical connection
  - **Boundary Specialist Agent** - Healthy limits and autonomy
  - **Stress Management Agent** - External pressures and resilience

* **Objective Mediation:** The system can process inputs from both partners simultaneously, cross-reference them, and provide neutral, balanced perspectives without taking sides.

* **Contextual Continuity:** With built-in memory capabilities, the system maintains structured context across sessions, recognizing patterns in behavior or recurring arguments that a stateless LLM would forget.

* **Responsible AI Guardrails:** Built with safety first. The system includes strict monitoring for crisis situations (abuse, self-harm, severe distress) with automatic routing to human professionals.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Counseling Coordinator                      │
│              (Root Agent - Orchestrator + Memory)               │
│                  11 Specialist Sub-Agents                       │
│                    31 Specialized Tools                         │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    Core Agents          Assessment          Growth & Healing
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│    Active    │    │ Relationship │    │   Conflict   │
│  Listening   │    │ Assessment   │    │ Resolution   │
├──────────────┤    ├──────────────┤    ├──────────────┤
│   Emotion    │    │  Goal        │    │   Values     │
│  Analysis    │    │  Setting     │    │ Alignment    │
├──────────────┤    ├──────────────┤    ├──────────────┤
│  Resource    │    │   Repair     │    │  Intimacy    │
│  Provider    │    │  & Healing   │    │  Specialist  │
└──────────────┘    └──────────────┘    ├──────────────┤
                                        │   Boundary   │
                                        │  Specialist  │
                                        ├──────────────┤
                                        │   Stress     │
                                        │ Management   │
                                        └──────────────┘
```

## Features

### Core Capabilities
- **Active Listening**: Empathetic reflection and validation
- **Emotion Analysis**: Pattern recognition and emotional insight
- **Resource Provision**: Communication exercises and proven strategies
- **Memory & Context**: Remembers past conversations for personalized support

### Relationship Assessment
- **10-Dimension Health Evaluation**: Communication, intimacy, trust, conflict resolution, commitment, shared values, life vision, physical connection, financial partnership, and stress management
- **Relationship Stage Identification**: Honeymoon, power struggle, stability, crisis, or renewal
- **Comprehensive Reporting**: Detailed assessment with actionable recommendations

### Goal Setting & Growth
- **SMART Goal Framework**: Specific, Measurable, Achievable, Relevant, Time-bound goals
- **Shared Vision Creation**: Align on life direction and dreams together
- **Progress Tracking**: Monitor and celebrate relationship growth
- **Action Planning**: Daily, weekly, and monthly actionable steps

### Conflict Resolution
- **Pattern Analysis**: Identify pursue-withdraw, escalation, avoidance cycles
- **De-escalation Techniques**: Immediate tools for reducing tension
- **Structured Resolution**: 6-step framework for solving specific conflicts
- **Post-Conflict Repair**: Reconnection and healing processes

### Values & Life Alignment
- **Personal Values Discovery**: 8 categories of life values
- **Shared Values Mapping**: Find common ground and complementary differences
- **Value Conflict Navigation**: Finances, family, lifestyle, career alignment
- **Life Vision Creation**: Build shared meaning and direction

### Repair & Healing
- **Repair Process Guidance**: Navigate betrayal, emotional distance, disrespect
- **Sincere Apology Framework**: 6-component effective apologies
- **Forgiveness Support**: Decision, process, and outcome stages
- **Trust Rebuilding**: After infidelity, deception, broken promises

### Intimacy Building
- **Emotional Intimacy**: Daily practices and deepening exercises
- **Physical Intimacy**: Healthy affection, communication, and safety
- **Quality Time Planning**: Daily to annual shared experiences
- **Fondness & Admiration**: Strengthen friendship and appreciation

### Boundary Setting
- **Assertive Communication**: Set healthy limits respectfully
- **Personal Boundaries**: Explore and define your needs
- **Violation Addressing**: Handle when boundaries are crossed
- **Family Boundaries**: Navigate extended family and in-law relationships
- **Autonomy in Togetherness**: Balance we with me

### Stress Management
- **External Stressors**: Work, financial, family, health pressures
- **Work-Life Balance**: Protect relationship from career demands
- **Life Transitions**: New parenthood, job changes, relocation, grief
- **Resilience Building**: Strengthen capacity to handle challenges

### Safety First
- **Crisis Detection**: Suicide, domestic violence, severe mental health
- **Immediate Resources**: Hotlines and emergency contacts
- **Professional Referral**: When to seek human therapy
- **Safety Planning**: Protection and support protocols

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

# Run end-to-end evaluation
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

### When to Seek Professional Help

The agent will recommend professional counseling for:
- Ongoing abuse or safety concerns
- Severe mental health conditions
- Deep-seated trauma
- Complex relationship patterns requiring therapy
- When issues persist despite best efforts

## Project Structure

```
marriage-counselor-agent/
├── marriage_counselor/
│   ├── __init__.py
│   ├── agent.py                 # Root agent with 11 sub-agents
│   ├── config.py                # Configuration & environment
│   ├── prompts.py               # System prompts & instructions
│   ├── sub_agents/              # 11 Specialist agents
│   │   ├── active_listening.py  # Empathetic reflection
│   │   ├── emotion_analysis.py  # Pattern recognition
│   │   ├── resource_provider.py # Frameworks & strategies
│   │   ├── relationship_assessment.py # Health evaluation
│   │   ├── goal_setting.py      # SMART goals & vision
│   │   ├── conflict_resolution.py # De-escalation & repair
│   │   ├── values_alignment.py  # Shared values discovery
│   │   ├── repair_healing.py    # Forgiveness & trust
│   │   ├── intimacy_specialist.py # Connection building
│   │   ├── boundary_specialist.py # Healthy limits
│   │   └── stress_management.py # External pressures
│   ├── tools/                   # 31 Specialized tools
│   │   ├── communication_tools.py
│   │   ├── emotion_tools.py
│   │   ├── safety_tools.py
│   │   ├── relationship_assessment_tools.py
│   │   ├── goal_setting_tools.py
│   │   ├── conflict_resolution_tools.py
│   │   ├── values_tools.py
│   │   ├── repair_tools.py
│   │   ├── intimacy_tools.py
│   │   ├── boundary_tools.py
│   │   └── stress_tools.py
│   ├── callbacks/               # Safety callbacks
│   └── schemas/                 # Input/output schemas
├── tests/
│   ├── unit/                    # 49 unit tests
│   └── eval/                    # 9 evaluation tests
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
2. Add type hints and comprehensive docstrings
3. Import in `tools/__init__.py`
4. Add to appropriate agent's `tools` list
5. Add unit tests in `tests/unit/test_tools.py`

### Adding New Sub-Agents

1. Create agent file in `marriage_counselor/sub_agents/`
2. Define agent with LlmAgent, instruction, and tools
3. Import in `sub_agents/__init__.py`
4. Add as AgentTool to coordinator in `agent.py`
5. Add evaluation tests in `tests/eval/test_agent_eval.py`

### Testing Guidelines

- Unit tests should verify tool outputs have expected structure
- Evaluation tests should verify agent behavior with real inputs
- All tests must pass before merging changes
- Test coverage should increase with new features

## System Capabilities Summary

| Component | Count | Description |
|-----------|-------|-------------|
| **Sub-Agents** | 11 | Specialized AI agents for each domain |
| **Tools** | 31 | Functions providing expert frameworks |
| **Tool Categories** | 8 | Communication, emotion, safety, assessment, goals, conflict, values, repair, intimacy, boundaries, stress |
| **Unit Tests** | 49 | Tests for all tool functions |
| **Evaluation Tests** | 9 | End-to-end agent behavior tests |
| **Memory** | ✓ | Long-term conversation context |

## License

Copyright 2025 Google LLC

Apache License 2.0

## Support

For issues and questions:
- Review the ADK documentation: https://google.github.io/adk-docs/
- Google ADK GitHub: https://github.com/google/adk
- Check samples: https://github.com/google/adk-samples
