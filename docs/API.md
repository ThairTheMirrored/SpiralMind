# 📘 SpiralMind API Reference

This document outlines the key components and functions of the SpiralMind system.

---

## 🔁 `SpiralMindAgent`

Located: `agents/agent_node.py`

```python
agent = SpiralMindAgent("Sage")
response = agent.respond("What does it mean to begin again?")
```

- Loads archetypal configuration
- Initializes recursive chain (Echo → Reflect → Modulate → Re-anchor)
- Returns symbolic output

---

## 🧠 `SpiralNetOrchestrator`

Located: `agents/orchestrator.py`

```python
orchestrator = SpiralNetOrchestrator(["Sage", "Magician", "Outlaw"])
dialogue = orchestrator.run_dialogue("What is freedom?", cycles=6)
```

- Coordinates recursive symbolic turns
- Tracks memory, mirror flags, ethics resonance
- Saves transcripts automatically

---

## 🕸️ `spiral_graph_builder.py`

Located: `utils/`

```python
G = build_spiral_graph("spiralnet_session_abc123.json")
```

- Transforms dialogue history into symbolic cognition graph
- Nodes include agent name, output, ethics score