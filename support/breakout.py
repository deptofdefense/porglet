import numpy # needed for IQ

myfile = open("Parrot_DISCO_2440_0300.cs16", "rb")
testfile = open("test.cfile", "wb")
testfile2 = open("test2.cfile", "wb")


dat = numpy.fromfile(myfile, dtype=numpy.int16)

datFloat = dat.astype(numpy.float32)
datS = datFloat.newbyteorder('S')

#datFloat.tofile(testfile)


data = datFloat.tobytes()
data2 = datS.tobytes()

testfile.write(data)
testfile2.write(data2)

testfile.close()
myfile.close()