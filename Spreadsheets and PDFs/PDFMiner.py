import PyPDF2

# Do not use double quotes in Line 4 to avoid OS Error
f = open('C:\\Users\\User-PC\\Desktop\\Sample.pdf','rb')

read_pdf = PyPDF2.PdfFileReader(f)

print(f"Number of pages in .pdf file : {read_pdf.numPages}")

page_one = read_pdf.getPage(0)

page_one_text = page_one.extractText()

print(page_one_text)

all_content=[]

for page_num in range(read_pdf.numPages):
    all_content.append((read_pdf.getPage(page_num)).extractText())
    
print(f"Entire Content : {all_content}")

f.close()

f = open('C:\\Users\\User-PC\\Desktop\\Sample.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)

first_page = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(first_page)

pdf_output = open('C:\\Users\\User-PC\\Desktop\\New_Sample.pdf','wb')

pdf_writer.write(pdf_output)

f.close()

pdf_output.close()

f = open('C:\\Users\\User-PC\\Desktop\\Sample.pdf','rb')

pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())
    
print(f"PDF Text : {pdf_text}")

f.close()


    



