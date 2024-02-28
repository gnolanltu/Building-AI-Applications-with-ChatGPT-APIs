from openai import OpenAI

client = OpenAI(api_key="<insert your key>")

question = input("What would you Like to ask OpenAI? ")

# Call the openai ChatCompletion endpoint, with th ChatGPT model
response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
      {"role": "user", "content": question}
  ])

# Extract the response
print(response.choices[0].message.content)
