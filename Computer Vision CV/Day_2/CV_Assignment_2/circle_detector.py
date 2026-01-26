import cv2
import numpy as np
import matplotlib . pyplot as plt
from sys import argv
from PIL import Image

def preprocess_image (image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error    : Unable to load image .")
        return None , None
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray , (5 , 5) , 0)
    return img , gray

def detect_circles (gray_image ,dp =1, minDist =50 , param1 =50 ,
param2 =30 , minRadius =10 , maxRadius =100) :
 
  circles = cv2.HoughCircles(gray_image,cv2.HOUGH_GRADIENT,dp,minDist=minDist,param1=param1,param2=param2,minRadius=minRadius,maxRadius=maxRadius)
  return circles

def visualize_circles (image , circles , save_path = "Circles.png" ):
  if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
      cx,cy,radius = i
      cv2.circle(image,(cx,cy),radius,(0,255,0),2)
      cv2.circle(image,(cx,cy),2,(0,0,255),3)
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    PIL_img = Image.fromarray(rgb_img)
    PIL_img.save(save_path)

def calculate_statistics ( circles ):
    state_dict = {}
    state_dict['Number_of_Circles'] = len(circles[0]) if circles is not None else 0
    if circles is not None:
        radii = circles[0][:,2]
        state_dict['Average_Radius'] = np.mean(radii)
        state_dict['Min_Radius'] = np.min(radii)
        state_dict['Max_Radius'] = np.max(radii)
        state_dict['Circles'] = []
        for circle in circles[0]:
           state_dict['Circles'].append({'Center_X': int(circle[0]), 'Center_Y': int(circle[1]), 'Radius': int(circle[2])})
    else:
       state_dict['Average_Radius'] = 0
       state_dict['Min_Radius'] = 0
       state_dict['Max_Radius'] = 0
       state_dict['Circles'] = []
    return state_dict

def main ():
    if len(argv) <3:
       print(f"Usage : {argv[0]} <image_path> <output_path>")
       return
    image_path = argv[1]
    img,gray = preprocess_image(image_path)
    image_height = gray.shape[0]
    required_min_dist = int(image_height / 6)//4
    strictness_level = 55
    expected_min_radius = 10
    expected_max_radius = 150
    circles = detect_circles(gray, 
                             minDist=required_min_dist,
                             param2=strictness_level, 
                             minRadius=expected_min_radius,
                             maxRadius=expected_max_radius)
    if img is None or gray is None:
       return
    visualize_circles(img,circles,argv[2])
    stats = calculate_statistics(circles)
    print("Circle Detection Statistics :")
    print(f"Number of Circles Detected : {stats['Number_of_Circles']}")
    print(f"Average Radius : {stats['Average_Radius']:.2f}")
    print(f"Minimum Radius : {stats['Min_Radius']}")
    print(f"Maximum Radius : {stats['Max_Radius']}")
    for idx, circle in enumerate(stats["Circles"]):
        print(f"Circle {idx + 1} : Center = ({circle['Center_X']}, {circle['Center_Y']}), Radius = {circle['Radius']}")

if __name__ == "__main__":
 main ()