pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'egp-asset-portal'
        PORT = '8085'
        TARGET_USER = 'ag51137'
    }
    stages {
        stage('Workspace Integrity') {
            steps {
                echo 'Checking Repository Files...'
                sh 'ls -la'
            }
        }
        stage('Extract Target Metadata') {
            steps {
                echo "Running Python Extraction Engine for ${TARGET_USER}..."
                sh "python3 parse_user.py"
            }
        }
        stage('DOCKER Stack Build') {
            steps {
                echo 'Building Production Container Image...'
                sh "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }
        stage('Local Cluster Deploy') {
            steps {
                echo 'Refreshing App Deployment on Port 8085...'
                script {
                    sh 'docker stop egp-portal-runtime || true'
                    sh 'docker rm egp-portal-runtime || true'
                }
                sh "docker run -d --name egp-portal-runtime -p ${PORT}:80 ${DOCKER_IMAGE}:latest"
            }
        }
    }
}
