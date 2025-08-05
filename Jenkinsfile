pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/PradeepYadav90/Sample-Docker-and-Jenkins-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-todo-api .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker rm -f flask-todo-api || true'
                sh 'docker run -d -p 5000:5000 --name flask-todo-api flask-todo-api'
            }
        }
    }
}
