import os, glob
import argparse

bin_pdftohtml = "bin\\xpdfbin-win-3.04\\bin64\\pdftohtml.exe"
bin_pdftopng = "bin\\xpdfbin-win-3.04\\bin64\\pdftopng.exe"
bin_pdftotext = "bin\\xpdfbin-win-3.04\\bin64\\pdftotext.exe"
bin_tesseract_ocr = "bin\\tesseract-ocr-3.02-win32-portable\\tesseract.exe"

def get_png_files(directory):
    print("get files from: {}*.png".format(directory))
    return glob.glob("{}*.png".format(directory))

def get_pdf_files(directory):
	print("get files from: {}*.pdf".format(directory))
	return glob.glob("{}*.pdf".format(directory))

def setup_target_directory(target):
    if os.path.exists(target):
        return False

    os.mkdir(target)
    os.mkdir(os.path.join(target, "png"))

    return True

def create_html_from_pdf(source, target):
	cmd = "{} -q -r 200 \"{}\" \"{}\"".format(bin_pdftohtml, source, target)
	os.system(cmd)
	
def create_png_from_pdf(source, target):
	cmd = "{} -q -r 200 \"{}\" \"{}\"".format(bin_pdftopng, source, target)
	os.system(cmd)

def create_text_from_pdf(source, target):
	cmd = "{} -q -enc UTF-8 -raw \"{}\" \"{}\"".format(bin_pdftotext, source, target)
	os.system(cmd)

def create_text_from_png(source, target):
	target = os.path.join(target, os.path.basename(source).replace(".png", ""))
	cmd = "{} \"{}\" \"{}\" -lang pol".format(bin_tesseract_ocr, source, target)
	os.system(cmd)

def workflow_default(source, target):
    if setup_target_directory(target):
        create_html_from_pdf(source, os.path.join(target, "html/"))
        create_png_from_pdf(source, os.path.join(target, "png", "page"))
        create_text_from_pdf(source, os.path.join(target, "content.txt"))

def workflow_ocr(source, target):
    print("OCR way is not implemented")
    exit()
    target_png = os.path.join(target, "png")

    if setup_target_directory(target):
        create_png_from_pdf(source, target_png)

        files = get_png_files(target_png)
        for filepath in files:
            create_text_from_png(filepath, target)

def workflow(name, source, target):
    to_execute = {
        "default": workflow_default,
        "ocr": workflow_ocr
    }.get(name, "default")

    to_execute(source, target)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF files")
    parser.add_argument('source', help="directory with PDF files to convert")
    parser.add_argument('target', help="destination path, where converted files was saved")
    parser.add_argument('workflow', choices=["default", "ocr"], help="workflow type: default or ocr")
    args = parser.parse_args()

    source_root_path = args.source
    target_root_path = args.target
    workflow_type = args.workflow

    if not os.path.exists(source_root_path):
        print("source path does not exists: {}".format(source_root_path))
        exit()

    if not os.path.exists(target_root_path):
        print("target path does not exists: {}".format(target_root_path))
        exit()

    files = get_pdf_files(source_root_path)
    for file_path in files:
        file_name = os.path.basename(file_path)
        file_target = os.path.join(target_root_path, file_name.replace(".pdf", ""))
        file_source = os.path.join(source_root_path, file_name)

        print("start: {}".format(file_name))
        workflow(workflow_type, file_source, file_target)
        print("finished: {}".format(file_name))