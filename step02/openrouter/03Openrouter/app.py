import requests

def ask_openrouter(question):
   
    url = "https://openrouter.ai/api/v1/chat/completions"
    
   
    api_key = "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"
    
 
    data = {
        "model": "openai/gpt-3.5-turbo",   # Model to use
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    }
    
   
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    
    if response.status_code == 200:
        answer = response.json()['choices'][0]['message']['content']
        print("AI's answer:", answer)
    else:
        print("Something went wrong:", response.status_code, response.text)


ask_openrouter("Can you tell me a emotional story with emoji?")
