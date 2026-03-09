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

"""Output schemas for the Marriage Counselor agents."""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class EmotionAnalysisOutput(BaseModel):
    """Output schema for emotion analysis."""

    primary_emotion: str = Field(description="The main emotion identified")
    secondary_emotions: List[str] = Field(
        default_factory=list,
        description="Additional emotions present",
    )
    intensity: str = Field(
        description="Intensity level (low, moderate, high)",
    )
    emotional_needs: List[str] = Field(
        default_factory=list,
        description="Underlying needs suggested by the emotions",
    )
    validation: str = Field(
        description="A validating statement acknowledging the emotions",
    )


class EmotionalPatternOutput(BaseModel):
    """Output schema for emotional pattern analysis."""

    patterns: List[str] = Field(
        default_factory=list,
        description="Identified emotional patterns",
    )
    triggers: List[str] = Field(
        default_factory=list,
        description="Common triggers for emotions",
    )
    themes: List[str] = Field(
        default_factory=list,
        description="Recurring themes in emotional responses",
    )
    insights: List[str] = Field(
        default_factory=list,
        description="Insights about emotional patterns",
    )


class CommunicationExerciseOutput(BaseModel):
    """Output schema for communication exercises."""

    name: str = Field(description="Name of the exercise")
    description: str = Field(description="Brief description of the exercise")
    steps: List[str] = Field(description="Step-by-step instructions")
    duration: str = Field(description="Expected time to complete")
    tips: List[str] = Field(
        default_factory=list,
        description="Tips for success",
    )
    benefits: str = Field(description="Expected benefits of the exercise")


class CopingStrategyOutput(BaseModel):
    """Output schema for coping strategies."""

    strategy_name: str = Field(description="Name of the coping strategy")
    description: str = Field(description="Description of the strategy")
    techniques: List[str] = Field(
        default_factory=list,
        description="Specific techniques to use",
    )
    timing_suggestions: List[str] = Field(
        default_factory=list,
        description="When to apply these techniques",
    )
    additional_resources: List[str] = Field(
        default_factory=list,
        description="Additional resources for support",
    )


class ReflectionResponse(BaseModel):
    """Output schema for reflective listening responses."""

    reflection: str = Field(description="The reflective statement")
    validation: str = Field(description="Validation of the user's experience")
    follow_up_question: Optional[str] = Field(
        default=None,
        description="Optional gentle follow-up question",
    )
