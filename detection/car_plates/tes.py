import cv2
import sys

# sys.path.insert(1, '/detection/car_plates')
import CarPlates

img  = cv2.imread('detection/car_plates/LicPlateImages/2.png')
print(CarPlates.SCALAR_BLACK)
# print(CarPlates.car_plate_detection(img))
