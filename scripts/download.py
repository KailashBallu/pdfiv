import os, sys, signal
import requests
import argparse

def download_file(target, url):
    filename = os.path.basename(url)
    filerequest = requests.get(url)

    with open(os.path.join(target, filename), "wb") as filelocal:
        filelocal.write(filerequest.content)
        return True

    return False

def get_first_url(filepath):
    try:
        with open(filepath, "r") as f:
            first_line = f.readline()
            f.close()
            return first_line.replace("\n", "").replace("\r", "") if first_line != "" else False
    except (OSError, IOError) as e:
        print("Can't open: {}".format(filepath))
        return False

def remove_first_url(filepath):
    with open(filepath, "r") as fin:
        data = fin.read().splitlines(True)
        fin.close()

    with open(filepath, "w") as fout:
        fout.writelines(data[1:])
        fout.close()

def signal_handler(signal, frame):
    print("\nBye!")
    sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download to directory urls from file.")
    parser.add_argument('urlist', help="file with list of urls to download")
    parser.add_argument('target', help="destination path, where files was donwloaded")
    args = parser.parse_args()

    urlist = args.urlist
    target = args.target
    signal.signal(signal.SIGINT, signal_handler)

    while(True):
        url = get_first_url(urlist)

        if not url:
            break

        if download_file(target, url):
            print("[OK] {}".format(url))
            remove_first_url(urlist)
        else:
            print("[ERROR] {}".format(url))
            break