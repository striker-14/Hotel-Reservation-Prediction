pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "project-02a04589-8e80-4642-a89"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }
    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo'Cloning Github repo to Jenkins.........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/striker-14/Hotel-Reservation-Prediction.git']])
                }
            }
        }

        stage('Setting up our Virtual Environmet and Installing dependencies'){
            steps{
                script{
                    echo'Setting up our Virtual Environmet and Installing dependencies.........'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

         stage('Building and Pushing Docker Image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key' , variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker Image to GCR.........'
                        sh '''set -x
                        export PATH=$PATH:${GCLOUD_PATH}
                        export CLOUDSDK_PYTHON_SITEPACKAGES=1
                        export GODEBUG=netdns=go
                        export PYTHONUNBUFFERED=1
                       
                        whoami
                        echo "HOME=$HOME"
                        echo "WORKSPACE=$WORKSPACE"
                        echo "GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS"
                       
                        ls -l "$GOOGLE_APPLICATION_CREDENTIALS"
                       
                        gcloud info
                        gcloud auth list
                       
                        gcloud auth activate-service-account --key-file="$GOOGLE_APPLICATION_CREDENTIALS"
                       
                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker images

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }
    }
}