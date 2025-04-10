#!/usr/bin/env python3

import os
import struct as st
import argparse as ap

from pybmp import *



input_path: str
output_path: str
output_path_specified = False
output_file_exists_already = False

hori_rev = False
vert_rev = False
verbose = False

# Prints only when `verbose` is true
def vprint(values: str, sep: str | None = "", end: str | None = "\n"):
    global verbose

    if verbose:
        print(values, sep=sep, end=end)

# Deal with arguments & errors
def init():
    global input_path
    global output_path
    global output_path_specified
    global hori_rev
    global vert_rev
    global verbose

    # Collect arguments
    __p = ap.ArgumentParser(
                                prog='bmp2bin',
                                description='Converts .bmp image data to a .bin file'
                            )

    __p.add_argument('-i', '--input', type=str, help="Path of the input .bmp file.")
    __p.add_argument('-o', '--output', type=str, help='Path of the generated .bin file. If not specified, then the output file will take the name of the input file with .bin appended to it.')
    __p.add_argument('-v', '--verbose', action='store_true')
    __p.add_argument('-hr', '--horizontal-reverse', action='store_true', help='Reverse the order of pixel rows in the output file.')
    __p.add_argument('-vr', '--vertical-reverse', action='store_true', help='Reverse the order of pixel columns in the output file.')

    args = __p.parse_args()

    # Check input file
    if args.input == None:  # specified?
        __p.error("Input file must be specified")
        __p.print_help()
        exit(1)
    elif not os.path.exists(args.input): # exists?
        __p.error(f"Input file \"{args.input}\" does not exist")
        __p.print_help()
        exit(1)
    elif not str(args.input).endswith('.bmp'): # is a .bmp file
        __p.error(f"Input file \"{args.input}\" is not a .bmp file")
        __p.print_help()
        exit(1)
    else:
        input_path = args.input
    
    # Check output file
    if args.output == None:
        output_path = input_path
        output_path += ".bin"
    else:
        output_path = args.output
        output_path_specified = True

    # Check modifiers
    hori_rev =  args.horizontal_reverse
    vert_rev = args.vertical_reverse
    verbose = args.verbose





def main():
    global input_path
    global output_path
    global output_path_specified
    global hori_rev
    global vert_rev
    global verbose

    init()

    # print parameters
    vprint(f"Input file: {input_path}")
    vprint(f"Output file: {output_path}", end="")

    if not output_path_specified:
        vprint(" (Output path not specified so it was assumed)")
    else:
        vprint("")

    vprint("Horizontal reversing ", end="")

    if hori_rev:
        vprint("enabled")
    else:
        vprint("disabled")

    vprint("Vertical reversing ", end="")

    if vert_rev:
        vprint("enabled")
    else:
        vprint("disabled")

    vprint(f"Opening {input_path}... ", end="")    
    input_file = open(input_path, mode="rb")
    vprint("Done")

    vprint(f"Reading... ", end="")
    input_data 

    vprint(f"Opening {output_path}... ", end="")
    output_file = open(output_path, "xb")
    vprint("Done")





### MAIN ###
main()