pip install -q -U google-generativeai

pip install streamlit

import streamlit as st

st.title ("Welcome to AI Assistant")

!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# 
# x = st.slider('Select a value')
# st.write(x, 'squared is', x * x)

!npm install localtunnel

!streamlit run /content/app.py &>/content/logs.txt &



import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
from google.colab import userdata

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
Google_API_KEY=userdata.get('Google_API_KEY')

genai.configure(api_key=Google_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# response = model.generate_content("What do you think of Indian Weavers ?")

to_markdown(response.text)

response = model.generate_content("What do you think of India ?")
to_markdown(response.text)
