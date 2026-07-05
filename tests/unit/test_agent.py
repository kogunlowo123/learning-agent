"""Learning Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_recommend_learning_path():
    """Test Recommend a personalized learning path based on role and goals."""
    tools = AgentTools()
    result = await tools.recommend_learning_path(employee_id="test", target_role="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_enroll_course():
    """Test Enroll an employee in a learning course or program."""
    tools = AgentTools()
    result = await tools.enroll_course(employee_id="test", course_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_progress():
    """Test Track learning progress and completion rates."""
    tools = AgentTools()
    result = await tools.track_progress(employee_id="test", team_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_measure_effectiveness():
    """Test Measure learning effectiveness through assessments and behavior change."""
    tools = AgentTools()
    result = await tools.measure_effectiveness(course_id="test", metrics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.learning_agent_agent import LearningAgentAgent
    agent = LearningAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
