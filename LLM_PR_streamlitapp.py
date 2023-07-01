import os
import pandas as pd
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent
import streamlit as st
import tempfile
from secret_key import openapi_key

os.environ["OPENAI_API_KEY"] = openapi_key

st.title("Excel_made_easy")
st.subheader("Chat auto data query")

uploaded_file = st.file_uploader("Upload your csv document", type=["csv"])
    
if uploaded_file is not None:
    loader = CSVLoader(uploaded_file)
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        file_path = temp_file.name
    csv = file_path


query = st.text_input("Ask anything about your records!")
# Create ask button
ask_button = st.button("Ask")

# Check if the ask button is clicked
if ask_button:
# Perform prediction or any desired action
    st.write("Query in progress...")
    agent = create_csv_agent(OpenAI(temperature=0), csv, verbose=True)
    response = agent.run(query)
    st.write("Done")
    #st.write(response)
    

    styled_container = '''
    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px;">
        <p style="font-size: 20px; color: gray; font-weight: bold;">{}</p>
    </div>
    '''.format(response)

    st.write(styled_container, unsafe_allow_html=True)

      
    #st.write("Prediction complete!")
    #st.write('This should be', images_dict_label2[prediction])