pipeline{
    agent any
    environment {
        VENV_NAME = 'venv'
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

        stage('Stage 2: Check Python Installation') {
            steps {
                script {
                    echo "Checking Python installation..."
                    sh """
                        echo "Available Python versions:"
                        ls -la /usr/bin/python* || echo "No python in /usr/bin/"
                        which python3 || echo "python3 not found"
                        which python || echo "python not found"
                        python3 --version || echo "python3 version check failed"
                    """
                }
            }
        }

        stage('Stage 3: Setup Python Environment') {
            steps {
                script {
                    echo "Setting up Python environment..."
                    sh """
                    python3 -m venv ${VENV_NAME}
                    . ${VENV_NAME}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    """
                }
            }
        }

        stage('Stage 4: Run Data Ingestion') {
            steps {
                script {
                    echo "Running data ingestion..."
                    sh """
                    . ${VENV_NAME}/bin/activate
                    python -m src.data_ingestion
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed."
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs for details."
        }
    }
}   
