############################################
#
#         Ultimate Image Compressor 
#
#                    by
#
#               Pancho Morlé
#
############################################
# packages
import cv2
import os

directory = r"D:\full\path\to\your\folder"
new_dir = r"D:\documents\brand_new_folder" #imagine a directory for ur new images
os.mkdir(new_dir) #-----------------------> actually create that directory

for file in os.listdir(directory): #list the names of all the files in the folder
    origin_image = os.path.join(directory, file) #create a path to a specific image
    
    #----------Now, the good stuff. --------------#
    #1) open image file with "Open Computer Vision" package
    image = cv2.imread(origin_image, cv2.IMREAD_UNCHANGED)
    
    #2) convert image to grayscale ----------------
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #3) convert image to black and white
    thresh, image_black = cv2.threshold(image_grayscale, 170, 255, cv2.THRESH_BINARY)
    
    #4) halve the size of the image
    small = cv2.resize(image_black, (0,0), fx=0.5, fy=0.5)

    #5) save new image
    new_name = file[:-3]+"png"  #slice whatever extension it had. Add png extension.
    cv2.imwrite(os.path.join(new_dir, new_name), small)

    # break out on a key press
    cv2.waitKey(0)

#-----------------------------------------------------------------------------------