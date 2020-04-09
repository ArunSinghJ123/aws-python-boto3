pipeline {
    agent any
    stages {
        stage('Writing the File') {
            steps {
                echo "testing build"
                sh '''
                aws sts assume-role --role-arn arn:aws:iam::125451170834:role/arun-asg --role-session-name devops-example
                aws s3 ls
                touch hello.txt
                echo "hello devops" > hello.txt
                cat hello.txt
                '''
            }
        }
         stage('Copying to S3') {
            steps {
                echo "testing this declarative build sample"
                sh '''
                echo "passes stage 2"
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
