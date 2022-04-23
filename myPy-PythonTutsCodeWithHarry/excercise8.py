#excercise 8----Oh soldier pretify my soldier

import os
def soldier(path,file,format):
    os.chdir(path)
    files=os.listdir(path)

    with open(file) as f:
        filelst=f.read().split("\n")
    i=1

    for File in files:
        if File not  in filelst:
            os.rename(File,File.capitalize())

        if os.path.splitext(File)[1]==format:

            os.rename(File,f"{i}{format}")
            i+=1


if __name__=='__main__':
    soldier(r"C:\Users\Pankaj Kumar\Pictures\Screenshots",r"D:\myPy-PythonTutsCodeWithHarry\ext.txt",".png")



