from PIL import Image
from sys import argv

if len(argv) != 4:
    exit("Usage: python resizee.py n infile outfile")

n = int(arv[1])
infile = argv[2]
outfile = argv[3]

inimage = Image.open(infile)
width, height = inimage.size
outimage = inimage.resize((width * n, height * n))

outimage.save(outfile)