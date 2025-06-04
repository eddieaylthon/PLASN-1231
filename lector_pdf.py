import pyttsx3
import PyPDF2
import sys


def leer_pdf(pdf_path, voice_index=0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    else:
        print("Indice de voz no valido; se utiliza la voz predeterminada")
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        texto = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    engine.say(texto)
    engine.runAndWait()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python lector_pdf.py archivo.pdf [indice_voz]")
        sys.exit(1)
    ruta = sys.argv[1]
    indice = int(sys.argv[2]) if len(sys.argv) >= 3 else 0
    leer_pdf(ruta, indice)
