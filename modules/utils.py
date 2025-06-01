import os
import re
import fitz
import docx2txt
import tempfile
from PIL import Image, ImageDraw, ImageFont
import io  # ⬅️ Add this to your imports if not already present


def extract_text(file, ext):
    if ext == ".pdf":
        file.seek(0)
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return " ".join([p.get_text() for p in doc])
    elif ext == ".docx":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(file.read())
            tmp.flush()
            text = docx2txt.process(tmp.name)
        return text
    elif ext == ".txt":
        return file.read().decode("utf-8")
    return ""

def clean_text(text):
    return re.sub(r"\s+", " ", text.strip())

def resume_to_image(text):
    lines = text.split('\n')
    img = Image.new("RGB", (800, 20 * len(lines) + 20), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    for i, line in enumerate(lines):
        draw.text((10, 20 * i), line, fill="black", font=font)
    return img


def preview_pdf_all_pages(file):
    file.seek(0)
    doc = fitz.open(stream=file.read(), filetype="pdf")
    images = []
    for page in doc:
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        images.append(img)
    return images





