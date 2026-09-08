pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python manage.py check'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t college-django:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}