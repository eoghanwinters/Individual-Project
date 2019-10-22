# My Workout App
**Follow the below instructions to run the application through the GCP instance;**

**1. Create a GCP instance and enter the following commands;**

    sudo apt-get update
    sudo apt-get install python3-pip  
    sudo apt-get install python3-venv  
    git clone https://github.com/eoghanwinters/Individual-Project.git 
    cd ./IndividualProject/application  
    sudo mv -f venv ~/venv  
    python3 -m venv venv  
    . venv/bin/activate  
    cd ..  
    pip install flask  
    pip install pyopenssl  
    export FLASK_APP=run.py FLASK_ENV=production FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000 FLASK_RUN_CERT=cert.pem FLASK_RUN_KEY=key.pem  
    flask run
    
**2. Open the external IP given on the VM instances page followed by ":5000"**
