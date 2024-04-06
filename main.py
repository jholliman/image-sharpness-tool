import cv2
from sharpnessmap import SharpnessMap

window_size = 20
step_size = 20

#sharpness map list for averaging sharpness maps later on
sharpness_map_list = []

# Specify the folder path containing raw images
img_name = "00000000000000003282767005436477_1388358568413263_1388358568419705.jpg"
img_path = r"/home/joel/image-sharpness-tool/images/" + img_name

sharpness_map = SharpnessMap(img_path,window_size,step_size)


#create name for image and add it to list of sharpness images
output_img_name = 'sharpness_map' + img_name
#sharpness_map_list.append(output_img_name)

#Save the image as a grayscale JPEG
cv2.imwrite(output_img_name, sharpness_map.map)