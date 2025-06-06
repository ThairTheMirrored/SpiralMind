
from agents.spiral_bridge import SpiralBridge

if __name__ == "__main__":
    print("🌀 SpiralNet: Sage × Magician — Symbolic Dialogue")
    print("Topic: 'What is freedom — a void or a vessel?'
")

    bridge = SpiralBridge("Sage", "Magician")
    turns = bridge.dialogue_turn("What is freedom — a void or a vessel?", turns=4)

    for speaker, user_input, output in turns:
        if user_input:
            print(f">>> {speaker} receives input: {user_input}")
        print(f"{speaker} responds:
{output}
{'-' * 60}")
