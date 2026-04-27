pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Repository cloned successfully.'
            }
        }
        
        stage('SonarQube Security Scan') {
            steps {
                echo 'Initializing SonarScanner...'
                sh '''
                # Check if the AI has applied the parameterized query fix (?)
                if grep -q "WHERE username = ?" user_auth.py; then
                    echo "[INFO] Analyzing user_auth.py..."
                    echo "[INFO] Sensor Python Sensor [python]"
                    echo "[INFO] 1 source file to be analyzed"
                    echo "[INFO] 0 Critical Vulnerabilities found."
                    echo "[INFO] ------------------------------------------------------------------------"
                    echo "[INFO] EXECUTION SUCCESS"
                    echo "[INFO] ------------------------------------------------------------------------"
                    echo "[INFO] QUALITY GATE STATUS: PASSED"
                    exit 0
                else
                    echo "[INFO] Analyzing user_auth.py..."
                    echo "[INFO] Sensor Python Sensor [python]"
                    echo "[INFO] 1 source file to be analyzed"
                    echo "[ERROR] Vulnerability found: Formatted SQL queries are vulnerable to injection (python:S3649)"
                    echo "[ERROR] user_auth.py: Line 9 - 'Make sure that formatting this SQL query is safe here.'"
                    echo "[INFO] ------------------------------------------------------------------------"
                    echo "[INFO] EXECUTION FAILURE"
                    echo "[INFO] ------------------------------------------------------------------------"
                    echo "[ERROR] QUALITY GATE STATUS: FAILED"
                    exit 1
                fi
                '''
            }
        }
        
        stage('Deploy to Production') {
            steps {
                echo 'Security clearance granted. Deploying...'
            }
        }
    }
}
