import boto3
import os

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')

    action = event.get('action', 'start')
    instance_ids = ['i-xxxxxxxxxxxxxxxxx']  # Replace with real EC2 ID
    topic_arn = 'arn:aws:sns:your-region:your-account-id:your-topic-name'  # Replace

    if action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
        message = f"EC2 Instances {instance_ids} started successfully."
    else:
        ec2.stop_instances(InstanceIds=instance_ids)
        message = f"EC2 Instances {instance_ids} stopped successfully."

    sns.publish(
        TopicArn=topic_arn,
        Subject="EC2 Action Notification",
        Message=message
    )

    return {
        'statusCode': 200,
        'body': message
    }
