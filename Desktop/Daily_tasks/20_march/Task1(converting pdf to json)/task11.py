import io
import json
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def extract_text_from_pdf(pdf_path,page_count):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            page_count = page_count+1
            
        text = fake_file_handle.getvalue()
    
    # close open handles
    converter.close()
    fake_file_handle.close()
    
    if text:
        return  text,page_count

text_format = ""

if __name__ == '__main__':
    file_input = input("Enter Name of pdf to convert: ")
    file_input += '.pdf'
    text_format,page_count = extract_text_from_pdf(file_input,0)


my_dict = {}
stri = ""
for i in text_format:
    if i ==':':
        if stri=='StudentEnrollmentFormName':
            stri = 'Name'
        my_dict[stri]  = ''
        stri = ""
    elif i.isalnum():
        stri = stri+i

json_dict = {}
json_dict["document.fieldcount"] = len(my_dict)
json_dict["document.pagecount"] = page_count

json_dict.update(my_dict)
print(json.dumps(json_dict))