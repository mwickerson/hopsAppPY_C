"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"


@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b


@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)

@hops.component(
    "/pointat2",
    name="PointAt2",
    nickname="PtAt2",
    description="Get point along curve",
    icon="pointat.png", 
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],

    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat2(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)

    

@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

# Working with Libraries

# python all-in-one for dummies, 2nd edition
# Chapter 1 Book 3

# Working
# 
# # Understand Text and Binary Files
# 
#  with Expternal Files
#folders and directories
# creating, reading, writing, and deleting files
 # Executabel Files: .py, .exe, .dll, .so, .dylib
 # Images: .png, .jpg, .bmp, .gif, .tiff, .ico
 # Text Files: .txt, .csv, .json, .xml, .html, .css, .js
# Binary Files: .bin, .dat, .zip, .gz, .rar, .7z
# Audio Files: .mp3, .wav, .aiff, .flac, .ogg, .wma
# Video Files: .mp4, .avi, .mov, .wmv, .flv, .mpeg, .mpg, .mkv, .3gp, .webm
# Document: .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .odt, .ods, .odp, .odg, .odc, .odf, .odb, .rtf, .tex, .txt, .md, .tex, .texi, .texinfo, .db, .sql, .dbf, .mdb, .sqlite, .db3, .sqlite3, .dbm, .dbs, .dbscript, .dbpro, .dbp, .dbpr, .dbpl, .dbq, .dbt, .dbx, .dbb, .dbc, .dbf, .dbk, .dbx, .db3, .db4, .db5, .db6, .db7, .db8, .db9, .db10, .db11, .db12, .db13, .db14, .db15, .db16, .db17, .db18, .db19, .db20, .db21, .db22, .db23, .db24, .db25, .db26, .db27, .db28, .db29, .db30, .db31, .db32, .db33, .db34, .db35, .db36, .db37, .db38, .db39, .db40, .db41, .db42, .db43, .db44, .db45, .db46, .db47, .db48, .db49, .db50, .db51, .db52, .db53, .db54, .db55, .db56, .db57, .db58, .db59, .db60, .db61, .db62, .db63, .db64, .db65, .db66, .db67, .db68, .db69, .db70, .db71, .db72, .db73, .db74, .db75, .db76, .db77, .db78, .db79, .db80, .db81, .db82, .db83, .db84, .db85, .db86, .db

# Use VS Studio Code for the Explorer Bar

# Opening and Closing Files
# use syntax: open(filename, mode)
# use forward slash for directories, rather than backslash for Windows paths

# r+ = read and write
# r = read only
# w = write only
# a = append

# b = binary mode
# t = text mode
# var = open(filename, mode)
# f = open(filename, mode)

@hops.component(
    "/open_txt",
    name="Open Text",
    nickname="OpenTxt",
    description="Open a text file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename of file to open")
        ],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of file")
    ]
)
def open_txt(filename: str):
    with open(filename, "r") as f:
        filecontents = f.read()
        print(filecontents)
    # The unindented line below is outside the function definition
    print('File is closed automatically: ', f.closed)
    return filecontents

# careful with .jpg files and UTF-8 files
@hops.component(
    "/open_UTF-8",
    name="Open UTF-8",
    nickname="OpenUTF-8",
    description="Open a UTF-8 file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename of file to open")
        ],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of file")
    ]
)
def open_utf8(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        filecontents = f.read()
        print(filecontents)
    # The unindented line below is outside the function definition
    print('File is closed automatically: ', f.closed)
    return filecontents

# Reading a Files contents
# use syntax: f.read()
# read([size]) reads at most size bytes from the file. 
# readline() reads until the end of the line. Good for txt files only.
# readlines() reads the entire file as a list of lines. Good for txt files only.

@hops.component(
    "/read_txt",
    name="Read Text",
    nickname="ReadTxt",
    description="Read a text file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename of file to read")
        ],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of file")
    ]
)
def read_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file
        filecontents = f.read()
        print(filecontents)
    # The unindented line below is outside the function definition
    print('File is closed automatically: ', f.closed)
    return filecontents

@hops.component(
    "/readlines_txt",
    name="Read Lines",
    nickname="ReadLines",
    description="Read a text file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename of file to read")
        ],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of file")
    ]
)
def readlines_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file
        filecontents = f.readlines()
        print(filecontents)
    # The unindented line below is outside the function definition
    print('File is closed automatically: ', f.closed)
    return filecontents

@hops.component(
    "/readline_txt",
    name="Read Line",
    nickname="ReadLine",
    description="Read a text file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename of file to read")
        ],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of file")
    ]
)
def readline_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file
        filecontents = f.readline()
        print(filecontents)
    # The unindented line below is outside the function definition
    print('File is closed automatically: ', f.closed)
    return filecontents

# Looping through a File's Contents

@hops.component(
    "/loop_txt",
    name="Loop Text",
    nickname="LoopTxt",
    description="Loop through a text file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename of file to loop through")
        ],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of file")
    ]
)
def loop_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file then loop through it
        listOut = []
        for line in f:
            print(line, end="")
            listOut.append(line)
        # The unindented line below is outside the function definition
        print('File is closed automatically: ', f.closed)
        return listOut

#Enumerate through a File's Contents
@hops.component(
    "/enum_txt",
    name="Loop",
    nickname="Loop",
    description="Loop through a file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of the file")
    ]
)
def enum_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file then loop through it
        # count each line starting at 0
        listOut = []
        for one_line in enumerate(f.readlines()):
            # If counter is even number, print with no extra newline
            if one_line[0] % 2 == 0:
                print(one_line[1], end='')  # print the line
                listOut.append(one_line[1]) # append the line to the list
            # Otherwise, print a couple spaces and an extra newline
            else:
                print('  ' + one_line[1])  # print the line
                listOut.append('  ' + one_line[1]) # append the line to the list
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut

# Looping through a File with readline()
#while loop
@hops.component(
    "/loop_readline_txt",
    name="Loop Readline",
    nickname="LoopReadline",
    description="Loop through a file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of the file")
    ]
)
def loop_readline_txt(filename: str):
    with open(filename, "r") as f:
        # read the entire file then loop through it
        listOut = []
        one_line = f.readline()
        while one_line:
            print(one_line, end="")
            listOut.append(one_line)
            one_line = f.readline()
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut

# Looping through a File with readline()
# while loop with a counter = 1
@hops.component(
    "/loop_counter_readline_txt",
    name="Loop Counter Readline",
    nickname="LoopCounterReadline",
    description="Loop through a file",
    inputs=[
        hs.HopsString("Filename", "F", "Filename to open")],
    outputs=[
        hs.HopsString("Contents", "C", "Contents of the file")
    ]
)
def loop_counter_readline_txt(filename: str):
    # Store a number to use as a loop counter
    counter = 1
    # Open the file
    with open(filename, "r") as f:
        # read one line from the file
        listOut = []
        one_line = f.readline()
        # As long as there are lines to read, loop through the file
        while one_line:
            # If the counter is even, print a couple spaces
            if counter % 2 == 0:
                print('  ' + one_line, end='')
                listOut.append('  ' + one_line)
            # Otherwise, print no new line at the end
            else:
                print(one_line, end='')
                listOut.append(one_line)
            # Increment the counter
            counter += 1
            # Read the next line from the file
            one_line = f.readline()
    # The unindented line below is outside the function definition.
    print('File is closed automatically: ', f.closed)
    return listOut

# Part two 







if __name__ == "__main__":
    app.run(debug=True)
