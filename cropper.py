import cv2
import os

download_directory = '/Users/guja/Downloads' # Specify download file path
upload_directory = '/Users/guja/Downloads' # Specifiy upload file path

counter = 1

for filename in os.listdir(download_directory):
    f = os.path.join(download_directory, filename)

    if (f.lower().endswith('.png')): # Change .png to other image format if applicable
        img = cv2.imread(f, cv2.IMREAD_COLOR)
        cropped_img = img[491:1246, 85: 1094]

        name = 'example' + str(counter) + '.jpg'
        cv2.imwrite(os.path.join(upload_directory, name), cropped_img)

        counter += 1

cv2.destroyAllWindows()