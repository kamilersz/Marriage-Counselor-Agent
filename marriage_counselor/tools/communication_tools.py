# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Communication and reflection tools for the Marriage Counselor agents."""

import random
from typing import Dict, Any


def reflect_feelings(feeling: str, context: str) -> Dict[str, str]:
    """
    Reflects back the user's feeling with validation.

    Args:
        feeling: The emotion the user is experiencing
        context: The situation or context for the feeling

    Returns:
        A dictionary with reflective validation statement
    """
    reflection_templates = [
        f"It sounds like you're feeling {feeling} about {context}. That makes sense given what you've shared.",
        f"I hear that {context} is bringing up {feeling} for you. Thank you for sharing that.",
        f"It seems like {context} has been really {feeling} for you. Your feelings are valid.",
        f"I can hear how {feeling} you are about {context}. It takes courage to share that.",
    ]

    return {
        "reflection": random.choice(reflection_templates),
        "validation": f"Your feeling of {feeling} is understandable in this situation.",
    }


def validate_experience(experience: str) -> Dict[str, str]:
    """
    Validates the user's experience without judgment.

    Args:
        experience: The experience the user has shared

    Returns:
        A dictionary with validation statement
    """
    validation_templates = [
        f"What you're experiencing with {experience} is valid and important.",
        f"Your experience with {experience} matters, and I'm glad you felt safe enough to share it.",
        f"I want you to know that what you're going through with {experience} deserves attention and care.",
        f"Thank you for trusting me with your experience about {experience}. Your feelings are completely valid.",
    ]

    return {
        "validation": random.choice(validation_templates),
        "acknowledgment": "It takes courage to share what you're going through.",
    }


def get_communication_exercise(topic: str) -> Dict[str, Any]:
    """
    Retrieves a communication exercise for the given topic.

    Args:
        topic: The relationship area to work on (e.g., "conflict", "intimacy", "trust")

    Returns:
        Dictionary with exercise details
    """
    exercises = {
        "conflict": {
            "name": "I-Statements Practice",
            "description": "Learn to express feelings without blame using 'I' statements.",
            "steps": [
                "Take turns sharing without interruption",
                "Use the format: 'I feel... when... because... I need...'",
                "Listener reflects back what they heard before responding",
                "Switch roles and repeat",
            ],
            "duration": "15-20 minutes",
            "tips": [
                "Focus on your own feelings, not your partner's behavior",
                "Avoid using 'you' statements that can sound accusatory",
                "Be specific about the situation and your feelings",
                "Keep needs constructive and actionable",
            ],
            "benefits": "Reduces defensiveness and increases understanding between partners.",
        },
        "intimacy": {
            "name": "Daily Check-In",
            "description": "Build emotional connection through daily meaningful conversations.",
            "steps": [
                "Set aside 10-15 minutes of uninterrupted time",
                "Each person shares: one high, one low, one hope",
                "Practice active listening without problem-solving",
                "End with appreciation or affirmation",
            ],
            "duration": "10-15 minutes daily",
            "tips": [
                "Put phones away and eliminate distractions",
                "Listen to understand, not to respond",
                "Validate feelings even if you don't agree",
                "Be consistent with timing",
            ],
            "benefits": "Builds emotional intimacy and keeps partners connected.",
        },
        "trust": {
            "name": "Trust-Building Conversation",
            "description": "Have an open conversation about what trust means to each of you.",
            "steps": [
                "Each person defines what trust means to them",
                "Share what behaviors build trust for you",
                "Discuss what actions break trust",
                "Identify one small commitment to build trust",
            ],
            "duration": "20-30 minutes",
            "tips": [
                "Approach with curiosity, not judgment",
                "Remember that trust means different things to different people",
                "Focus on understanding before problem-solving",
                "Be honest about your own needs",
            ],
            "benefits": "Creates shared understanding and concrete steps to build trust.",
        },
        "listening": {
            "name": "Mirroring Exercise",
            "description": "Practice deep listening by mirroring back what your partner says.",
            "steps": [
                "Partner A shares for 2-3 minutes",
                "Partner B mirrors back: 'What I heard you say is...'",
                "Partner A confirms or clarifies",
                "Partner B validates: 'That makes sense because...'",
                "Switch roles and repeat",
            ],
            "duration": "15-20 minutes",
            "tips": [
                "Don't interrupt while your partner is sharing",
                "Focus on understanding, not preparing your response",
                "If you get it wrong, ask your partner to clarify",
                "Validation doesn't mean agreement, just understanding",
            ],
            "benefits": "Improves listening skills and helps partners feel truly heard.",
        },
    }

    return exercises.get(
        topic.lower(),
        exercises["conflict"]  # Default to conflict resolution
    )


def get_journaling_prompt(focus: str, mood: str = "neutral") -> Dict[str, str]:
    """
    Generates a journaling prompt based on focus area and mood.

    Args:
        focus: The focus area for journaling
        mood: User's current mood for context

    Returns:
        Dictionary with journaling prompt
    """
    prompts = {
        "emotions": [
            "What emotions am I feeling right now? Where do I feel them in my body?",
            "What emotion have I been avoiding lately? What might happen if I allowed myself to feel it?",
            "Describe a recent moment when you felt fully understood. What made it special?",
            "What emotion do I wish I could express more freely? What holds me back?",
        ],
        "relationships": [
            "What do I appreciate most about my partner today?",
            "Describe a conflict from my partner's perspective. What might they be feeling?",
            "What patterns do I notice in how I react during disagreements?",
            "What would I like my partner to understand about me that they might not know?",
        ],
        "self-reflection": [
            "What are my core needs in my relationship? Are they being met?",
            "What boundaries do I need to set or maintain for my wellbeing?",
            "What parts of myself do I hide in my relationship? Why?",
            "What am I learning about myself through my relationship challenges?",
        ],
        "gratitude": [
            "List three things about my relationship that I'm grateful for.",
            "What moment of connection did I share today? What made it meaningful?",
            "What qualities do I appreciate in myself as a partner?",
        ],
        "growth": [
            "What have I learned about relationships in the past year?",
            "What old patterns am I ready to release?",
            "What would my relationship look like if I responded from my best self?",
            "What small step can I take today to improve my relationship?",
        ],
    }

    focus_prompts = prompts.get(focus.lower(), prompts["emotions"])

    if mood.lower() == "stressed":
        additional = " Take your time and be gentle with yourself as you write."
    elif mood.lower() == "sad":
        additional = " Remember, it's okay to feel whatever comes up."
    elif mood.lower() == "hopeful":
        additional = " Let your hope and optimism guide your reflection."
    else:
        additional = " Allow yourself to be honest and curious."

    return {
        "prompt": random.choice(focus_prompts) + additional,
        "suggested_duration": "10-15 minutes",
    }
