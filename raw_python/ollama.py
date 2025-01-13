import ollama 

prompt = """
Je krijgt een tweet te zien, laat weten of er in deze tweet sprake is van haat of niet.
De tweet is in het Nederlands. Je kijkt specifiek naar misoygne termen en homohaat. 
Geef een Boolean terug, dus False of True. Geef alleen de boolean terug.
"""

test_tweet = "Ik hoop dat die vadsige teringhond eens van tv verdwijnt."

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

response = ollama.chat(model='llama3.2', messages=messages)

try:
    ollama_response = response['message']['content']
    print(ollama_response)
except Exception as e:
    print(f"Failing to parse Ollama answer: {e}")