import streamlit as st


AZURE_OPENAI_API_KEY = st.secrets["AZURE_OPENAI_API_KEY"]
AZURE_OPENAI_ENDPOINT = st.secrets["AZURE_OPENAI_ENDPOINT"]
EMBEDDING_DEPLOYMENT = st.secrets["EMBEDDING_DEPLOYMENT"]
CHAT_DEPLOYMENT = st.secrets["CHAT_DEPLOYMENT"]
CORPUS_PATH = st.secrets["CORPUS_PATH"]
TOP_K = st.secrets["TOP_K"]


'''
load_dotenv()

with open(os.path.join(os.path.dirname(__file__), "..", "config.yaml")) as f:
    config = yaml.safe_load(f)


AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
EMBEDDING_DEPLOYMENT = config["AZURE_EMBEDDING_OPENAI_CHAT_DEPLOYMENT_NAME"]
CHAT_DEPLOYMENT = config["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"]
TOP_K = config["top_k"]
CORPUS_PATH = config["corpus_path"]
'''