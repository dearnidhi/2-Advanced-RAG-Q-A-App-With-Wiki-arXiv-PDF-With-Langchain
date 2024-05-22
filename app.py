import streamlit as st
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Wikipedia API Wrapper
wikipedia_api = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_query = WikipediaQueryRun(api_wrapper=wikipedia_api)

# Web Base Loader
web_loader = WebBaseLoader("https://docs.smith.langchain.com/")
documents = web_loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
document_chunks = text_splitter.split_documents(documents)

# FAISS vector store with OpenAI Embeddings
vector_store = FAISS.from_documents(document_chunks, OpenAIEmbeddings(openai_api_key=openai_api_key))
retriever = vector_store.as_retriever()

# Retriever Tool
retriever_tool = create_retriever_tool(retriever, "langsmith_search", "Search LangSmith documentation")

# Arxiv API Wrapper
arxiv_api = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv_query = ArxivQueryRun(api_wrapper=arxiv_api)

# Create OpenAI language model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Pull prompt from Hub
prompt = hub.pull("hwchase17/openai-functions-agent")

# Create OpenAI tools agent
agent = create_openai_tools_agent(llm, [wiki_query, arxiv_query, retriever_tool], prompt)

# Create agent executor
agent_executor = AgentExecutor(agent=agent, tools=[wiki_query, arxiv_query, retriever_tool], verbose=True)

# Streamlit UI
st.set_page_config(page_title="LangChain Knowledge Center", layout="wide")

st.title("LangChain Knowledge Center")

st.markdown("""
    <style>
    .st-sidebar .sidebar-content {
        background-color: #f5f5f5;
        padding: 20px;
        border-right: 1px solid #e8e8e8;
    }
    .st-sidebar .sidebar-content h1 {
        font-size: 24px;
        margin-bottom: 10px;
    }
    .st-sidebar .sidebar-content p {
        font-size: 16px;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<h1>About LangChain</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p>LangChain is a powerful tool for building AI-powered applications.</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p>This demo showcases how LangChain can be used to create a knowledge center.</p>", unsafe_allow_html=True)

query_input = st.text_input("Ask a question:", "Type Here...")

if st.button("Submit"):
    if query_input:
        response = agent_executor.invoke({"input": query_input})
        st.success("Response:")
        st.write(response)
    else:
        st.warning("Please enter a question.")

st.markdown("", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><i>Powered by LangChain</i></p>", unsafe_allow_html=True)