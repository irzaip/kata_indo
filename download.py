import os,re, glob, gtts,time

f = open("full_indo_word.txt",'r')
allwords = f.readlines()

wstart = 0
wstop = 15000
outdir="./kata_TAN.1"

def process(ffn,slow=False):
    ffn.replace("\n","")
    ffn = re.sub(r"[^a-zA-Z]","",ffn)
    ffx = os.path.join(outdir,ffn+".mp3")
    try:
        af = gtts.gTTS(ffn+"?",lang='id',slow=slow)
    except:
        print("Error retrieveing :",ffx)
    try:
        af.save(ffx)
    except:
        print("ERROR - saving", ffx)
    time.sleep(0.1)


for idx, i in enumerate(allwords[wstart:wstop]):
    if idx % 100 == 0: time.sleep(10)
    process(i,slow=True)
    print(idx," - ",i)
    time.sleep(0.5)
