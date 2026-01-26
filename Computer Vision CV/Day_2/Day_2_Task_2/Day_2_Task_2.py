import cv2
import numpy as np
from sys import argv, exit

def main():
    argc = len(argv)
    if argc!=3:
        print(f"Usage: python3 {argv[0]} filepath")
        exit()
    
    img = cv2.imread(argv[1])

    orb = cv2.ORB_create(nfeatures =500)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    keypoints, descriptors = orb.detectAndCompute(gray,None)

    result = cv2.drawKeypoints(img,keypoints,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    image2 = cv2.imread(argv[2])
    gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2,None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches = bf.match(descriptors,descriptors2)

    matches = sorted(matches,key=lambda x:x.distance)

    match_img = cv2.drawMatches(img,keypoints,image2,keypoints2,matches[:50],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    print("Number of good matches:",len(matches))

    cv2.imshow("Matches",match_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()