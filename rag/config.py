import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

GRAPHML_PATH = os.path.join(DATA_DIR, "rel19_3gpp_telecom_kg.graphml")
NODES_CSV_PATH = os.path.join(DATA_DIR, "nodes.csv")
EDGES_CSV_PATH = os.path.join(DATA_DIR, "edges.csv")
TEXT_CHUNKS_PATH = os.path.join(DATA_DIR, "rel19_text_chunks.jsonl")

CHATBOT_MODEL = "llama-3.3-70b-versatile"
CHATBOT_TEMPERATURE = 0.7
CHATBOT_MAX_TOKENS = 1024

TOP_K_GRAPH_RESULTS = 80
TOP_K_SECOND_PASS = 10
TOP_K_TEXT_RESULTS = 5

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.groq.com/openai/v1")
