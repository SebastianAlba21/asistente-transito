# ====== Importar librerías ======
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
import os

# ====== Cargar documento ======
def cargar_documento(archivo):
    print("📄 Procesando documento...")
    loader = TextLoader(archivo, encoding='utf-8')  # Especificamos la codificación utf-8
    documents = loader.load()
    print(f"✅ Se cargaron {len(documents)} fragmentos.")
    return documents

# ====== Generar vectores ======
def generar_vectores(documents):
    print("🔍 Generando vectores...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    vectorstore = FAISS.from_documents(documents, embeddings)
    print("✅ Vectores generados.")
    return vectorstore

# ====== Cargar modelo Mistral ======
def cargar_modelo():
    print("🧠 Cargando modelo Mistral...")
    # Cargar el pipeline de generación con Mistral
    pipe = pipeline(model="mistralai/Mistral-7B-Instruct-v0.2", task="text-generation")
    llm = HuggingFacePipeline(pipeline=pipe)
    print("✅ Modelo Mistral cargado.")
    return llm

# ====== Consultar el modelo ======
def consultar_modelo(llm, vectorstore, pregunta):
    print(f"🔍 Realizando consulta: {pregunta}")
    # Crear la cadena de preguntas y respuestas
    qa_chain = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    # Obtener la respuesta
    respuesta = qa_chain.run(pregunta)
    print(f"✅ Respuesta: {respuesta}")
    return respuesta

# ====== Función principal ======
def main():
    # Ruta del archivo de texto
    archivo = "codigo_transito.txt"
    
    # Cargar el documento
    documents = cargar_documento(archivo)
    
    # Generar vectores
    vectorstore = generar_vectores(documents)
    
    # Cargar el modelo Mistral
    llm = cargar_modelo()
    
    # Realizar una consulta
    pregunta = "¿Cuáles son las normas para el exceso de velocidad?"
    respuesta = consultar_modelo(llm, vectorstore, pregunta)
    
    # Mostrar la respuesta
    print(f"Respuesta a la pregunta '{pregunta}': {respuesta}")

# ====== Ejecutar el script ======
if __name__ == "__main__":
    main()
