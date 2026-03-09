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

"""Emotion analysis tools for the Marriage Counselor agents."""

import re
from typing import Dict, List, Any


# Emotion keywords for basic detection
EMOTION_KEYWORDS = {
    "sadness": ["sad", "down", "depressed", "unhappy", "crying", "tears", "hopeless", "empty", "lonely", "grief"],
    "anger": ["angry", "mad", "furious", "rage", "frustrated", "irritated", "annoyed", "resentful"],
    "fear": ["afraid", "scared", "anxious", "worried", "nervous", "terrified", "panic", "dread"],
    "joy": ["happy", "glad", "joyful", "excited", "pleased", "delighted", "grateful", "optimistic"],
    "shame": ["ashamed", "embarrassed", "humiliated", "mortified", "self-conscious"],
    "guilt": ["guilty", "regret", "remorse", "bad", "wrong", "fault"],
    "love": ["love", "caring", "affection", "attached", "connected", "devoted"],
    "disappointment": ["disappointed", "let down", "expectations not met"],
    "hurt": ["hurt", "pain", "wounded", "broken heart", "rejected"],
    "confusion": ["confused", "uncertain", "unsure", "conflict", "torn"],
}

# Emotional needs mapping
EMOTIONAL_NEEDS = {
    "sadness": ["comfort", "support", "connection", "understanding"],
    "anger": ["respect", "fairness", "boundaries", "being heard"],
    "fear": ["safety", "reassurance", "security", "protection"],
    "shame": ["acceptance", "belonging", "worthiness", "forgiveness"],
    "guilt": ["forgiveness", "making amends", "clarification", "learning"],
    "loneliness": ["connection", "belonging", "intimacy", "companionship"],
    "overwhelm": ["support", "space", "help", "understanding"],
    "hurt": ["validation", "care", "understanding", "reassurance"],
}


def identify_emotions(text: str) -> Dict[str, Any]:
    """
    Identifies emotions expressed in text.

    Args:
        text: The user's narrative

    Returns:
        Dictionary with primary_emotion, secondary_emotions, intensity, and validation
    """
    text_lower = text.lower()

    # Count emotion keyword matches
    emotion_scores = {}
    for emotion, keywords in EMOTION_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > 0:
            emotion_scores[emotion] = score

    # Determine primary and secondary emotions
    sorted_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)

    if not sorted_emotions:
        return {
            "primary_emotion": "uncertain",
            "secondary_emotions": [],
            "intensity": "low",
            "emotional_needs": ["understanding", "support"],
            "validation": "Thank you for sharing. It's okay if your feelings aren't clear right now.",
        }

    primary_emotion = sorted_emotions[0][0]
    secondary_emotions = [e[0] for e in sorted_emotions[1:4]]  # Top 3 secondary

    # Determine intensity based on keyword frequency
    total_score = sum(e[1] for e in sorted_emotions)
    if total_score >= 5:
        intensity = "high"
    elif total_score >= 3:
        intensity = "moderate"
    else:
        intensity = "low"

    # Get emotional needs
    emotional_needs = EMOTIONAL_NEEDS.get(primary_emotion, ["understanding", "support"])

    # Create validation statement
    validation_templates = [
        f"It's completely understandable to feel {primary_emotion} in this situation.",
        f"Your {primary_emotion} makes sense given what you've shared.",
        f"Thank you for sharing your {primary_emotion} with me. It takes courage.",
        f"Feeling {primary_emotion} is a valid response to what you're going through.",
    ]

    return {
        "primary_emotion": primary_emotion,
        "secondary_emotions": secondary_emotions,
        "intensity": intensity,
        "emotional_needs": list(set(emotional_needs)),
        "validation": validation_templates[hash(primary_emotion) % len(validation_templates)],
    }


def analyze_emotional_patterns(history: List[str]) -> Dict[str, Any]:
    """
    Analyzes emotional patterns across conversation history.

    Args:
        history: List of conversation messages

    Returns:
        Dictionary with patterns, triggers, themes, and insights
    """
    patterns = []
    triggers = []
    themes = []

    # Analyze patterns based on frequency and repetition
    emotion_counts = {}
    for text in history:
        emotion_result = identify_emotions(text)
        primary = emotion_result["primary_emotion"]
        emotion_counts[primary] = emotion_counts.get(primary, 0) + 1

    # Identify recurring emotions
    for emotion, count in emotion_counts.items():
        if count >= 2:
            patterns.append(f"Recurring feelings of {emotion}")

    # Common triggers based on content analysis
    trigger_keywords = {
        "money": ["money", "finances", "spending", "budget", "debt"],
        "communication": ["talk", "listen", "understand", "communicate", "share"],
        "intimacy": ["close", "intimate", "affection", "sex", "touch"],
        "time": ["time", "busy", "schedule", "together", "apart"],
        "trust": ["trust", "honest", "lie", "secret", "faithful"],
        "family": ["family", "parent", "child", "in-law", "relative"],
    }

    for trigger_name, keywords in trigger_keywords.items():
        for text in history:
            if any(keyword in text.lower() for keyword in keywords):
                if trigger_name not in triggers:
                    triggers.append(trigger_name)
                break

    # Identify themes
    if any("sad" in text.lower() or "lonely" in text.lower() for text in history):
        themes.append("Emotional disconnection")
    if any("angry" in text.lower() or "frustrated" in text.lower() for text in history):
        themes.append("Unresolved conflict")
    if any("talk" in text.lower() for text in history):
        themes.append("Communication challenges")
    if any("trust" in text.lower() for text in history):
        themes.append("Trust concerns")

    # Generate insights
    insights = []
    if patterns:
        insights.append(f"You've mentioned similar feelings before, which suggests this is an ongoing concern.")
    if len(triggers) > 1:
        insights.append(f"Multiple topics seem to trigger emotions: {', '.join(triggers)}.")
    if themes:
        insights.append(f"There are some recurring themes: {', '.join(set(themes))}.")

    if not insights:
        insights.append("Sharing your experiences is an important first step toward understanding your patterns.")

    return {
        "patterns": patterns if patterns else ["Beginning to explore emotional patterns"],
        "triggers": triggers if triggers else ["Still exploring what triggers emotions"],
        "themes": list(set(themes)) if themes else ["Self-discovery and understanding"],
        "insights": insights,
    }


def suggest_emotional_vocabulary(emotion: str) -> Dict[str, List[str]]:
    """
    Suggests more precise emotional vocabulary.

    Args:
        emotion: The general emotion category

    Returns:
        Dictionary with more precise emotion words and their descriptions
    """
    vocabulary = {
        "sadness": {
            "melancholy": "A gentle, ongoing feeling of sadness",
            "heartbroken": "Deep sadness and grief",
            "lonely": "Feeling isolated or disconnected",
            "disappointed": "Sadness about unmet expectations",
            "grieving": "Processing a significant loss",
            "empty": "Feeling hollow or numb",
            "hopeless": "Feeling like things won't improve",
        },
        "anger": {
            "frustrated": "Blocked from achieving something important",
            "resentful": "Unfairly treated or unappreciated",
            "irritated": "Mild annoyance or impatience",
            "furious": "Intense, explosive anger",
            "betrayed": "Anger from broken trust",
            "disrespected": "Not valued or honored",
        },
        "fear": {
            "anxious": "Uneasy or worried about the future",
            "overwhelmed": "Too much to handle or process",
            "insecure": "Unsure or lacking confidence",
            "vulnerable": "Exposed to potential harm",
            "terrified": "Intense, paralyzing fear",
            "apprehensive": "Anxious about something upcoming",
        },
        "love": {
            "cherished": "Valued and cared for deeply",
            "connected": "Bonded and close to someone",
            "appreciated": "Recognized and valued",
            "supported": "Backed and encouraged",
            "accepted": "Received without judgment",
        },
        "confusion": {
            "uncertain": "Not sure what to think or feel",
            "torn": "Pulled between different options or feelings",
            "ambivalent": "Mixed feelings about something",
            "conflicted": "Experiencing opposing emotions",
        },
    }

    emotion_variations = vocabulary.get(
        emotion.lower(),
        vocabulary.get("sadness", {
            "uncertain": "Not sure what you're feeling",
            "mixed": "Multiple emotions at once",
            "processing": "Still understanding your feelings",
        })
    )

    return {
        "emotions": [
            f"{word}: {desc}"
            for word, desc in emotion_variations.items()
        ],
        "guidance": "Using specific emotional words can help you understand and communicate your feelings better.",
    }
