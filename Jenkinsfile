pipeline {
    agent any
    stages {
        stage('stage one') {
            steps {
                echo "testing build"
                sh 'aws sts assume-role --role-arn arn:aws:iam::125451170834:role/arun-asg --role-session-name devops-example'
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
