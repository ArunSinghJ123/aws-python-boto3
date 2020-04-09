pipeline {
    agent any
    stages {
        stage('stage one') {
            steps {
                echo "testing build"
                sh 'aws s3 ls'
            }
        }
        stage('stage two') {
            steps {
                echo "testing this declarative build sample"
            }
        }
    }
}
