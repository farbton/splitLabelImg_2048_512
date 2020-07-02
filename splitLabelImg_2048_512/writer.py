import os
import cv2

class Writer(object):
    def __init__(self, outDir):
        self.outDir = outDir

    def writeNewFiles(self, txtFilename, jpgFilename, listOfListBbox, imgSplitedList):
        print(txtFilename)
        self.writeTxt(txtFilename, listOfListBbox)
        self.writeJpg(jpgFilename, imgSplitedList)

    def writeJpg(self, jpgFilename, imgSplitedList):
        head, tail = os.path.split(jpgFilename)
        fileName, fileExt = os.path.splitext(tail)
        for i, img in enumerate(imgSplitedList):
            newFileName = fileName + "sub" + str(i+1) + fileExt
            newFilePath = self.outDir +"\\" + newFileName
            cv2.imwrite(newFilePath, img)
            #print(newFilePath)
        

    def writeTxt(self, txtFilename, listOfListBbox):
        head, tail = os.path.split(txtFilename)
        fileName, fileExt = os.path.splitext(tail)
        for i, bboxlist in enumerate(listOfListBbox):
            newFileName = fileName + "sub" + str(i + 1) + fileExt
            newFilePath = self.outDir + "\\" + newFileName
            new_file = open(newFilePath, "w")
            new_file.writelines(str(bbox) for bbox in bboxlist)
            new_file.close()
            