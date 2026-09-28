                    AGENT
        ┌─────────────────────────┐
        │                         │
        │          LLM            │
        │     "What should I do?" │
        │            │            │
        │            ▼            │
        │       Tool selection    │
        │            │            │
        │     ┌──────┼──────┐     │
        │     ▼      ▼      ▼     │
        │ Calculator RAG  Kubernetes
        │     │      │      │     │
        │     └──────┼──────┘     │
        │            ▼            │
        │       Tool result       │
        │            │            │
        │            └──→ LLM     │
        │                         │
        │       LOOP              │
        └─────────────────────────┘

Tool = what the agent can do.
LLM = what decides what to do.
Agent = the system that repeatedly decides and acts.
Agent = LLM + Tools + Loop
