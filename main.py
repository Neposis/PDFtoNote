from pathlib import Path
from pypdf import PdfReader, PdfWriter, Transformation


def open_pdfs():
	p = Path('./in')
	files = p.glob('*.pdf')
	files = list(files)
	
	pdfs = {}
	
	for i in range(len(files)):
		pdfs[files[i].name] = PdfReader(files[i].absolute())
	
	return pdfs


if __name__ == '__main__':
	pdfs = open_pdfs()
	lines = PdfReader("./Lined.pdf")
	
	right = Transformation().scale(0.5, 0.5).translate(650, 75)
	left = Transformation().scale(0.75, 0.75).translate(-25.0, 75.0)
	
	lines = lines.pages[0]
	
	for i in pdfs:
		writer = PdfWriter()
		reader = PdfReader("./in/{}".format(i))
		
		for p in reader.pages:
			tmp_page = p
			tmp_page.add_transformation(left)
			tmp_page.merge_transformed_page(lines, right)
			
			writer.add_page(tmp_page)
		
		writer.write("./out/{}".format(i))
		
		
