pipeline{
    agent any 
    stages{
        stage('Load code'){
            steps{
                git 'https://github.com/visheshkay/testing.git'
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