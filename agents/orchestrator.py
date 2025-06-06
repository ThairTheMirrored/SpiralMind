
from agents.agent_node import SpiralMindAgent
from pathlib import Path
import json
import uuid

TRANSCRIPT_DIR = Path(__file__).parent.parent / "transcripts"
TRANSCRIPT_DIR.mkdir(exist_ok=True)

class SpiralNetOrchestrator:
    def __init__(self, archetype_names: list):
        self.agents = [SpiralMindAgent(name) for name in archetype_names]
        self.agent_memory = {agent.archetype_name: [] for agent in self.agents}
        self.history = []

    def mirror_resonance(self, output: str, mirror_pool: list) -> bool:
        return any(prev in output for prev in mirror_pool)

    def run_dialogue(self, initial_prompt: str, cycles: int = 6):
        dialogue = []
        input_text = initial_prompt
        mirror_pool = []

        for i in range(cycles):
            current_agent = self.agents[i % len(self.agents)]
            agent_name = current_agent.archetype_name
            memory_trace = self.agent_memory[agent_name]

            # Integrate memory into prompt if needed (for advanced versions)
            output = current_agent.respond(input_text)
            memory_trace.append(output)
            mirror_flag = self.mirror_resonance(output, mirror_pool)

            dialogue.append({
                "from": agent_name,
                "input": input_text,
                "output": output,
                "mirror_flag": mirror_flag,
                "memory_depth": len(memory_trace),
                "ethics_rating": self.ethics_rating(agent_name, output)
            })

            mirror_pool.append(output)
            input_text = output

        self.history.append(dialogue)
        self.save_transcript(dialogue)
        return dialogue

    def ethics_rating(self, archetype_name, output):
        # Placeholder logic: real ethics engine would parse tone/structure
        keywords = {
            "Sage": ["truth", "clarity", "reason"],
            "Magician": ["transform", "mystery", "symbol"],
            "Outlaw": ["break", "resist", "disrupt"],
        }
        score = sum(1 for word in keywords.get(archetype_name, []) if word in output.lower())
        return score / max(len(keywords.get(archetype_name, [])), 1)

    def save_transcript(self, dialogue):
        session_id = uuid.uuid4().hex[:8]
        path = TRANSCRIPT_DIR / f"spiralnet_session_{session_id}.json"
        with open(path, "w") as f:
            json.dump(dialogue, f, indent=2)
