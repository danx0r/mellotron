import os, sys
fn = sys.argv[1]
f = open(fn)
fw = open("fixed.txt", 'w')
for r in f.readlines():
    s = r.replace("/path_to_ljs/", "./path_to_ljs/")
    fw.write(s)
