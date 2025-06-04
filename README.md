# PLASN-1231

Comandos, trucos, estudio, programación.

## Lector de PDF con voces en español

Este proyecto incluye un script en Python para leer archivos PDF utilizando
voces instaladas en el sistema mediante la librería `pyttsx3`.

### Requisitos

- Python 3
- Instalar dependencias:
  ```bash
  pip install pyttsx3 PyPDF2
  ```

### Uso

```
python lector_pdf.py archivo.pdf [indice_voz]
```

`indice_voz` es opcional e indica la voz que se utilizará dentro de las voces
instaladas en el sistema. Si no se especifica, se utiliza la primera voz
Disponible.
