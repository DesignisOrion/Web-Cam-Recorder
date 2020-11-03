import numpy as np
import os  # If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module.
import cv2


filename = 'video.avi'  # this can be an .avi or .mp4 format
# this is the frames per second being recorded. Movies or films are usually 24 seconds
frames_per_second = 24.0
# we will start with 720p will lower the file size which is great.
res = '720p'

# Set resolution for the video capture
# Function adapted from https://kirr.co/0l6qmh


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


# Standard Video Dimensions Sizes in a dictionary
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    # set the default of 480p so that if a resolution isn't set then this one would works.
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:  # checks to see if the resolution we wanted is listed in the dictionairy STD_DIMENSIONS
        width, height = STD_DIMENSIONS[res]
    # change the current caputre device
    # to the resulting resolution
    change_res(cap, width, height)
    return width, height


# Video Encoding, might require additional installs so be sure to watch for that.

# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

# www.DesignIsOrion.com... I just like to make commments within my coding.


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename, get_video_type(
    filename), 25, get_dims(cap, res))


# This loop allows the cam to continue reading the frame and give output.

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
