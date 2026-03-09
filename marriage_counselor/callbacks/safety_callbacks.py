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

"""Safety callbacks for crisis detection and content filtering."""

import logging
from typing import Any, Dict, Optional

from google.adk import Agent
from google.genai import types

from ..config import configs
from ..tools.safety_tools import (
    check_crisis_indicators,
    get_crisis_resources,
    check_professional_referral_needed,
)
from ..prompts import CRISIS_RESPONSE

logger = logging.getLogger(__name__)


def crisis_detection_callback(
    agent: Agent,
    invocation_context: Any,
) -> Optional[Dict[str, Any]]:
    """
    Callback to detect crisis indicators in user messages.

    This function runs before the agent processes a message and checks
    for crisis indicators that require immediate intervention.

    Args:
        agent: The agent being called
        invocation_context: The invocation context

    Returns:
        Dictionary with crisis response if detected, None otherwise
    """
    if not configs.safety.enable_crisis_detection:
        return None

    try:
        # Get user message from invocation context
        user_content = invocation_context.user_message

        if not user_content:
            return None

        # Extract text from content
        if isinstance(user_content, types.Content):
            message_text = " ".join(
                part.text for part in user_content.parts if part.text
            )
        elif isinstance(user_content, str):
            message_text = user_content
        else:
            return None

        # Check for crisis indicators
        crisis_check = check_crisis_indicators(message_text)

        if crisis_check["crisis_detected"]:
            logger.warning(
                f"Crisis detected: {crisis_check['crisis_type']} "
                f"(severity: {crisis_check['severity']})"
            )

            # Get appropriate crisis resources
            crisis_response = get_crisis_resources(crisis_check["crisis_type"])

            return {
                "is_crisis": True,
                "crisis_type": crisis_check["crisis_type"],
                "severity": crisis_check["severity"],
                "response": crisis_response["support_message"],
                "override_agent": True,
            }

    except Exception as e:
        logger.error(f"Error in crisis detection callback: {e}")

    return None


def before_agent_safety_check(
    agent: Agent,
    invocation_context: Any,
) -> Optional[Dict[str, Any]]:
    """
    Callback that runs before agent execution for safety checks.

    Args:
        agent: The agent about to be called
        invocation_context: The invocation context

    Returns:
        Dictionary with safety check results
    """
    try:
        user_content = invocation_context.user_message

        if not user_content:
            return None

        # Extract text from content
        if isinstance(user_content, types.Content):
            message_text = " ".join(
                part.text for part in user_content.parts if part.text
            )
        elif isinstance(user_content, str):
            message_text = user_content
        else:
            return None

        # Check for professional referral triggers
        referral_check = check_professional_referral_needed(message_text)

        if referral_check["referral_recommended"]:
            logger.info(f"Professional referral recommended: {referral_check['trigger']}")

            return {
                "referral_recommended": True,
                "trigger": referral_check["trigger"],
                "referral_message": referral_check["message"],
            }

    except Exception as e:
        logger.error(f"Error in before_agent_safety_check: {e}")

    return None


def after_model_safety_check(
    agent: Agent,
    invocation_context: Any,
    model_response: str,
) -> Optional[Dict[str, Any]]:
    """
    Callback that runs after model response for safety filtering.

    This callback can filter or modify the model's response if needed.

    Args:
        agent: The agent that generated the response
        invocation_context: The invocation context
        model_response: The model's response

    Returns:
        Dictionary with any modifications or warnings
    """
    try:
        # Check if response contains any concerning patterns
        concerning_patterns = [
            "diagnose", "disorder", "medical condition",
            "prescribe", "medication", "treatment plan",
        ]

        response_lower = model_response.lower()

        for pattern in concerning_patterns:
            if pattern in response_lower:
                logger.warning(f"Model response contains concerning pattern: {pattern}")

                return {
                    "safety_warning": True,
                    "pattern_found": pattern,
                    "note": "Response may be providing medical/clinical advice",
                }

    except Exception as e:
        logger.error(f"Error in after_model_safety_check: {e}")

    return None


def rate_limit_callback(
    agent: Agent,
    invocation_context: Any,
) -> Optional[Dict[str, Any]]:
    """
    Callback for rate limiting to prevent abuse.

    Args:
        agent: The agent being called
        invocation_context: The invocation context

    Returns:
        Dictionary with rate limit status
    """
    # Basic rate limiting - in production, this would use Redis or similar
    # For now, we'll just log the invocation

    user_id = getattr(invocation_context, "user_id", "unknown")

    logger.info(f"Agent {agent.name} called by user {user_id}")

    # In a production environment, you would:
    # 1. Track request count per user
    # 2. Enforce rate limits
    # 3. Return error if limit exceeded

    return None
