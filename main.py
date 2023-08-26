# from dotenv import load_dotenv
#calling .env for API
# load_dotenv()
from langchain.chat_models import ChatOpenAI
import streamlit as st

chat_model = ChatOpenAI()

st.title('AI Poet')

content = st.text_input('Please provide topic of poet.')
if st.button('Request my poem'):
    with st.spinner('I''m thinking'):
        result = chat_model.predict("Write poem about "+ content)
        st.write(result)





