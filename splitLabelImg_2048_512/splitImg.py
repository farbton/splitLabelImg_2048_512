import os
import cv2
from reader import Reader
from writer import Writer


class SplitImgAndLabel(object):
    """description of class"""

    def __init__(self, source_dir, out_dir):
            self.source_dir = source_dir
            self.out_dir = out_dir

    def manipulate_files(self, listOfFilenames):
        print("manipulate files...")
        for i, (txtFilename, jpgFilename) in enumerate(listOfFilenames):
            bboxList = self.reader.get_bbox_list(txtFilename)
            print("Länge der BboxList: " + str(len(bboxList)))
            bboxListSplited = self.splitOldBboxList(bboxList)
            imgSplitedList = self.splitImg(jpgFilename)
            print("Anzahl der gespliteten Images: " + str(len(imgSplitedList)))
            self.writer.writeNewFiles(txtFilename, jpgFilename, bboxListSplited, imgSplitedList)
            #self.writer.write_rotate_bbox_list(txt_filename,
            #bbox_list_rotated)
            #self.writer.write_img_rotated(jpg_filename, img_rotated)
        print("Edited files:",2 * (i + 1), "| txt_files:",i + 1, "| jpg_files:",i + 1)

    def splitOldBboxList(self, oldBboxList):
        listOfLists = []
        counter = 0
        #for l in range(1,16):
        #    newList + l = []
        newList1 = []
        newList2 = []
        newList3 = []
        newList4 = []
        newList5 = []
        newList6 = []
        newList7 = []
        newList8 = []
        newList9 = []
        newList10 = []
        newList11 = []
        newList12 = []
        newList13 = []
        newList14 = []
        newList15 = []
        newList16 = []
  
        for bbox in oldBboxList:
            cls, x_center, y_center, width, height = bbox.split()
            if 0 + float(height) / 2 < float(y_center) <= 0.25 - float(height) / 2:
                if 0 + float(width) / 2 < float(x_center) <= 0.25 - float(width) / 2: #subframe 1
                    x_new = (float(x_center) * 2048) / 512
                    y_new = (float(y_center) * 2048) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList1.append(bbox)
                    newList1.append("\n")
                    counter = counter + 1
                if 0.25 + float(width) / 2 < float(x_center) <= 0.5 - float(width) / 2: #subframe 2
                    x_new = ((float(x_center) * 2048)-512) / 512
                    y_new = (float(y_center) * 2048) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList2.append(bbox)
                    newList2.append("\n")
                    counter = counter + 1
                if 0.5 + float(width) / 2 < float(x_center) <= 0.75 - float(width) / 2: #subframe 3
                    x_new = ((float(x_center) * 2048)-1024) / 512
                    y_new = (float(y_center) * 2048) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList3.append(bbox)
                    newList3.append("\n")
                    counter = counter + 1
                if 0.75 + float(width) / 2 < float(x_center) < 1 - float(width) / 2: #subframe 4
                    x_new = ((float(x_center) * 2048)-1536) / 512
                    y_new = (float(y_center) * 2048) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList4.append(bbox)
                    newList4.append("\n")
                    counter = counter + 1
            
            if 0.25 + float(height) / 2 < float(y_center) <= 0.5 - float(height) / 2:
                if 0 + float(width) / 2 < float(x_center) <= 0.25 - float(width) / 2: #subframe 5
                    x_new = (float(x_center) * 2048) / 512
                    y_new = ((float(y_center) * 2048)-512) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList5.append(bbox)
                    newList5.append("\n")
                    counter = counter + 1
                if 0.25 + float(width) / 2 < float(x_center) <= 0.5 - float(width) / 2: #subframe 6
                    x_new = ((float(x_center) * 2048)-512) / 512
                    y_new = ((float(y_center) * 2048)-512) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList6.append(bbox)
                    newList6.append("\n")
                    counter = counter + 1
                if 0.5 + float(width) / 2 < float(x_center) <= 0.75 - float(width) / 2: #subframe 7
                    x_new = ((float(x_center) * 2048)-1024) / 512
                    y_new = ((float(y_center) * 2048)-512) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList7.append(bbox)
                    newList7.append("\n")
                    counter = counter + 1
                if 0.75 + float(width) / 2 < float(x_center) < 1 - float(width) / 2: #subframe 8
                    x_new = ((float(x_center) * 2048)-1536) / 512
                    y_new = ((float(y_center) * 2048)-512) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList8.append(bbox)
                    newList8.append("\n")
                    counter = counter + 1

            if 0.5 + float(height) / 2 < float(y_center) <= 0.75 - float(height) / 2:
                if 0 + float(width) / 2 < float(x_center) <= 0.25 - float(width) / 2: #subframe 9
                    x_new = (float(x_center) * 2048) / 512
                    y_new = ((float(y_center) * 2048)-1024) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList9.append(bbox)
                    newList9.append("\n")
                    counter = counter + 1
                if 0.25 + float(width) / 2 < float(x_center) <= 0.5 - float(width) / 2: #subframe 10
                    x_new = ((float(x_center) * 2048)-512) / 512
                    y_new = ((float(y_center) * 2048)-1024) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList10.append(bbox)
                    newList10.append("\n")
                    counter = counter + 1
                if 0.5 + float(width) / 2 < float(x_center) <= 0.75 - float(width) / 2: #subframe 11
                    x_new = ((float(x_center) * 2048)-1024) / 512
                    y_new = ((float(y_center) * 2048)-1024) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList11.append(bbox)
                    newList11.append("\n")
                    counter = counter + 1
                if 0.75 + float(width) / 2 < float(x_center) < 1 - float(width) / 2: #subframe 12
                    x_new = ((float(x_center) * 2048)-1536) / 512
                    y_new = ((float(y_center) * 2048)-1024) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList12.append(bbox)
                    newList12.append("\n")
                    counter = counter + 1

            if 0.75 + float(height) / 2 <= float(y_center) < 1.0 - float(height) / 2:
                if 0 + float(width) / 2 < float(x_center) <= 0.25 - float(width) / 2: #subframe 13
                    x_new = (float(x_center) * 2048) / 512
                    y_new = ((float(y_center) * 2048)-1536) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList13.append(bbox)
                    newList13.append("\n")
                    counter = counter + 1
                if 0.25 + float(width) / 2 < float(x_center) <= 0.5 - float(width) / 2: #subframe 14
                    x_new = ((float(x_center) * 2048)-512) / 512
                    y_new = ((float(y_center) * 2048)-1536) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList14.append(bbox)
                    newList14.append("\n")
                    counter = counter + 1
                if 0.5 + float(width) / 2 < float(x_center) <= 0.75 - float(width) / 2: #subframe 15
                    x_new = ((float(x_center) * 2048)-1024) / 512
                    y_new = ((float(y_center) * 2048)-1536) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList15.append(bbox)
                    newList15.append("\n")
                    counter = counter + 1
                if 0.75 + float(width) / 2 < float(x_center) < 1 - float(width) / 2: #subframe 16
                    x_new = ((float(x_center) * 2048)-1536) / 512
                    y_new = ((float(y_center) * 2048)-1536) / 512
                    width_new = (float(width) * 2048) / 512
                    height_new = (float(height) * 2048) / 512
                    bbox = "{}, {:f}, {:f}, {:f}, {:f}".format(int(cls), float(x_new), float(y_new), float(width_new), float(height_new))
                    bbox = bbox.replace(",","")
                    newList16.append(bbox)
                    newList16.append("\n")
                    counter = counter + 1


        listOfLists.insert(0,newList1)
        listOfLists.insert(1,newList2)
        listOfLists.insert(2,newList3)
        listOfLists.insert(3,newList4)
        listOfLists.insert(4,newList5)
        listOfLists.insert(5,newList6)
        listOfLists.insert(6,newList7)
        listOfLists.insert(7,newList8)
        listOfLists.insert(8,newList9)
        listOfLists.insert(9,newList10)
        listOfLists.insert(10,newList11)
        listOfLists.insert(11,newList12)
        listOfLists.insert(12,newList13)
        listOfLists.insert(13,newList14)
        listOfLists.insert(14,newList15)
        listOfLists.insert(15,newList16)
        print("Bbox Counter: " + str(counter))
        return listOfLists


    def splitImg(self, imgFilename):
        print("splitImg()")
        counter = 1
        imgSplittedList = []
        img = cv2.imread(imgFilename)
        for y in range(0,4):
            for x in range(0,4):
                img1 = img[y * 513 + 1:y * 513 + 513, x * 513 + 1:x * 513 + 513]
                number = str(counter)
                #cv2.imshow(number, img1)
                #cv2.waitKey(1000)
                counter = counter + 1
                imgSplittedList.append(img1)
        return imgSplittedList


    def start(self):
        self.reader = Reader(source_dir=self.source_dir)
        self.writer = Writer(outDir = self.out_dir)
        list_of_filenames = self.reader.get_list_of_filenames()
        self.manipulate_files(list_of_filenames)