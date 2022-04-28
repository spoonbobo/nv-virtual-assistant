# AI Virtual Assistant using NVIDIA SDKs

Build AI virtual Assistant with NVIDIA SDKs is powerful and easy. Let's get started!

## 1. Prerequisites

1. Clone the project directory to get the scripts for training and sample web application
```
git clone https://github.com/spoonbobo/nv-virtual-assistant.git
```
2. Set up the training and deployment environment in the [setup guide](https://nvsa-virtualassistant.readthedocs.io/en/latest/prereq.html).

## 2. Model preparation

Follow [training guide](https://nvsa-virtualassistant.readthedocs.io/en/latest/training.html) for model training. 

The scripts for training can be found in *scripts* in the project directory.

## 3. Deployment

To deploy the models you trained, follow [deployment guide](https://nvsa-virtualassistant.readthedocs.io/en/latest/deploy.html).

## 4. Webapp

When the deployment is finished, you are ready to use Riva AI service with the trained model. 

A sample web application *webapp-flask* is provided for you. To use it, firstly install necessary packages:

```
sudo apt-get install python3-flask libsndfile1 libsndfile1-dev 
pip numpy==1.18 soundfile librosa pydub
```

grpc is used for your the frontend to communicate with Riva AI Service, install grpc along with Riva API that is included in the Riva Quick Start directory.

```
pip install your/path/to/riva_quickstart_v1.10.0-beta/riva_api-1.10.0b0-py3-none-any.whl
```

After installing these required packages, go to *webapp-flask* sample application foldera and run the application. Enjoy!
```
cd webapp-flask
flask run
```

## Feedback
Feel free to try out the setup and post the issues you meet when setting up the AI virtual assistant here.

## Documentation
Please find the [documentation](https://nvsa-virtualassistant.readthedocs.io/en/latest/) for this project.

## Ongoing work
* Streaming ASR implementation
