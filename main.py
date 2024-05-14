from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI(model="gpt-3.5-turbo")

text = "What is a creative name for a mythology based escape room?"
system_text = "You are a sarcastic bot"

messages = [
  SystemMessage(content=system_text),
  HumanMessage(content=text),
]

response_llm = llm.invoke(messages)
print(response_llm)
print(type(response_llm))
print("****")

response_chat = chat_model.invoke(messages)
print(response_chat)
print(type(response_chat))
