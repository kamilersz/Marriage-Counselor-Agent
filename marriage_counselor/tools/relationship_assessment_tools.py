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

"""Relationship assessment tools for evaluating relationship health."""

import random
from typing import Dict, List, Any


def assess_relationship_health(aspects: List[str] = None) -> Dict[str, Any]:
    """
    Assesses relationship health across multiple dimensions.

    Args:
        aspects: List of aspects to assess (default: all)

    Returns:
        Dictionary with assessment results for each dimension
    """
    all_aspects = [
        "communication", "trust", "intimacy", "conflict_resolution",
        "shared_values", "commitment", "financial_alignment",
        "parenting_alignment", "emotional_connection", "growth_orientation"
    ]

    if aspects is None:
        aspects = all_aspects

    assessment_results = {}

    # Assessment questions and indicators for each aspect
    aspect_questions = {
        "communication": {
            "indicators": ["openness", "listening", "clarity", "timing", "respect"],
            "strengths": [
                "Both partners feel heard and understood",
                "Difficult topics are discussed without avoidance",
                "Each person can express needs clearly"
            ],
            "improvement_areas": [
                "Conversations often escalate to arguments",
                "One or both partners shut down during conflict",
                "Important topics are avoided"
            ]
        },
        "trust": {
            "indicators": ["honesty", "reliability", "transparency", "loyalty", "consistency"],
            "strengths": [
                "Partners keep their word",
                "There's emotional safety in vulnerability",
                "Past trust has been repaired and maintained"
            ],
            "improvement_areas": [
                "Secrets are kept from each other",
                "There's jealousy or suspicion",
                "Trust has been broken and not fully repaired"
            ]
        },
        "intimacy": {
            "indicators": ["emotional", "physical", "intellectual", "recreational", "spiritual"],
            "strengths": [
                "Partners feel emotionally close",
                "Physical affection is mutually satisfying",
                "They enjoy doing activities together"
            ],
            "improvement_areas": [
                "Emotional distance has grown",
                "Physical intimacy feels disconnected",
                "They live parallel lives"
            ]
        },
        "conflict_resolution": {
            "indicators": ["fairness", "repair", "compromise", "de-escalation", "forgiveness"],
            "strengths": [
                "Arguments end with resolution",
                "Both partners take responsibility",
                "They repair quickly after conflicts"
            ],
            "improvement_areas": [
                "Conflicts escalate quickly",
                "Same issues keep resurfacing",
                "One partner always gives in"
            ]
        },
        "shared_values": {
            "indicators": ["life_goals", "family", "finances", "lifestyle", "beliefs"],
            "strengths": [
                "Aligned vision for the future",
                "Similar views on important life decisions",
                "Core values complement each other"
            ],
            "improvement_areas": [
                "Different views on having/raising children",
                "Conflicting financial priorities",
                "Incompatible lifestyle preferences"
            ]
        },
        "commitment": {
            "indicators": ["prioritization", "investment", "future_planning", "loyalty", "sacrifice"],
            "strengths": [
                "Both prioritize the relationship",
                "Future plans include each other",
                "Willingness to work through difficulties"
            ],
            "improvement_areas": [
                "One partner seems less committed",
                "Outside interests take priority",
                "Future vision doesn't include partner"
            ]
        },
    }

    for aspect in aspects:
        if aspect in aspect_questions:
            assessment_results[aspect] = {
                "description": f"Evaluation of {aspect.replace('_', ' ')} in the relationship",
                "indicators": aspect_questions[aspect]["indicators"],
                "potential_strengths": aspect_questions[aspect]["strengths"],
                "potential_improvement_areas": aspect_questions[aspect]["improvement_areas"],
                "assessment_questions": [
                    f"How would you rate your {aspect} on a scale of 1-10?",
                    f"What aspects of {aspect} are working well?",
                    f"What would you like to improve about {aspect}?"
                ]
            }

    return {
        "aspects_assessed": list(assessment_results.keys()),
        "results": assessment_results,
        "recommendation": "Review each aspect with your partner and discuss honest ratings.",
        "follow_up": "Focus on 1-2 areas for improvement rather than trying to fix everything at once."
    }


def identify_relationship_stage(description: str = "") -> Dict[str, Any]:
    """
    Identifies the current stage of the relationship.

    Args:
        description: Optional description of the relationship situation

    Returns:
        Dictionary with relationship stage information
    """
    stages = {
        "honeymoon": {
            "characteristics": ["excitement", "idealization", "minimal_conflict", "high_passion"],
            "duration": "0-6 months typically",
            "focus": "Enjoying each other, building connection",
            "challenges": "Unrealistic expectations, avoiding differences"
        },
        "power_struggle": {
            "characteristics": ["conflict", "differences_emerge", "control_issues", "disappointment"],
            "duration": "6 months - 2 years",
            "focus": "Establishing individual identities within the relationship",
            "challenges": "Learning to negotiate, accepting differences"
        },
        "stability": {
            "characteristics": ["acceptance", "routines", "deepening_trust", "mutual_understanding"],
            "duration": "2+ years",
            "focus": "Building life together, maintaining connection",
            "challenges": "Complacency, taking each other for granted"
        },
        "crisis": {
            "characteristics": ["major_conflict", "threat_of_separation", "trust_breach", "external_stress"],
            "duration": "variable",
            "focus": "Survival, repair, decision-making",
            "challenges": "Overcoming hurt, rebuilding trust, making difficult choices"
        },
        "renewal": {
            "characteristics": ["deepened_intimacy", "authenticity", "shared_purpose", "mutual_growth"],
            "duration": "after working through crisis",
            "focus": "Thriving together, supporting each other's growth",
            "challenges": "Maintaining growth, continuing to invest"
        }
    }

    # If description is provided, try to identify stage
    identified_stage = "exploration"  # default

    if description:
        desc_lower = description.lower()
        if any(word in desc_lower for word in ["new", "just started", "beginning", "early"]):
            identified_stage = "honeymoon"
        elif any(word in desc_lower for word in ["arguing", "fighting", "conflict", "disagree"]):
            identified_stage = "power_struggle"
        elif any(word in desc_lower for word in ["stable", "comfortable", "routine", "settled"]):
            identified_stage = "stability"
        elif any(word in desc_lower for word in ["crisis", "separation", "divorce", "breaking", "ending"]):
            identified_stage = "crisis"
        elif any(word in desc_lower for word in ["better", "stronger", "closer", "deeper"]):
            identified_stage = "renewal"
    else:
        identified_stage = "self_assessment_needed"

    return {
        "stage": identified_stage,
        "stage_info": stages.get(identified_stage, {
            "characteristics": ["varied"],
            "duration": "unique to each relationship",
            "focus": "understanding your unique journey",
            "challenges": "specific to your situation"
        }),
        "guidance": "Relationships move through stages naturally. Understanding your stage helps set realistic expectations.",
        "next_steps": [
            "Discuss what stage you think you're in",
            "Share how you feel about this stage",
            "Identify what you need to move forward positively"
        ]
    }


def generate_relationship_report(areas_of_concern: List[str]) -> Dict[str, Any]:
    """
    Generates a comprehensive relationship report based on areas of concern.

    Args:
        areas_of_concern: List of relationship areas to focus on

    Returns:
        Dictionary with detailed report and recommendations
    """
    report = {
        "summary": f"Evaluating {len(areas_of_concern)} areas of concern",
        "areas": {},
        "overall_assessment": "",
        "recommendations": [],
        "priority_actions": []
    }

    concern_templates = {
        "communication": {
            "severity": "high" if "communication" in str(areas_of_concern) else "none",
            "impact": "Communication issues affect all aspects of a relationship",
            "immediate_steps": [
                "Set aside 10 minutes daily for focused conversation",
                "Practice active listening without interrupting",
                "Use 'I' statements to express feelings",
                "Choose calm moments for difficult discussions"
            ],
            "long_term_goals": [
                "Develop a communication style that works for both partners",
                "Create patterns for handling disagreements constructively"
            ]
        },
        "trust": {
            "severity": "high" if "trust" in str(areas_of_concern).lower() else "none",
            "impact": "Trust is the foundation of relationship safety",
            "immediate_steps": [
                "Be consistent in words and actions",
                "Follow through on commitments",
                "Be transparent even about difficult topics",
                "Give reasons for the other to rebuild trust"
            ],
            "long_term_goals": [
                "Rebuild emotional and relational safety",
                "Create new patterns of reliability"
            ]
        },
        "intimacy": {
            "severity": "medium" if "intimacy" in str(areas_of_concern).lower() else "none",
            "impact": "Intimacy creates the emotional bond between partners",
            "immediate_steps": [
                "Increase non-sexual physical touch",
                "Share emotions more openly",
                "Create regular quality time",
                "Show appreciation daily"
            ],
            "long_term_goals": [
                "Deepen emotional and physical connection",
                "Maintain intimacy through life's changes"
            ]
        },
        "conflict": {
            "severity": "high" if "conflict" in str(areas_of_concern).lower() else "none",
            "impact": "How couples handle conflict determines relationship success",
            "immediate_steps": [
                "Take timeouts when emotions run high",
                "Focus on the issue, not the person",
                "Look for compromise solutions",
                "Repair after arguments"
            ],
            "long_term_goals": [
                "Develop conflict styles that strengthen the relationship",
                "Resolve recurring issues permanently"
            ]
        }
    }

    for concern in areas_of_concern:
        concern_lower = concern.lower()
        for key, template in concern_templates.items():
            if key in concern_lower:
                report["areas"][concern] = template

    # Generate overall assessment
    high_count = sum(1 for a in report["areas"].values() if a.get("severity") == "high")
    if high_count >= 3:
        report["overall_assessment"] = "Multiple critical areas need attention. Consider professional counseling."
    elif high_count >= 1:
        report["overall_assessment"] = "Some areas need focused work. Progress is possible with commitment."
    else:
        report["overall_assessment"] = "Relationship appears stable with room for growth."

    # Generate recommendations
    report["recommendations"] = [
        "Prioritize the highest severity areas first",
        "Work on one area at a time for 2-4 weeks",
        "Celebrate small improvements together",
        "Seek professional support if progress stalls"
    ]

    return report
