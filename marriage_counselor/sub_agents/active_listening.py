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

"""Active Listening Agent for empathetic reflection and validation."""

from google.adk.agents import LlmAgent

from ..config import configs
from ..prompts import ACTIVE_LISTENING_INSTRUCTION
from ..tools import reflect_feelings, validate_experience


active_listening_agent = LlmAgent(
    model=configs.agent.specialist_model,
    name="active_listening_agent",
    description=(
        "An empathetic active listener who provides reflective listening, "
        "validates feelings, and helps users feel heard and understood. "
        "Specializes in relationship communication and emotional support."
    ),
    instruction=ACTIVE_LISTENING_INSTRUCTION,
    tools=[reflect_feelings, validate_experience],
    output_key="active_listening_response",
)
