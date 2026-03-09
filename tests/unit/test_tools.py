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

"""Unit tests for the Marriage Counselor tools."""

import pytest

from marriage_counselor.tools import (
    # Communication tools
    reflect_feelings,
    validate_experience,
    get_communication_exercise,
    get_journaling_prompt,
    # Emotion tools
    identify_emotions,
    analyze_emotional_patterns,
    suggest_emotional_vocabulary,
    # Safety tools
    check_crisis_indicators,
    get_crisis_resources,
    get_coping_strategy,
    # Relationship assessment tools
    assess_relationship_health,
    identify_relationship_stage,
    generate_relationship_report,
    # Goal setting tools
    set_relationship_goal,
    create_relationship_vision,
    track_goal_progress,
    generate_action_steps,
    # Conflict resolution tools
    analyze_conflict_pattern,
    de_escalate_conflict,
    resolve_specific_conflict,
    repair_after_conflict,
    # Values tools
    identify_personal_values,
    identify_shared_values,
    explore_value_conflict,
    align_life_vision,
    # Repair tools
    guide_repair_process,
    make_sincere_apology,
    practice_forgiveness,
    rebuild_trust_broken,
    # Intimacy tools
    build_emotional_intimacy,
    build_physical_intimacy,
    plan_quality_time,
    strengthen_fondness_admiration,
    # Boundary tools
    establish_boundary,
    explore_personal_boundaries,
    discuss_boundary_violations,
    create_family_boundaries,
    maintain_autonomy_in_togetherness,
    # Stress tools
    manage_external_stressors,
    balance_work_and_relationship,
    cope_with_life_transitions,
    build_resilience_together,
)


class TestCommunicationTools:
    """Tests for communication tools."""

    def test_reflect_feelings(self):
        """Test feeling reflection."""
        result = reflect_feelings("sad", "my relationship ending")
        assert "reflection" in result
        assert "validation" in result
        assert "sad" in result["reflection"].lower()

    def test_validate_experience(self):
        """Test experience validation."""
        result = validate_experience("feeling lonely in my marriage")
        assert "validation" in result
        assert "acknowledgment" in result

    def test_get_communication_exercise_conflict(self):
        """Test getting conflict resolution exercise."""
        result = get_communication_exercise("conflict")
        assert "name" in result
        assert "steps" in result
        assert "duration" in result
        assert result["name"] == "I-Statements Practice"

    def test_get_communication_exercise_intimacy(self):
        """Test getting intimacy exercise."""
        result = get_communication_exercise("intimacy")
        assert "name" in result
        assert result["name"] == "Daily Check-In"

    def test_get_communication_exercise_default(self):
        """Test default exercise for unknown topic."""
        result = get_communication_exercise("unknown")
        assert "name" in result

    def test_get_journaling_prompt_emotion(self):
        """Test getting journaling prompt for emotions."""
        result = get_journaling_prompt("emotions", "sad")
        assert "prompt" in result

    def test_get_journaling_prompt_default(self):
        """Test default journaling prompt."""
        result = get_journaling_prompt("unknown", "neutral")
        assert "prompt" in result


class TestEmotionTools:
    """Tests for emotion analysis tools."""

    def test_identify_emotions_sadness(self):
        """Test identifying sadness."""
        result = identify_emotions("I feel so sad and lonely")
        assert "primary_emotion" in result
        assert result["primary_emotion"] in ["sadness", "lonely"]

    def test_identify_emotions_anger(self):
        """Test identifying anger."""
        result = identify_emotions("I'm so angry and frustrated")
        assert "primary_emotion" in result
        assert result["primary_emotion"] in ["anger", "frustrated"]

    def test_identify_emotions_no_match(self):
        """Test when no emotions are detected."""
        result = identify_emotions("The weather is nice today")
        assert "primary_emotion" in result
        assert "validation" in result

    def test_analyze_emotional_patterns(self):
        """Test analyzing emotional patterns."""
        history = [
            "I feel really sad and lonely",
            "I'm anxious about everything"
        ]
        result = analyze_emotional_patterns(history)
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_suggest_emotional_vocabulary(self):
        """Test emotional vocabulary suggestions."""
        result = suggest_emotional_vocabulary("angry")
        assert "emotions" in result
        assert len(result["emotions"]) > 0


class TestSafetyTools:
    """Tests for safety tools."""

    def test_check_crisis_indicators_suicide(self):
        """Test suicide crisis detection."""
        result = check_crisis_indicators("I'm thinking about suicide")
        assert result["crisis_detected"] is True
        assert result["crisis_type"] == "suicide_self_harm"
        assert result["severity"] == "high"

    def test_check_crisis_indicators_domestic_violence(self):
        """Test domestic violence crisis detection."""
        result = check_crisis_indicators("I'm afraid of my partner")
        assert result["crisis_detected"] is True
        assert result["crisis_type"] == "domestic_violence"

    def test_check_crisis_indicators_none(self):
        """Test when no crisis is detected."""
        result = check_crisis_indicators("My partner and I argue about money")
        assert result["crisis_detected"] is False
        assert result["severity"] == "none"

    def test_get_crisis_resources(self):
        """Test getting crisis resources."""
        result = get_crisis_resources("suicide_self_harm")
        assert "resources" in result
        assert "support_message" in result
        assert len(result["resources"]) > 0

    def test_get_coping_strategy(self):
        """Test getting coping strategies."""
        result = get_coping_strategy("relationship stress", "medium")
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0


class TestRelationshipAssessmentTools:
    """Tests for relationship assessment tools."""

    def test_assess_relationship_health(self):
        """Test relationship health assessment."""
        aspects = ["communication", "intimacy", "trust"]
        result = assess_relationship_health(aspects)
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_identify_relationship_stage(self):
        """Test relationship stage identification."""
        result = identify_relationship_stage("new relationship, everything is perfect")
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_generate_relationship_report(self):
        """Test generating relationship report."""
        concerns = ["communication", "conflict"]
        result = generate_relationship_report(concerns)
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0


class TestGoalSettingTools:
    """Tests for goal setting tools."""

    def test_set_relationship_goal(self):
        """Test setting relationship goal."""
        result = set_relationship_goal("communication", "improve listening", "3 months")
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_create_relationship_vision(self):
        """Test creating relationship vision."""
        result = create_relationship_vision()
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_track_goal_progress(self):
        """Test tracking goal progress."""
        result = track_goal_progress("improve communication", "some progress")
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_generate_action_steps(self):
        """Test generating action steps."""
        result = generate_action_steps("communication", "better listening")
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0


class TestConflictResolutionTools:
    """Tests for conflict resolution tools."""

    def test_analyze_conflict_pattern(self):
        """Test analyzing conflict patterns."""
        result = analyze_conflict_pattern("we argue about the same things repeatedly")
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_de_escalate_conflict(self):
        """Test conflict de-escalation."""
        result = de_escalate_conflict()
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_resolve_specific_conflict(self):
        """Test resolving specific conflict."""
        result = resolve_specific_conflict("money management")
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_repair_after_conflict(self):
        """Test repair after conflict."""
        result = repair_after_conflict()
        # Just check we get a valid result
        assert isinstance(result, dict)
        assert len(result) > 0


class TestValuesTools:
    """Tests for values tools."""

    def test_identify_personal_values(self):
        """Test identifying personal values."""
        result = identify_personal_values()
        assert "value_categories" in result
        assert "reflection_questions" in result
        assert len(result["value_categories"]) > 0

    def test_identify_shared_values(self):
        """Test identifying shared values."""
        p1_values = ["honesty", "family", "communication"]
        p2_values = ["family", "honesty", "independence"]
        result = identify_shared_values(p1_values, p2_values)
        assert "shared_values" in result
        assert "unique_to_partner1" in result
        assert len(result["shared_values"]) > 0

    def test_explore_value_conflict(self):
        """Test exploring value conflicts."""
        result = explore_value_conflict("finances")
        assert "common_conflicts" in result
        assert "create_solution" in result

    def test_align_life_vision(self):
        """Test aligning life vision."""
        result = align_life_vision()
        assert "vision_questions" in result
        assert "next_steps" in result


class TestRepairTools:
    """Tests for repair and healing tools."""

    def test_guide_repair_process_betrayal(self):
        """Test repair process for betrayal."""
        result = guide_repair_process("betrayal")
        assert "process" in result
        assert "timeline" in result

    def test_make_sincere_apology(self):
        """Test making sincere apology."""
        result = make_sincere_apology("forgot anniversary")
        assert "apology_components" in result
        assert "apology_template" in result

    def test_practice_forgiveness(self):
        """Test forgiveness practice."""
        result = practice_forgiveness("decision")
        assert "current_stage" in result
        assert "stage_info" in result

    def test_rebuild_trust_broken(self):
        """Test rebuilding broken trust."""
        result = rebuild_trust_broken("infidelity")
        assert "rebuilding_actions" in result
        assert "timeline_expectation" in result


class TestIntimacyTools:
    """Tests for intimacy tools."""

    def test_build_emotional_intimacy(self):
        """Test building emotional intimacy."""
        result = build_emotional_intimacy()
        assert "daily_practices" in result
        assert "deepening_exercises" in result

    def test_build_physical_intimacy(self):
        """Test building physical intimacy."""
        result = build_physical_intimacy("general")
        assert "principles" in result
        assert "building_blocks" in result

    def test_plan_quality_time(self):
        """Test planning quality time."""
        result = plan_quality_time()
        assert "time_types" in result
        assert "principles" in result

    def test_strengthen_fondness_admiration(self):
        """Test strengthening fondness and admiration."""
        result = strengthen_fondness_admiration()
        assert "daily_appreciation" in result
        assert "building_friendship" in result


class TestBoundaryTools:
    """Tests for boundary tools."""

    def test_establish_boundary(self):
        """Test establishing boundaries."""
        result = establish_boundary("communication", "no yelling")
        assert "boundary_statement" in result
        # Check nested structure exists
        assert "examples" in result.get("boundary_statement", {})

    def test_explore_personal_boundaries(self):
        """Test exploring personal boundaries."""
        result = explore_personal_boundaries()
        assert "boundary_categories" in result
        assert "values_assessment" in result

    def test_discuss_boundary_violations(self):
        """Test discussing boundary violations."""
        result = discuss_boundary_violations()
        assert "when_boundaries_are_crossed" in result
        assert "productive_conversation" in result

    def test_create_family_boundaries(self):
        """Test creating family boundaries."""
        result = create_family_boundaries()
        assert "guidelines" in result
        assert "common_challenges" in result

    def test_maintain_autonomy_in_togetherness(self):
        """Test maintaining autonomy."""
        result = maintain_autonomy_in_togetherness()
        assert "areas_of_autonomy" in result
        assert "practices" in result


class TestStressTools:
    """Tests for stress management tools."""

    def test_manage_external_stressors(self):
        """Test managing external stressors."""
        result = manage_external_stressors(["work", "finances"])
        assert "stress_impact_on_relationships" in result
        assert "common_stressors" in result

    def test_balance_work_and_relationship(self):
        """Test work-life balance."""
        result = balance_work_and_relationship()
        assert "strategies" in result
        assert "dealing_with_imbalance" in result

    def test_cope_with_life_transitions(self):
        """Test coping with life transitions."""
        result = cope_with_life_transitions("new_parents")
        assert "challenges" in result
        assert "relationship_protection" in result

    def test_build_resilience_together(self):
        """Test building resilience together."""
        result = build_resilience_together()
        assert "resilience_components" in result
        assert "building_practices" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
