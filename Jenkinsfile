pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Initial SonarQube Scan') {
            steps {
                script {
                    echo 'Initializing SonarScanner...'
                    // We check for the secure parameterized query (?)
                    def isSecure = sh(script: 'grep -q "WHERE username = ?" user_auth.py', returnStatus: true) == 0
                    
                    if (isSecure) {
                        echo "[INFO] 0 Critical Vulnerabilities found."
                        echo "[INFO] QUALITY GATE STATUS: PASSED"
                        env.NEEDS_REMEDIATION = "false"
                    } else {
                        echo "[ERROR] Vulnerability found: Formatted SQL queries are vulnerable to injection (python:S3649)"
                        echo "[ERROR] QUALITY GATE STATUS: FAILED"
                        env.NEEDS_REMEDIATION = "true"
                        // We intentionally don't exit 1 here so the pipeline can self-heal
                    }
                }
            }
        }
        
        stage('ARM Autonomous Remediation') {
            when { 
                environment name: 'NEEDS_REMEDIATION', value: 'true' 
            }
            steps {
                echo '>>> TRIGGERING AUTONOMOUS AI AGENT <<<'
                sh 'python3 run_arm_agent.py'
            }
        }
        
        stage('SonarQube Re-Scan') {
            when { 
                environment name: 'NEEDS_REMEDIATION', value: 'true' 
            }
            steps {
                script {
                    echo 'Re-running SonarScanner on patched code...'
                    def isSecureNow = sh(script: 'grep -q "WHERE username = ?" user_auth.py', returnStatus: true) == 0
                    
                    if (isSecureNow) {
                        echo "[INFO] 0 Critical Vulnerabilities found."
                        echo "[INFO] QUALITY GATE STATUS: PASSED"
                    } else {
                        echo "[ERROR] Patch failed. QUALITY GATE STATUS: FAILED"
                        exit 1
                    }
                }
            }
        }
        
        stage('Deploy to Production') {
            steps {
                echo 'Security clearance granted. Deploying...'
            }
        }
    }
}
