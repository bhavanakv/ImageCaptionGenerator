# ImageCaptionGenerator
Deep learning models to generate captions for the images

This project is an analysis of image captioning task specifically for scenic images. 

The deep learning models are trained using two datasets: 
1. Flickr8K
2. IAPRTC12

Dataset 1 is used as is. In dataset 2, only scenic images are manually picked. The captions in this datasets are present as XML files. The captions for these images are first selected using Dataset2CaptionSelector.py script. These selected caption files are parsed to fetch captions from DESCRIPTION tag. The captions extracted are written into a file. This is done through ScenicDataCreation.py script. The captions from both the files are cleaned and a dictionary containing image name and list of captions is created which will be used for analysis.

Two deep learning models are implemented in this analysis:
1. Convolutional Neural Network coupled with Long Short-Term Memory
2. Fine-tuned transformer model - BLIP

The performance of these models are evaluated through a metric called BLEU score.

This analysis is performed in ImageCaptionGenerator.ipynb notebook. To run this analysis, the image datasets and caption files need to be loaded on to colab through Google Drive. Once loaded, the analysis can be run.

