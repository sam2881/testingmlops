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

         stage('Pulling Model from GCP') {
            steps{
              sh 'exit 0'

                }
            }
        stage('Pipe line Training') {
            steps {
            dir("packages/gradient_boosting_model") {
                sh 'tox -e train '
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







}
    }
