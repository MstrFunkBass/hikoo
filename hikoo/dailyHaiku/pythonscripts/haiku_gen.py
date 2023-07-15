def return_haiku():
    import os
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello Chat, please generate me a haiku."}
    ]
    )

    haiku = completion.choices[0].message.content.split('\n')

    line_1, line_2, line_3 = haiku[0], haiku[1], haiku[2]

    return [line_1, line_2, line_3]

print(return_haiku())