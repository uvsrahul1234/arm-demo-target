pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Repository cloned successfully.'
            }
        }
        
        stage('Security & Regression Testing (Pytest)') {
            steps {
                echo 'Running automated test suite...'
                sh '''
                pip install pytest
                pytest test_math_utils.py -v
                '''
            }
        }
        
        stage('Deploy to Production') {
            steps {
                echo 'Vulnerability check passed. Deploying...'
            }
        }
    }
}
