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

"""Root agent definition for the Marriage Counselor system."""

import logging
import warnings

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import load_memory
from google.adk.memory import InMemoryMemoryService

from .config import configs
from .prompts import (
    GLOBAL_INSTRUCTION,
    COORDINATOR_INSTRUCTION,
)
from .sub_agents import (
    # Core agents
    active_listening_agent,
    emotion_analysis_agent,
    resource_provider_agent,
    # Specialized agents
    relationship_assessment_agent,
    goal_setting_agent,
    conflict_resolution_agent,
    values_alignment_agent,
    repair_healing_agent,
    intimacy_specialist_agent,
    boundary_specialist_agent,
    stress_management_agent,
)

warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")

logger = logging.getLogger(__name__)

# Create a shared memory service for long-term conversation memory
# This will be shared across all sessions and runners
memory_service = InMemoryMemoryService()


# Create the counseling coordinator (root agent)
counseling_coordinator = LlmAgent(
    model=configs.agent.model,
    name=configs.agent.name,
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=COORDINATOR_INSTRUCTION,
    description=(
        "A comprehensive marriage counseling coordinator who guides users "
        "through a supportive process by orchestrating specialist agents. "
        "Creates a safe space for exploring relationship concerns with "
        "empathy, while maintaining professional boundaries. "
        "Has access to past conversation memory to provide personalized support. "
        "Coordinates assessment, goal setting, conflict resolution, values alignment, "
        "repair and healing, intimacy building, boundary setting, and stress management."
    ),
    tools=[
        # Core specialist agents
        AgentTool(agent=active_listening_agent),
        AgentTool(agent=emotion_analysis_agent),
        AgentTool(agent=resource_provider_agent),
        # Comprehensive specialist agents
        AgentTool(agent=relationship_assessment_agent),
        AgentTool(agent=goal_setting_agent),
        AgentTool(agent=conflict_resolution_agent),
        AgentTool(agent=values_alignment_agent),
        AgentTool(agent=repair_healing_agent),
        AgentTool(agent=intimacy_specialist_agent),
        AgentTool(agent=boundary_specialist_agent),
        AgentTool(agent=stress_management_agent),
        # Memory tool for long-term conversation memory
        load_memory,
    ],
    output_key="counseling_coordination_output",
)

# Export the root agent
root_agent = counseling_coordinator


# Allow running the agent directly
def main():
    """Main entry point for running the agent interactively."""
    import asyncio
    import os

    # Import config to ensure environment variables are loaded
    from . import config
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    from google.genai import types

    async def run_agent():
        """Run the agent interactively."""
        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        print("=" * 60)
        print("Marriage Counselor Agent")
        print("=" * 60)
        print(f"Agent: {root_agent.name}")
        print(f"Model: {root_agent.model}")
        print()
        print("DISCLAIMER: This is an AI assistant, not a licensed mental")
        print("health professional. For serious concerns, please seek")
        print("professional help.")
        print()
        print("Crisis Resources:")
        print("  - Suicide & Crisis Lifeline: 988")
        print("  - Domestic Violence Hotline: 1-800-799-7233")
        print("  - Crisis Text Line: Text HOME to 741741")
        print()
        print("Type your message below (or 'quit' to exit)")
        print("-" * 60)

        # Set up session and runner with memory service
        session_service = InMemorySessionService()
        runner = Runner(
            agent=root_agent,
            app_name=configs.app.app_name,
            session_service=session_service,
            memory_service=memory_service,  # Add memory service for long-term memory
        )

        # Create session
        user_id = "user"
        session_id = "session"

        # Try to load existing session, or create new one
        try:
            session = await session_service.get_session(
                app_name=configs.app.app_name,
                user_id=user_id,
                session_id=session_id,
            )
            logger.info(f"Loaded existing session: {session.id}")
        except Exception:
            await session_service.create_session(
                app_name=configs.app.app_name,
                user_id=user_id,
                session_id=session_id,
            )
            logger.info(f"Created new session: {session_id}")

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if user_input.lower() in ["quit", "exit", "q"]:
                    print("\nThank you for using the Marriage Counselor Agent.")
                    print("Remember: You deserve support. Don't hesitate to reach")
                    print("out to professional resources if you need them.")
                    break

                if not user_input:
                    continue

                # Send message to agent
                user_content = types.Content(
                    role="user",
                    parts=[types.Part(text=user_input)]
                )

                print("\nCounselor: ", end="", flush=True)

                response_received = False
                async for event in runner.run_async(
                    user_id=user_id,
                    session_id=session_id,
                    new_message=user_content,
                ):
                    if event.is_final_response() and event.content:
                        response_received = True
                        for part in event.content.parts:
                            if part.text:
                                print(part.text, end="", flush=True)

                if response_received:
                    print()  # New line after response

                    # Auto-save session to memory after each interaction
                    # This allows the agent to remember past conversations
                    try:
                        current_session = await session_service.get_session(
                            app_name=configs.app.app_name,
                            user_id=user_id,
                            session_id=session_id,
                        )
                        await memory_service.add_session_to_memory(current_session)
                        logger.debug("Session saved to memory")
                    except Exception as e:
                        logger.warning(f"Could not save session to memory: {e}")

            except KeyboardInterrupt:
                print("\n\nGoodbye! Remember to reach out for support when you need it.")
                break
            except Exception as e:
                logger.error(f"Error: {e}")
                print(f"\nAn error occurred. Please try again.")

    # Run the async main function
    asyncio.run(run_agent())


if __name__ == "__main__":
    main()
