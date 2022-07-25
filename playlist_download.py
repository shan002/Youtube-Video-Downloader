from bs4 import BeautifulSoup
import requests
import pytube
from pytube import YouTube
import os
import sys


def fetch_videos(url):

    linklist = []

    def fetch():
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')


        for atag in soup.findAll('a'):
            link = atag['href']
            if atag.h4 != None:
                index = link.split('index=')[-1]
                title = f'{index}. ' + atag.h4.text.strip()
                linklist.append((title, link, index))


    while(len(linklist) == 0):
        fetch()

    return linklist


# conf = input("Do you want any of the videos to exclude [y/n]? ")
# if conf == 'y':
#     exclude_list = input("Enter the serial numbers of videos to be excluded (you can enter adjacent numbers using hypen and different number preceeded by a space\n--> ")
#     exclude_list = exclude_list.split(" ");
#     for item in exclude_list:
#         if "-" in item:
#             start_range, end_range = map(lambda x: int(x)-1, item.split("-"))
#             print(start_range, end_range)
#             linklist = linklist[:start_range] + linklist[end_range+1:]
#         else:
#             linklist.pop(int(item)-1)

# print("Following videos will be downloaded [y/n]? ")
# for video in linklist:
#     print(video[0])

# conf = input("proceed [y/n]? ")
# if conf.lower() == 'n':
#   sys.exit()
# print()


# for video in linklist:
#   link = video[1]
#   print(f"Downloading...  {video[0]}")

#   yt = YouTube(link)
#   streamlist = yt.streams.filter(progressive=True)

#   newdict = {}
#   for stream in streamlist:
#       res = str(stream).split(' ')[3].split('"')[1]
#       newdict[res] = stream

#   newstreamlist = []
#   for res in sorted(newdict.keys(), reverse=True):
#       newstreamlist.append(newdict[res])

#   outfile = newstreamlist[0].download()
#   title = f'{video[2]}. ' + outfile.split('\\')[-1]
#   print("Title: ", title)
#   os.rename(outfile, title)

#   print("Completed.\n\n")

# print("\nAll downloads completed.")


