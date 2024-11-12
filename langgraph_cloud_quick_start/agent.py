from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

model = ChatOpenAI(model="gpt-4")

tools = [TavilySearchResults(max_results=2)]

# compiled graph
graph = create_react_agent(model, tools)

# TODO: LangGraph Cloudが有料なので、ここから先は試してない
