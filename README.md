# My Workout App
## Intro
The app has originally been developed on an Ubuntu Distritibution and primarily developed for deployment on GCP.

## Pre-Requisites

    sudo apt-get update
    sudo apt-get install -y python3
    sudo apt-get install -y python3-pip
    sudo apt-get install -y virtualenv
    sudo apt-get install -y git
    
## Running the App
Clone the repo using;

    git clone https://www.github.com/eoghanwinters/Individual-Project
cd into the "Individual-Project" folder
    
    virtualenv -p python3 venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 run.py
open the external IP given on the GCP console page followed by ":5000"

## Docker
If you are wanting to deploy the application using Docker then user the below method;

Install docker

    git clone https://www.github.com/eoghanwinters/Individual-Project
cd into the "Individual-Project" folder

    docker build . -t flask
    docker run -d -p 5000:5000 flask
open the external IP given on the GCP console page followed by ":5000"   
