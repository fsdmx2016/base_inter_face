pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirments.txt'
            }
        }
        stage('Test'){
            steps {
                sh 'python3 main.py'
            }
        }

    }
  }
