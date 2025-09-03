import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

model = ChatOllama(
    model=ollama_model,
    temperature=0.5,
    verbose=True,
    # reasoning=True,
)

messages = [
   SystemMessage(content="Give a breif summary of the following topics"),
   HumanMessage(content="n8n automation platform"),
   AIMessage(content="n8n is a free and open-source workflow automation platform that allows you to create workflows that can be used to automate tasks and processes."),
   HumanMessage(content="how does LSTM work in deep learning?"),
]

Response = model.invoke(messages)
print(Response.content)