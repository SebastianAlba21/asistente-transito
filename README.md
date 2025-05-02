# 🛣️ **Sistema de Pregunta-Respuesta sobre el Código Nacional de Tránsito de Colombia**

Este proyecto tiene como objetivo proporcionar un sistema de **Pregunta-Respuesta (Q&A)** sobre el **Código Nacional de Tránsito de Colombia**. Utilizando técnicas de **embeddings** y **modelos de lenguaje**, el sistema responde de manera precisa a consultas relacionadas con el código, extrayendo la información relevante de un documento de texto cargado previamente.

## 🧑‍💻 **Tecnologías utilizadas**

- **Sentence-Transformers**: Para crear embeddings de los fragmentos del texto, permitiendo una búsqueda rápida y precisa.
- **Transformers** (Hugging Face): Usado para el modelo de pregunta-respuesta basado en RoBERTa, afinado con el dataset SQuAD.
- **Scikit-learn**: Para la construcción de un índice rápido para la búsqueda de fragmentos relevantes usando k-NN (k-Nearest Neighbors).
- **Gradio**: Para la creación de una interfaz interactiva que permite al usuario realizar preguntas al sistema y recibir respuestas.

## 📂 **Estructura del Proyecto**

