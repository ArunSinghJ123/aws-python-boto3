# AWS Hammer

The idea of this repo is to write a wrapper functionality for frequently used aws automation scenarios


*******IAM*******

**Creating IAM Role and Attaching custom managed Policy to the IAM Role**

Note:  Do not remove the mandate_iam_assume.json as it provides the AssumeRolePolicyDocument (change as needed for other entities like lambda)

Edit sample_s3.json as per need - This is an example code

Step 1: git clone this repository

Step 2: virtualenv aws-python-boto3

Step 3: source aws-python-boto3/bin/activate

Step 4: python setup.py install

Step 4: Run  iam  [ROLENAME]  [POLICYNAME]  [CUSTOM JSON POLICY DOCUMENT]

*********S3 BUCKET POLICY ATTACHMENT TO BUCKETS*********

**Creating Custom Bucket Policies and Attaching to List of S3 Buckets:**

Note: Existing bucket policies if any might get overrided - This is meant for scenarios where 100 buckets need same policy attached

bucketlist - provides the list of buckets to which policies will be attached

bucket_policy.json - bucket policy json , appends bucketname as per the given list

Change the bucketlist file and bucket_policy.json as per need - This is an example code

Step 1: git clone this repository

Step 2: virtualenv aws-python-boto3

Step 3: source aws-python-boto3/bin/activate

Step 4: python setup.py install

Run  bucket  [BUCKET_LIST_FILE]  [BUCKET_POLICY_JSON]
