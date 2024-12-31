import openai

def get_gpt_response(user_message):
    openai.api_key = "YOUR_OPENAI_API_KEY"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
