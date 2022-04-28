# AI Virtual Assistant using NVIDIA SDKs

Build AI virtual Assistant with NVIDIA SDKs is powerful and easy. Let's get started!

## 1. Prerequisites

1. Clone the project directory to get the scripts for training and sample web application
```
git clone https://github.com/spoonbobo/nv-virtual-assistant.git
```
2. Set up the training and deployment environment in the [setup guide](https://nvsa-virtualassistant.readthedocs.io/en/latest/prereq.html).

## 2. Text classification model training

Follow [training guide](https://nvsa-virtualassistant.readthedocs.io/en/latest/training.html) for model training. 

The scripts for training can be found in *scripts* in the project directory.

## 3. Deployment

To deploy the models you trained, follow [deployment guide](https://nvsa-virtualassistant.readthedocs.io/en/latest/deploy.html).

## 4. Webapp

When the deployment is finished, you are ready to use Riva AI service with the trained model. A sample web application *webapp-flask* is provided for you. To use it, firstly install necessary packages:

```
sudo apt-get install python3-flask libsndfile1 libsndfile1-dev numpy==1.18 soundfile pydub
```
