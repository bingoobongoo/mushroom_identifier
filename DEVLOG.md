# Mushroom Identifier

This project aims to identify most popular species of european mushrooms based on an image. I want to start completely from scratch, so there is a number of challenges I need to face:

* Getting mushroom data.
* Creating a deep learning image classification model.
* Training a model and further tuning it.
* Create a friendly interface to display model's predictions

Those are the main goals, but there is also a lot of smaller problems on the way.

## Used libraries

I will be using numerous libraries such as:

* **TensorFlow**
* NumPy, Pandas, Matplotlib
* Beautiful Soup 4

## Progress documentation

Down below I will be updating this document with what I've managed to accomplish, further plans, ideas, encountered problems etc.

### 06.03.2024

I started working on this project and created a small plan of what I need to do next. I wrote the main idea of this project and its goals. Basically **it will tell the user what species of mushroom is on the image**. Eventually, **it's should also display basic information about the identified mushroom** (```edibility```, ```size```, ```season```, etc. ). Plan *minimum* is just to create deep learning model that will work relatively good. Plan *minimum+* is to also **create a nice UI** (maybe a web app) that will present model's predictions. Plan *minimum++* is to **create whole app** (frontend + backend) which will load photos of mushrooms and present model's predictions.

Next steps I need to take:

* Think of a way to aquire mushroom images that my model will train on. Specifically, either **create a web scraper** and automatize the whole process or **do it manually**.
* Learn more about training such models in TensorFlow and choose best approach.
* Learn about creating nice and simple UI (basically how to create HTML websites with CSS).

In the next few days, I will be focusing on ```creating my own dataset of mushroom images```. In the meantime, I also want to **create simple *.csv* file containg basic information about mushroom species** I will use in my DNN model.

### 07.03.2024

Added web-scraping functionality and wrote Python script resizing all images in data folder to uniform size.

### 08.03.2024

Yesterday and today I'm focusing on downloading mushroom images and making sure everything works as it should. Right now there aren't any problems with getting data. While new images are being downloaded, I still need to manually check every picture to see if it will be good enough for DNN model. That's pretty boring stuff, but also necessary if I want to have a working classification algorithm. From what I've seen so far, there should be about 80-90 images for every class, which is good for a start. Unfortunately, some classes will have much less images due to difficulty in aquiring those from the internet.

Next, when I have all classes manually cleaned up and checked, I will then resize them using python script, and finally I will have proper dataset to start working on image classification model. To sum up, next goals will be:

* Create Jupyter notebook in which I will be training the model.
* Think of what approach to use when creating that notebook, so that it will be `clean and communicative`.
* Do a research on `what model to use for this task` and also if it will be a good idea to utilize **transfer learning**.
