import fitz


def read_uploaded_file(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

f = read_uploaded_file('curriculos/CV Pedro Argento.pdf')
print(f)