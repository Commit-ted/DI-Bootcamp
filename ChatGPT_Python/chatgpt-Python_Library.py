
import openai

# Replace with your OpenAI API key
openai.api_key = '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'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4o",  # You can specify the model here
        prompt=prompt,
        max_tokens=150,  # Adjust the response length as needed
        n=1,  # Number of responses to return
        stop=None,
        temperature=0.7  # Control the creativity of the response
    )

    message = response.choices[0].text.strip()
    return message

if __name__ == "__main__":
    user_prompt = "Tell me a joke about programming."
    response = get_chatgpt_response(user_prompt)
    print(response)
