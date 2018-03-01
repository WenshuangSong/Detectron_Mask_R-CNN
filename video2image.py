import os
import cv2

videos_src_path = '/home/shijiaying/video/video'
videos_save_path = '/home/shijiaying/video/videoresult'

videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith('mp4'), videos)

for each_video in videos:
    print each_video

    # get the name of each video, and make the directory to save frames
    each_video_name, _ = each_video.split('.')
    os.mkdir(videos_save_path + '/' + each_video_name)

    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'

    # get the full path of each video, which will open the video tp extract frames
    each_video_full_path = os.path.join(videos_src_path, each_video)

    cap = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True
    while(success):
        success, frame = cap.read()
        print 'Read a new frame: ', success
        cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_count, frame)
	if cv2.waitKey(10) == 27:
      	   break

        frame_count = frame_count + 1

    cap.release()



#import cv2
#vidcap = cv2.VideoCapture('Compton.mp4')
#success,image = vidcap.read()
#count = 0
#success = True
#while success:
#  success,image = vidcap.read()
#  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
#      break
#  count += 1
