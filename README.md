# My Workout App
**Follow the below instructions to run the application through the GCP instance;**

**1. Create a GCP instance and enter the following commands;**

    cd
    sudo apt-get update
    sudo apt-get install -y python3-pip
    sudo apt-get install -y python-pip
    cd /home/eoghanwinters1/Individual-Project/application     
    cd ..  
    pip install -r requirements.txt
    export FLASK_APP=run.py FLASK_ENV=production FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000 FLASK_RUN_CERT=cert.pem FLASK_RUN_KEY=key.pem  
    python -m flask run
    
**2. Open the external IP given on the VM instances page followed by ":5000"**
