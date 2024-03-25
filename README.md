# Mentorness
repo for NLP projects
This project is a Streamlit-based application that allows users to ask questions related to the content of uploaded PDF files. It utilizes the LangChain framework, which provides various components for building language-based applications, such as text splitters, language models, and vector stores.
The key features of this project are:
PDF File Uploading: Users can upload one or more PDF files through the Streamlit file uploader widget.
Text Extraction and Chunking: The application extracts the text from the uploaded PDF files and splits it into smaller chunks using the RecursiveCharacterTextSplitter from LangChain.
Vector Store Creation: The text chunks are then used to create a vector store using the FAISS library, which allows for efficient similarity search.
Question Answering: Users can enter a question in the text input field, and the application will use the vector store and a language model (in this case, the ChatGoogleGenerativeAI model) to provide a detailed answer based on the context of the uploaded PDF files.
Customization: The application allows users to customize the prompt template used for the question-answering process, as well as the language model used for generating the responses.
Persistence: The created vector store is saved locally, allowing users to reuse the processed PDF files without having to upload them again.
This project demonstrates the integration of various natural language processing (NLP) techniques and tools, such as text extraction, text chunking, vector store creation, and language model-based question answering. It can be a useful starting point for building more advanced NLP-based applications or for exploring the capabilities of the LangChain framework.