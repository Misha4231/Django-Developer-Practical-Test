import requests
import json

target_language = "Manx"
content = """
Skills: Basketball, Communications, C++

Projects: Todo app, Habit tracker

Bio: LeBron Raymone James Sr. is an American professional basketball player for the Los Angeles Lakers of the National Basketball Association.

Contacts: E-mail: james@gmail.com Phone: +19823764234
"""

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": f"You are a professional translator. Translate the provided text into {target_language} language preserving meaning and formatting where possible."
            },
            {
                "role": "user",
                "content": content
            }
        ]
    })
)

data = json.loads(response.content)
print(data['choices'][0]['message']['content'])