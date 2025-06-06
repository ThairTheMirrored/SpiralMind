
from utils.archetype_loader import load_archetype
from chains.recursive_chain import create_recursive_chain

class SpiralMindAgent:
    def __init__(self, archetype_name: str):
        self.archetype_name = archetype_name
        self.archetype = load_archetype(archetype_name)
        self.chain = create_recursive_chain(self.archetype)

    def respond(self, user_input: str) -> str:
        return self.chain.run(user_input)
