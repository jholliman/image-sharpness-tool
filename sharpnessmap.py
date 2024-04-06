import cv2
import numpy as np
import os


class SharpnessMap:
    def __init__ (self, image_path, window_size, step_size):
        self.image_path = image_path
        self.window_size = window_size
        self.step_size = step_size
        self.create_sharpness_map()

    def create_sharpness_map(self):
        #read image 
        img = cv2.imread((self.image_path), cv2.IMREAD_UNCHANGED)

        print('raw image size: ', img.shape[0], img.shape[1])

        #compute the size of sharpness map
        height = img.shape[0]//self.window_size
        width = img.shape[1]//self.window_size

        print('making downsampled map with height ', height, ' and width ', width)
        
        #initialize sharpness map
        self.map = np.zeros((height, width), dtype=np.uint8)

        # Loop through the image using sliding window technique
        for y in range(0, img.shape[0] - self.window_size + 1, self.step_size):#for each row
            for x in range(0, img.shape[1] - self.window_size + 1, self.step_size): #for each column
                # Extract the current window
                window = img[y:y+self.window_size, x:x+self.window_size]

                # Calculate Laplacian variance as a measure of sharpness
                sharpness = cv2.Laplacian(window, cv2.CV_64F).var()

                #print('at point in raw image: ', y, x)
                #print('at point in sharpness map,',(y//step_size),(x//step_size))

                #fill the sharpness map accordingly
                self.map[(y//self.step_size),(x//self.step_size)] = sharpness
                #print(sharpness)
        print("finished creating sharpness map")
            




    #######################################################################################################
    # Iterate through the image and create a downsampled sharpness map
    ######################################################################################################

    


    ################# if you want to export the individual sharpness map (debug only really)#####################
    #############################################################################################################

    #for fun you can change the color ramp from gray scale
    #sharpness_map_colorized = cv2.applyColorMap(sharpness_map, cv2.COLORMAP_COOL)

    #create name for image and add it to list of sharpness images
    #output_img_name = 'sharpness_map' + img_name
    #sharpness_map_list.append(output_img_name)

    # Save the image as a grayscale JPEG
    #cv2.imwrite(output_img_name, sharpness_map)


