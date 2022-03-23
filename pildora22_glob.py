import glob,os

#files=glob.glob("*.txt")
#print (files)

#lastfile=max(glob.glob("*.txt"),key=os.path.getctime)
lastfile=min(glob.glob("*.txt"),key=os.path.getctime)
print (lastfile)
