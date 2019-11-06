# My Workout App
## Intro
The app has originally been developed on an Ubuntu Distritibution and primarily developed for deployment on GCP.

## Pre-Requisites
Run the following command;

    sudo apt-get install git -y
Run the following script to install all required Pre-Requisites;
    
    ./pre-requisites.sh
    
## Running the App
Clone the repo using;

    git clone https://www.github.com/eoghanwinters/Individual-Project
cd into the "Individual-Project" folder and run the following script;
    
    ./app-run.sh
Open the external IP given on the GCP console page followed by ":5000"

## Docker
### If you want to deploy the application using Docker then use the below method;

Install docker;

    curl https://get.docker.com | sudo bash  
Clone the repo using;

    git clone https://www.github.com/eoghanwinters/Individual-Project
cd into the "Individual-Project" folder and run the following script;

    ./docker-run.sh
open the external IP given on the GCP console page followed by ":5000"   

## SystemD Deployment
### If you want to deploy the application using SystemD then use the below method;
Clone the repo using;

    git clone https://www.github.com/eoghanwinters/Individual-Project
cd into the "Individual-Project" folder and run the following script;
    
    ./systemD-run.sh
open the external IP given on the GCP console page followed by ":5000"   
