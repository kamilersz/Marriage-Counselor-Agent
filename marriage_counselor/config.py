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

"""Configuration module for the Marriage Counselor Agent."""

import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import Literal

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    # Try to load from .env in the project root
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(env_path)

    # Support both GEMINI_API_KEY and GOOGLE_API_KEY
    if os.getenv("GEMINI_API_KEY") and not os.getenv("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
except ImportError:
    # Support both GEMINI_API_KEY and GOOGLE_API_KEY without dotenv
    if os.getenv("GEMINI_API_KEY") and not os.getenv("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")


@dataclass
class AgentSettings:
    """Settings for agent models and names."""

    model: str = field(
        default_factory=lambda: os.getenv(
            "COORDINATOR_MODEL", "gemini-3.1-flash-preview"
        )
    )
    specialist_model: str = field(
        default_factory=lambda: os.getenv(
            "SPECIALIST_MODEL", "gemini-3.1-flash-lite-preview"
        )
    )
    name: str = "counseling_coordinator"


@dataclass
class AppSettings:
    """Application-level settings."""

    app_name: str = "marriage_counselor"
    max_session_duration: int = field(
        default_factory=lambda: int(os.getenv("MAX_SESSION_DURATION", "1800"))
    )


@dataclass
class SafetySettings:
    """Safety and crisis detection settings."""

    enable_crisis_detection: bool = field(
        default_factory=lambda: (
            os.getenv("ENABLE_CRISIS_DETECTION", "true").lower() == "true"
        )
    )
    crisis_hotline_number: str = field(
        default_factory=lambda: os.getenv("CRISIS_HOTLINE_NUMBER", "988")
    )


@dataclass
class SessionSettings:
    """Session management settings."""

    enable_session_persistence: bool = True
    max_conversation_history: int = 50


@dataclass
class CounselorConfig:
    """Main configuration class for the Marriage Counselor Agent."""

    agent: AgentSettings = field(default_factory=AgentSettings)
    app: AppSettings = field(default_factory=AppSettings)
    safety: SafetySettings = field(default_factory=SafetySettings)
    session: SessionSettings = field(default_factory=SessionSettings)

    @classmethod
    def from_env(cls) -> "CounselorConfig":
        """Create configuration from environment variables."""
        return cls()


# Global configuration instance
configs = CounselorConfig.from_env()
