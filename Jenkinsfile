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
        stage('Unit test') {
            steps {
            dir("packages/gradient_boosting_model") {
                sh 'tox'
                }

            }
        }

         stage('API test') {
            steps {
            dir("packages/ml_api") {
                sh 'tox'
                }
            }
        }


        stage('Build') {
        steps {
            sh " docker build -t mlops -f /packages/deploying-with-containers/Dockerfile ."
        }
        }
}
    }
