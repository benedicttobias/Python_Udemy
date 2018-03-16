from datetime import datetime
import glob

def readFile(filename):
    with open(filename, "r") as myfile:
        return myfile.read()

def writer(text, filePath):
    with open(fileName, "a") as myfile:
        myfile.write("\n" + text)

now = datetime.now()
fileName = now.strftime("%Y-%m-%d-%H-%M-%S-%f.txt")

for item in glob.glob('file*.txt'):
    writer(readFile(item), fileName)
