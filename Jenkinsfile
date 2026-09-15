pipeline {
    agent any

    environment {
        PATH = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312;${env.PATH}"
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

        stage('Install pytest') {
            steps {
                bat 'python -m pip install pytest'
            }
        }

        stage('Run test') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}