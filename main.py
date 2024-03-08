# import fitz <--- this one is not working  
import PyPDF2

pdf = PyPDF2.PdfReader('students.pdf')
print(pdf.pages[0].extract_text())
for page in pdf.pages:
  print(20*"-")
  print(page.extract_text())