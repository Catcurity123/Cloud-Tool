import boto3 
import boto3.session
import botocore.exceptions

user_access_key_id = 'AKIAZQ3DQ2C5E6E5EG56'
user_secret_access_key = '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'
user_region_name = 'us-east-1'

try:
    aws_session = boto3.session.Session(
        aws_access_key_id=user_access_key_id,
        aws_secret_access_key=user_secret_access_key,
        region_name=user_region_name
    )

    iam = aws_session.resource('iam')

    user_names = []

    for each_user in iam.users.all():
        user_names.append(each_user.name)

    if not user_names:
        print("Error: No users found.")
    else:
        for name in user_names:
            print(name)

except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == 'InvalidClientTokenId':
        print("Error: Invalid credentials provided.")
    else:
        print("An error occurred:", e)
