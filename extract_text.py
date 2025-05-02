import fitz  # PyMuPDF

def extraer_texto(pdf_path):
    doc = fitz.open(pdf_path)
    texto_total = ""
    for pagina in doc:
        texto_total += pagina.get_text()
    return texto_total

if __name__ == "__main__":
    texto = extraer_texto("codigo_transito.pdf")
    with open("codigo_transito.txt", "w", encoding="utf-8") as f:
        f.write(texto)
    print("Texto extraído correctamente.")
