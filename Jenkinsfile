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
                bat 'python --version'
            }
        }

        stage('Install pytest') {
            steps {
                bat 'pip install pytest'
            }
        }

        stage('Run test') {
            steps {
                bat 'pytest'
            }
        }
    }
}