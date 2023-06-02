from langchain.llms import OpenAI
from langchain.requests import RequestsWrapper
from langchain.agents.agent_toolkits.openapi import planner
from langchain.agents.agent_toolkits.openapi.spec import reduce_openapi_spec
import requests

url = "https://fastapilangchain-1-w0858112.deta.app/openapi.json"
response = requests.get(url)
data = response.json()

openai_api_spec = reduce_openapi_spec(data)

llm = OpenAI()

requests_wrapper = RequestsWrapper()

agent = planner.create_openapi_agent(openai_api_spec, requests_wrapper, llm)
agent.run("I want to add a new todo, buying groceries")