# Satellite Imagery Segmentation with FastSAM

## Description:
Satellite Imagery Segmentation with FastSAM is a powerful application that leverages the **Fast Segment Anything Model (FastSAM)** to efficiently and accurately segment objects and regions of interest in satellite images. This app provides a user-friendly interface for users to upload and process satellite images, making it accessible to a wide range of users, including researchers, environmentalists, and urban planners.


## Model:
**FastSAM (Fast Segment Anything Model)** is a state-of-the-art convolutional neural network (CNN)-based model designed for the Segment Anything task. It offers exceptional speed and competitive performance in image segmentation, object detection, and image editing tasks. FastSAM is the heart of this application, ensuring rapid and precise satellite image segmentation.

## Use Cases:

+ **Environmental Analysis**: Quickly identify and analyze changes in vegetation, land use, or water bodies over time.
+ **Urban Planning**: Assess urban sprawl, traffic patterns, and infrastructure development.
+ **Agriculture**: Monitor crop health and optimize resource allocation.
+ **Disaster Response**: Identify affected areas after natural disasters and plan rescue and relief efforts.
+ **Wildlife Conservation**: Track and protect wildlife habitats and migration patterns.

## Limitations:

+ **Data Quality**: The accuracy of the segmentation results heavily depends on the quality of the input satellite imagery.
+ **Cloud Cover**: Cloud cover in satellite images can affect the accuracy of segmentation.
+ **Resolution**: Lower-resolution images may lead to less precise segmentation results.
+ **Processing Time**: Extremely large images may require significant processing time.

## Ethics:

+ **Privacy**: Respect privacy by avoiding the use of high-resolution satellite images for intrusive purposes.
+ **Bias**: Ensure that the segmentation model does not introduce bias in its predictions, particularly in sensitive areas like urban planning and environmental analysis.
+ **Transparency**: Clearly communicate the limitations and potential errors of the model to users.

## Acknowledgment:
This project relies on the FastSAM model, and credit goes to the original authors and developers of the model.

## Usage : 

```
pip install -r requirements.txt
python app.py
```
+ You can check The Demo from here: **https://huggingface.co/spaces/ayoubkirouane/Fast-SAM-Satellite-Imagery-Segmentation**


![Screenshot at 2023-09-27 11-05-44](https://github.com/Kirouane-Ayoub/Satellite-Imagery-Segmentation-with-Fast-SAM/assets/99510125/bd609912-3852-42e7-bfab-43587f69954f)
