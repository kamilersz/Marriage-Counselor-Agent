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

"""Conflict resolution tools for managing relationship conflicts."""

from typing import Dict, List, Any


def analyze_conflict_pattern(description: str) -> Dict[str, Any]:
    """
    Identifies conflict cycles, triggers, and escalation patterns.

    Args:
        description: Description of the conflict pattern

    Returns:
        Dictionary with conflict analysis and insights
    """
    conflict_patterns = {
        "pursue_withdraw": {
            "pattern": "One partner pursues/confronts, the other withdraws/avoids",
            "cycle": [
                "Issue raised → One pursues → Other withdraws → Pursuer intensifies → Withdrawer escapes further → Escalation"
            ],
            "impact": "Both feel unfulfilled - pursuer feels abandoned, withdrawer feels pressured",
            "break_the_cycle": [
                "Pursuer: Give space, lower intensity",
                "Withdrawer: Stay engaged, express needs",
                "Both: Acknowledge the pattern, try new responses"
            ]
        },
        "escalation": {
            "pattern": "Conflict quickly escalates to hurtful words or actions",
            "cycle": [
                "Disagreement → Defensive response → Counterattack → Hurtful statements → Damage"
            ],
            "impact": "Trust erodes, resentment builds, emotional safety decreases",
            "break_the_cycle": [
                "Recognize escalation signs early",
                "Take agreed-upon timeout",
                "Use de-escalation phrases",
                "Return when calm to resolve"
            ]
        },
        "avoidance": {
            "pattern": "Important issues are avoided to prevent conflict",
            "cycle": [
                "Issue arises → One or both avoid → Tension builds → Resentment grows → Distance increases"
            ],
            "impact": "Problems fester, connection weakens, small issues become big",
            "break_the_cycle": [
                "Create safe space for difficult conversations",
                "Start with less threatening topics",
                "Use structured communication",
                "Celebrate successful discussions"
            ]
        },
        "recurring": {
            "pattern": "Same arguments happen repeatedly without resolution",
            "cycle": [
                "Topic raised → Same positions stated → Neither budges → Argument ends → Issue resurfaces"
            ],
            "impact": "Hopelessness develops, both feel unheard",
            "break_the_cycle": [
                "Understand the underlying need or value",
                "Look for compromise that meets both needs",
                "Consider: Is this about the issue or something deeper?"
            ]
        }
    }

    desc_lower = description.lower()

    # Identify patterns from description
    identified = []
    for pattern_name, pattern_info in conflict_patterns.items():
        if (pattern_name == "pursue_withdraw" and
            any(word in desc_lower for word in ["pursue", "chase", "withdraw", "avoid", "shut down"])):
            identified.append(pattern_name)
        elif (pattern_name == "escalation" and
              any(word in desc_lower for word in ["escalate", "yell", "scream", "hurtful", "name calling"])):
            identified.append(pattern_name)
        elif (pattern_name == "avoidance" and
              any(word in desc_lower for word in ["avoid", "don't talk", "ignore", "pretend"])):
            identified.append(pattern_name)
        elif (pattern_name == "recurring" and
              any(word in desc_lower for word in ["same", "always", "over and over", "again", "never"])):
            identified.append(pattern_name)

    if not identified:
        identified = ["unknown"]

    return {
        "identified_patterns": identified,
        "patterns_detail": {p: conflict_patterns[p] for p in identified if p in conflict_patterns},
        "universal_insight": "Understanding your conflict pattern is the first step to changing it.",
        "next_steps": [
            "Both partners must acknowledge the pattern",
            "Commit to trying one new response",
            "Notice what happens when you change your reaction",
            "Practice, practice, practice - new patterns take time"
        ]
    }


def de_escalate_conflict() -> Dict[str, Any]:
    """
    Provides immediate de-escalation techniques for heated moments.

    Returns:
        Dictionary with de-escalation strategies
    """
    return {
        "immediate_actions": [
            "Take a timeout: 'I need 20 minutes to cool down, then let's continue'",
            "Use a safe word or signal that means pause",
            "Physical separation: different rooms, a walk outside",
            "Deep breathing: 4-7-8 breath to calm nervous system"
        ],
        "what_to_say": [
            '"I care about this discussion, but I\'m too upset to think clearly right now. Can we take a break and come back in 30 minutes?"',
            '"I want to resolve this, but I\'m escalating. Let me pause and return when I can listen better."',
            '"I love you and I don\'t want to say something I\'ll regret. Time out?"'
        ],
        "what_not_to_do": [
            "Don't continue when emotionally flooded",
            "Don't threaten or issue ultimatums",
            "Don't bring up past grievances",
            "Don't use the silent treatment as punishment"
        ],
        "returning_to_conversation": [
            "Both partners return when calm",
            "First: Acknowledge feelings on both sides",
            "Second: Identify what triggered escalation",
            "Third: Try a different approach",
            "Fourth: Repair any damage done during escalation"
        ],
        "prevention": [
            "Recognize early warning signs in yourself",
            "Have a timeout agreement in advance",
            "Practice de-escalation when not in conflict",
            "Address issues before they explode"
        ]
    }


def resolve_specific_conflict(issue: str) -> Dict[str, Any]:
    """
    Provides structured approach to resolving a specific conflict.

    Args:
        issue: The specific conflict issue

    Returns:
        Dictionary with resolution framework
    """
    return {
        "issue": issue,
        "resolution_framework": {
            "step_1_understand": {
                "action": "Each person shares their perspective without interruption",
                "listener_role": "Listen to understand, not to respond",
                "goal": "Both feel heard before problem-solving",
                "prompt": '"What does this situation look like from your perspective?"'
            },
            "step_2_identify": {
                "action": "Identify the underlying needs and values of both partners",
                "look_for": [
                    "What matters most to each person?",
                    "What fears or concerns are present?",
                    "What values are being challenged?"
                ],
                "goal": "Understand what's really at stake"
            },
            "step_3_brainstorm": {
                "action": "Generate possible solutions together",
                "rules": [
                    "No judging or rejecting ideas yet",
                    "Aim for quantity over quality initially",
                    "Build on each other's suggestions",
                    "Include wild ideas - they might lead somewhere good"
                ],
                "goal": "Create options before evaluating them"
            },
            "step_4_evaluate": {
                "action": "Evaluate options against shared criteria",
                "criteria": [
                    "Does this work for both of us?",
                    "Is this realistic and sustainable?",
                    "Does it address the underlying needs?",
                    "Are both willing to commit to this?"
                ],
                "goal": "Find a solution both can accept"
            },
            "step_5_agree": {
                "action": "Agree on specific actions and timeline",
                "be_specific": [
                    "What exactly will each person do?",
                    "When will this start?",
                    "How will we know it's working?",
                    "What do we do if it doesn't work?"
                ],
                "goal": "Clear commitment and accountability"
            },
            "step_6_check_in": {
                "action": "Schedule a follow-up to evaluate progress",
                "timing": "1-2 weeks later",
                "questions": [
                    "Is this solution working?",
                    "Do adjustments need to be made?",
                    "How do we both feel about it?"
                ],
                "goal": "Ensure the resolution sticks"
            }
        },
        "key_principle": "The goal isn't for one person to win - it's for the relationship to win.",
        "mindset_shift": "From 'me vs you' to 'us vs the problem'"
    }


def repair_after_conflict(conflict_description: str = "") -> Dict[str, Any]:
    """
    Provides steps for repairing connection after conflict.

    Args:
        conflict_description: Optional description of the conflict

    Returns:
        Dictionary with repair process and tools
    """
    return {
        "repair_process": {
            "phase_1_cool_down": {
                "actions": [
                    "Ensure both are calm before attempting repair",
                    "Take responsibility for your own actions",
                    "Reflect on what triggered you",
                    "Consider your partner's perspective"
                ],
                "mindset": "Repair happens when both are ready and regulated"
            },
            "phase_2_initiate": {
                "actions": [
                    "Reach out gently",
                    "Express desire to reconnect",
                    "Show you still care",
                    "Be patient with their response"
                ],
                "examples": [
                    '"I\'ve cooled down and I\'d like to talk when you\'re ready"',
                    '"I love you and I want to resolve this"',
                    '"Can we try again to understand each other?"'
                ]
            },
            "phase_3_listen": {
                "actions": [
                    "Hear their experience of the conflict",
                    "Validate their feelings",
                    "Acknowledge your impact",
                    "Don't defend or explain yet"
                ],
                "phrases": [
                    '"I can see that really hurt you"',
                    '"I understand why you felt that way"',
                    '"I\'m sorry I made you feel..."'
                ]
            },
            "phase_4_take_responsibility": {
                "actions": [
                    "Own your part without buts",
                    "Acknowledge specific words or actions",
                    "Avoid minimizing your impact",
                    "Don't demand they take responsibility too"
                ],
                "example": '"I snapped at you and that was wrong. I\'m sorry I raised my voice."'
            },
            "phase_5_make_amends": {
                "actions": [
                    "Ask what they need to repair",
                    "Offer to make changes",
                    "Commit to different behavior",
                    "Follow through consistently"
                ]
            },
            "phase_6_learn": {
                "actions": [
                    "Discuss what triggered this conflict",
                    "Identify early warning signs",
                    "Plan for next time",
                    "Practice new approaches"
                ],
                "goal": "Learn from the conflict to prevent future damage"
            }
        },
        "repair_timelines": {
            "minor_conflicts": "Same day repair is ideal",
            "moderate_conflicts": "Within 24-48 hours",
            "major_conflicts": "May need days, but don't let it go too long",
            "principle": "Unrepaired conflict accumulates and damages trust"
        },
        "forgiveness_path": {
            "not_forgetting": "Forgiveness doesn't mean forgetting or condoning",
            "letting_go": "It means releasing the grip of resentment",
            "process": "Forgiveness is often a journey, not a single decision",
            "benefits": [
                "Emotional freedom for both",
                "Opportunity to rebuild trust",
                "Possibility of deeper understanding",
                "Growth in resilience and compassion"
            ]
        }
    }
