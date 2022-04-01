pipeline {
    agent any
    stages {
        stage('build'){
            steps {
             sh 'pip install -r requirments.txt'
            }
        }
    }
     stages {
        stage('test'){
            steps {
             sh 'python3 main.py'
            }
        }
    }
}