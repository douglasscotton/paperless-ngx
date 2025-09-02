from flask import Flask, request, jsonify
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os

app = Flask(__name__)

# Carrega embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Cria ou carrega índice FAISS
index_path = "/app/data/vector_index"
if os.path.exists(index_path):
    db = FAISS.load_local(index_path, embeddings)
else:
    os.makedirs(index_path, exist_ok=True)
    db = FAISS.from_texts(["Paperless RAG iniciado."], embeddings)
    db.save_local(index_path)

llm = Ollama(model="llama2", base_url="http://ollama:11434")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    answer = qa.run(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
