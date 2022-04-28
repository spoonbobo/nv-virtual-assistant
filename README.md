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
pip install numpy==1.18 soundfile librosa pydub
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

The original responses to queries are specified to NVIDIA DGX systems. To modify the responses to accommodate your virtual assistant, please change the conditional statements in <code>webapp-flask/dgx_resp.py</code> like this

```
if query == intent: return [message]
```

Similarly, the initial message from this sample application can be changed at <code>webapp-flask/app.py</code>. The sample application uses a List object to represent paragraphs of responses like this

```
["Sentence1", "Sentence2", "", ...]
```

If you pass in an empty string, the application will treat it as a break rendered on the template.

## Feedback
Feel free to try out the setup and post the issues you meet when setting up the AI virtual assistant here.

## Documentation
Please find the [documentation](https://nvsa-virtualassistant.readthedocs.io/en/latest/) for this project.

## Ongoing work
* Streaming ASR implementation
