#!/bin/bash

sudo docker build . -t flask
sudo docker run -d -p 5000:5000 flask