import os,shutil,datetime,time

def move():
    while True:
        fromfile = "C:/Users/Jadhav/Desktop/sample/"
        tofile = "V:/KUNDAN/sample/"
        tfiles = [ i for base,dirs,files in os.walk(tofile) for i in files]
        ffiles = [ j for base,dirs,files in os.walk(fromfile) for j in files]
        samefiles = [i for i in ffiles for j in tfiles if i==j]
        if len(ffiles)==0:
            print("No files to move...")
        for i in ffiles:
            if i in samefiles:
                filename = fromfile + str(i)
                filename2 = tofile + datetime.datetime.now().strftime(" %M_%S") + str(i)
                print(f"Moving file {i} by changing name...")
                shutil.move(filename,filename2)
            else:
                filename = fromfile + str(i)
                filename2 = tofile + str(i)
                print(f"Moving file {i}")
                shutil.move(filename,filename2)
        time.sleep(60)

move()