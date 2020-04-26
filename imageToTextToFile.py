import cv2
import pytesseract
import os


def image_to_text_to_file():
    """imageToText"""
    img = cv2.imread('temp_screenshot.png')
    text = pytesseract.image_to_string(img)
    os.remove("temp_screenshot.png")
    """cleanTheText"""
    text = text.replace('\n\n\n', '\n').replace('\n\n', '\n').replace('\n \n', '\n')
    """textToFile"""
    with open("temp_file.txt", "w") as temp_file:
        temp_file.write(text)
