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

"""Values clarification tools for relationship alignment."""

from typing import Dict, List, Any


def identify_personal_values() -> Dict[str, Any]:
    """
    Helps individuals identify their core personal values.

    Returns:
        Dictionary with values exploration framework
    """
    value_categories = {
        "relationship": [
            "loyalty", "honesty", "communication", "quality_time", "affection",
            "respect", "trust", "commitment", "growth", "independence"
        ],
        "family": [
            "family_time", "tradition", "parenting_style", "extended_family",
            "family_routines", "religious_upbringing", "education"
        ],
        "career": [
            "ambition", "work_life_balance", "financial_success", "creativity",
            "leadership", "security", "contribution", "recognition"
        ],
        "lifestyle": [
            "adventure", "stability", "simplicity", "luxury", "health",
            "fitness", "nature", "urban_living", "travel", "home_focus"
        ],
        "financial": [
            "security", "generosity", "frugality", "investment", "experiences",
            "spontaneity", "planning", "risk_tolerance", "sharing"
        ],
        "personal_growth": [
            "learning", "spirituality", "creativity", "self_awareness",
            "health", "mindfulness", "challenges", "comfort_zone"
        ],
        "social": [
            "community", "friendship", "privacy", "social_activities",
            "alone_time", "entertaining", "belonging"
        ],
        "ethical": [
            "integrity", "fairness", "compassion", "justice", "honesty",
            "accountability", "environmental_consciousness", "service"
        ]
    }

    reflection_questions = {
        "priority": [
            "What matters most to you in life?",
            "What would you regret not having or doing?",
            "What do you want your life to stand for?"
        ],
        "daily_life": [
            "What do your choices say about what you value?",
            "How do you spend your time and money?",
            "What frustrates you when it's missing?"
        ],
        "childhood": [
            "What values were important in your family growing up?",
            "What values did you reject from your upbringing?",
            "What values do you share with your family?"
        ],
        "relationship": [
            "What do you need most in a relationship?",
            "What values must your partner share?",
            "What differences in values can you accept?"
        ]
    }

    return {
        "value_categories": value_categories,
        "reflection_questions": reflection_questions,
        "exercise": "Review each category and select your top 3-5 values.",
        "next_step": "Share your top values with your partner and discuss overlaps and differences."
    }


def identify_shared_values(partner1_values: List[str], partner2_values: List[str]) -> Dict[str, Any]:
    """
    Finds common ground and areas of difference between partners.

    Args:
        partner1_values: Values from partner 1
        partner2_values: Values from partner 2

    Returns:
        Dictionary with values comparison and guidance
    """
    # Find shared values
    shared = [v for v in partner1_values if v in partner2_values]

    # Find values unique to each partner
    unique_to_1 = [v for v in partner1_values if v not in partner2_values]
    unique_to_2 = [v for v in partner2_values if v not in partner1_values]

    # Identify potential complementarity
    complementary_pairs = {
        ("stability", "adventure"): "Can balance security with excitement",
        ("ambition", "family_focus"): "Success at work and at home",
        ("social", "privacy"): "Balance of social engagement and alone time",
        ("planning", "spontaneity"): "Structure with room for surprises",
        ("independence", "togetherness"): "Autonomy within connection"
    }

    complementary = []
    for v1 in unique_to_1:
        for v2 in unique_to_2:
            pair = tuple(sorted([v1, v2]))
            if pair in complementary_pairs:
                complementary.append({
                    "values": [v1, v2],
                    "potential": complementary_pairs[pair]
                })

    return {
        "shared_values": shared,
        "shared_significance": f"You have {len(shared)} values in common",
        "unique_to_partner1": unique_to_1,
        "unique_to_partner2": unique_to_2,
        "complementary_opportunities": complementary,
        "guidance": {
            "celebrate_common": f"Your shared values ({', '.join(shared)}) are a strong foundation",
            "discuss_differences": "Different values don't have to divide you - understanding them is key",
            "find_balance": "Look for ways to honor both partners' values",
            "create compromises": "Creative solutions often integrate different perspectives"
        },
        "conversation_starter": "Which shared value most guides your relationship? What different value do you want to better understand?"
    }


def explore_value_conflict(value_area: str) -> Dict[str, Any]:
    """
    Helps navigate conflicts arising from different values.

    Args:
        value_area: The area of value conflict

    Returns:
        Dictionary with conflict exploration framework
    """
    conflict_scenarios = {
        "finances": {
            "common_conflicts": [
                "Spender vs saver",
                "Present enjoyment vs future security",
                "Shared finances vs independence",
                "Risk tolerance differences",
                "Different priorities for spending"
            ],
            "understand_values": [
                "What does money represent to each of you?",
                "What financial experiences shaped you?",
                "What does financial security mean to you?",
                "What financial freedom looks like for you?"
            ],
            "find_common_ground": [
                "Shared financial goals",
                "Values you both want to teach children",
                "What you're working toward together",
                "Non-negotiables you both agree on"
            ],
            "create_solution": [
                "His/hers/ours budget structure",
                "Autonomy amounts for personal spending",
                "Decision thresholds for large purchases",
                "Regular money check-ins"
            ]
        },
        "family": {
            "common_conflicts": [
                "Time with extended family",
                "Family traditions",
                "Parenting differences",
                "Boundaries with in-laws",
                "Holiday priorities"
            ],
            "understand_values": [
                "What role did family play in your upbringing?",
                "What does family mean to you now?",
                "What family traditions matter most?",
                "How do you balance partner and family?"
            ],
            "find_common_ground": [
                "Importance of family to both",
                "Desire for family harmony",
                "Love for your children",
                "Building your own family culture"
            ],
            "create_solution": [
                "Clear boundaries with extended family",
                "Compromise on holiday time",
                "United front with children",
                "Creating new traditions together"
            ]
        },
        "lifestyle": {
            "common_conflicts": [
                "Social vs homebody",
                "Adventure vs routine",
                "Cleanliness standards",
                "Early bird vs night owl",
                "City vs country preference"
            ],
            "understand_values": [
                "What makes you feel alive?",
                "How do you recharge?",
                "What does ideal weekend look like?",
                "What environment helps you thrive?"
            ],
            "find_common_ground": [
                "Wanting each other to be happy",
                "Quality time together (even if different activities)",
                "Creating a comfortable home",
                "Supporting each other's needs"
            ],
            "create_solution": [
                "Solo time for different interests",
                "Compromise on shared activities",
                "Take turns choosing activities",
                "Create new shared interests"
            ]
        },
        "career": {
            "common_conflicts": [
                "Work hours and availability",
                "Career ambition vs family time",
                "Geographic preferences for jobs",
                "Risk tolerance in career changes",
                "Work-life balance priorities"
            ],
            "understand_values": [
                "What does your work mean to you?",
                "What lifestyle do you want work to provide?",
                "How do you define success?",
                "What sacrifices are worth making?"
            ],
            "find_common_ground": [
                "Financial security for family",
                "Personal fulfillment matters",
                "Supporting each other's growth",
                "Building a life together"
            ],
            "create_solution": [
                "Defined work hours/boundaries",
                "Career phases with different priorities",
                "Geographic timeline agreements",
                "Regular communication about work stress"
            ]
        }
    }

    area_lower = value_area.lower()
    if area_lower in conflict_scenarios:
        return conflict_scenarios[area_lower]
    else:
        return {
            "guidance": f"Explore your values around {value_area}",
            "questions": [
                f"What does {value_area} mean to each of you?",
                f"What experiences shaped your views on {value_area}?",
                f"What do you need from each other regarding {value_area}?"
            ]
        }


def align_life_vision() -> Dict[str, Any]:
    """
    Helps couples create a shared vision for their life together.

    Returns:
        Dictionary with vision alignment framework
    """
    vision_dimensions = {
        "time_horizon": {
            "short": "Next 1-2 years",
            "medium": "3-5 years",
            "long": "5-10+ years"
        },
        "life_areas": [
            "relationship and family",
            "home and location",
            "career and work",
            "finances and lifestyle",
            "personal growth",
            "community and social",
            "health and wellbeing",
            "leisure and adventure"
        ]
    }

    vision_questions = {
        "individually": [
            "If everything went well, what would your life look like in 5 years?",
            "What would make you feel fulfilled and happy?",
            "What do you definitely want in your life?",
            "What do you definitely want to avoid?"
        ],
        "together": [
            "What do we want our life together to look like?",
            "What experiences do we want to share?",
            "What do we want to build together?",
            "How do we want to grow together?"
        ],
        "practical": [
            "Where do we want to live?",
            "Do we want children? What would that look like?",
            "What kind of work/life balance do we want?",
            "What lifestyle is important to us?",
            "How do we handle finances as a team?",
            "What does home look like for us?"
        ]
    }

    return {
        "vision_dimensions": vision_dimensions,
        "vision_questions": vision_questions,
        "activity": "Separately write your ideal life vision, then share and discuss.",
        "goal": "Create a shared vision that incorporates both partners' dreams",
        "reality_check": "Life may unfold differently - hold vision with flexibility",
        "benefits": [
            "Provides direction and purpose",
            "Helps decision-making",
            "Creates shared meaning",
            "Inspires during challenges"
        ],
        "next_steps": [
            "Write individual visions",
            "Share without judgment",
            "Find common themes",
            "Integrate both visions",
            "Create joint mission statement"
        ]
    }
