# Image Classification with TensorFlow and Flask

This project involves training a deep learning model using TensorFlow to classify images into two categories: "happy" and "sad". A Flask server is provided to serve the model, allowing for easy testing of the model through a simple HTML interface.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Flask Server](#flask-server)
- [Testing the Model](#testing-the-model)

## Prerequisites

- TensorFlow
- OpenCV
- Matplotlib
- Flask (if you want to run the server)

## Installation

To install the required libraries, run:

```bash
pip install tensorflow opencv-python matplotlib flask
```

## Data Preprocessing

The data preprocessing step involves:

- Loading image data from the `data` directory.
- Checking for valid image extensions: jpg, jpeg, png, bmp.
- Scaling the image data for the neural network.
- Splitting the data into training, validation, and test sets.

## Model Training

A sequential deep learning model is built using TensorFlow. The model is trained on the preprocessed data. After training, the performance of the model can be visualized using metrics like loss and validation loss.

## Flask Server

In your terminal just run `app.py` to start the flask server

## Testing the Model

Before passing an image to the neural network for prediction:

- Ensure the image is 256 pixels high and 256 pixels wide.
- Ensure the image has 3 channels.

The prediction will classify the image as either "Happy image" or "Sad image".
