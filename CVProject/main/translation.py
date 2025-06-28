import json
import requests
import os
from django.core.cache import cache

from .models import CV

def translate_content(content: str, target_language: str):
    # request openrouter to translate given content
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_AI_KEY')}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "openai/gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": f"You are a professional translator. Translate the provided text into {target_language} language preserving meaning and formatting where possible. IMPORTANT: avoid any other lines line ```html ```. ONly give html code"
                },
                {
                    "role": "user",
                    "content": content
                }
            ]
        })
    )

    data = json.loads(response.content)
    return data['choices'][0]['message']['content']

def clean_fenced_code_blocks(text: str):
    if text.startswith("```html"):
        text = text[len("```html"):].lstrip()
    if text.endswith("```"):
        text = text[:-3].rstrip()
    return text

def build_cv_html(cv: CV):
    return f"""
        <div class="list-group-item">
            <p class="mb-1"><strong>Skills:</strong> {cv.skills}</p>
            <p class="mb-1"><strong>Projects:</strong> {cv.projects}</p>
            <p class="mb-1"><strong>Bio:</strong> {cv.bio}</p>
            <p class="mb-1"><strong>Contacts:</strong> {cv.contacts}</p>
        </div>
    """

def handle_translation(cv: CV, language: str):
    if not language:
        return None
    
    # Redis caching to save api tokens
    cache_key = f"cv_translation_{cv.pk}_{language}"
    translated = cache.get(cache_key)

    if translated is None:
        content_to_translate = build_cv_html(cv)
        translated = clean_fenced_code_blocks(translate_content(content_to_translate, language))

        # Cache for 24 hours
        cache.set(cache_key, translated, timeout=60*60*24)

    return translated