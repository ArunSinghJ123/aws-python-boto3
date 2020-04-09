pipeline {
    agent any
    stages {
        stage('Writing the File') {
            steps {
                echo "testing build"
                sh '''
                aws sts assume-role --role-arn arn:aws:iam::125451170834:role/arun-asg --role-session-name devops-example
                aws s3 ls
                '''
            }
        }
         stage('Copying to S3') {
            steps {
                echo "testing this declarative build sample"
                sh '''
                aws sts assume-role --role-arn arn:aws:iam::125451170834:role/arun-asg --role-session-name devops-example
                touch hello.txt
                echo "hello devops" > hello.txt
                aws s3 cp hello.txt s3://arunsinj/devops/
                '''
            }
         }
         stage('Sending slack notification') {
            steps {
                   slackSend color: '#BADA55', message: 'Hello Devops pipe Success', channel: 'devops-planet'
                 }
            }                    
         }
     }
