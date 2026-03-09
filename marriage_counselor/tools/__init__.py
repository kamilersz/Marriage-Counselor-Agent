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

"""Tools for the Marriage Counselor agents."""

# Communication tools
from .communication_tools import (
    reflect_feelings,
    validate_experience,
    get_communication_exercise,
    get_journaling_prompt,
)

# Emotion tools
from .emotion_tools import (
    identify_emotions,
    analyze_emotional_patterns,
    suggest_emotional_vocabulary,
)

# Safety tools
from .safety_tools import (
    check_resource_safety,
    check_crisis_indicators,
    get_crisis_resources,
    get_coping_strategy,
)

# Relationship assessment tools
from .relationship_assessment_tools import (
    assess_relationship_health,
    identify_relationship_stage,
    generate_relationship_report,
)

# Goal setting tools
from .goal_setting_tools import (
    set_relationship_goal,
    create_relationship_vision,
    track_goal_progress,
    generate_action_steps,
)

# Conflict resolution tools
from .conflict_resolution_tools import (
    analyze_conflict_pattern,
    de_escalate_conflict,
    resolve_specific_conflict,
    repair_after_conflict,
)

# Values tools
from .values_tools import (
    identify_personal_values,
    identify_shared_values,
    explore_value_conflict,
    align_life_vision,
)

# Repair tools
from .repair_tools import (
    guide_repair_process,
    make_sincere_apology,
    practice_forgiveness,
    rebuild_trust_broken,
)

# Intimacy tools
from .intimacy_tools import (
    build_emotional_intimacy,
    build_physical_intimacy,
    plan_quality_time,
    strengthen_fondness_admiration,
)

# Boundary tools
from .boundary_tools import (
    establish_boundary,
    explore_personal_boundaries,
    discuss_boundary_violations,
    create_family_boundaries,
    maintain_autonomy_in_togetherness,
)

# Stress tools
from .stress_tools import (
    manage_external_stressors,
    balance_work_and_relationship,
    cope_with_life_transitions,
    build_resilience_together,
)

__all__ = [
    # Communication tools
    "reflect_feelings",
    "validate_experience",
    "get_communication_exercise",
    "get_journaling_prompt",
    # Emotion tools
    "identify_emotions",
    "analyze_emotional_patterns",
    "suggest_emotional_vocabulary",
    # Safety tools
    "check_resource_safety",
    "check_crisis_indicators",
    "get_crisis_resources",
    "get_coping_strategy",
    # Relationship assessment tools
    "assess_relationship_health",
    "identify_relationship_stage",
    "generate_relationship_report",
    # Goal setting tools
    "set_relationship_goal",
    "create_relationship_vision",
    "track_goal_progress",
    "generate_action_steps",
    # Conflict resolution tools
    "analyze_conflict_pattern",
    "de_escalate_conflict",
    "resolve_specific_conflict",
    "repair_after_conflict",
    # Values tools
    "identify_personal_values",
    "identify_shared_values",
    "explore_value_conflict",
    "align_life_vision",
    # Repair tools
    "guide_repair_process",
    "make_sincere_apology",
    "practice_forgiveness",
    "rebuild_trust_broken",
    # Intimacy tools
    "build_emotional_intimacy",
    "build_physical_intimacy",
    "plan_quality_time",
    "strengthen_fondness_admiration",
    # Boundary tools
    "establish_boundary",
    "explore_personal_boundaries",
    "discuss_boundary_violations",
    "create_family_boundaries",
    "maintain_autonomy_in_togetherness",
    # Stress tools
    "manage_external_stressors",
    "balance_work_and_relationship",
    "cope_with_life_transitions",
    "build_resilience_together",
]
