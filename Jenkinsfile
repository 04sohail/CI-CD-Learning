pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=.
                pytest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ CI pipeline succeeded'
        }
        failure {
            echo '❌ CI pipeline failed'
        }
    }
}
