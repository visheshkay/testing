pipeline{
    agent any 
    stages{
        stage('Load code'){
            steps{
                checkout scm
            }
        }
        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests'){
            steps{
                sh 'python3 -m pytest -v'
            }
        }
    }
}