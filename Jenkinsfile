pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '-u root:sudo'
        }
    }
    stages {
        stage('setup') {
            steps {
                sh 'pip install flake8'
                sh 'pip install tox'
                sh 'pip install tox-pyenv'
            }
        }
        stage('Pipe line Training') {
            steps {
            dir("packages/gradient_boosting_model") {
                sh 'tox -e train '
                }

            }
        }

        stage('Copy model from GCP Bucket') {
            steps {
            dir("packages/final") {
                sh 'python gcp_model_pull.py '
                }

            }
        }

        stage('Unit Test') {
            steps {
            dir("packages/gradient_boosting_model") {
                sh 'tox -e train '
                }

            }
        }

         stage('API Test') {
            steps {
            dir("packages/ml_api") {
                sh 'tox'
                }
            }
        }

         stage('Deploy to staging area') {
            steps{
              sh 'exit 0'

                }
            }

             stage('Load Test') {
            steps{
              sh 'exit 0'

                }
            }






}
    }
