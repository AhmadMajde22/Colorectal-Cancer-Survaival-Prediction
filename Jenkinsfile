pipeline {
    agent any

    environment {
        VENV = "venv"
        DOCKER_IMAGE = "cancer-survival-app"
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
                    // Clean up existing virtual environment
                    sh "rm -rf ${env.VENV}"
                    sh "python3 -m venv ${env.VENV}"
                }
                sh """
                    . ${env.VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                """
            }
        }

        stage('Lint') {
            steps {
                script {
                    sh ". ${env.VENV}/bin/activate && pip install flake8"
                    
                    def lintCommand = ". ${env.VENV}/bin/activate && flake8"
                    def paths = []
                    
                    // Check which directories exist before linting
                    if (fileExists('src')) { paths.add('src') }
                    if (fileExists('pipeline')) { paths.add('pipeline') }
                    if (fileExists('kubeflow_pipeline')) { paths.add('kubeflow_pipeline') }
                    if (fileExists('utils')) { paths.add('utils') }
                    if (fileExists('app.py')) { paths.add('app.py') }
                    if (fileExists('application.py')) { paths.add('application.py') }
                    
                    if (paths.size() > 0) {
                        def lintStatus = sh(
                            script: "${lintCommand} ${paths.join(' ')}",
                            returnStatus: true
                        )
                        if (lintStatus != 0) {
                            echo "⚠️ Linting completed with issues. Review the warnings above."
                        } else {
                            echo "✅ Code passed linting."
                        }
                    } else {
                        echo "⚠️ No Python files found to lint."
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh ". ${env.VENV}/bin/activate && pip install pytest"
                    
                    if (fileExists('tests') || fileExists('test')) {
                        sh ". ${env.VENV}/bin/activate && pytest --maxfail=1 --disable-warnings -v"
                    } else {
                        echo "⚠️ No test directory found. Skipping tests."
                    }
                }
            }
        }

        stage('Train Model') {
            steps {
                script {
                    if (fileExists('pipeline/training_pipeline.py')) {
                        sh ". ${env.VENV}/bin/activate && python pipeline/training_pipeline.py"
                    } else {
                        echo "⚠️ Training pipeline not found at pipeline/training_pipeline.py"
                        error "Training pipeline file does not exist"
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    if (fileExists('Dockerfile')) {
                        sh "docker build -t ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
                        sh "docker tag ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER} ${env.DOCKER_IMAGE}:latest"
                        echo "✅ Docker image built successfully: ${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                    } else {
                        echo "⚠️ Dockerfile not found. Skipping Docker build."
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up virtual environment
                sh "rm -rf ${env.VENV}"
                
                // Archive artifacts if they exist
                if (fileExists('artifacts')) {
                    archiveArtifacts artifacts: 'artifacts/**', allowEmptyArchive: true
                }
                if (fileExists('models')) {
                    archiveArtifacts artifacts: 'models/**', allowEmptyArchive: true
                }
                if (fileExists('logs')) {
                    archiveArtifacts artifacts: 'logs/**', allowEmptyArchive: true
                }
            }
        }
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs above for details.'
        }
        cleanup {
            script {
                // Clean up Docker images if they exist
                sh """
                    docker images | grep ${env.DOCKER_IMAGE} | awk '{print \$3}' | xargs -r docker rmi -f || true
                """
            }
        }
    }
}
