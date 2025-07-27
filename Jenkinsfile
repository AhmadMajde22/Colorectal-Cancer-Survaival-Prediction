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
                        sh "python3 -m venv ${env.VENV}"
                    }
                }
                sh ". ${env.VENV}/bin/activate && pip install --upgrade pip && pip install -e ."
            }
        }

        stage('Lint') {
            steps {
                sh ". ${env.VENV}/bin/activate && pip install flake8 && flake8 src pipeline kubeflow_pipeline utils app.py application.py"
            }
        }

        stage('Run Tests') {
            steps {
                sh ". ${env.VENV}/bin/activate && pytest --maxfail=1 --disable-warnings"
            }
        }

        stage('Train Model') {
            steps {
                sh ". ${env.VENV}/bin/activate && python pipeline/training_pipeline.py"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t cancer-survival-app ."
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'artifacts/**', allowEmptyArchive: true
        }
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
