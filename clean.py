import glob
filelist = glob.glob('*.csv')
for filename in filelist:
    print("checking " + filename)
    file = open(filename, "r")
    file.readline()
    prev = int(file.readline().split(',')[0])
    next = prev + 1
    line_num = 1
    for line in file.readlines():
        line_num += 1
        if next < prev:
            print("error on line:" + filename + str(line_num))
        prev,next = next,int(line.split(',')[0])
    file.close()
