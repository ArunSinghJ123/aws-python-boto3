import sys
import json
import boto3

class createrole:
    def __init__(self, rolename, policyname, policydocument):
        self.role = rolename
        self.policy = policyname
        self.policy_document = policydocument
    def kickoff_policy(self):
        print ('in policy')
        try:
            client = boto3.client('iam')
            with open(self.policy_document, 'r') as policy:
                tmp_holder = policy.read()
                response = client.create_policy(PolicyName=self.policy, Path='/', PolicyDocument=tmp_holder)
                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    return response['Policy']['Arn']
                else:
                    return 'failure in creating the policy for the policyname {}'.format(self.policy)
        except Exception as e:
            print ('Error in creating policy, exception as'.format(e))

    def kickoff_role(self, policy_Arn):
        '''create a role and attaching the policy created'''
        client = boto3.client('iam')
        try:
            print (self.policy_document)
            with open('iam.json', 'r') as policy:
                tmp_holder = policy.read()
            response = client.create_role(Path='/', RoleName=self.role, AssumeRolePolicyDocument=tmp_holder, Description='sample role')
        except Exception as e:
            print ('Error in creating role'.format(e))
        try:
            print (policy_Arn)
            response = client.attach_role_policy(RoleName=self.role, PolicyArn=policy_Arn)
            print (response)
        except Exception as e:
            print ('Error in creating role'.format(e))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ('Error. Provide the arguments - rolename, policyname, policydocument')
    rolename = sys.argv[1]
    policyname = sys.argv[2]
    policydocument = sys.argv[3]
    create_policy = createrole(rolename, policyname, policydocument)
    policy_Arn = create_policy.kickoff_policy()
    if policy_Arn:
        print ('Creating a Role and Attaching Policy to the Role now....')
        create_policy.kickoff_role(policy_Arn)


    #create_role = createrole(rolename)
    #print (create_role.kickoff_role())
