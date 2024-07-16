# Face Detection Application using Custom Cascade Classifier Algorithm using OpenCV

## Introduction

Face detection is categorized in object detection applications. For OpenCV, face detection has two main algorithms which are both regarded boosted cascade of weak classifiers or cascade classifiers for short. The main algorithms include: [LBP (Local Binary Pattern)](https://en.wikipedia.org/wiki/Local_binary_patterns) and [Haar Cascade Classifier](https://en.wikipedia.org/wiki/Haar-like_feature). Both have their strengths and weaknesses and the table below shows them.
|Features|LBP|Haar Features|
|--------|---|-------------|
|Output format|Integers|Floating points|
|Speed|Fast|Slow|
|Accuracy|Less accurate than Haar features|More accurate than LBP|
|Training time|Fast|Slow|

I will be sticking to the Haar Cascade Classifier for this project due to its accuracy. OpenCV already supplies users with their own Haar Cascade Classifier but we will be making a custom one from scratch.

## Theory

Quoting [OpenCV's page](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) on the theory behind Haar feature-based cascade classifiers:
> Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

I have gathered the positive and negative images required to train the cascade classifier from the internet and the positive images were a total of 100.

The video below describes the theory behind the Haar feature-based cascade classifiers (Viola Jones Algorithm):

<div>
  <iframe width="1519" height="561" src="https://www.youtube.com/embed/uEJ71VlUmMQ" 
    title="Detecting Faces (Viola Jones Algorithm) - Computerphile" frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
  </iframe>
</div>

## Training

Training is split into two datasets: positive and negative pictures. Positive pictures are the ones that we want to train the data on (faces) and negative pictures are the ones we want to avoid. For negative pictures, we just need to loop through `neg.txt` which was generated by the `generate_negative_files()` function inside `functions.py`. For the positive pictures on the other hand, annotations are needed and luckily the work of days has been made easy by an OpenCV console application. Training on positive images is demonstrated below:

<video src="training.mp4" width="320" height="240" controls></video>

## Result

## Usage

## Resources

- [Great video on custom training](https://www.youtube.com/watch?v=XrCAvs9AePM&t=620s)
- [OpenCV cascade classifier training documentation](https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html)
- [Positive images dataset](https://huggingface.co/datasets/HengJi/human_faces)
- [Negative images dataset](https://github.com/JoakimSoderberg/haarcascade-negatives)
