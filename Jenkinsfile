pipeline {
    agent any
    stages {

        stage('Load code') {
            steps {
                checkout scm   
            }
        }

        stage('Set Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install pytest dependency library') {
            steps {
                sh 'python3 -m pip install pytest --break-system-packages'
            }
        }

        stage('Run test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        

        stage('Docker agent stage') {
            agent{
                docker{
                    image 'python:3.12'
                }
            }
            steps {
            sh 'python3 --version'
            sh 'python3 -m pip install --user pytest'
            sh 'python3 -m pytest'
            }
        }

        stage('Build image of docker') {
            steps{
                sh 'docker build -t image_jenkins .'
            }
        }
        stage('Docker login'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'Docker-cred',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]){
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                }
            }
        }
        stage('Push image'){
            steps{
                sh 'docker tag image_jenkins bhakthisp/image_jenkins:latest'
                sh 'docker push bhakthisp/image_jenkins:latest'
            }
        }
    } 
}    