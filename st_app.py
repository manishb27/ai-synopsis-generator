import streamlit as st
import ai.synopsis_gen as syn
import ai.gen_image as gen_image 
from PIL import Image

# importing the logo
logo = Image.open('logo (1).png')

# header and logo together
col1, col2 = st.columns([2,10])
col2.header('The synopsis generator app')
col1.image(logo,  width= 50)

# markdown
st.markdown(
        """
        Introducing an AI-powered synopsis and image creator app that simplifies the process of creating captivating content. 
        
        This app generates summaries and descriptions of any classical book you provide, in a matter of seconds. 
                
        Say goodbye to tedious content creation and let our AI-powered app do the heavy lifting.
        """
        )
# Initialize the book_name variable
book_name = ""


# clear text on refresh
def clear_text():
    st.session_state["text"] = ""

# getting the input
user_input = st.container()
book_name = user_input.text_input(label = "Enter the name of the classical book", 
                                    placeholder = 'Please write the name of the classical book for which you want to synopsis',
                                    value=book_name, key="text")

# submit button
if st.button("Submit"):
    
    with st.spinner("Generating synopsis..."):
        if book_name is not '':
            synopsis = syn.get_synopsis(book_name)
            image_url = gen_image.get_image(book_name)
            syn_container = st.container()
            image_container =  st.container()
            syn_container.markdown(synopsis)
            image_container.image(image_url, use_column_width=True)
        else:
            st.write('Please provide some book name')
        
if st.button('Refresh', on_click=clear_text):
    pass