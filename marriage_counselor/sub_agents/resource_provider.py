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

"""Resource Provider Agent for practical tools and strategies."""

from google.adk.agents import LlmAgent

from ..config import configs
from ..prompts import RESOURCE_PROVIDER_INSTRUCTION
from ..tools import get_communication_exercise, get_journaling_prompt, get_coping_strategy


resource_provider_agent = LlmAgent(
    model=configs.agent.specialist_model,
    name="resource_provider_agent",
    description=(
        "A resource specialist who provides evidence-based communication exercises, "
        "coping strategies, journaling prompts, and practical tools for relationship health. "
        "Helps users develop skills for healthier relationships."
    ),
    instruction=RESOURCE_PROVIDER_INSTRUCTION,
    tools=[get_communication_exercise, get_journaling_prompt, get_coping_strategy],
    output_key="resource_recommendations",
)
