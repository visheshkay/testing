pipeline{
    agent any 
    stages{
        stage('Load code'){
            steps{
                checkout scm
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t student-app .'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'python -m pytest -v'
            }
        }
    }
}