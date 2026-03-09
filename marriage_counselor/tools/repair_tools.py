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

"""Repair and forgiveness tools for relationship healing."""

from typing import Dict, List, Any


def guide_repair_process(hurt_type: str) -> Dict[str, Any]:
    """
    Provides structured steps for apologizing, forgiving, and repairing.

    Args:
        hurt_type: Type of hurt (betrayal, emotional_distance, disrespect, broken_promise, etc.)

    Returns:
        Dictionary with repair process framework
    """
    repair_processes = {
        "betrayal": {
            "description": "Deep breach of trust - infidelity, secrets, major deception",
            "timeline": "Recovery takes months to years, not days",
            "process": {
                "phase_1_immediate": {
                    "actions": [
                        "Complete honesty about what happened",
                        "No more secrets or half-truths",
                        "Answer questions honestly",
                        "Show remorse through actions"
                    ],
                    "for_betrayed": [
                        "Take time to process",
                        "Seek support from trusted sources",
                        "Don't make immediate decisions",
                        "Set boundaries for your healing"
                    ],
                    "for_betrayer": [
                        "Accept responsibility fully",
                        "Be patient with their emotions",
                        "Don't minimize their pain",
                        "Be transparent with everything"
                    ]
                },
                "phase_2_understanding": {
                    "actions": [
                        "Understand what led to the betrayal",
                        "Identify vulnerabilities in the relationship",
                        "Acknowledge the pattern of choices",
                        "Recognize the impact on both partners"
                    ]
                },
                "phase_3_accountability": {
                    "actions": [
                        "Betrayer takes full responsibility",
                        "No blaming partner for betrayal",
                        "Make amends where possible",
                        "Demonstrate reliability consistently"
                    ]
                },
                "phase_4_rebuilding": {
                    "actions": [
                        "Create new relationship patterns",
                        "Build new trust through consistency",
                        "Seek counseling support",
                        "Celebrate small steps forward"
                    ]
                }
            },
            "reality_check": "Many relationships survive betrayal - but both must be committed to the work"
        },
        "emotional_distance": {
            "description": "Growing apart, lack of connection, emotional unavailability",
            "timeline": "Reconnection takes consistent effort over weeks/months",
            "process": {
                "phase_1_recognize": {
                    "actions": [
                        "Acknowledge the distance openly",
                        "Share feelings without blame",
                        "Both commit to reconnection",
                        "Identify when distance started"
                    ]
                },
                "phase_2_understand": {
                    "actions": [
                        "Understand what created distance",
                        "Identify individual needs not being met",
                        "Recognize protective walls built",
                        "Acknowledge fears of vulnerability"
                    ]
                },
                "phase_3_reconnect": {
                    "actions": [
                        "Daily check-ins",
                        "Scheduled quality time",
                        "Increasing emotional sharing",
                        "Physical affection (hugs, touch)",
                        "Shared activities you both enjoy"
                    ]
                },
                "phase_4_maintain": {
                    "actions": [
                        "Continue connection practices",
                        "Address distance quickly when it returns",
                        "Celebrate emotional intimacy",
                        "Keep learning about each other"
                    ]
                }
            }
        },
        "disrespect": {
            "description": "Dismissiveness, criticism, contempt, name-calling",
            "timeline": "Respect must be restored immediately for safety",
            "process": {
                "immediate_action": [
                    "Stop disrespectful behavior immediately",
                    "Acknowledge it was wrong",
                    "Apologize sincerely",
                    "Commit to change"
                ],
                "understand_impact": [
                    "Disrespect destroys emotional safety",
                    "It's damaging even if 'just joking'",
                    "It erodes love over time",
                    "It must be zero tolerance"
                ],
                "rebuild_respect": {
                    "during_conflict": [
                        "Speak to your partner as you'd want to be spoken to",
                        "Take breaks instead of lashing out",
                        "Remember you're on the same team",
                        "Use de-escalation techniques"
                    ],
                    "daily_practices": [
                        "Express appreciation regularly",
                        "Show interest in their thoughts",
                        "Validate their feelings",
                        "Avoid criticism, use requests instead"
                    ]
                }
            },
            "warning": "Ongoing disrespect is abuse - seek help if it continues"
        },
        "broken_promise": {
            "description": "Commitments made but not kept",
            "timeline": "Trust rebuilds with each kept promise",
            "process": {
                "understand": [
                    "Why was the promise broken?",
                    "What made it hard to keep?",
                    "Was the promise realistic?",
                    "What needs were not being met?"
                ],
                "repair": [
                    "Acknowledge the broken promise",
                    "Apologize without excuses",
                    "Make amends if possible",
                    "Recommit with realistic expectations"
                ],
                "prevent": [
                    "Make realistic commitments",
                    "Communicate if circumstances change",
                    "Understand what keeping promises means to your partner",
                    "Follow through consistently"
                ]
            }
        }
    }

    hurt_lower = hurt_type.lower()

    # Find matching process or provide general guidance
    for key, process in repair_processes.items():
        if key in hurt_lower:
            return process

    # General repair framework
    return {
        "hurt_type": hurt_type,
        "general_process": {
            "acknowledge": "Both partners acknowledge the hurt and its impact",
            "understand": "Seek to understand what happened and why",
            "apologize": "Sincere apology that acknowledges specific harm",
            "repair": "Actions to make amends and prevent recurrence",
            "rebuild": "Consistently demonstrate change over time"
        },
        "for_hurt_partner": [
            "Your feelings are valid",
            "Take time you need",
            "You don't have to forgive immediately",
            "Set boundaries for your healing",
            "Seek support from others"
        ],
        "for_responsible_partner": [
            "Take full responsibility",
            "Listen without defending",
            "Validate their pain",
            "Be patient with their timeline",
            "Demonstrate change through actions"
        ]
    }


def make_sincere_apology(mistake: str) -> Dict[str, Any]:
    """
    Guides the process of making a sincere apology.

    Args:
        mistake: The mistake that needs apologizing for

    Returns:
        Dictionary with apology framework
    """
    return {
        "apology_components": {
            "acknowledge": {
                "what": f"Clearly state what you did: 'I {mistake}'",
                "examples": [
                    '"I snapped at you when you asked about dinner"',
                    '"I forgot our plans and went out with friends"',
                    '"I criticized you in front of others"'
                ]
            },
            "accept_responsibility": {
                "what": "Own it completely - no buts, no excuses",
                "examples": [
                    '"I was wrong to do that"',
                    '"There\'s no excuse for my behavior"',
                    '"I take full responsibility"'
                ],
                "avoid": [
                    "I'm sorry BUT...",
                    "I'm sorry you feel that way",
                    "I'm sorry IF I hurt you"
                ]
            },
            "acknowledge_impact": {
                "what": "Show you understand how it affected them",
                "examples": [
                    '"I can see that made you feel unimportant"',
                    '"I understand that embarrassed you"',
                    '"I know that broke your trust"'
                ]
            },
            "express_regret": {
                "what": "Genuine remorse for the hurt caused",
                "examples": [
                    '"I regret that I hurt you"',
                    '"I wish I had handled that differently"',
                    '"I\'m truly sorry for the pain I caused"'
                ]
            },
            "make_amends": {
                "what": "Offer to repair the damage",
                "examples": [
                    '"What can I do to make this right?"',
                    '"How can I repair this?"',
                    '"Let me fix this"'
                ]
            },
            "commit_change": {
                "what": "Plan to prevent recurrence",
                "examples": [
                    '"Next time I\'ll...',
                    '"I\'m working on...',
                    '"Here\'s what I\'ll do differently"'
                ]
            }
        },
        "apology_template": f"'I apologize for {mistake}. I was wrong to do that. I understand it made you feel [impact], and I regret that. What can I do to make this right? In the future, I'll [different behavior].'",
        "after_apologizing": [
            "Give them space to process",
            "Don't demand forgiveness immediately",
            "Demonstrate change through actions",
            "Be patient with their timeline",
            "Accept that rebuilding trust takes time"
        ],
        "common_mistakes": [
            "Making it about your intentions",
            "Expecting immediate forgiveness",
            "Getting defensive about their reaction",
            "Minimizing what happened",
            "Turning it back on them"
        ]
    }


def practice_forgiveness(process: str = "decision") -> Dict[str, Any]:
    """
    Guides the forgiveness process for the hurt partner.

    Args:
        process: Current stage - decision, process, outcome

    Returns:
        Dictionary with forgiveness guidance
    """
    forgiveness_stages = {
        "decision": {
            "description": "Forgiveness is a decision you make for yourself",
            "understand": [
                "Forgiveness doesn't mean what happened was okay",
                "Forgiveness doesn't mean reconciliation",
                "Forgiveness releases you from carrying the hurt",
                "Forgiveness is for your healing, not theirs"
            ],
            "consider": [
                "What am I gaining by holding onto this?",
                "What is this costing me?",
                "Am I ready to let go of this burden?",
                "What would forgiveness give me?"
            ],
            "action": 'Decide: "I choose to forgive for my own peace of mind"'
        },
        "process": {
            "description": "Working through emotions as they arise",
            "understand": [
                "Forgiveness is often a journey, not a one-time event",
                "Feelings may come and go - that's normal",
                "Healing has its own timeline",
                "Be patient with yourself"
            ],
            "practices": [
                "Acknowledge feelings as they arise",
                "Release them healthily (journal, talk, therapy)",
                "Choose forgiveness each time resentment returns",
                "Focus on your healing, not their behavior"
            ],
            "boundary": "Forgiveness doesn't mean trusting again - trust is rebuilt separately"
        },
        "outcome": {
            "description": "The freedom that comes from forgiveness",
            "signs": [
                "Memory doesn't trigger intense emotions",
                "You can wish them well",
                "You've learned and grown",
                "The experience no longer controls you"
            ],
            "maintain": [
                "Continue choosing forgiveness if resentment returns",
                "Honor your journey of healing",
                "Share your wisdom with others",
                "Protect your emotional wellbeing"
            ]
        }
    }

    stage = process.lower() if process else "decision"

    return {
        "current_stage": stage,
        "stage_info": forgiveness_stages.get(stage, forgiveness_stages["decision"]),
        "key_principle": "Forgiveness is a gift you give yourself, not something you earn for others",
        "not_forgiveness": [
            "Holding onto anger and hurt",
            "Letting the past control your present",
            "Damaging your own emotional health",
            "Remaining stuck in the pain"
        ],
        "myths": {
            "myth": "Forgiveness means you're okay with what happened",
            "reality": "Forgiveness means you're no longer letting it hurt you"
        },
        "encouragement": "Forgiveness is possible, even for deep hurts - but it's a journey, not a destination"
    }


def rebuild_trust_broken(breach_type: str = "general") -> Dict[str, Any]:
    """
    Provides framework for rebuilding broken trust.

    Args:
        breach_type: Type of trust breach

    Returns:
        Dictionary with trust rebuilding framework
    """
    trust_breach_types = {
        "infidelity": {
            "what_was_broken": "Sexual and/or emotional exclusivity",
            "rebuilding_components": {
                "transparency": "Complete openness about activities, communications",
                "accountability": "Willingness to be accountable for all time",
                "patience": "Understanding this takes years, not weeks",
                "consistency": "Reliability in words and actions over time"
            }
        },
        "deception": {
            "what_was_broken": "Honesty and authenticity in relationship",
            "rebuilding_components": {
                "truth_telling": "Absolute honesty, even about uncomfortable things",
                "oversharing": "Sharing more than asked to prove honesty",
                "no_secrets": "Complete transparency in all areas",
                "verification": "Willingness to let partner verify"
            }
        },
        "broken_promise": {
            "what_was_broken": "Reliability and commitment",
            "rebuilding_components": {
                "realistic_commitments": "Only promise what can be delivered",
                "communication": "Speak up if circumstances change",
                "follow_through": "Do exactly what you say you'll do",
                "consistency": "Build track record of reliability"
            }
        },
        "emotional_abandonment": {
            "what_was_broken": "Emotional safety and availability",
            "rebuilding_components": {
                "presence": "Be emotionally available consistently",
                "responsiveness": "Respond to bids for connection",
                "vulnerability": "Share your own emotions",
                "validation": "Acknowledge their feelings"
            }
        }
    }

    breach_lower = breach_type.lower()
    components = trust_breach_types.get(breach_lower, {
        "what_was_broken": "Confidence in reliability and safety",
        "rebuilding_components": {
            "consistency": "Do what you say, every time",
            "communication": "Keep partner informed",
            "accountability": "Accept responsibility for actions",
            "patience": "Understand trust takes time to rebuild"
        }
    })

    return {
        "breach_type": breach_type,
        "understanding": components["what_was_broken"],
        "rebuilding_actions": components["rebuilding_components"],
        "timeline_expectation": "Trust rebuilds slowly - think months to years, not days",
        "for_trust_breaker": [
            "Accept that trust must be earned back",
            "Be patient with their questions and concerns",
            "Be transparent in all areas",
            "Don't expect forgiveness on your timeline",
            "Demonstrate change through consistent action"
        ],
        "for_hurt_partner": [
            "Trust your instincts about safety",
            "Take your time - there's no rush",
            "Communicate your needs clearly",
            "Acknowledge progress when it occurs",
            "Seek support for yourself"
        ],
        "rebuilding_phase": {
            "early": "Compliance with boundaries, answering questions",
            "middle": "Consistency building, new patterns forming",
            "late": "Natural trust returning, less monitoring needed",
            "maintenance": "Trust maintained through ongoing reliability"
        },
        "realistic_expectations": [
            "Trust will likely never be exactly the same",
            "Some triggers may remain sensitive",
            "Both partners contribute to healing",
            "Professional support often helps"
        ]
    }
