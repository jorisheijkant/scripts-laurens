from ollama import chat
from ollama import ChatResponse

prompt = """
Je krijgt een tweet te zien, laat weten of er in deze tweet sprake is van haat of niet.
De tweet is in het Nederlands. Je kijkt specifiek naar misogyne termen (vrouwenhaat) en homohaat. 
Geef een Boolean terug, dus False of True. Geef alleen de boolean terug.
"""

test_tweet = "Teringwijf"

messages = [
    {
        "role": "system",
        "content": prompt
    },
    {
        "role": "user",
        "content": test_tweet
    }
]

response: ChatResponse = chat(model='llama3.1', messages=messages)

try:
    ollama_response = response['message']['content']
    print(f"Does tweet '{test_tweet}' have hate? {ollama_response}")
except Exception as e:
    print(f"Failing to parse Ollama answer: {e}")