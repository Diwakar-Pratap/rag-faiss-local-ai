import os
from pypdf import PdfReader

ALLOWED_EXTENSIONS = [".txt", ".pdf", ".md"]

def load_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""

def load_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text
    except:
        return ""

def load_file(file_path):
    if file_path.endswith((".txt", ".md")):
        return load_txt(file_path)

    elif file_path.endswith(".pdf"):
        return load_pdf(file_path)

    return ""

def load_from_folder(folder_path):
    all_data = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                text = load_file(file_path)

                if text.strip():
                    all_data.append((file_path, text))  # ✅ IMPORTANT

    return all_data