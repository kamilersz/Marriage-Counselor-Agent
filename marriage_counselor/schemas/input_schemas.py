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

"""Input schemas for the Marriage Counselor agents."""

from pydantic import BaseModel, Field


class CounselingInput(BaseModel):
    """Input schema for the main counseling coordinator."""

    message: str = Field(
        description="The user's message or concern they want to share"
    )
    session_phase: str = Field(
        default="introduction",
        description="Current phase of the counseling session",
    )


class EmotionAnalysisInput(BaseModel):
    """Input schema for emotion analysis."""

    text: str = Field(description="The text to analyze for emotions")
    context: str = Field(
        default="",
        description="Additional context about the situation",
    )


class FeelingReflectionInput(BaseModel):
    """Input schema for feeling reflection."""

    feeling: str = Field(description="The emotion the user is experiencing")
    context: str = Field(description="The situation or context for the feeling")


class CommunicationExerciseInput(BaseModel):
    """Input schema for communication exercises."""

    topic: str = Field(
        description="The relationship area to work on (e.g., 'conflict', 'intimacy', 'trust')"
    )
    relationship_type: str = Field(
        default="couple",
        description="Type of relationship (couple, individual, family)",
    )


class CopingStrategyInput(BaseModel):
    """Input schema for coping strategies."""

    challenge: str = Field(description="The challenge or stressor the user is facing")
    severity: str = Field(
        default="moderate",
        description="Severity level (mild, moderate, severe)",
    )


class JournalingPromptInput(BaseModel):
    """Input schema for journaling prompts."""

    focus: str = Field(
        description="The focus area for journaling (emotions, relationships, self-reflection, etc.)"
    )
    mood: str = Field(
        default="neutral",
        description="User's current mood for context",
    )
