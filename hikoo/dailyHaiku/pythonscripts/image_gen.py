import environ
import os
import openai
import urllib.request

env = environ.Env()

environ.Env.read_env()

def generate_image(haiku_prompt):

    image_prompt = f'generate a painterly image with a slight green hue, based on the following haiku: {haiku_prompt}'

    openai.api_key = env("OPENAI_API_KEY")

    response = openai.Image.create(
        prompt=image_prompt,
        n=1,
        size="1024x1024",
    )

    return response["data"][0]["url"]