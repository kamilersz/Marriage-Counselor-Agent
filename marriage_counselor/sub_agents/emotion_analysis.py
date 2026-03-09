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

"""Emotion Analysis Agent for understanding emotional patterns."""

from google.adk.agents import LlmAgent

from ..config import configs
from ..prompts import EMOTION_ANALYSIS_INSTRUCTION
from ..tools import identify_emotions, analyze_emotional_patterns, suggest_emotional_vocabulary


emotion_analysis_agent = LlmAgent(
    model=configs.agent.model,  # Use more capable model for analysis
    name="emotion_analysis_agent",
    description=(
        "An emotion specialist who helps users understand their emotional patterns, "
        "identify underlying feelings, and recognize emotional needs. "
        "Provides insights into emotional dynamics in relationships."
    ),
    instruction=EMOTION_ANALYSIS_INSTRUCTION,
    tools=[identify_emotions, analyze_emotional_patterns, suggest_emotional_vocabulary],
    output_key="emotion_analysis_result",
)
