import cv2
import argparse
import os
import re
from operator import itemgetter

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='jpg', help="extension name. default is 'png'.")
# ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
args = vars(ap.parse_args())

# Arguments
dir_path = '/home/shijiaying/video/jpg'
ext = args['extension']

file_list=os.listdir(dir_path)
for name in file_list:
    output = dir_path+'/'+name
    images = []
    image_list=os.listdir(dir_path+'/'+name)
    image_list.sort()
    image_list_dict={}
    for f in image_list:
        keys = int(f.split('_')[-1].split(".")[0])
        values=f
        image_list_dict[keys]=values
        # if f.endswith(ext):
        items=image_list_dict.items()
        items.sort()
        images.append(f)
    images=[value for key,value in items]
    print (images)
# Determine the width and height from the first image
    image_path = os.path.join(dir_path+'/'+name, images[0])
    frame = cv2.imread(image_path)
    print (image_path)
    height, width, channels = frame.shape

# Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case out = cv2.VideoWriter(output+name, fourcc, 20.0, (width, height))
    out = cv2.VideoWriter(output+'/'+name+'.m4v', fourcc, 30.0, (width, height))
    for image in images:

        image_path = os.path.join(dir_path+'/'+name, image)
        frame = cv2.imread(image_path)

        out.write(frame) # Write out frame to video

#        cv2.imshow('video',frame)
#        if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
#            break

# Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()

    print("The output video is {}".format(output+'/'+name+'.m4v'))


#tk-img2video -ext png -o output.mp4


# import cv2
# import os

# image_folder = '/home/shijiaying/video/output/IMG_1100'
# video_name = 'video.mp4'


# images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# #print (images)
# frame = cv2.imread(os.path.join(image_folder, images[0]))
# height, width, layers = frame.shape

# video = cv2.VideoWriter(video_name, -1, 1, (width,height))

# for image in images:
   # video.write(cv2.imread(os.path.join(image_folder, image)))

# cv2.destroyAllWindows()
# video.release()
