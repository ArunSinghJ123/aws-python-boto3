# aws-python-boto3

The Idea of this repo is to write a wrapper functionality for frequently used aws services


*******IAM*******

**Creating IAM Role and Attaching custom managed Policy to the IAM Role**

Note:  Do not remove the mandate_iam_assume.json as it provides the AssumeRolePolicyDocument (change as needed for other entities like lambda)

Edit sample_s3.json as per need - This is an example code

Step 1: git clone this repository

Step 2: virtualenv aws-python-boto3

Step 3: source aws-python-boto3/bin/activate

Step 4: Run  python  iam/roles.py  [ROLENAME]  [POLICYNAME]  [CUSTOM JSON POLICY DOCUMENT]

Example: python iam/roles.py samplerole samplepolicy sample_s3.json

*********S3 BUCKET POLICY ATTACHMENT TO BUCKETS*********

**Creating Custom Bucket Policies and Attaching to List of S3 Buckets:**

bucketlist - provides the list of buckets to which policies will be attached

bucket_policy.json - bucket policy json , appends bucketname as per the given list

Change the bucketlist file and bucket_policy.json as per need - This is an example code

Run  python  s3_bucketpolicy/s3_bucket_policy.py  [BUCKET_LIST_FILE]  [BUCKET_POLICY_JSON]

Example: python s3_bucketpolicy/s3_bucket_policy.py bucketlist bucket_policy.json
