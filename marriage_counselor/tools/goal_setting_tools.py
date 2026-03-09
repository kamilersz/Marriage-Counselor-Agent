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

"""Goal setting tools for relationship improvement."""

import random
from typing import Dict, List, Any


def set_relationship_goal(area: str, goal: str, timeline: str = "3 months") -> Dict[str, Any]:
    """
    Helps couples set SMART goals for relationship improvement.

    Args:
        area: The relationship area to focus on
        goal: The specific goal description
        timeline: Target timeline for achievement

    Returns:
        Dictionary with structured goal and action plan
    """
    # Make goal SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
    smart_framework = {
        "specific": f"Goal: {goal}",
        "measurable": [
            "How will you know when this is achieved?",
            "What specific behaviors will change?",
            "What will be different in daily life?"
        ],
        "achievable": [
            "Is this realistic given your current situation?",
            "What resources or support do you need?",
            "What might get in the way?"
        ],
        "relevant": [
            "Why does this matter to your relationship?",
            "How does this align with your values?",
            "What happens if you don't achieve this?"
        ],
        "time_bound": {
            "timeline": timeline,
            "checkpoints": f"Weekly progress reviews for {timeline}",
            "celebration": "Plan to celebrate milestones along the way"
        }
    }

    # Action plan template
    action_plan = {
        "goal": goal,
        "area": area,
        "timeline": timeline,
        "first_steps": [
            f"Discuss what success looks like for both partners",
            "Identify what each person will do differently",
            "Set up weekly check-in time",
            "Choose a start date"
        ],
        "potential_obstacles": [
            "Old habits kicking in during stress",
            "Forgetting the commitment when busy",
            "One partner more motivated than the other",
            "External stressors interfering"
        ],
        "obstacle_solutions": [
            "Set up reminder systems",
            "Create accountability check-ins",
            "Address motivation differences openly",
            "Plan for how to handle stressful periods"
        ],
        "success_indicators": [
            "Both partners report progress",
            "Specific situations going differently",
            "Increased satisfaction in the area",
            "Reduced conflict related to this issue"
        ]
    }

    return {
        "smart_goal": smart_framework,
        "action_plan": action_plan,
        "encouragement": "Setting goals together creates shared purpose and hope."
    }


def create_relationship_vision() -> Dict[str, str]:
    """
    Guides couples in creating a shared relationship vision.

    Returns:
        Dictionary with vision prompts and framework
    """
    vision_prompts = {
        "emotional": [
            "How do you want to feel when you're together?",
            "What emotional safety looks like for you?",
            "How do you want to support each other emotionally?"
        ],
        "practical": [
            "What does a typical day look like in your ideal relationship?",
            "How do you handle daily responsibilities together?",
            "What routines strengthen your connection?"
        ],
        "growth": [
            "How do you want to grow together?",
            "What do you want to learn as a couple?",
            "What experiences do you want to share?"
        ],
        "long_term": [
            "Where do you see yourselves in 5 years?",
            "What do you want to have built together?",
            "How do you want to handle life's challenges together?"
        ],
        "crisis": [
            "How do you want to handle difficult times?",
            "What support do you need from each other?",
            "What will help you weather storms together?"
        ]
    }

    return {
        "vision_framework": "A shared vision gives your relationship direction and meaning.",
        "prompts": vision_prompts,
        "activity": "Take 30 minutes to separately write your vision, then share and combine them.",
        "benefits": [
            "Creates shared purpose",
            "Guides decision-making",
            "Inspires during difficult times",
            "Strengthens commitment"
        ]
    }


def track_goal_progress(goal: str, current_status: str) -> Dict[str, Any]:
    """
    Tracks and evaluates progress toward relationship goals.

    Args:
        goal: The goal being tracked
        current_status: Current progress description

    Returns:
        Dictionary with progress assessment and guidance
    """
    progress_assessment = {
        "goal": goal,
        "current_status": current_status,
        "evaluation_questions": [
            "What progress have you made since starting?",
            "What's working well with your approach?",
            "What obstacles have you encountered?",
            "What needs to be adjusted?"
        ],
        "celebrate": [
            "Acknowledge the effort you're both putting in",
            "Recognize even small changes",
            "Share appreciation for each other's contributions"
        ],
        "adjust": [
            "Is the timeline realistic?",
            "Do you need additional resources?",
            "Should the goal be modified?",
            "Are both partners still committed?"
        ],
        "next_steps": [
            "Schedule next check-in",
            "Update action plan if needed",
            "Address any barriers that emerged",
            "Reaffirm commitment to the goal"
        ]
    }

    return progress_assessment


def generate_action_steps(area: str, specific_goal: str) -> Dict[str, Any]:
    """
    Generates specific, actionable steps for relationship goals.

    Args:
        area: The relationship area
        specific_goal: The specific goal

    Returns:
        Dictionary with detailed action steps
    """
    action_steps_templates = {
        "communication": {
            "daily": [
                "Share one thing you appreciated about your partner",
                "Ask one open-ended question about their day",
                "Practice active listening for 5 minutes",
                "Express one need clearly and kindly"
            ],
            "weekly": [
                "Have a 30-minute uninterrupted conversation",
                "Discuss one thing that went well and one to improve",
                "Plan enjoyable time together for next week",
                "Review and appreciate progress"
            ]
        },
        "intimacy": {
            "daily": [
                "Greet each other warmly when reuniting",
                "Show physical affection (hug, touch, holding hands)",
                "Share one feeling or experience",
                "Show appreciation for one thing"
            ],
            "weekly": [
                "Have a dedicated date night or quality time",
                "Try something new together",
                "Share emotional vulnerably",
                "Discuss relationship satisfaction"
            ]
        },
        "conflict": {
            "daily": [
                "Respond rather than react in stressful moments",
                "Take a timeout if emotions run high",
                "Remember you're on the same team",
                "Choose kindness over being right"
            ],
            "weekly": [
                "Review any conflicts from the week",
                "Discuss what worked and what didn't",
                "Repair any damage from arguments",
                "Practice a new conflict skill"
            ]
        },
        "trust": {
            "daily": [
                "Follow through on small commitments",
                "Be transparent about your day",
                "Show reliability in small ways",
                "Be emotionally available"
            ],
            "weekly": [
                "Discuss how trust is building",
                "Share any concerns honestly",
                "Acknowledge trust-building actions",
                "Plan meaningful experiences together"
            ]
        },
        "finances": {
            "daily": [
                "Communicate about purchases over agreed amount",
                "Respect spending agreements",
                "Discuss money without blame",
                "Acknowledge each other's contributions"
            ],
            "weekly": [
                "Review spending together briefly",
                "Discuss upcoming financial decisions",
                "Progress toward financial goals",
                "Align on priorities"
            ]
        }
    }

    area_lower = area.lower()
    if area_lower in action_steps_templates:
        steps = action_steps_templates[area_lower]
    else:
        steps = {
            "daily": ["Take one action toward your goal", "Support your partner's effort"],
            "weekly": ["Review progress together", "Adjust approach as needed"]
        }

    return {
        "goal": specific_goal,
        "area": area,
        "daily_actions": steps["daily"],
        "weekly_actions": steps.get("weekly", []),
        "implementation_tips": [
            "Start small - consistency beats intensity",
            "Both partners should have clear actions",
            "Track progress visually (checklist, app)",
            "Celebrate weekly wins together",
            "Adjust if something isn't working"
        ],
        "accountability": [
            "Daily: briefly check in about your action",
            "Weekly: review how the week went",
            "Monthly: assess overall progress and adjust",
            "Share successes and challenges honestly"
        ]
    }
