import cv2
import os
import PyPDF2
import PythonMagick


input_path = '/home/shijiaying/video/result'
output_path = '/home/shijiaying/video/png'

input_dir = os.listdir(input_path)

for name in input_dir:
    print (name)
    os.mkdir(output_path + '/' + name)
    for f in os.listdir(input_path+'/'+name):
        print(f)
        try:
            pdf = input_path+'/'+name+'/'+f
            p = PythonMagick.Image()
            p.verbose()
            p.density('250')
            # p.trim()
            p.read(pdf)
            p.quality(70)
            p.resize('60%')
            # p.resize(str(p.rows()))
            p.magick('png')
            # p.flatten()
            p.sharpen(0*1.0)
            p.write(output_path+'/'+name+'/'+f+'.png')
        except Exception as e:
            print(e)
