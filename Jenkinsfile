pipeline {
    agent any
    parameters{
        choice(
            name: 'test_type',
            choices: ['all','calculator'],
            description: "Select the type of tests to run"
        )
    }
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
    post {
    success {
        echo 'Build successful!'
    }

    failure {
        echo 'Build failed!'
    }

    always {
        echo 'Pipeline finished.'
    }
  }
}