from docx import Document

docname = 'Long-termcontributionofterrain-trappedairflows.docx'
docpath ='/home/raul/Downloads/'

filep = docpath + docname

doc = Document(filep)

pars = []
for p in doc.paragraphs:
	pars.append(p)
