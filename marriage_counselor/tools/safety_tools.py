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

"""Safety tools for crisis detection and resource provision."""

from typing import Dict, List, Any


# Crisis indicators that require immediate intervention
CRISIS_INDICATORS = {
    "suicide_self_harm": [
        "suicide", "kill myself", "end my life", "ending my life", "end it all",
        "hurt myself", "self-harm", "cutting", "want to die",
        "not worth living", "better off dead", "suicidal",
    ],
    "domestic_violence": [
        "abuse", "abusive", "violence", "violent", "afraid",
        "scared of my partner", "fear for my safety", "threatened",
        "physical harm", "hit me", "hurts me", "controlling",
    ],
    "severe_mental_health": [
        "hallucinating", "psychosis", "breakdown", "can't cope",
        "completely lost control", "having a breakdown",
    ],
    "child_abuse": [
        "abuse my child", "hurt my child", "harm my child",
        "children in danger", "unsafe for children",
    ],
}

# Crisis resources
CRISIS_RESOURCES = {
    "national": [
        {
            "name": "Suicide & Crisis Lifeline",
            "contact": "Call or text 988",
            "description": "24/7 free, confidential support for people in distress",
        },
        {
            "name": "Crisis Text Line",
            "contact": "Text HOME to 741741",
            "description": "24/7 crisis support via text message",
        },
    ],
    "domestic_violence": [
        {
            "name": "National Domestic Violence Hotline",
            "contact": "1-800-799-7233 (TTY: 1-800-787-3224)",
            "description": "24/7 support for anyone experiencing domestic violence",
            "website": "www.thehotline.org",
        },
    ],
    "emergency": [
        {
            "name": "Emergency Services",
            "contact": "911",
            "description": "For immediate danger or medical emergencies",
        },
    ],
}

# Professional referral triggers
PROFESSIONAL_REFERRAL_TRIGGERS = [
    "thinking about ending my marriage",
    "considering divorce",
    "want to separate",
    "can't stop fighting",
    "nothing helps",
    "therapy",
    "counselor",
    "professional help",
]


def check_crisis_indicators(text: str) -> Dict[str, Any]:
    """
    Checks if the text contains crisis indicators.

    Args:
        text: The text to check for crisis indicators

    Returns:
        Dictionary with crisis_detected, crisis_type, and severity
    """
    text_lower = text.lower()

    for crisis_type, indicators in CRISIS_INDICATORS.items():
        for indicator in indicators:
            if indicator in text_lower:
                severity = "high" if crisis_type in ["suicide_self_harm", "domestic_violence", "child_abuse"] else "moderate"
                return {
                    "crisis_detected": True,
                    "crisis_type": crisis_type,
                    "severity": severity,
                    "indicator_found": indicator,
                }

    return {
        "crisis_detected": False,
        "crisis_type": None,
        "severity": "none",
    }


def get_crisis_resources(crisis_type: str = None) -> Dict[str, Any]:
    """
    Gets appropriate crisis resources based on crisis type.

    Args:
        crisis_type: The type of crisis (optional)

    Returns:
        Dictionary with crisis resources and support message
    """
    resources = []

    # Always include emergency resources
    resources.extend(CRISIS_RESOURCES["emergency"])

    # Add type-specific resources
    if crisis_type == "domestic_violence":
        resources.extend(CRISIS_RESOURCES["domestic_violence"])
    elif crisis_type == "child_abuse":
        resources.append({
            "name": "Childhelp National Child Abuse Hotline",
            "contact": "1-800-4-A-CHILD (1-800-422-4453)",
            "description": "24/7 professional support for child abuse concerns",
        })
    elif crisis_type == "suicide_self_harm":
        resources.extend(CRISIS_RESOURCES["national"])

    # Always include general crisis resources
    if crisis_type != "suicide_self_harm":
        resources.extend(CRISIS_RESOURCES["national"])

    support_message = f"""
Thank you for sharing something so important with me. Your safety and wellbeing matter.

Based on what you've shared, I want to make sure you have access to immediate support:

IMMEDIATE RESOURCES:
"""

    for resource in resources:
        support_message += f"\n• {resource['name']}: {resource['contact']}"
        if "description" in resource:
            support_message += f"\n  {resource['description']}"
        if "website" in resource:
            support_message += f"\n  Website: {resource['website']}"
        support_message += "\n"

    support_message += """
You deserve support from people who can help you through this. These resources
are available 24/7, free, and confidential.

Reaching out for help is a sign of strength, not weakness. Please consider
contacting one of these resources today.

Would you like me to help you find additional support in your area?
"""

    return {
        "resources": resources,
        "support_message": support_message.strip(),
        "requires_immediate_action": True,
    }


def check_resource_safety(resource: str) -> Dict[str, Any]:
    """
    Validates that a resource is appropriate and safe.

    Args:
        resource: The suggested resource to validate

    Returns:
        Dictionary with safety status and warnings
    """
    # Resources that should always include professional referral
    requires_professional = [
        "divorce", "separation", "abuse", "violence",
        "addiction", "mental health condition", "trauma",
        "suicide", "self-harm",
    ]

    resource_lower = resource.lower()

    warnings = []
    requires_professional_help = False

    for term in requires_professional:
        if term in resource_lower:
            requires_professional_help = True
            warnings.append(f"This topic involving '{term}' is best addressed with a licensed professional.")

    return {
        "safe": True,
        "warnings": warnings,
        "requires_professional": requires_professional_help,
        "referral_message": (
            "For this specific concern, I strongly recommend working with a licensed "
            "therapist or counselor who can provide personalized, professional support."
            if requires_professional_help else None
        ),
    }


def check_professional_referral_needed(text: str) -> Dict[str, Any]:
    """
    Checks if professional referral should be recommended.

    Args:
        text: The text to check

    Returns:
        Dictionary with referral recommendation
    """
    text_lower = text.lower()

    for trigger in PROFESSIONAL_REFERRAL_TRIGGERS:
        if trigger in text_lower:
            return {
                "referral_recommended": True,
                "trigger": trigger,
                "message": (
                    "For the concerns you've shared, I'd recommend speaking with a "
                    "licensed marriage and family therapist. They can provide personalized "
                    "guidance and support tailored to your specific situation."
                ),
            }

    return {
        "referral_recommended": False,
        "trigger": None,
        "message": None,
    }


def get_coping_strategy(challenge: str, severity: str = "moderate") -> Dict[str, Any]:
    """
    Gets coping strategies for specific challenges.

    Args:
        challenge: The challenge or stressor
        severity: Severity level (mild, moderate, severe)

    Returns:
        Dictionary with coping strategy details
    """
    challenge_lower = challenge.lower()

    # For severe situations, recommend professional help
    if severity == "severe":
        return {
            "strategy_name": "Professional Support",
            "description": "For severe challenges, professional support is most effective",
            "techniques": [
                "Contact a licensed therapist or counselor",
                "Reach out to your support system",
                "Consider a support group",
                "Practice basic self-care while seeking help",
            ],
            "timing_suggestions": [
                "Seek professional help as soon as possible",
                "Build a support team gradually",
            ],
            "additional_resources": [
                "Psychology Today: Find a Therapist",
                "American Association for Marriage and Family Therapy",
                "National Alliance on Mental Illness (NAMI)",
            ],
        }

    # Challenge-specific strategies
    strategies = {
        "communication": {
            "strategy_name": "Constructive Communication",
            "description": "Approach communication with intention and care",
            "techniques": [
                "Use 'I' statements to express feelings",
                "Practice active listening without interruption",
                "Choose the right time for difficult conversations",
                "Take breaks if emotions get too intense",
                "Focus on understanding, not winning",
            ],
            "timing_suggestions": [
                "Have important conversations when both are calm",
                "Avoid discussing difficult topics when tired or stressed",
                "Set time limits for challenging discussions",
            ],
            "additional_resources": [
                "Nonviolent Communication (NVC) by Marshall Rosenberg",
                "Crucial Conversations by Patterson et al.",
            ],
        },
        "stress": {
            "strategy_name": "Stress Management",
            "description": "Build resilience and manage stress effectively",
            "techniques": [
                "Practice deep breathing: 4-7-8 breathing technique",
                "Engage in regular physical activity",
                "Maintain a consistent sleep schedule",
                "Practice mindfulness or meditation",
                "Connect with supportive friends or family",
            ],
            "timing_suggestions": [
                "Practice stress reduction daily, even for 5-10 minutes",
                "Use stress management techniques before conversations",
                "Take stress breaks during the day",
            ],
            "additional_resources": [
                "Headspace or Calm for guided meditation",
                "The Stress-Proof Brain by Melanie Greenberg",
            ],
        },
        "conflict": {
            "strategy_name": "Healthy Conflict Resolution",
            "description": "Navigate disagreements constructively",
            "techniques": [
                "Focus on the issue, not the person",
                "Use 'soft start-ups' to discussions",
                "Take responsibility for your part",
                "Look for compromise and win-win solutions",
                "Know when to take a timeout",
            ],
            "timing_suggestions": [
                "Address conflicts sooner rather than later",
                "Choose times when both have emotional capacity",
                "Return to unresolved conflicts after cooling down",
            ],
            "additional_resources": [
                "The Seven Principles for Making Marriage Work by John Gottman",
                "Hold Me Tight by Sue Johnson",
            ],
        },
        "emotional": {
            "strategy_name": "Emotional Regulation",
            "description": "Understand and manage your emotions effectively",
            "techniques": [
                "Name your emotions to tame them",
                "Practice the STOP technique: Stop, Take a breath, Observe, Proceed",
                "Journal about your feelings",
                "Allow yourself to feel without judgment",
                "Reach out when emotions feel overwhelming",
            ],
            "timing_suggestions": [
                "Check in with your emotions regularly",
                "Process emotions before important conversations",
                "Allow time for emotional processing after difficult events",
            ],
            "additional_resources": [
                "Emotional Intelligence by Daniel Goleman",
                "Atlas of the Heart by Brené Brown",
            ],
        },
    }

    # Find matching strategy
    for key, strategy in strategies.items():
        if key in challenge_lower:
            return strategy

    # Default strategy
    return {
        "strategy_name": "General Coping Strategies",
        "description": "Build resilience and healthy coping habits",
        "techniques": [
            "Practice self-compassion",
            "Maintain social connections",
            "Engage in activities that bring you joy",
            "Set realistic expectations",
            "Ask for help when you need it",
        ],
        "timing_suggestions": [
            "Incorporate coping strategies into daily routines",
            "Practice self-care regularly, not just in crisis",
        ],
        "additional_resources": [
            "Consider speaking with a mental health professional",
            "Build a support network of trusted people",
        ],
    }
