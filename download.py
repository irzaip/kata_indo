import os
import re
import glob
import sys
import time
import gtts

f = open("full_indo_word.txt",'r')
allwords = f.readlines()

outdir="./kata_mp3"

lfrom=40000
lto=50000

def process(ffn,slow=False):
    ffn.replace("\n","")
    ffn = re.sub(r"[^a-zA-Z]","",ffn)
    try:
        af = gtts.gTTS(ffn,lang='id',slow=slow)
    except:
        print("Error getting - GTTS:",ffn)
    try:
        ffx = os.path.join(outdir,ffn+".mp3")
        af.save(ffx)
        print(ffx)
    except:
        print("ERROR saving - ", ffx)
    time.sleep(0.3)
    
    
for idx, i in enumerate(allwords[lfrom:lto]):
    if idx % 100 == 0: time.sleep(10)
    process(i,slow=False)
    print(idx)
    time.sleep(0.5)
