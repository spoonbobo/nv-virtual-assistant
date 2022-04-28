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
sudo apt-get install python3-flask libsndfile1 libsndfile1-dev numpy==1.18 soundfile librosa pydub
```

Also, grpc is needed for your the frontend to communicate with Riva AI Service, install Riva API that is included in the Riva Quick Start.

```
cd your/path/to/riva_quickstart_v1.10.0-beta
pip install riva_api-1.10.0b0-py3-none-any.whl
````

After installing these required packages, go to *webapp-flask* sample application foldera and run the application. Enjoy!
```
cd webapp-flask
flask run
```
