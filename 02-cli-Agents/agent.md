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


Piece	                 What it does
---------------------------------------
LLM	                  Decides what action is needed
Tool	                  Performs an actual operation
Tool definition           Tells the LLM what tools are available
Tool registry	          Maps tool names to Python functions
Tool result	          Gives the LLM the result of its action
Agent loop	           Lets the LLM continue deciding until it can answer
