# Image to Pencil Sketch Converter

This is a Python script used to convert images in any format (supported by cv2's imread) to a pencil sketch either in color format or grayscale

## Overview:

This directory contains all the necessary steps to setup and run the pencil_sketch.py program

```
Directory  Structure

CV_Assignment_1/
├── output_sketches
|    ├── Color
|    |   ├── Distinct Edges.png
|    |   ├── Landscape.png
|    |   └── Portrait.png
|    ├── Gray
|    |   ├── Distinct Edges.png
|    |   ├── Landscape.png
|    |   └── Portrait.png 
├── test_images
|    ├── Distinct Edges.jpg
|    ├── Landscape.jpg
|    └── Portrait.jpeg
├── pencil_sketch.py
├── README.md
└── setup.sh
```

## Setup:

The program requires the following libraries:

```
1.opencv-python
2.numpy
3.customtkinter
4.tkinter
5.Pillow
```

In case your system doesn't have the above libraries the program cannot run hence run the following commands on the terminal

```
chmod +x setup.sh
./setup.sh
```

This downloads the above given libraries except tkinter if they do not exist

If tkinter is not downloaded on your computer run the following command:

```
sudo apt install python3-tk
```

## Usage:

To start the program run

```
python3 pencil_sketch.py
```

```
1. Enter the address of the image to be converted into the label box above and click on submit
2. Select the mode: Color or Grayscale
3. Adjust the kernel size using the slider given to the left of the screen
4. To save the image click on save which opens up a file dialog
5. Click the file destination and name the output file
```

## Testing:

3 test images and their outputs are provided. You can either use those or use your own

## License:

This project is released under the MIT License — see LICENSE for details.

## Author:

Developed by M Nharen
