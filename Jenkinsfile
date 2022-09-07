pipeline {
     agent
     {
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
         stage('Push model from mlflow repo to train repo ') {
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
                sh 'tox  '
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
