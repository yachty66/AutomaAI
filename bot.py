import requests
import re
import json
import subprocess
import config

def parse():
    with open("Test.txt", "r") as f:
        content = f.read()
    return content

def request():
    command = parse()
    OPENAI_API_KEY = config.OPENAI_API_KEY
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + OPENAI_API_KEY
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": command}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

response = request()
print(response)

def filename(): 
    content = response['choices'][0]['message']['content']
    filename = content.split('\n\n')[1].split(':')[1].strip()
    with open(filename, "w") as f:
        f.write("")
    return filename
 
def script():
    content = response['choices'][0]['message']['content']
    pattern = r'Script code:(.*?)Run:'
    script_code = re.search(pattern, content, re.DOTALL).group(1).strip()
    with open(filename(), "w") as f:
        f.write(script_code)
    return script_code

def run():
    content = response['choices'][0]['message']['content']
    output = content.split('Run:')[1].strip()
    result = subprocess.run(['python', output], capture_output=True, text=True)
    if result.returncode == 0:
        print('Script executed successfully.')
        print('Output:', result.stdout)
    else:
        print('Error:', result.stderr)
    pass

if __name__ == "__main__":
    filename()
    script()
    run()