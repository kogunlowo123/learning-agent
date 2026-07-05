"""Test configuration for Learning Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "learning-agent", "category": "Human Resources"}
