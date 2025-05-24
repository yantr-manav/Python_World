import fitz  # PyMuPDF

with open("resume.pdf", "rb") as f:
    doc = fitz.open(stream=f.read(), filetype="pdf")
    for page in doc:
        print(page.get_text())
