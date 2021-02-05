#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Gain Correction
# Author: ZeeTulsa
# GNU Radio version: 3.8.2.0

from gnuradio import blocks
from gnuradio.blocks.blocks_swig0 import file_source
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

import os # needed for file manupilation
import numpy # needed for IQ conversion

class cfileGainCorrect(gr.top_block):

    def __init__(self):
        global fileSource
        global fileSink

        gr.top_block.__init__(self, "Gain Correction")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100e6

        ##################################################
        # Blocks
        ##################################################
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(0.0001, 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, fileSource, False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, fileSink, False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)





def main(top_block_cls=cfileGainCorrect, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    global fileSource
    global fileSink
    #main()

    path = "."

    tmpPath = input("Enter a file path for the IQ files, or leave blank if in current directory.  \nPress Enter to continue: ")

    if tmpPath:
        path = tmpPath

    print(f"Using file path: {str(path)}")

    for root, dirs, files in os.walk(path):
        for file in files:
            #print(os.path.join(root, file))
            
            if file.endswith('.16sc'):
                filename = os.path.join(root, file)

                print(f"Reading {str(filename)}")

                # generating the base filename without extension
                basename = os.path.splitext(filename)[0]
                #print(str(basename))

                # opening files to read and write to
                hostFile = open(filename, 'rb')
                sc16File = open(basename + '.sc16', 'wb')
                tmpFile = open(basename + '.tmp', 'wb')

                # setting file sourve and sink
                fileSource = basename + '.tmp'
                fileSink = basename + '.cfile'

                #print(f"{str(fileSource)} \n{str(fileSink)}")

                data = numpy.fromfile(hostFile, dtype=numpy.int16)
                dataFloat = data.astype(numpy.float32)

                print(f"Writing: {basename + '.sc16'}")
                sc16File.write(data.tobytes())

                print(f"Writing: {basename + '.tmp'}")
                tmpFile.write(dataFloat.tobytes())

                # closing the files
                hostFile.close()
                sc16File.close()
                tmpFile.close()      

                print(f"Starting GNURadio conversion for {str(fileSink)}")      
                main()

                #clearing the waste files
                os.remove(fileSource)
    
    print("Finished file conversion")