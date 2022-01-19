# Importing all necessary libraries
import sys
import cv2
from pathlib import Path


def extractFrames(videoPath, outPath):
    path = Path(videoPath)
    # print(path.parent.absolute())

    if not path.exists:
        return

    # Read the video from specified path
    cam = cv2.VideoCapture(videoPath)

    try:
        # creating a folder named ExtractImageFrames
        if not Path.exists(outPath):
            outPath.mkdir()

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    extractFramesFromVideoElement(cam, outPath)


def extractFramesFromVideoElement(cam, outPath):
    # frame
    currentframe = 0

    while(True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = str(outPath) + '/frame' + str(currentframe).rjust(4, '0') + '.jpg'
            print('Creating... ' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        inputFile = str(sys.argv[1])
        outputDir = Path(sys.argv[2]).joinpath('ExtractImageFrames')
    except:
        inputFile = "D:\\StudyTime\\ProgrammingWorld\\CodeZone\\Development\\AI_ML\\Python\\Pressure Gauge Reader\\Data\\1 Training videos\data from videos\out2\\out2_train.mp4"
        outputDir = Path(sys.argv[0]).parent.joinpath('ExtractImageFrames')

    extractFrames(inputFile, outputDir)
