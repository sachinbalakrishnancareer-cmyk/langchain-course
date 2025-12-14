from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI 
from langchain_tavily import TavilySearch


tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")

# Returns a runnable (chain) we saw in the initial lessons
agent = create_react_agent(
    llm=llm,
    tools=tools, 
    prompt=react_prompt
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Flow : 
# 1. create_react_agent retuns a ruunable chain taking in the input prompt, tools and send it to LLM
# 2. LLM returns a response and the agent_executor runs the tool or another llm prompt to orchestrate the whole process

chain = agent_executor

def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
        }
    )
    print(result)


if __name__ == "__main__":
    main()
