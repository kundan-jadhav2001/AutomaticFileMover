import os,shutil,datetime,time

def move():
    while True:
        fromfile = "C:/Users/Jadhav/Desktop/sample/"                            #file location from where you want to move file.
        tofile = "V:/KUNDAN/sample/"                                            #file location to where you want to move file.
        tfiles = [ i for base,dirs,files in os.walk(tofile) for i in files]     #list of names of files in file where you want to move file.
        ffiles = [ j for base,dirs,files in os.walk(fromfile) for j in files]   #list of names of files in from file.
        samefiles = [i for i in ffiles for j in tfiles if i==j]                 #list of names of files with same name in both files.
        if len(ffiles)==0:
            print("No files to move...")
        for i in ffiles:
            if i in samefiles:
                filename = fromfile + str(i)                                                #actual file name.
                filename2 = tofile + datetime.datetime.now().strftime(" %M_%S") + str(i)    #new name of file if file already exist with same name.
                print(f"Moving file {i} by changing name...")
                shutil.move(filename,filename2)
            else:
                filename = fromfile + str(i)
                filename2 = tofile + str(i)
                print(f"Moving file {i}")
                shutil.move(filename,filename2)
        time.sleep(60)                                                           #wait for 1min before checking again.

move()
