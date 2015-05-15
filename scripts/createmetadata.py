import os, glob
import json
import argparse

def get_number_of_pages(directory):
    return len(glob.glob("{}/png/*.png".format(directory)))

def get_converted_files(directory):
    return [f for f in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, f))]

def has_html(file_path):
    return os.path.isdir(os.path.join(file_path, "html"))

def metadata(file_path):
    file_name = os.path.basename(file_path)
    file_number_of_pages = get_number_of_pages(file_path)
    file_has_html = has_html(file_path)
    file_content = os.path.join(file_path, "content.txt")
    file_cover = os.path.join(file_path, "png", "page-{}.png".format(str(1).zfill(6)))
    file_pages = []

    for page in range(1, file_number_of_pages):
        file_pages.append({
            "png": os.path.join(file_path, "png", "page-{}.png".format(str(page).zfill(6))),
            "html": os.path.join(file_path, "html", "page{}.html".format(page)) if file_has_html else ""
        })

    return {
        "name": file_name,
        "path": file_path,
        "cover": file_cover,
        "number_of_pages": file_number_of_pages,
        "content": file_content,
        "pages": file_pages
    }

def save_metadata(file_path, metadata):
    metadata_file = os.path.join(file_path, "metadata.json")
    json.dump(metadata, open(metadata_file, "w"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create metadata information about converted PDF files")
    parser.add_argument('source', help="directory with converted files")
    args = parser.parse_args()

    source_root_path = args.source
    
    if not os.path.exists(source_root_path):
        print("source path does not exists: {}".format(source_root_path))
        exit()

    files = get_converted_files(source_root_path)
    for file_name in files:
        file_path = os.path.join(source_root_path, file_name)
        save_metadata(file_path, metadata(file_path))