import os
import cv2
from reader import Reader


class SplitImgAndLabel(object):
    """description of class"""

    def __init__(self, source_dir, out_dir):
            self.source_dir = source_dir
            self.out_dir = out_dir

    def manipulate_files(self, listOfFilenames):
        print("manipulate files...")
        for i, (txtFilename, jpgFilename) in enumerate(listOfFilenames):
            bboxList = self.reader.get_bbox_list(txtFilename)
            bboxListSplited = self.splitBboxList(bboxList)
            imgSplited = self.splitImg(jpgFilename)
            #self.writer.write_rotate_bbox_list(txt_filename, bbox_list_rotated)
            #self.writer.write_img_rotated(jpg_filename, img_rotated)
        print("Edited files:",2 * (i + 1), "| txt_files:",i + 1, "| jpg_files:",i + 1)

    def splitBboxList(self, bboxList):
        pass

    def splitImg(self, imgFilename):
        img = cv2.imread(imgFilename)
        for i in range(1,2):
            img1 = img[i*512:i*1024, 0:512]
            cv2.imshow("test", img1)
            cv2.waitKey(0)
        return img


    def start(self):
        self.reader = Reader(source_dir=self.source_dir)
        list_of_filenames = self.reader.get_list_of_filenames()
        self.manipulate_files(list_of_filenames)