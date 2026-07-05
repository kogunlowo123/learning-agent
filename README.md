# Learning Agent

[![CI](https://github.com/kogunlowo123/learning-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/learning-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Human Resources | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Learning and development agent that recommends personalized training paths, tracks skill development, manages course enrollments, measures learning effectiveness, and identifies organizational skill gaps.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `recommend_learning_path` | Recommend a personalized learning path based on role and goals |
| `enroll_course` | Enroll an employee in a learning course or program |
| `track_progress` | Track learning progress and completion rates |
| `measure_effectiveness` | Measure learning effectiveness through assessments and behavior change |
| `identify_skill_gaps` | Identify organizational skill gaps by team or department |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/learning/recommend` | Recommend learning path |
| `POST` | `/api/v1/learning/enroll` | Enroll in course |
| `GET` | `/api/v1/learning/progress` | Track progress |
| `POST` | `/api/v1/learning/effectiveness` | Measure effectiveness |
| `GET` | `/api/v1/learning/skill-gaps` | Identify skill gaps |

## Features

- Path Recommendation
- Skill Tracking
- Course Management
- Effectiveness Measurement
- Gap Identification

## Integrations

- Cornerstone
- Linkedin Learning
- Udemy Business
- Coursera Enterprise
- Workday Learning

## Architecture

```
learning-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── learning_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LMS + Skills Database + Learning Content**

---

Built as part of the Enterprise AI Agent Platform.
