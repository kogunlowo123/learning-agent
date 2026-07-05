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

![7-Layer Architecture](docs/diagrams/architecture-7-layer.png)

*Where RAG sits in the stack — the 7-layer enterprise AI agent architecture.*


```
learning-agent/
│
├── modules/                              # Per-cloud building blocks
│   ├── contracts/                        # Cloud-agnostic interface contracts
│   │   ├── network.md                    # VPC/VNet with private subnets
│   │   ├── vectorstore.md                # Vector search, BM25, hybrid, metadata filter
│   │   ├── object-store.md               # Encrypted object storage
│   │   └── inference-gateway.md          # LLM chat, embeddings, reranking
│   ├── netops/                           # Network boundary (VPC, subnets, SGs)
│   ├── secops/                           # Keys, identity, guardrails
│   ├── appops/                           # Data and model plane
│   └── devops/                           # State backend and CI/CD
│
├── blueprints/                           # RAG topologies that compose modules
│   ├── rag-naive/                        # Keyword-only (pilot)
│   ├── rag-hybrid/                       # Keyword + vector + reranker (production)
│   ├── rag-graph/                        # Entity-relationship graph retrieval
│   ├── rag-multimodal/                   # Text + image + table retrieval
│   └── rag-agentic/                      # RAG as a tool in multi-agent system
│
├── live/                                 # Real environments, pinned versions
│   ├── _bootstrap/aws/                   # One-time state bucket creation
│   ├── dev/us/rag-hybrid/                # Development
│   ├── staging/                          # Pre-production
│   └── prod/                             # Production
│
├── factory/                              # Stamping machinery
│   ├── scaffold.sh                       # Stamps a blueprint into live/
│   └── catalog.yaml                      # Registry of available patterns
│
├── platform/                             # Agentic RAG reference implementation
│   └── reference-apps/reference-agentic-rag/
│       ├── app/contracts/                # DataLane enum, models, tenancy
│       ├── app/search/                   # FULL search pipeline
│       │   ├── retrievers/               # bm25, dense, hybrid, graph, parent_doc
│       │   ├── reranking/                # cross_encoder, llm_rerank, boost, cascade
│       │   ├── query/                    # classify, rewrite, expand, hyde, decompose
│       │   ├── multi_hop/                # budget, planner, executor, synthesizer
│       │   ├── corrective/               # self_critique, web_fallback
│       │   ├── adaptive/router.py        # Public facade for all search
│       │   └── cache/                    # exact, semantic, redis backend
│       └── data/raw_examples/            # Sample data (indexed, live, structured lanes)
│
├── src/                                  # FastAPI backend (7-layer architecture)
│   ├── gateway/                          # Layer 2: AI Gateway (control plane)
│   │   ├── middleware.py                 # Auth, rate limiting, request routing
│   │   ├── guardrails.py                 # Prompt injection, content safety
│   │   ├── pii_redactor.py               # PII detection and redaction
│   │   ├── token_budget.py               # Per-user/org token limits
│   │   └── audit_trail.py                # Immutable request/response log
│   ├── agent/                            # Layer 3: Agent orchestration
│   │   ├── learning_agent_agent.py     # Main agent implementation
│   │   ├── tools.py                      # 5 domain-specific tools
│   │   ├── prompts.py                    # Expert system prompts
│   │   └── orchestrator/                # Plan → Research → Execute → Validate → Respond
│   │       ├── planner.py               # Task decomposition and routing
│   │       ├── researcher.py            # RAG retrieval and knowledge gathering
│   │       ├── executor.py              # Tool execution with retry
│   │       ├── validator.py             # Output verification
│   │       └── guard.py                 # RBAC and destructive action gating
│   ├── tools/                            # Layer 4: Tool integrations
│   │   └── registry.py                  # Domain tool dispatch with permissions
│   ├── data/                             # Company data integration
│   │   └── lanes.py                     # INDEXED / LIVE / STRUCTURED routing
│   ├── memory/                           # Layer 6: Persistent state
│   │   ├── short_term.py                # Redis session context
│   │   ├── long_term.py                 # Vector DB embeddings
│   │   ├── lexical.py                   # PostgreSQL BM25 index
│   │   ├── knowledge_graph.py           # Entity-relationship graph
│   │   ├── decisions.py                 # Durable decision log
│   │   └── manager.py                   # Unified memory interface
│   ├── llm/                              # Layer 7: Multi-model router
│   │   ├── router.py                    # GPT/Claude/Gemini routing + fallbacks
│   │   └── providers/                   # OpenAI, Anthropic, Google providers
│   ├── api/                              # FastAPI routes and middleware
│   ├── rag/                              # RAG pipeline
│   ├── mcp/                              # MCP server (tool exposure)
│   ├── a2a/                              # Agent-to-agent protocol
│   ├── auth/                             # JWT + RBAC + API key auth
│   ├── config/                           # Application settings
│   ├── connectors/                       # Data source connectors
│   └── models/                           # Pydantic schemas
│
├── configs/                              # Environment configurations
│   ├── dev.yaml                          # Local development
│   ├── staging.yaml                      # Pre-production
│   └── prod.yaml                         # Production
│
├── infrastructure/                       # Deployment configurations
│   └── docker/                           # Multi-stage Dockerfiles
│
├── policy/                               # Policy as code
│   ├── opa/                              # Open Policy Agent rules
│   └── checkov/                          # Infrastructure security scanning
│
├── tests/                                # Unit, integration, E2E
├── docs/                                 # Architecture, security, deployment, operations
├── .github/workflows/                    # CI/CD pipelines
├── docker-compose.yml                    # Local development stack
├── pyproject.toml                        # Python dependencies
├── Makefile                              # Developer workflow commands
└── openapi.yaml                          # API specification
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
