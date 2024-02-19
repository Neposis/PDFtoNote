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

def get_width(page):
	media_box = page.mediabox
	width = media_box.upper_right[0] - media_box.upper_left[0]
	height = media_box.upper_right[1] - media_box.lower_right[1]
	return width, height


if __name__ == '__main__':
	pdfs = open_pdfs()
	lines = PdfReader(Path(__file__).resolve().with_name("Lined.pdf"))
	
	lines = lines.pages[0]
	print("Processing PDFs")
	count = 1
	for i in pdfs:
		writer = PdfWriter()
		reader = PdfReader("./in/{}".format(i))
		
		width, height = get_width(reader.pages[0])
		scalew = 500/width
		scaleh = 590/height
		scalef = min(scalew, scaleh)
		# print(scalew, scaleh)
		right = Transformation().scale(0.5, 0.6).translate(500, 65)
		left = Transformation().scale(scalef, scalef).translate(0, 150*(scaleh>1))
		
		for leftp in reader.pages:
			tmpp = writer.add_blank_page(840, 590)
			leftp.add_transformation(left)
			tmpp.merge_page(leftp)
			tmpp.merge_transformed_page(lines, right)
		
		writer.write("./out/{}".format(i))
		print(" {0}/{1}".format(count, len(pdfs)))
		count += 1
		
	print("Completed, enjoy :P")
	print("Press any key to continue...")
	input()
		
