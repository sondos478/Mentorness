Bo2loz: A Conversational AI Powered by Google Generative AI and LangChain
Overview
Bo2loz is a conversational AI application that leverages the power of Google Generative AI and LangChain to provide detailed answers to user questions based on uploaded PDF files. This application is built using Streamlit, a Python library for creating web applications, and utilizes the LangChain framework to integrate with Google Generative AI models.
Features
Upload PDF files and extract text using PyPDF2
Split text into chunks using RecursiveCharacterTextSplitter
Create a vector store using Google Generative AI Embeddings and FAISS
Perform conversational question-answering using ChatGoogleGenerativeAI and LangChain
Getting Started
Installation
To run this application, you'll need to install the required packages:
streamlit
PyPDF2
langchain-google-genai
google.generativeai
You can install these packages using pip:
pip install streamlit PyPDF2 langchain-google-genai google.generativeai

Environment Variables
You'll need to set the GOOGLE_API_KEY environment variable to use the Google Generative AI models. You can do this by creating a .env file with the following content:
GOOGLE_API_KEY=YOUR_API_KEY_HERE

Replace YOUR_API_KEY_HERE with your actual Google API key.
Running the Application
To run the application, simply execute the following command:
streamlit run app.py

This will launch the application in your default web browser.
Usage
Uploading PDF Files
To use the application, simply upload one or more PDF files using the file uploader in the sidebar. Once the files are uploaded, the application will extract the text and create a vector store.
Asking Questions
Once the vector store is created, you can ask questions in the main input field. The application will use the ChatGoogleGenerativeAI model to generate a response based on the uploaded PDF files.
Troubleshooting
If you encounter any issues with the application, please check the following:
Ensure that you have installed all the required packages.
Verify that your Google API key is set correctly in the .env file.
Check the console output for any error messages.
License
This application is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
This application was built using the following resources:
LangChain documentation: https://python.langchain.com/docs/integrations/llms/google_ai/
Google Generative AI Embeddings: https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/
Streamlit documentation: https://docs.streamlit.io/
Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. We welcome any bug fixes, feature enhancements, or documentation improvements.
