# aws-python-boto3

The Idea of this repo is to write a wrapper functionality for frequently used aws services
The idea of Devops and Automating infrastructure in the public cloud space has boiled down to the point of lifting heavy tasks to much simpler libraries

Creating IAM Role and Attaching custom managed Policy to the IAM Role

Note:  Do not remove the mandate_iam_assume.json as it provides the AssumeRolePolicyDocument (change as needed for other entities like lambda)
Step 1: git clone this repository

Step 2: virtualenv aws-python-boto3

Step 3: source aws-python-boto3/bin/activate

Step 4: Run python iam/role.py [ROLENAME] [POLICYNAME] [CUSTOM JSON POLICY DOCUMENT]
