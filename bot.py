'''
- [x] parse command
- [x] create a venv 
- [ ] send command to gpt
    - [ ] write the prompt in a way so that the response is expeced. like "Write your response in the following format: Filename: T"
- [ ] create  
'''
import requests
import json

def parse():
    #parse the the content from commands.txt 
    with open("Test.txt", "r") as f:
        content = f.read()
    return content

def request():
    #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
    #send request to gpt
    command = parse()
    OPENAI_API_KEY = "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"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + OPENAI_API_KEY # Replace OPENAI_API_KEY with your actual API key
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": command}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()


if __name__ == "__main__":
    #parse()
    request()