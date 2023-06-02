import os

from langchain.chains import OpenAPIEndpointChain
from langchain.llms import OpenAI
from langchain.requests import Requests
from langchain.tools import APIOperation, OpenAPISpec


url = "https://fastapilangchain-1-w0858112.deta.app/openapi.json"

spec = OpenAPISpec.from_url(url=url)

operation = APIOperation.from_openapi_spec(spec, "/todos", "get")

llm = OpenAI()

chain = OpenAPIEndpointChain.from_api_operation(
    operation,
    llm,
    requests=Requests(),
    verbose=True,
    return_intermediate_steps=True,
)

output = chain("How many todos do I have?")
print(output)