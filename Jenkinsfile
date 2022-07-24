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


        stage('Cloning our Git') {
            steps {
                git url: 'https://github.com/sam2881/testingmlops', branch: 'master'
            }
        }
        stage('Building and deploying image') {
            steps {
                script {
                    docker.withRegistry('https://gcr.io', 'gcr:AutomaticTrainingCICD') {
                        app = docker.build('automatictrainingcicd/prediction-api')
                        app.push("latest")
                    }
                }
            }
        }
        stage('Deploying to GKE') {
            steps{
                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'pod.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
            }
        }



}
    }
