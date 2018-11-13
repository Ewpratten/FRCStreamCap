import cv2

import getdata as data
import sys


vid = cv2.VideoCapture(sys.argv[1])
success,image = vid.read()

filebuffer = ""

filebuffer = "Frame,Red_Score,Blue_Score,Match_Time"

frame = 0

while success:
	parsed_frame = data.getFrameFromVid(vid)
	output = data.parseFrame(parsed_frame[1])
	
	success = parsed_frame[0]
	
	frame +=1
	
	filebuffer += "\n"+ str(frame) + "," + str(output["red_score"]) + "," + str(output["blue_score"]) + "," + str(output["match_time"])
	print(frame)

file = open(sys.argv[2], "w")
file.writelines(filebuffer)
file.close()