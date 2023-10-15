import streamlit as st
from googletrans import Translator

translator = Translator()
Indian_Languages = {'Hindi':'hi',
                    'Marathi':'mr',
                    'Gujrati':'gu',
                    'Punjabi':'pa',
                    'Tamil':'ta',
                    'Bengali':'bn'} 

Foreign_Languages = {'Chinese':'zh-cn',
                     'Danish':'da',
                     'English':'en',
                     'French':'fr',
                     'Greek':'el',
                     'Japanese':'ja',
                     'Spanish':'es'}

st.title('Real Time Language Translator')
text = st.text_area('Enter your Text')
lang = st.radio("Select Option", ['Indian_Languages', 'Foreign_Languages'])

if lang == 'Indian_Languages':
    selectlang = st.selectbox('Select Language', list(Indian_Languages.keys()))
    language = Indian_Languages[selectlang]
else:
    selectlang = st.selectbox('Select Language', list(Foreign_Languages.keys()))
    language = Foreign_Languages[selectlang]


if st.button('Click'):
    if text:
        output = translator.translate( text, dest= language ).text
        st.markdown(f'<p style="font-size:40px; color:Green; ">{output}</p>',unsafe_allow_html=True)





