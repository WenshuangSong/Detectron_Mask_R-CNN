import cv2
import argparse
import os

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
args = vars(ap.parse_args())

# Arguments
dir_path = '/home/shijiaying/video/output/IMG_1090'
ext = args['extension']
output = args['output']

images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)
        print (images)
# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output+name, fourcc, 20.0, (width, height))

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)

    out.write(frame) # Write out frame to video

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))


#tk-img2video -ext png -o output.mp4


#import cv2
#import os

#image_folder = '/home/shijiaying/video/result'
#video_name = 'video.m4v'

#images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
#frame = cv2.imread(os.path.join(image_folder, images[0]))
#height, width, layers = frame.shape

#video = cv2.VideoWriter(video_name, -1, 1, (width,height))

#for image in images:
#    video.write(cv2.imread(os.path.join(image_folder, image)))

#cv2.destroyAllWindows()
#video.release()
