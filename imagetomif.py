from PIL import Image
import sys, getopt

def rgb_to_hex(rgb, hexPerColour):
	return bin(int(rgb[0] * (16**hexPerColour-1)/255))[2:].zfill(hexPerColour*4) + bin(int(rgb[1] * (16**hexPerColour-1)/255))[2:].zfill(hexPerColour*4) + bin(int(rgb[2] * (16**hexPerColour-1)/255))[2:].zfill(hexPerColour*4)


def main(argv):
	inputfile = ''
	outputfile = ''
	hexPer = 1
	try:
		opts, args = getopt.getopt(argv, "hi:o:p:", ["ifile=", "ofile=", "hexPerColour="])
	except getopt.GetoptError:
		print("Invalid arguments")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("miftoimage.py -i <inputfile> -o <outputfile> -p <int>")
			sys.exit(2)
		elif opt in ('-i', '--ifile'):
			inputfile = arg
		elif opt in ('-o', '--ofile'):
			outputfile = arg
		elif opt in ('-p', '--hexPerColour'):
			hexPer = int(arg)


	im = Image.open(inputfile, 'r').convert('RGB')
	width, height = im.size
	pix = im.load()
	


	binColours = []
	for imy in range(height):
		for imx in range(width):
			binColours.append(rgb_to_hex(pix[imx,imy], hexPer))

	DEPTH = len(binColours)
	WIDTH = len(binColours[0])
	ADDRESSRADIX = "hex"
	DATARADIX = "bin"

	with open(outputfile, 'w') as generatedmif:
		generatedmif.write(f"Depth = {DEPTH};\n")
		generatedmif.write(f"Width = {WIDTH};\n")
		generatedmif.write(f"Address_radix={ADDRESSRADIX};\n")
		generatedmif.write(f"Data_radix={DATARADIX};\n")
		generatedmif.write(f"Content\n")
		generatedmif.write(f"BEGIN\n")

		memoryFilled = 0;
		for i in range(height):
			generatedmif.write(f"\t{hex(memoryFilled)[2:].upper().rjust(4)}:\t{' '.join(binColours[i*width:i*width+width])};\n")
			memoryFilled += width
		generatedmif.write(f"END;")

if __name__ == '__main__':
	main(sys.argv[1:])

