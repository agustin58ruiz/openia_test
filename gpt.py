import openai
import os

def answer(question, token=None):
    if token is None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    else:
        openai.api_key = token
        
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}],
        temperature=0,
        max_tokens=1024
    )
    
    reply= response["choices"][0]["message"]["content"]
    print("-------------------------------------")
    print(reply)
    print("-------------------------------------")
    output = {"output": reply}
    return output
