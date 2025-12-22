import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

def main():
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: python3 {argv[0]} picture_address.")
        sys.exit()

    filepath = sys.argv[1]
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    intensity_list = []
    for i in gray:
        for j in i:
            intensity_list.append(j)

    np_intensity = np.array(intensity_list)
    mean = np.mean(np_intensity)
    median = np.median(np_intensity)
    stdev = np.std(np_intensity)

    print(f"Mean: {mean}\nMedian:{median}\nStdev:{stdev}")

    fig,axes = plt.subplots(1,2)

    axes[0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    
    axes[1].hist(intensity_list)
    axes[1].set_title("Grayscale Intensity Histogram")
    axes[1].set_xlabel("Pixel Intensity")
    axes[1].set_ylabel("Frequency")
    plt.show()

main()