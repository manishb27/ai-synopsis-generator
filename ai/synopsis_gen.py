import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

def get_synopsis(book):

    response = openai.Completion.create(
                model="text-davinci-002",
                prompt=f"Generate the long summary of around 1000 words for the following book: \n\nBook: {book}\n\nSynopsis:\n\n",
                temperature=0.65,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )

    generated_text = response.choices[0].text.strip()

    return generated_text



if __name__ == '__main__':
    book_name = input('Please tell me the classical book name:  ')
    synopsis = get_synopsis(book_name)

    print('\n\n' + synopsis)

