# from PIL import Image
# import glob
# image_list = []
# for filename in glob.glob('/Users/yazeed/Desktop/','*.png','*.jpg'): #assuming gif
#     print(filename)
#     im=Image.open(filename)
#     image_list.append(im)
from os.path import join
from glob import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import psutil
import math
import os


files = []
fileLocation = input('drag an drop the directory for compressing files: ').strip()
# fileLocation = '/Users/yazeed/Desktop/'
fileLocation += '/'
for ext in ('*.gif', '*.png', '*.jpg'):
   files.extend(glob(join(fileLocation, ext)))

if not os.path.exists(fileLocation+'compressed'):
    os.makedirs(fileLocation+'compressed')
for filename in files:
    # img=mpimg.imread(filename)

    # plt.imshow(img)
    img = Image.open(filename)
    img.show() 
    width, height = img.size
    print('width = '+ str(width), 'height = '+ str(height))
    size = int(input('compress by the factor of? '))
    width2, height2 = math.floor(width/size), math.floor(height/size)
    img = img.resize((width2,height2), Image.ANTIALIAS)
    locations = filename.split('/')
    name = locations[len(locations)-1]

    img.save(fileLocation+'compressed/'+name, quality=95)
    # img.close()
    # plt.show()
# files_grabbed is the list of pdf and cpp files