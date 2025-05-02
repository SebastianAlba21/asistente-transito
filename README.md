# 🛣️ **Sistema de Pregunta-Respuesta sobre el Código Nacional de Tránsito de Colombia**

Este proyecto tiene como objetivo proporcionar un sistema de **Pregunta-Respuesta (Q&A)** sobre el **Código Nacional de Tránsito de Colombia**. Utilizando técnicas de **embeddings** y **modelos de lenguaje**, el sistema responde de manera precisa a consultas relacionadas con el código, extrayendo la información relevante de un documento de texto cargado previamente.

## 🧑‍💻 **Tecnologías utilizadas**

- **Sentence-Transformers**: Para crear embeddings de los fragmentos del texto, permitiendo una búsqueda rápida y precisa.
- **Transformers** (Hugging Face): Usado para el modelo de pregunta-respuesta basado en RoBERTa, afinado con el dataset SQuAD.
- **Scikit-learn**: Para la construcción de un índice rápido para la búsqueda de fragmentos relevantes usando k-NN (k-Nearest Neighbors).
- **Gradio**: Para la creación de una interfaz interactiva que permite al usuario realizar preguntas al sistema y recibir respuestas.

## 📂 **Estructura del Proyecto**

proyecto_transito/ │ ├── app.py # Script principal con la lógica de Pregunta-Respuesta ├── codigo_transito.txt # Texto extraído del PDF con el Código Nacional de Tránsito ├── requirements.txt # Dependencias necesarias para ejecutar el proyecto

bash
Copiar
Editar

## ⚙️ **Instrucciones de Instalación y Ejecución**

### Paso 1: Clonar el repositorio

Si aún no lo has hecho, clona el repositorio:

```bash
git clone https://github.com/tu_usuario/proyecto_transito.git
cd proyecto_transito
Paso 2: Crear un entorno virtual (opcional pero recomendado)
Para evitar conflictos de dependencias, se recomienda crear un entorno virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
Paso 3: Instalar las dependencias
Instala todas las dependencias necesarias desde requirements.txt:

bash
Copiar
Editar
pip install -r requirements.txt
Paso 4: Ejecutar la aplicación
Una vez instaladas las dependencias, corre la aplicación con el siguiente comando:

bash
Copiar
Editar
python app.py
Esto lanzará un servidor local en http://localhost:7860 donde podrás interactuar con el sistema de pregunta-respuesta a través de una interfaz web.

Paso 5: Probar el sistema
En la interfaz web de Gradio, podrás escribir preguntas sobre el Código Nacional de Tránsito de Colombia y recibir respuestas precisas basadas en el texto del documento cargado.

📑 Cómo funciona el modelo
Carga del texto: El texto del Código Nacional de Tránsito de Colombia es cargado desde un archivo .txt (extraído de un PDF).

Fragmentación del texto: El texto es dividido en fragmentos de tamaño manejable para crear embeddings eficientes.

Embeddings: Se utilizan los embeddings generados por el modelo BGE de Sentence-Transformers para representar semánticamente los fragmentos.

Índice rápido: Usamos k-NN (k-Nearest Neighbors) para realizar búsquedas rápidas de fragmentos relevantes para la pregunta.

Pregunta-respuesta: Finalmente, el modelo de Transformers (RoBERTa fine-tuned con SQuAD) se utiliza para responder la pregunta basándose en el contexto encontrado en los fragmentos más relevantes.

🤖 Modelos Utilizados
Embeddings: BAAI/bge-base-en-v1.5

Pregunta-Respuesta: deepset/roberta-base-squad2

💬 Contribuir
Si deseas contribuir a este proyecto, por favor abre un pull request con tus sugerencias y mejoras.

📜 Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

yaml
Copiar
Editar

---

Este documento ya está listo para ser colocado en un archivo `README.md` en tu proyecto. Puedes copiarlo tal cual o pegarlo directamente en el archivo `README.md` de tu repositorio.