pipeline{
    agent any
    environment {
        VENV_NAME = 'venv'
        PYTHON_VERSION = '3.11.0'
    }
    stages {
        stage('Stage 1: Clone Repository') {
            steps {
                script {
                    echo "Cloning the repository..."
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'MLOps-01', url: 'https://github.com/davanntet/Jenkins-Test.git']])
                }
            }
        }

        stage('Stage 2: Setup Python Environment') {
            steps {
                script {
                    echo "Setting up Python environment..."
                    sh "python${PYTHON_VERSION} -m venv ${VENV_NAME}"
                    sh ". ${VENV_NAME}/bin/activate"
                    sh "pip install --upgrade pip"
                    sh "pip install -e ."
                }
            }
        }
    }

}   
