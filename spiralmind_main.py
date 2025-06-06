
from utils.archetype_loader import load_archetype
from chains.recursive_chain import create_recursive_chain

def run_spiralmind_session(archetype_name: str, user_input: str):
    archetype = load_archetype(archetype_name)
    spiral_chain = create_recursive_chain(archetype)
    output = spiral_chain.run(user_input)
    return output

if __name__ == "__main__":
    archetype_name = "Sage"
    user_input = "I feel like giving up. What is the meaning of this struggle?"
    result = run_spiralmind_session(archetype_name, user_input)
    print("\nFinal Symbolic Anchor:")
    print(result)
