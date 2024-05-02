import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Replace 'Bhagavad_Gita.pdf' with the actual name of your Bhagavad Gita PDF file
pdf_text = extract_text_from_pdf(r"C:\Users\MY PC\Desktop\AI_Intern_Mentorness\Developing-a-Chatbot-for-Bhagavad-Gita\Bhagavad_Gita.pdf")
print(pdf_text)
