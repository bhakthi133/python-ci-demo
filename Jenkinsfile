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
                bat 'echo %PATH%'
                bat 'where python'
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