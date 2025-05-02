# ====== Imports ======
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import gradio as gr
import torch

# ====== 1. Cargar y dividir el texto ======
def load_and_split_text(file_path, chunk_size=1000, chunk_overlap=100):
    loader = TextLoader(file_path, encoding="utf-8")
    docs = loader.load()
    splitter = CharacterTextSplitter(separator=" ", chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)

# ====== 2. Crear base vectorial con embeddings ======
def create_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

# ====== 3. Cargar modelo generativo (instruct) ======
def load_llm():
    model_id = "mistralai/Mistral-7B-Instruct-v0.1"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

    instruct_pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.7,
        top_p=0.9,
        do_sample=True
    )

    return HuggingFacePipeline(pipeline=instruct_pipe)

# ====== 4. Crear QA chain con LangChain ======
def create_qa_chain(vectorstore, llm):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False)
    return chain

# ====== 5. App con Gradio ======
def main():
    print("📄 Procesando documento...")
    docs = load_and_split_text("codigo_transito.txt")
    print(f"✅ Se cargaron {len(docs)} fragmentos.")

    print("🔍 Generando vectores...")
    vectorstore = create_vectorstore(docs)

    print("🧠 Cargando modelo LLM...")
    llm = load_llm()

    print("🤖 Creando cadena de preguntas y respuestas...")
    qa_chain = create_qa_chain(vectorstore, llm)

    def answer_fn(question):
        if question.strip() == "":
            return "Por favor, ingresa una pregunta válida."
        result = qa_chain.run(question)
        return result

    print("🚀 Lanzando interfaz...")
    gr.Interface(
        fn=answer_fn,
        inputs=gr.Textbox(lines=2, placeholder="Pregunta sobre el Código de Tránsito"),
        outputs="text",
        title="🛣️ Código de Tránsito Colombiano",
        description="Pregunta lo que quieras sobre el Código de Tránsito. El modelo buscará en el texto y generará una respuesta completa."
    ).launch(server_name="0.0.0.0", server_port=7860)

# ====== 6. Ejecutar ======
if __name__ == "__main__":
    main()
