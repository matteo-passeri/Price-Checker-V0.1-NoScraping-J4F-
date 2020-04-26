import cleanFile1AndPutToFile2
import imageToTextToFile
import makeScreenshot
import temporaryCheck


def look_at_link(url):
    makeScreenshot.make_screenshot(url)
    imageToTextToFile.image_to_text_to_file()
    cleanFile1AndPutToFile2.clean_file1_and_put_to_file2()
    #temporaryCheck.temporary_check()
