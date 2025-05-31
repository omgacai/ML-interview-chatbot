import os
import yaml
from dotenv import load_dotenv

load_dotenv()

with open(os.path.join(os.path.dirname(__file__), "..", "config.yaml")) as f:
    config = yaml.safe_load(f)

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
EMBEDDING_DEPLOYMENT = config["AZURE_EMBEDDING_OPENAI_CHAT_DEPLOYMENT_NAME"]
CHAT_DEPLOYMENT = config["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"]
TOP_K = config["top_k"]
CORPUS_PATH = config["corpus_path"]
