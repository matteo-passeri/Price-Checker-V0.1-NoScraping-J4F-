import imageToTextToFile
import makeScreenshot
import googleCleanFile1AndPutToFile2
import temporaryCheck


def look_on_google(url='http://www.google.com', query="gibson+les+paul"):
    makeScreenshot.make_screenshot(url, query, google=True)
    imageToTextToFile.image_to_text_to_file()
    googleCleanFile1AndPutToFile2.google_clean_file1_and_put_to_file2()
    #temporaryCheck.temporary_check()
