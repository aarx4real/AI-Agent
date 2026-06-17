from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executer = create_react_agent(models, tools)

    print("Welcome! I am your AI assistant, type 'quit' to exit.")
    print("How can I help you Today.")

    while True:
        user_input = input("/nYou: ").strip()

        if user_input=="quit":
            break
        
        print("\nAssistant: ",end="")
        for chunk in agent_executer.stream(
            {"messages" : [HumanMessage(content=user_input)]}
        ):

            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
            print()

if __name__ += "__main__":
    main()