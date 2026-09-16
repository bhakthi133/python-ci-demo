pipeline {
    agent any
    environment {
    PATH = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Admin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin;${env.PATH}"
    }

    stages {

        stage('Load code') {
            steps {
                checkout scm   
            }
        }

        stage('Set Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install pytest dependency library') {
            steps {
                bat 'python -m pip install pytest'
            }
        }

        stage('Run test') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build image of docker') {
            steps{
                bat 'docker build -t image_jenkins .'
            }
        }
        stage('Docker login'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'Docker-cred',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]){
                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                }
            }
        }
        stage('Push image'){
            steps{
                bat 'docker tag image_jenkins bhakthisp/image_jenkins:latest'
                bat 'docker push bhakthisp/image_jenkins:latest'
            }
        }
    } 
}    