import json
import boto3
import sys
import logging


class bucketpolicy:
    def __init__(self, buckets, policys):
        self.buckets = buckets
        self.policy = policys
    def attach_bucketpolicies(self):
        s3 = boto3.client('s3')
        try:
            #store the policydata and iterate to append the bucket names in the bucket policys
            with open(self.policy, 'r') as bucket_policy:
                policy_data = json.load(bucket_policy)
            tmp = policy_data['Statement'][0]['Resource']
            #Iterate through the buckets and add the policies as per the bucket name
            with open(self.buckets, 'r') as bucket_list:
                s3_list = [line.rstrip('\n') for line in bucket_list]
            for name in s3_list:
                policy_data['Statement'][0]['Resource'] = 'arn:aws:s3:::{}'.format(name)
                bucket_policy = json.dumps(policy_data)
                s3.put_bucket_policy(Bucket=name, Policy=bucket_policy)
        except Exception as e:
            logging.info('Error in attaching policies to the bucketsv{}'.format(e))

    def revert_json(self):
        try:
            with open(self.policy, 'r') as revert:
                policy_data = json.load(revert)
            tmp = policy_data['Statement'][0]['Resource']
            policy_data['Statement'][0]['Resource'] = 'arn:aws:s3:::'
            with open(self.policy, 'r') as revert:
                json.dump(policy_data)
            logging.info('Execution of Bucket Policy attachment to the buckets in file {} success'.format(self.buckets))
        except Exception as e:
            logging.info('Error in reverting the json{}'.format(e))
def main():
    if len(sys.argv) != 3:
        print ('Error. Provide the arguments - bucketlist_filename, policy_filename')
        exit()
    buckets = sys.argv[1]
    policys = sys.argv[2]
    bucket_policy = bucketpolicy(buckets, policys)
    if bucket_policy.attach_bucketpolicies():
        bucket_policy.revert_json()

if __name__ == "__main__":
    main()
