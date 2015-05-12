import os, glob

source_root_path = "files/pdf/"
target_root_path = "files/target/"

bin_path = "bin\\xpdfbin-win-3.04\\bin64\\"
bin_pdftohtml = "pdftohtml.exe"
bin_pdftopng = "pdftopng.exe"
bin_pdftotext = "pdftotext.exe"

def get_pdf_files(directory):
	print("get files from: {}*.pdf".format(directory))
	return glob.glob("{}*.pdf".format(directory))

def setup_target_directory(target):
	if not os.path.exists(target):
		os.mkdir(target)
	
	if not os.path.exists(os.path.join(target, "png")):
		os.mkdir(os.path.join(target, "png"))

def create_html_from_pdf(source, target):
	cmd = "{}{} -q -r 200 \"{}\" \"{}\"".format(bin_path, bin_pdftohtml, source, target)
	os.system(cmd)
	
def create_png_from_pdf(source, target):
	cmd = "{}{} -q -r 200 \"{}\" \"{}\"".format(bin_path, bin_pdftopng, source, target)
	os.system(cmd)

def create_text_from_pdf(source, target):
	cmd = "{}{} -q -enc UTF-8 -raw \"{}\" \"{}\"".format(bin_path, bin_pdftotext, source, target)
	os.system(cmd)

if __name__ == "__main__":
	files = get_pdf_files(source_root_path)
	for filepath in files:
		filename = os.path.basename(filepath)

		print("start: {}".format(filename))

		file_target = os.path.join(target_root_path, filename.replace(".pdf", ""))
		file_source = os.path.join(source_root_path, filename)

		setup_target_directory(file_target)
		create_html_from_pdf(file_source, os.path.join(file_target, "html/"))
		create_png_from_pdf(file_source, os.path.join(file_target, "png", "page"))
		create_text_from_pdf(file_source, os.path.join(file_target, "content.txt"))

		print("finished: {}".format(filename))