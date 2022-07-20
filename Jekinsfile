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
        stage('test') {
            steps {
                sh 'tox'
                //Get coverage
                cobertura coberturaReportFile: 'coverage.xml'
                //Get test results
                junit 'junit_reports/*.xml'
            }
        }
    }
}