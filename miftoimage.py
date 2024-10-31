from PIL import Image
import sys, getopt

def hex_to_rgb(hex, hexPerColour):
	return tuple(int(hex[i:i+hexPerColour], 16) * (255//min(16**(hexPerColour)-1, 255))  for i in range(0, len(hex), hexPerColour))
def main(argv):

	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
	except getopt.GetoptError:
		print("Invalid arguments")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("miftoimage.py -i <inputfile> -o <outputfile>")
			sys.exit(2)
		elif opt in ('-i', '--ifile'):
			inputfile = arg
		elif opt in ('-o', '--ofile'):
			outputfile = arg


	lines = []
	actualData = False
	WIDTH = 0
	with open(inputfile) as file:
		for line in file:
			if line.startswith("BEGIN"):
				actualData = True
			elif line.startswith("END"):
				break
			elif line.startswith("Width"):
				WIDTH = int(line.split(" ")[2][:-2])
				
			elif actualData:
				newline = "".join((line.rstrip()[6:-1].split()))
				lines.append([newline[i:i+WIDTH] for i in range(0, len(newline), WIDTH)])

	output = [[hex_to_rgb(hex(int(x, 2))[2:].zfill(WIDTH//4), (WIDTH//12)) for x in lines[i]] for i in range(len(lines))]

	width, height = len(output[0]), len(output)
	output = sum(output,[])

	im = Image.new('RGB', (width, height))
	im.putdata(output)
	im.save(outputfile)

if __name__ == '__main__':
	main(sys.argv[1:])