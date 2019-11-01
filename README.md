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
If you want to deploy the application using Docker then use the below method;

Install docker

    git clone https://www.github.com/eoghanwinters/Individual-Project
cd into the "Individual-Project" folder

    docker build . -t flask
    docker run -d -p 5000:5000 flask
open the external IP given on the GCP console page followed by ":5000"   

## SystemD Deployment
If you want to deploy the application using SystemD then use the below method;

    git clone https://www.github.com/eoghanwinters/Individual-Project
cd into the "Individual-Project" folder
    
    sudo cp flask-app.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl stop flask-app
    install_dir=/opt/flask-app
    sudo rm -rf ${install_dir}
    sudo mkdir ${install_dir}
    sudo cp -r ./* ${install_dir}
    sudo chown -R pythonadm:pythonadm ${install_dir}
    sudo su - pythonadm
    cd ${install_dir}
    virtualenv -p python3 venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    sudo systemctl start flask-app
open the external IP given on the GCP console page followed by ":5000"   
