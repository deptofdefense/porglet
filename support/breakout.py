import numpy # needed for IQ

myfile = open("Parrot_DISCO_2440_0300.16sc", "r")
#testfile = open("test.cfile", "wb")

dat = numpy.fromfile(myfile, dtype=numpy.int16)

datFloat = dat.astype(numpy.float32)

datFloat.tofile("test.cfile")

myfile.close()