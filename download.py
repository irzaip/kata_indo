import os
import re
import glob
import sys
import time


f = open("full_indo_word.txt",'r')
allwords = f.readlines()

outdir="/home/ubuntu/result"

lfrom=71500
lto=71560

def process(ffn,slow=False):
    ffn.replace("\n","")
    ffn = re.sub(r"[^a-zA-Z]","",ffn)
    try:
        af = gtts.gTTS(ffn,lang='id',slow=slow)
        af.save(os.path.join(outdir,ffn+".mp3"))
    except:
        print("ERROR - ", ffn)
    print(ffn)
    time.sleep(0.3)
    
    
for idx, i in enumerate(allwords[lfrom:lto]):
    if idx % 100 == 0: time.sleep(10)
    process(i,slow=False)
    print(idx)
    time.sleep(0.5)