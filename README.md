
# FLight Fare Prediction 


![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) ![Python 3.10.4](https://img.shields.io/badge/Python-3.10.4-brightgreen.svg) ![Scikit-Learn](https://img.shields.io/badge/Library-ScikitLearn-orange.svg)


This repository consists of files required for end to end implementation and deployment of Machine Learning Flight Fare Prediction web application created with Flask and deployed on the Heroku platform.

## Table of Contents
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Technologies Used](#technologies-used)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
## Demo

App Link : - https://airline-ticket-fare-prediction.herokuapp.com/ 

![GIF](Resource/demo.gif)


## Overview

The Airline Flight Fare Prediction is a Flask web application to predict airline flight fares across the Indian cities. The dataset for the project is taken from Kaggle, and it is a time-stamped dataset so, while building the model, extensive pre-processing was done on the dataset especially on the date-time columns to finally come up with a ML model which could effectively predict airline fares across various Indian Cities. The dataset had many features which had to pre-processed and transformed into new parameters for a cleaner and simple web application layout to predict the fares.


## Installation

The code is written in Python 3.10.4. 
If you don't have Python installed, you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

```bash
  pip install -r requirements.txt
```
    
## Deployment on Heroku

Login or signup in order to create virtual app. You can either connect your github profile or download Heroku CLI to manually to deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

The next step would be to follow the instruction given in the [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)


## Directory Tree

```
├── static 
│   ├── css
├── template
│   ├── home.html
├── Procfile
├── README.md
├── app.py
├── flight_price.ipynb
├── flight_rf.pkl
├── requirements.txt
```
## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/PranavShendre/Flight-Fare-Prediction-using-ML/issues) here by including your search query and the expected result

