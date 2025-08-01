pipeline{
    agent any
    
    stages {
        stage('Stage 1: Clone Repository') {
            steps {
                echo "Cloning the repository..."
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'MLOps-01', url: 'https://github.com/davanntet/Jenkins-Test.git']])
            }
        }
    }
}