
from agents.agent_node import SpiralMindAgent

class SpiralBridge:
    def __init__(self, agent_a_name: str, agent_b_name: str):
        self.agent_a = SpiralMindAgent(agent_a_name)
        self.agent_b = SpiralMindAgent(agent_b_name)
        self.history = []

    def spiral_dialogue(self, initial_prompt: str, cycles: int = 3):
        dialogue = []
        input_text = initial_prompt

        for i in range(cycles):
            speaker = self.agent_a if i % 2 == 0 else self.agent_b
            listener = self.agent_b if i % 2 == 0 else self.agent_a

            output = speaker.respond(input_text)
            dialogue.append({
                "from": speaker.archetype_name,
                "to": listener.archetype_name,
                "input": input_text,
                "output": output
            })

            # The output becomes the symbolic anchor passed to the next agent
            input_text = output

        self.history.append(dialogue)
        return dialogue
