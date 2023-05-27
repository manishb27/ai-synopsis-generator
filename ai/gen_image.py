import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_image(prompt):
    """Get the image from the prompt."""
    response = openai.Image.create(prompt=prompt, n=1, size="256x256")
    image_url = response["data"][0]["url"]
    return image_url

if __name__ == '__main__':
    prompt_gen = input('Please pass in the prompt for image generation: ')
    image_url = get_image(prompt_gen)
    print(image_url)