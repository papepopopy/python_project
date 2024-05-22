import openai as oi

oi.api_key = "sk-proj-iTQctJvnxIETFsmbxWbRT3BlbkFJiqlmixKGjW1vBEgNdVab"

def create_completion(messages):
    try:
        return oi.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except oi.OpenAIError as e:
        print("GPT ERROR: ", str(e))
        return None

    