import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# logo = Image.open('logo.png')
st.set_page_config(layout = 'wide')
# st.image(logo, width=100)



## write elements
# st.header('this is a header')
# st.subheader('some subheader')
# st.text('''Some text as it is
# this is the next line of text''')
# st.markdown('''# This is a markdown cell
# - we can do this
# - and we can do this as well
# ''')
# st.caption('This is a nice caption')



# st.divider()
# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language='python')
            
# data show elements
# df = pd.DataFrame({'col1': [1,2,3]})
# st.write(df)
# st.write('some text')

# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")


# st.json({
#     'foo': 'bar',
#     'baz': 'boz',
#     'stuff': [
#         'stuff 1',
#         'stuff 2',
#         'stuff 3',
#         'stuff 5',
#     ],
# })


# Selectors:
# Radio button
# genre = st.radio(
#     "What\'s your favorite movie genre",
#     ('Comedy', 'Drama', 'Documentary'))

# if genre == 'Comedy':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn\'t select comedy.")

# # SelectBox
# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# # slider
# st.slider(label= 'some slider',min_value= 0, max_value= 100)


# # Charts
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.area_chart(chart_data)
# st.line_chart(chart_data)


# # audio image
# logo = Image.open('logo.png')
# st.image(logo, width= 100)

# def display_image(image_url):
#     st.image(image_url, use_column_width=True)

# image_url = ('https://oaidalleapiprodscus.blob.core.windows.net/private/org-ZbTizCWiojJBpiXxrIMnD778/user-64EqIKa1oZDYeqH5whJqjgR2/img-ftRvny6P2ZsRLuN6Oa9I5IAw.png?st=2023-05-26T10%3A17%3A28Z&se=2023-05-26T12%3A17%3A28Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-05-26T11%3A10%3A39Z&ske=2023-05-27T11%3A10%3A39Z&sks=b&skv=2021-08-06&sig=LLTKJAGdLa/PJB8K5xBubI4K%2ByWPfstXt45Hfj1fY2o%3D')
# display_image(image_url)

# # running and displaying code
# def get_user_name():
#     return 'John'

# with st.echo():
#     # Everything inside this block will be both printed to the screen
#     # and executed.

#     def get_punctuation():
#         return '!!!'

#     greeting = "Hi there, "
#     value = get_user_name()
#     punctuation = get_punctuation()

#     st.write(greeting, value, punctuation)


# # Using object notation
# main_text = st.container()
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     shipping = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

#     if shipping == 'Standard (5-15 days)':
#         main_text.write('standard')
#     else:
#         main_text.write('Express')

## Expander
# st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

# with st.expander("See explanation"):
#     st.write("""
#         The chart above shows some numbers I picked for you.
#         I rolled actual dice for these, so they're *guaranteed* to
#         be random.
#         """)
#     st.image(logo, width= 400)
#     st.slider(label='Some slider', min_value=0, max_value=200)



# import streamlit as st

# def clear_form():
#     st.session_state["foo"] = ""
#     st.session_state["bar"] = ""
    
# with st.form("myform"):
#     f1, f2 = st.columns([1, 1])
#     with f1:
#         st.text_input("Foo", key="foo")
#     with f2:
#         st.text_input("Bar", key="bar")
#     f3, f4 = st.columns([1, 1])
#     with f3:
#         submit = st.form_submit_button(label="Submit")
#     with f4:
#         clear = st.form_submit_button(label="Clear", on_click=clear_form)

# if submit:
#     st.write('Submitted')

# if clear:
#     st.write('Cleared')

import streamlit as st

def clear_text():
    st.session_state["text"] = ""

input = st.text_input("text", key="text")    
st.button("clear text input", on_click=clear_text)
st.write(input)