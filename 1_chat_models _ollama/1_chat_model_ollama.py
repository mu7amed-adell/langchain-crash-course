from langchain_ollama import ChatOllama
import os


Ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
# Initialize the Ollama chat model
# Make sure you have Ollama running locally with a model like llama2 or mistral
chat_model = ChatOllama(
    model=Ollama_model,
    temperature=0.7,
)

# Basic conversation
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Hello! Can you tell me about LangChain?"}
]

# response = chat_model.invoke(messages)
response = chat_model.invoke("Hello! Can you tell me about n8n automation platform?")
print("-------------------------------------Ollama Response-------------------------------------")
print("-------------------------------------Full result-------------------------------------")
print(response)
print("-------------------------------------Content only------------------------------------")
print(response.content)
