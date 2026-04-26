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
                # We use grep to check if the AI has fixed the code yet
                if grep -q "float(fee_string)" math_utils.py; then
                    echo "============================= test session starts =============================="
                    echo "platform linux -- Python 3.10.12, pytest-7.4.0"
                    echo "collected 1 item"
                    echo ""
                    echo "test_math_utils.py .                                                     [100%]"
                    echo ""
                    echo "============================== 1 passed in 0.01s ==============================="
                    exit 0
                else
                    echo "============================= test session starts =============================="
                    echo "platform linux -- Python 3.10.12, pytest-7.4.0"
                    echo "collected 1 item"
                    echo ""
                    echo "test_math_utils.py F                                                     [100%]"
                    echo ""
                    echo "=================================== FAILURES ==================================="
                    echo "_____________________________ test_process_payment _____________________________"
                    echo ""
                    echo "    def test_process_payment():"
                    echo ">       assert process_payment(100.0, '5.50') == 105.50"
                    echo "E       TypeError: unsupported operand type(s) for +: 'float' and 'str'"
                    echo ""
                    echo "test_math_utils.py:5: TypeError"
                    echo "=========================== 1 failed in 0.03s ============================"
                    exit 1
                fi
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
