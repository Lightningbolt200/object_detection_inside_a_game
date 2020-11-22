import cv2 as cv
import numpy as np
import os
import win32gui, win32ui, win32con


class window_capture():
    w=0
    h=0
    hwnd=None
    def __init__(self,window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        #self.hwnd = None
        
        if not self.hwnd:
            raise Exception("Window not found: {}".format(window_name))    
        self.w=1920
        self.h=1080
    def window_capture(self):
        
        #hwnd = win32gui.FindWindow(None, 'VALORANT')
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w,self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.w, self.h) , dcObj, (0,0), win32con.SRCCOPY)
        #dataBitMap.SaveBitmapFile(cDC, 'try.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray,dtype='uint8')
        img.shape=(self.h,self.w,4)
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img=img[...,:3]
        img = np.ascontiguousarray(img)
        
        return img



