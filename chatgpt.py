import openai

# set your API key
openai.api_key = "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"

# set the temperature parameter
temperature = 0.7

# set the prompt
prompt = "What is the capital of France? "

# make the API call
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=temperature,
)

# print the response
print(response["choices"][0]["text"])
