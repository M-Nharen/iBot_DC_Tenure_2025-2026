#!/usr/bin/env bash

echo "Installing dependencies for SKETCHER PRO..."

python3 -m ensurepip --upgrade

python3 -m pip install --upgrade pip

python3 -m pip install \
    opencv-python \
    numpy \
    customtkinter \
    Pillow

echo "All dependencies installed successfully!"
echo "Run the app using:"
echo "python3 main.py"
