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

"""Boundary setting tools for healthy relationships."""

from typing import Dict, List, Any


def establish_boundary(area: str, boundary: str) -> Dict[str, Any]:
    """
    Helps set healthy boundaries assertively in relationships.

    Args:
        area: The relationship area requiring boundary
        boundary: The specific boundary being set

    Returns:
        Dictionary with boundary establishment framework
    """
    return {
        "boundary_statement": {
            "framework": "I need/feel [X] when [Y happens]. Would you be willing to [Z]?",
            "examples": [
                "I feel overwhelmed when I'm interrupted. Would you be willing to let me finish my thoughts?",
                "I need privacy when I'm decompressing after work. Could we have 30 minutes before we talk?",
                "I feel hurt when criticism happens in front of others. Can we discuss concerns privately?",
                "I need advance notice for schedule changes. Would you communicate changes earlier?"
            ]
        },
        "assertive_not_aggressive": {
            "characteristics": {
                "assertive": "Clear, confident, respectful of both parties",
                "aggressive": "Hostile, attacking, disregarding of other's needs",
                "passive": "Indirect, avoiding, self-sacrificing"
            },
            "being_assertive": [
                "Use 'I' statements",
                "Be clear and specific",
                "Maintain calm tone",
                "Make eye contact",
                "Respectful body language",
                "Open to discussion"
            ]
        },
        "common_boundary_areas": {
            "time": {
                "examples": [
                    "Time alone each day",
                    "No work discussions after hours",
                    "Weekend mornings for personal time",
                    "Annual trip with friends"
                ],
                "why": "Autonomy and individual identity within relationship"
            },
            "communication": {
                "examples": [
                    "No yelling during conflicts",
                    "No criticism in front of others",
                    "Respect when one says 'I can't talk right now'",
                    "Allow time to process before responding"
                ],
                "why": "Emotional safety and respectful communication"
            },
            "family": {
                "examples": [
                    "No discussing partner with family without permission",
                    "Boundaries with in-laws about drop-ins",
                    "Privacy about relationship issues",
                    "Decisions about your own family"
                ],
                "why": "Couple as primary family unit"
            },
            "digital": {
                "examples": [
                    "No checking partner's phone/messages",
                    "Response time expectations for texts",
                    "Social media privacy",
                    "Device-free times (meals, bedroom)"
                ],
                "why": "Trust and autonomy in digital age"
            },
            "physical": {
                "examples": [
                    "Right to refuse touch",
                    "Need for physical space",
                    "Privacy in bathroom/bedroom",
                    "Sleep needs and preferences"
                ],
                "why": "Bodily autonomy and comfort"
            }
        }
    }


def explore_personal_boundaries() -> Dict[str, Any]:
    """
    Helps individuals identify their personal boundaries.

    Returns:
        Dictionary with boundary exploration framework
    """
    return {
        "boundary_categories": {
            "emotional": {
                "description": "What you're emotionally available for",
                "questions": [
                    "What emotional requests feel like too much?",
                    "When do you feel emotionally drained?",
                    "What emotional support can you realistically give?",
                    "What emotions are hard for you to handle from partner?"
                ]
            },
            "time": {
                "description": "How you spend your time and energy",
                "questions": [
                    "What time do you absolutely need for yourself?",
                    "What schedule pressures feel overwhelming?",
                    "What activities drain vs recharge you?",
                    "What balance of together/apart time works for you?"
                ]
            },
            "physical": {
                "description": "Your body, space, and physical needs",
                "questions": [
                    "What physical touch feels good vs too much?",
                    "What personal space do you need?",
                    "What are your sleep and rest needs?",
                    "What physical activities are you willing/not willing to do?"
                ]
            },
            "digital": {
                "description": "Technology, social media, communication",
                "questions": [
                    "What communication frequency feels overwhelming?",
                    "What digital privacy do you need?",
                    "When is device use affecting connection?",
                    "What boundaries do you need around work availability?"
                ]
            },
            "family": {
                "description": "Relationship with extended family",
                "questions": [
                    "What family involvement feels comfortable?",
                    "What family issues are yours to handle?",
                    "What boundaries do you need with in-laws?",
                    "What family information is private?"
                ]
            },
            "financial": {
                "description": "Money, spending, financial decisions",
                "questions": [
                    "What financial autonomy do you need?",
                    "What spending decisions require mutual agreement?",
                    "What financial boundaries are important?",
                    "How do you handle differing money values?"
                ]
            }
        },
        "identifying_boundary_violations": {
            "signs": [
                "Feeling resentful about giving in",
                "Feeling guilty for saying no",
                "Feeling drained after interactions",
                "Feeling like you've lost yourself",
                "Feeling controlled or controlling others",
                "Feeling anxious about upcoming interactions"
            ],
            "physical_signals": [
                "Tension in your body when certain topics arise",
                "Feeling sick or stressed before interactions",
                "Difficulty sleeping related to boundary issues",
                "Feeling physically exhausted from trying to please"
            ]
        },
        "values_assessment": {
            "questions": [
                "What matters most to me in life?",
                "What kind of partner do I want to be?",
                "What example am I setting with my boundaries?",
                "What do I need to feel like myself?",
                "What am I willing to accept? Not accept?"
            ]
        },
        "boundary_spectrum": {
            "firm": "Non-negotiables for your wellbeing",
            "flexible": "Open to discussion and compromise",
            "negotiable": "Preferences you're willing to adjust"
        }
    }


def discuss_boundary_violations() -> Dict[str, Any]:
    """
    Provides framework for addressing when boundaries are crossed.

    Returns:
        Dictionary with boundary violation discussion framework
    """
    return {
        "when_boundaries_are_crossed": {
            "immediate_response": [
                "Name the boundary clearly",
                "Remove yourself if necessary",
                "Don't debate or justify excessively",
                "Stay calm but firm",
                "Remember: You have a right to boundaries"
            ],
            "what_to_say": [
                '"I\'ve asked for [boundary] and it keeps happening. We need to discuss this."',
                '"This isn\'t working for me. I need [boundary] to be respected."',
                '"I love you AND I need this boundary to be honored."',
                '"I\'m willing to discuss this, but not when [boundary violation] is happening."'
            ]
        },
        "productive_conversation": {
            "timing": "Have conversation when both are calm and can focus",
            "structure": {
                "share": [
                    "State the boundary that was crossed",
                    "Share how it affected you",
                    "Share why this boundary matters to you"
                ],
                "listen": [
                    "Hear their perspective",
                    "Understand their reaction",
                    "Don't interrupt or defend yet"
                ],
                "problem_solve": [
                    "Discuss what makes this boundary hard",
                    "Address obstacles to respecting it",
                    "Find solutions that work for both",
                    "Plan for how to handle going forward"
                ],
                "agree": [
                    "Clear agreement on the boundary",
                    "Consequences for repeated violations",
                    "Plan for follow-up",
                    "Both commit to the agreement"
                ]
            }
        },
        "challenges": [
            "Partner doesn't take boundary seriously",
            "Boundary brings up deeper issues",
            "Each has different understanding",
            "Cultural differences in boundaries",
            "Past patterns are hard to change"
        ],
        "solutions": {
            "clarity": [
                "Be very specific about what boundary is",
                "Give concrete examples",
                "Explain the 'why' behind the boundary",
                "Use 'when-then' format"
            ],
            "consistency": [
                "Maintain the boundary yourself",
                "Follow through on stated consequences",
                "Don't send mixed messages",
                "Reinforce positively when respected"
            ],
            "support": [
                "Seek counseling for deep-seated issues",
                "Get objective perspective",
                "Have difficult conversations with mediator",
                "Address underlying relationship issues"
            ]
        },
        "boundary_types": {
            "internal_boundaries": "Limits you set with yourself",
            "external_boundaries": "Limits you communicate to others",
            "material_boundaries": "Physical items, money, time, space",
            "emotional_boundaries": "Feelings, energy, emotional labor",
            "mental_boundaries": "Thoughts, values, opinions, beliefs",
            "sexual_boundaries": "Physical intimacy, sexual activities"
        },
        "healthy_mindset": {
            "principles": [
                "Boundaries create safety and respect",
                "Good boundaries strengthen relationships",
                "Both partners' needs matter",
                "Boundaries can change over time with discussion",
                "Cultural differences in boundaries are valid but must be negotiated"
            ],
            "not_betrayal": [
                "Having boundaries ≠ betrayal",
                "Saying no ≠ withholding love",
                "Autonomy ≠ rejecting the relationship",
                "Self-care = selfishness myth"
            ]
        }
    }


def create_family_boundaries() -> Dict[str, Any]:
    """
    Creates healthy boundaries with extended family and in-laws.

    Returns:
        Dictionary with family boundary framework
    """
    return {
        "importance": "Healthy boundaries with extended family protect the couple relationship",
        "common_challenges": {
            "over_involved_parents": {
                "issues": [
                    "Frequent unannounced visits",
                    "Unsolicited advice",
                    "Interference in decisions",
                    "Lack of respect for couple's autonomy"
                ],
                "strategies": {
                    "united_front": "Present as a team to family",
                    "information_diet": "Limit sharing about relationship",
                    "scheduled_contact": "Set regular times for contact",
                    "gentle_redirect": "Redirect conversations",
                    "direct_communication": "Be clear about preferences"
                }
            },
            "in_law_conflicts": {
                "issues": [
                    "Criticism from in-laws",
                    "Favoritism among siblings/couples",
                    "Holiday pressures",
                    "Different traditions or expectations",
                    "Boundary crossing"
                ],
                "strategies": {
                    "partner_manages_their_parents": "Each deals with their own family",
                    "support_publicly": "Support partner publicly even in disagreement",
                    "discuss_privately": "Address issues in private, not in front of family",
                    "create_new_traditions": "Establish your own family traditions"
                }
            },
            "holiday_stress": {
                "issues": [
                    "Competing family demands",
                    "Travel pressures",
                    "Gift expectations",
                    "Religious or cultural obligations"
                ],
                "strategies": {
                    "alternate_years": "Alternate holidays between families",
                    "create_new": "Start your own holiday traditions",
                    "set_boundaries": "Clear limits on time and activities",
                    "communicate_early": "Discuss plans well in advance",
                    "manage_expectations": "Be clear about what you can and can't do"
                }
            }
        },
        "guidelines": {
            "united_front": "Present as a team to extended family",
            "privacy": "Keep relationship issues private from family",
            "prioritize": "Your relationship comes before extended family",
            "respect": "Respect each other's family relationships",
            "support": "Support partner with their family challenges",
            "compromise": "Both make efforts with each other's families"
        },
        "difficult_conversations": {
            "family_decision": [
                '"We\'ve decided to [decision] because [reason]"',
                '"We appreciate your input, but we\'re going to [action]"',
                '"We understand you feel differently, and we\'ve considered that, but..."',
                '"This is what works for our family"'
            ],
            "setting_boundary": [
                '"We\'d prefer not to discuss [topic]"',
                '"That\'s not something we\'re comfortable sharing"',
                '"We\'ll handle that ourselves, but thank you for your concern"',
                '"We\'ve made our decision and appreciate your support"'
            ]
        },
        "building_boundaries": {
            "early": [
                "Set boundaries early in relationship",
                "Be consistent from the beginning",
                "Discuss family expectations before marriage",
                "Align on approach to family issues"
            ],
            "ongoing": [
                "Reinforce boundaries as needed",
                "Support each other with difficult families",
                "Review boundaries as family circumstances change",
                "Celebrate successes in managing family"
            ]
        }
    }


def maintain_autonomy_in_togetherness() -> Dict[str, Any]:
    """
    Balances togetherness with maintaining individual identity.

    Returns:
        Dictionary with autonomy framework
    """
    return {
        "balance_principle": "Healthy relationships balance we with me",
        "areas_of_autonomy": {
            "social": {
                "maintain": [
                    "Your own friendships",
                    "Social activities separate from partner",
                    "Hobbies and interests of your own",
                    "Time with friends without partner"
                ],
                "benefits": [
                    "Brings fresh energy into relationship",
                    "Maintains your support network",
                    "Preserves your individuality",
                    "Prevents codependency"
                ]
            },
            "personal_growth": {
                "maintain": [
                    "Your own goals and ambitions",
                    "Personal learning and development",
                    "Self-care practices",
                    "Spiritual or philosophical exploration"
                ],
                "benefits": [
                    "Keeps you growing and evolving",
                    "Brings new insights to relationship",
                    "Prevents stagnation",
                    "Maintains self-respect"
                ]
            },
            "decision_making": {
                "maintain": [
                    "Autonomy in certain areas",
                    "Personal preferences and tastes",
                    "Right to your own opinion",
                    "Space to make some decisions alone"
                ],
                "benefits": [
                    "Reduces decision fatigue",
                    "Maintains personal agency",
                    "Prevents resentment",
                    "Builds mutual respect"
                ]
            },
            "identity": {
                "maintain": [
                    "Your own personality and quirks",
                    "Personal style and preferences",
                    "Individual interests and passions",
                    "Your own name and story"
                ],
                "benefits": [
                    "Authenticity in relationship",
                    "Attraction to authentic partner",
                    "Self-esteem and self-worth",
                    "Prevents losing yourself"
                ]
            }
        },
        "warning_signs": {
            "losing_yourself": [
                "Can't remember last thing you did alone",
                "Feel you've lost your identity",
                "All your friends are mutual friends",
                "No separate interests or hobbies",
                "Constantly compromising who you are"
            ],
            "codependency": [
                "Your mood depends entirely on partner",
                "You've stopped seeing your friends",
                "You can't make decisions without them",
                "You've lost touch with your own values",
                "Your boundaries are consistently ignored"
            ]
        },
        "practices": {
            "regular": [
                "Schedule regular 'me time'",
                "Maintain your own friendships",
                "Pursue individual interests",
                "Have separate hobbies sometimes",
                "Take trips apart occasionally"
            ],
            "relationship": {
                "share_experiences": "Tell partner about your independent activities",
                "celebrate_individuality": "Cheer each other's individual successes",
                "bring_learning": "Share what you learn on your own",
                "respect_differences": "Honor your different interests and needs"
            },
            "check_ins": {
                "questions": [
                    "Am I maintaining my identity?",
                    "Do I have friendships outside this relationship?",
                    "Am I pursuing my own goals?",
                    "Do I feel like myself in this relationship?"
                ]
            }
        }
    }
