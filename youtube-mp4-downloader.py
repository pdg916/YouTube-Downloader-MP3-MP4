from cProfile import label
import sys
from pytube import YouTube
import os 
import time


SaveFolder = "SaveFolderMP4"

file = os.listdir("./")
try:
	MyFile = "./mp4.txt"
	Links = open(MyFile).read().splitlines() 
except:
	if "mp4.txt" not in file:
		print("링크 파일이 존재하지 않습니다.")
		print("다운로드를 위해선 링크 파일이 반드시 필요합니다.")
		time.sleep(4)
		sys.exit(0)


try:
	if not os.path.exists(SaveFolder):
		print("MP4 폴더를 생성합니다...\n")
		os.makedirs(SaveFolder)
except OSError:
	pass

print("="*40,"\n")
for i in Links:
	url = i
	try:
		yt = YouTube(url)
		stream = yt.streams.get_highest_resolution()
		stream.download(SaveFolder)
		print(yt.title,"을(를) 다운로드합니다...\n")
	except:
		print("다운로드가 불가능한 영상이므로 넘어갑니다...\n")
print("="*40,"\n")
