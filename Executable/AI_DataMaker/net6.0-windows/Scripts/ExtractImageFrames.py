# Importing all necessary libraries
import sys
import cv2
from pathlib import Path


def extractFrames(videoPath, outPath, prefix, fileNumberingLength):
    path = Path(videoPath)
    # print(path.parent.absolute())

    if not path.exists:
        return

    # Read the video from specified path
    cam = cv2.VideoCapture(videoPath)

    try:
        # creating a folder named ExtractImageFrames
        if not Path.exists(outPath):
            outPath.mkdir(parents=True, exist_ok=True)

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    extractFramesFromVideoElement(cam, outPath, prefix, fileNumberingLength)


def extractFramesFromVideoElement(cam, outPath, prefix, fileNumberingLength):
    # frame
    currentframe = 0

    while(True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = str(outPath) + '/' + prefix + str(currentframe).rjust(fileNumberingLength, '0') + '.jpg'
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
        outputDir = Path(sys.argv[2])
        prefix = str(sys.argv[3])
        fileNumberingLength = int(sys.argv[4])
    except:
        inputFile = "D:\\StudyTime\\ProgrammingWorld\\CodeZone\\Development\\AI_ML\\Python\\Pressure Gauge Reader\\Data\\1 Training videos\data from videos\out2\\out2_train.mp4"
        outputDir = Path(sys.argv[0]).parent.joinpath('ExtractImageFrames')
        prefix = "frame"
        fileNumberingLength = 4

    extractFrames(inputFile, outputDir, prefix, fileNumberingLength)
