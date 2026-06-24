pipeline {
    agent any
    environment {
        PODMAN_IMAGE = 'egp-asset-portal'
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
        stage('podman Stack Build') {
            steps {
                echo 'Building Production Container Image...'
                sh "podman build -t ${DOCKER_IMAGE}:latest ."
            }
        }
        stage('Local Cluster Deploy') {
            steps {
                echo 'Refreshing App Deployment on Port 8085...'
                script {
                    sh 'podman stop egp-portal-runtime || true'
                    sh 'podman rm egp-portal-runtime || true'
                }
                sh "podman run -d --name egp-portal-runtime -p ${PORT}:80 ${DOCKER_IMAGE}:latest"
            }
        }
    }
}
