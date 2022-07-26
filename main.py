import os
import shutil
import sys
import urllib.request

def download(url: str, path: str):
    file = urllib.request.urlopen(url)
    with open(path, "wb") as writer:
        writer.write(file.read())

def download_ts(file_name: str, url_home: str, start_at: int, zfill: int):
    os.mkdir("temp_download")
    working_directory = "temp_download"
    flag = True
    index = start_at
    while flag:
        try:
            index_str = str(index).zfill(zfill)
            url = url_home.replace("{NUMBERING}", index_str)
            download(url, working_directory + "/ts" + index_str + ".ts")
            print(index_str + " COMPLETE")
            index += 1
        except:
            flag = False
            print("ALL COMPLETE")
    os.system("copy /b " + working_directory + " " + file_name + ".ts")
    shutil.rmtree(working_directory)

if __name__ == '__main__':
    download_ts(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))

# ↓ sys.argv
# name
# path
# start_at
# zfill
# 
# ex )
# video1 "https://website/index_{NUMBERING}.ts" 0 3