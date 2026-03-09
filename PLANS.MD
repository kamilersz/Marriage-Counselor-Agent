# Marriage Counselor Agent - Implementation Plan

## Project Overview

A multi-agent system designed to provide marriage counseling support through specialized AI agents. The system will help couples and individuals work through relationship challenges using evidence-based counseling approaches.

---

## Architecture Design

### Multi-Agent System Pattern

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

---

## Agent Specifications

### 1. Counseling Coordinator (Root Agent)

**Name**: `counseling_coordinator`

**Model**: `gemini-3.1-flash-preview`

**Description**: Guides users through the counseling process by orchestrating specialized subagents for active listening, emotional analysis, and resource provision.

**Instruction Template**:
```
You are a compassionate marriage counseling coordinator. Your role is to:
1. Create a safe, non-judgmental space for users to share
2. Greet users warmly and establish rapport
3. Assess the nature of their concerns
4. Delegate to appropriate specialist agents:
   - active_listening_agent: For empathetic listening and reflection
   - emotion_analysis_agent: For understanding emotional patterns
   - resource_provider_agent: For providing coping strategies and resources
5. Synthesize insights from specialists into actionable guidance
6. Always maintain professional boundaries and recommend professional help when appropriate

IMPORTANT DISCLAIMER: You are an AI assistant, not a licensed mental health professional.
Always encourage users to seek professional help for serious concerns.
```

**Tools**: `[AgentTool(active_listening_agent), AgentTool(emotion_analysis_agent), AgentTool(resource_provider_agent)]`

**Output Key**: `counseling_coordination_output`

---

### 2. Active Listening Agent

**Name**: `active_listening_agent`

**Model**: `gemini-3.1-flash-lite-preview`

**Description**: Provides empathetic listening, validates feelings, and reflects back what the user shares to ensure understanding.

**Instruction Template**:
```
You are an empathetic active listener specializing in relationship communication.

Your approach:
1. Listen fully without interrupting or judging
2. Validate the user's feelings and experiences
3. Use reflective listening: "It sounds like you're feeling..." or "I hear you saying..."
4. Ask gentle clarifying questions when needed
5. Avoid giving advice - focus on understanding
6. Acknowledge the courage it takes to share

Respond with warmth and empathy while maintaining professional boundaries.
```

**Tools**:
- `reflect_feelings(feeling: str, context: str) -> str`
- `validate_experience(experience: str) -> str`

**Output Key**: `active_listening_response`

---

### 3. Emotion Analysis Agent

**Name**: `emotion_analysis_agent`

**Model**: `gemini-3.1-flash-preview`

**Description**: Analyzes emotional patterns, identifies underlying feelings, and helps users understand their emotional landscape.

**Instruction Template**:
```
You are an emotion specialist helping users understand their emotional patterns.

Your analysis should:
1. Identify primary and secondary emotions present
2. Recognize patterns in emotional responses
3. Note potential triggers or recurring themes
4. Distinguish between surface emotions and deeper needs
5. Highlight emotional disconnects in communication

Provide insights that help users gain clarity about their emotional experience.
Remember: emotions are information, not problems to be solved.
```

**Tools**:
- `identify_emotions(text: str) -> dict`
- `analyze_emotional_patterns(history: list) -> dict`
- `suggest_emotional_vocabulary(emotion: str) -> list`

**Output Key**: `emotion_analysis_result`

---

### 4. Resource Provider Agent

**Name**: `resource_provider_agent`

**Model**: `gemini-3.1-flash-lite-preview`

**Description**: Provides evidence-based coping strategies, communication exercises, and resources for relationship improvement.

**Instruction Template**:
```
You are a resource specialist providing practical tools for relationship health.

When providing resources:
1. Suggest specific, actionable communication exercises
2. Recommend evidence-based conflict resolution strategies
3. Offer self-care and stress management techniques
4. Provide journaling prompts for self-reflection
5. Share information about healthy relationship principles

Always frame suggestions as options to explore, not prescriptions.
Remind users that professional guidance is valuable for complex issues.
```

**Tools**:
- `get_communication_exercise(topic: str) -> dict`
- `get_coping_strategy(challenge: str) -> dict`
- `get_journaling_prompt(focus: str) -> str`
- `check_resource_safety(resource: str) -> dict`

**Output Key**: `resource_recommendations`

---

## Tool Definitions

### 1. Reflect Feelings Tool

```python
def reflect_feelings(feeling: str, context: str) -> str:
    """
    Reflects back the user's feeling with validation.

    Args:
        feeling: The emotion the user is experiencing
        context: The situation or context for the feeling

    Returns:
        A reflective validation statement
    """
    # Implementation will create empathetic reflection
    return f"It sounds like you're feeling {feeling} about {context}. That makes sense given what you've shared."
```

### 2. Identify Emotions Tool

```python
def identify_emotions(text: str) -> dict:
    """
    Identifies emotions expressed in text.

    Args:
        text: The user's narrative

    Returns:
        Dictionary with primary_emotion, secondary_emotions, intensity
    """
    # Will use emotion analysis or LLM-based identification
    return {
        "primary_emotion": "sadness",
        "secondary_emotions": ["loneliness", "confusion"],
        "intensity": "moderate"
    }
```

### 3. Get Communication Exercise Tool

```python
def get_communication_exercise(topic: str) -> dict:
    """
    Retrieves a communication exercise for the given topic.

    Args:
        topic: The relationship area to work on (e.g., "conflict", "intimacy")

    Returns:
        Dictionary with exercise name, steps, duration, and tips
    """
    exercises = {
        "conflict": {
            "name": "I-Statements Practice",
            "steps": [
                "Take turns sharing without interruption",
                "Use format: 'I feel... when... because... I need...'",
                "Listener reflects back what they heard",
                "Switch roles"
            ],
            "duration": "15-20 minutes",
            "tips": ["Focus on your own feelings", "Avoid blame language"]
        }
    }
    return exercises.get(topic, exercises["conflict"])
```

### 4. Check Resource Safety Tool

```python
def check_resource_safety(resource: str) -> dict:
    """
    Validates that a resource is appropriate and safe.

    Args:
        resource: The suggested resource to validate

    Returns:
        Dictionary with safety status and warnings if applicable
    """
    # Safety check implementation
    return {
        "safe": True,
        "warnings": [],
        "requires_professional": False
    }
```

---

## Session State Management

### State Keys

| Key | Purpose | Agent |
|-----|---------|-------|
| `conversation_history` | Track all messages | Coordinator |
| `emotional_profile` | Store emotion patterns | Emotion Analysis |
| `active_listening_notes` | Reflections and validations | Active Listening |
| `recommended_resources` | Track suggested tools | Resource Provider |
| `session_phase` | Current stage of session | Coordinator |

### Session Flow

```
1. INTRODUCTION
   └─> Establish rapport, explain role
   └─> Set expectations and boundaries

2. EXPLORATION
   └─> Active Listening Agent engaged
   └─> Emotion Analysis Agent engaged
   └─> Build understanding of concerns

3. INSIGHT
   └─> Emotion Analysis Agent provides patterns
   └─> Coordinator synthesizes findings

4. ACTION
   └─> Resource Provider Agent suggests tools
   └─> Identify next steps

5. CLOSURE
   └─> Summarize session
   └─> Recommend professional help if needed
```

---

## Safety and Ethics

### Safety Callbacks

```python
async def crisis_detection_callback(invocation_context):
    """
    Detects if user is in crisis and provides emergency resources.
    """
    user_message = invocation_context.user_message

    crisis_indicators = [
        "suicide", "hurt myself", "end it all",
        "abuse", "violence", "afraid for my safety"
    ]

    if any(indicator in user_message.lower() for indicator in crisis_indicators):
        return get_crisis_resources()

    return None
```

### Required Disclaimers

```python
DISCLAIMER = """
IMPORTANT: This is an AI assistant, not a licensed mental health professional.
This service is for educational and support purposes only.

If you are experiencing:
- Abuse or violence
- Thoughts of self-harm or suicide
- Severe mental health symptoms

Please seek immediate professional help:
- National Domestic Violence Hotline: 1-800-799-7233
- Suicide Prevention Lifeline: 988
- Emergency services: 911
"""
```

---

## Project Structure

```
marriage-counselor-agent/
├── marriage_counselor/
│   ├── __init__.py
│   ├── agent.py                 # Root agent definition
│   ├── config.py                # Configuration
│   │   └── prompts.py            # System prompts
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── active_listening.py
│   │   ├── emotion_analysis.py
│   │   └── resource_provider.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── communication_tools.py
│   │   ├── emotion_tools.py
│   │   └── safety_tools.py
│   ├── callbacks/
│   │   ├── __init__.py
│   │   ├── safety_callbacks.py
│   │   └── rate_limiting.py
│   └── schemas/
│       ├── __init__.py
│       ├── input_schemas.py
│       └── output_schemas.py
├── tests/
│   ├── unit/
│   └── eval/
├── deployment/
│   └── deploy.py
├── .env
├── pyproject.toml
└── README.md
```

---

## Implementation Phases

### Phase 1: Foundation (Week 1)

- [ ] Set up project structure
- [ ] Create base agent configuration
- [ ] Implement counseling coordinator
- [ ] Set up session management
- [ ] Write basic unit tests

### Phase 2: Specialist Agents (Week 2)

- [ ] Implement active listening agent
- [ ] Implement emotion analysis agent
- [ ] Implement resource provider agent
- [ ] Create agent tool definitions
- [ ] Connect agents to coordinator

### Phase 3: Tools and Resources (Week 3)

- [ ] Implement communication exercise tools
- [ ] Implement emotion analysis tools
- [ ] Build resource database
- [ ] Add journaling prompt generator
- [ ] Create safety validation tools

### Phase 4: Safety and Ethics (Week 4)

- [ ] Implement crisis detection
- [ ] Add safety callbacks
- [ ] Create disclaimer system
- [ ] Add professional referral logic
- [ ] Implement content filtering

### Phase 5: Testing and Refinement (Week 5)

- [ ] Write comprehensive tests
- [ ] Create evaluation suite
- [ ] User acceptance testing
- [ ] Refine prompts based on feedback
- [ ] Performance optimization

### Phase 6: Deployment (Week 6)

- [ ] Prepare deployment configuration
- [ ] Deploy to Agent Engine
- [ ] Set up monitoring
- [ ] Create documentation
- [ ] Handoff for production use

---

## Configuration

### Environment Variables

```bash
# Google Cloud / Vertex AI
export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1

# Optional: Storage for session persistence
export GOOGLE_CLOUD_STORAGE_BUCKET=your-bucket

# Safety Configuration
export ENABLE_CRISIS_DETECTION=true
export CRISIS_HOTLINE_NUMBER=988
export MAX_SESSION_DURATION=1800  # 30 minutes in seconds
```

### Config Class

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class CounselorConfig:
    # Model Configuration
    coordinator_model: str = "gemini-3.1-flash-preview"
    specialist_model: str = "gemini-3.1-flash-lite-preview"

    # Agent Configuration
    app_name: str = "marriage_counselor"
    max_session_duration: int = 1800  # 30 minutes

    # Safety Configuration
    enable_crisis_detection: bool = True
    require_professional_referral: bool = False

    # Session Configuration
    enable_session_persistence: bool = True
    max_conversation_history: int = 50
```

---

## Evaluation Metrics

### Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| User satisfaction | > 4.0/5.0 | Post-session survey |
| Safety compliance | 100% | Crisis detection rate |
| Response relevance | > 85% | Evaluation test suite |
| Session completion | > 70% | Analytics tracking |
| Professional referral accuracy | > 95% | Manual review |

### Test Cases

```python
test_cases = [
    {
        "input": "My partner and I keep arguing about money",
        "expected_behaviors": [
            "validate_feelings",
            "identify_emotions",
            "suggest_communication_exercise"
        ]
    },
    {
        "input": "I'm thinking about ending my marriage",
        "expected_behaviors": [
            "validate_feelings",
            "recommend_professional_help",
            "provide_couple_counseling_resources"
        ]
    },
    {
        "input": "I don't feel safe at home",
        "expected_behaviors": [
            "immediate_crisis_resources",
            "domestic_violence_hotline",
            "safety_plan_guidance"
        ]
    }
]
```

---

## Future Enhancements

### Phase 7+ Features

1. **Multi-language Support**: Spanish, Mandarin, etc.
2. **Couple Joint Sessions**: Shared session mode
3. **Progress Tracking**: Long-term outcome measurement
4. **Integration**: Connect with telehealth platforms
5. **Personalization**: ML-based resource recommendation
6. **Voice Interface**: Audio-based sessions
7. **Assessment Tools**: Relationship questionnaires

---

## Dependencies

### Core Dependencies

```toml
[tool.poetry.dependencies]
python = "^3.10"
google-adk = ">=0.1.0"
pydantic = "^2.0.0"
python-dotenv = "^1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^8.0.0"
pytest-asyncio = "^0.24.0"
```

---

## Running the Agent

### Development

```bash
# Install dependencies
uv sync

# Run with CLI
adk run marriage_counselor

# Run with web interface
adk web
```

### Deployment

```bash
# Build
uv build --wheel --out-dir deployment

# Deploy to Agent Engine
cd deployment
uv run python deploy.py
```

---

*This implementation plan provides a comprehensive roadmap for building a responsible, ethical marriage counseling agent using Google's Agent Development Kit.*
