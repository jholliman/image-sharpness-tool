import os
import cv2
import numpy as np
from sharpnessmap import SharpnessMap

window_size = 20
step_size = 20

# Specify the folder path containing raw imagery
folder_path = r"/home/joel/image-sharpness-tool/images/"

# List all files in the folder
file_list = os.listdir(folder_path)

# Filter files based on image extensions (you can customize this list)
image_extensions = ['.jpg', '.jpeg']
image_files = [file for file in file_list if any(file.lower().endswith(ext) for ext in image_extensions)]

#######################################################################################################
# create an array of downsampled sharpness maps, one map per raw image
#######################################################################################################

sharpness_map_list = []

for img_file in image_files:

    full_img_path = folder_path + img_file
    print("creating sharpness map from ", full_img_path)
    sharpness_map = SharpnessMap(full_img_path,window_size,step_size)
 

    #create name for image and add it to list of sharpness images
 
    sharpness_map_list.append(sharpness_map)

    ##### uncomment the rest of this loop to save the individual sharpness maps as a grayscale JPEG

    #for fun, change the colorramp
    #sharpness_map_colorized = cv2.applyColorMap(sharpness_map, cv2.COLORMAP_COOL)

    #output_image_name = 'sharpness_map' + img_file

    #cv2.imwrite(output_image_name, sharpness_map.map)

    ###############################################################################



#######################################################################################################
# Iterate through the sharpness maps and create a single average sharpness map
#######################################################################################################

#create an average sharpness map. 
#im being lazy here and manually defining the size (200,300)
#size should be the same as all of your sharpness maps, which is (height/window_size, width/window_size)
average_sharpness_map = np.zeros((200, 300), dtype=np.uint8)

for sharpness_map in sharpness_map_list:

    #read sharpness map
    map = sharpness_map.map

    #add up all sharpness values (apply coefficient for average)
    for y in range(0, map.shape[0]):#for each row
        for x in range(0, map.shape[1]): #for each column
            

            #average map equals the sum of all individual_map values, however we apply a 1/sample-size coefficient to make it an average
            average_sharpness_map[y,x] = average_sharpness_map[y,x] + (map[y,x] * (1/len(sharpness_map_list)))
    
equalized = cv2.equalizeHist(average_sharpness_map)

#for funnzies
average_sharpness_map_colorized = cv2.applyColorMap(equalized, cv2.COLORMAP_COOL)

print("exporting average sharpness map")
# Save the image as a grayscale JPEG
cv2.imwrite("average_sharpness_map_equalized.jpg", average_sharpness_map_colorized)
cv2.imwrite("average_sharpness_map.jpg", average_sharpness_map)
