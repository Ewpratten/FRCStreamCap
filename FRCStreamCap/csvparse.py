import sys

def containsStr(string) -> bool:
	try:
		int(string)
		return False
	except:
		return True

def isStr(string) -> bool:
	for n in [0,1,2,3,4,5,6,7,8,9]:
		if str(n) in string:
			return False
	return True

infile = open(sys.argv[1], "r")
file = infile.read()

# prelim search
prelim = [] # stores the raw file in an array

for line in file.split("\n")[1:]:
	prelim.append(line.split(","))

# deap search
parsed = []
for frame in prelim:
	# Check if it is a fully useless frame
	# if so, remove it
	markTicker = 0
	for field in frame[1:]:
		if isStr(field):
			markTicker += 1
	if markTicker >= 3:
		continue
	
	# Check if the frame is dirty
	# if so, mark it
	doMark = False
	for field in frame:
		if containsStr(field):
			doMark = True
	if doMark:
		frame[4] = True
	
	
		
