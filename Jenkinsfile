pipeline{
        agent any
        stages{ 
		    stage('---Build_Image---'){
                        steps{
                            sh "sudo docker build -t flask-app ."
                        }
                }
                stage('---clean---'){
                        steps{
                              sh label: '', script:
				      
				      '''if [ "$(sudo docker ps -qa)" ]; then
        						sudo docker rm -f flask-app
				      fi'''
                        }
                }
		stage('---run---'){
			steps{
			sh "sudo docker run -d --name flask-app -p 5000:5000 flask-app"
			}
		}
        }
}
