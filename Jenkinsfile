pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/AhmadMajde22/Colorectal-Cancer-Survaival-Prediction.git'
                    ]]
                ])
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    if (!fileExists("${env.VENV}")) {
                        bat "python -m venv ${env.VENV}"
                    }
                }
                bat "${env.VENV}\\Scripts\\activate && pip install --upgrade pip && pip install -r requirements.txt"
            }
        }

        stage('Lint') {
            steps {
                bat "${env.VENV}\\Scripts\\activate && pip install flake8 && flake8 src pipeline kubeflow_pipeline utils app.py application.py"
            }
        }

        stage('Run Tests') {
            steps {
                bat "${env.VENV}\\Scripts\\activate && pytest --maxfail=1 --disable-warnings"
            }
        }

        stage('Train Model') {
            steps {
                bat "${env.VENV}\\Scripts\\activate && python pipeline/training_pipeline.py"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t cancer-survival-app ."
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'artifacts/**', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
