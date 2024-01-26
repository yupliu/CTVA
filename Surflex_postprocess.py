import os

stPath = '/data/camd/Database/DUDE/DUDE-plus-rev1_AH'
lstFolder = [f.name for f in os.scandir(stPath) if f.is_dir()]
#arTest = []
#arTest.append(lstFolder[0])
for stDir in lstFolder:    
    stFile = stPath + "/" + stDir + "/surflex_result-log"    
    print(stFile)
    file = open(stFile, 'r')    
    arContent = file.readlines()

    stOutFile = "/data/camd/Database/DUDE/out/" + stDir + ".txt"
    print(stOutFile)
    out = open(stOutFile,"+wt") 

    index = 0
    names = []
    scores = []
    while index < len(arContent):
        name = arContent[index].split()[0]
        name = name[:-1]
        names.append(name)
        index=index+1
        score = arContent[index].split()[1]
        scores.append(score)
        index=index+1
        stOutLine = name + " " + score + "\n"
        out.write(stOutLine)
    file.close()
    out.close()



