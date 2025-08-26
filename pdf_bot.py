import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import io

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai

from langchain_community.vectorstores import FAISS #for vector embedding
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.chains.question_answering import load_qa_chain #help us to do chat,prompting
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv #to load for the environment variable

load_dotenv()#helps to see environment variable

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# confirming the API key w.r.t 
# google API_KEY in .env file till now


def get_pdf_text(pdf_docs):# take the pdf
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(io.BytesIO(pdf.read()))   #responsible in reading the pdf's
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

# now read the pdf and then read the pages and then text

def get_text_chunks(text): #convert then into chunks
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)  
    #divide the entire text into these particular size of 10000 tokens they can be overlap 1000
    chunks=text_splitter.split_text(text)
    return chunks

#till now Tokenization take place

def get_vector_store(text_chunks): # Convert chunks into vectors
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")    #inside model folder in library embedding present
    vector_store=FAISS.from_texts(text_chunks,embedding=embeddings)     
    #takes all these text chunks and embed acording tom our embedding initialized 
    vector_store.save_local("faiss_index")  
    #save all the embedding in local, file named as faiss_index where data is stored as vector(which is not readable)

def get_conversational_chain():
    prompt_template="""
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in 
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n{context}?\n
    Question:\n{question}\n
    Answer:
"""
                        #information used in prompt template 
    model=ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.3) #Load gemini-1.5-flash model
    
    prompt=PromptTemplate(template=prompt_template, input_variables=["context","question"]) #Create a template
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt) #for getting the chain
    return chain


def user_input(user_questions):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001") #loading embedding

    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)  # importing faiss_index from the local, 
                                                          # already pdf are converted into faiss in form of vector
    docs = new_db.similarity_search(user_questions)         #similarty search based of user question 

    chain = get_conversational_chain()

    response = chain(
        {"input_documents":docs,"question":user_questions}
        ,return_only_outputs=True
    )

    print(response)
    st.write("Reply: ", response["output_text"])



def main():
    st.set_page_config("Chat with PDF's")
    st.header("Hey, What do you want me to answer from your PDF")

    user_question = st.text_input("Type Question below")

    if user_question:
        user_input(user_question)
    
    with st.sidebar: # Where pdf upload and convert into vector
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files",accept_multiple_files=True,type=["pdf"])
        if st.button("Submit"):
            with st.spinner("Processing..."):
                raw_text=get_pdf_text(pdf_docs)
                text_chunks=get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")


if __name__ == "__main__":
    main()