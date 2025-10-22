
# AWS EC2 Auto Start/Stop with Lambda



This project automatically starts/stops EC2 instances on a schedule using Lambda and sends email notifications via SNS.



---



\## 📦 Services Used



\- AWS Lambda

\- AWS EC2

\- Amazon EventBridge

\- Amazon SNS

\- IAM Roles \& Policies



---



\## 🧠 How It Works



1\. EventBridge triggers Lambda on schedule.

2\. Lambda starts/stops EC2 instance(s).

3\. Lambda sends email via SNS.



---



\## 📁 Files



| File | Purpose |

|

| lambda\_function.py | Code for Lambda |

| policy.json | IAM policy for Lambda role |

| eventbridge\_schedule.json | EventBridge rule |

| lambda.jpg | Architecture image (diagram) 




\## 🖼 Architecture



!\[Architecture](lambda.jpg)

STEPS-
🧩 Step 1: Create or Identify an EC2 Instance

Go to the EC2 console → Instances.

If you already have an instance, note down:

Instance ID (e.g., i-0abc123456789def0)

Region (e.g., ap-south-1)

If you don’t have one:

Click Launch Instance → choose Amazon Linux or any OS → launch it.

You can stop it later so Lambda can start it automatically.

💬 Step 2: Create an SNS Topic (for notifications)

Go to the SNS console → Topics → Create topic.

Choose Standard type.

Give it a name (e.g., EC2NotificationTopic).

Click Create topic.

Now create a Subscription:

Protocol: Email

Endpoint: your email address.

Check your inbox and confirm the subscription (click the link in the AWS email).

✅ Done — now SNS can send you notifications.

⚙️ Step 3: Create a Lambda Function

Go to the Lambda console → click Create function.

Choose:

Author from scratch

Function name: EC2AutoStart

Runtime: Python 3.12

Execution role: Choose Create a new role with basic Lambda permissions

Click Create function.

✅ Lambda function created successfully.

🔐 Step 4: Add Permissions to Lambda Role

Now your Lambda needs permission to manage EC2 and send SNS notifications.

Go to IAM Console → Roles.

Search for the role with the same name as your Lambda function (it usually starts with your function name).

Click the role → Add permissions → Attach policies.

Attach these managed policies:

AmazonEC2FullAccess

AmazonSNSFullAccess

AWSLambdaBasicExecutionRole

Click Add permissions.

✅ Lambda now has access to EC2, SNS, and CloudWatch Logs.

⚙️ Step 5: Configure Lambda Function

Go back to Lambda Console → open your function.

Click Configuration → Environment variables → Add:

INSTANCE_ID → your EC2 instance ID

SNS_TOPIC_ARN → copy from SNS console (Topic details page)

REGION → your region (example: ap-south-1)

Click Save.

✅ Lambda knows which EC2 instance and SNS topic to use.

⏰ Step 6: Create EventBridge Schedule (Automatic Trigger)

Go to EventBridge console → Schedules → Create schedule.

Name it something like: StartEC2DailyMorning.

Choose:

Schedule pattern: “At a specific time” or “Every day at…”

Example: “Every day at 07:30 AM (UTC)”
(You can convert your local time to UTC if needed)

Under Target, choose:

Target type: AWS service

Service: Lambda function

Function: Select your Lambda function (EC2AutoStart)

Click Next → Create schedule.

✅ EventBridge is now set to automatically trigger your Lambda every day.

🧪 Step 7: Test Everything Once

You can test manually once to make sure it works before the schedule runs automatically:

Go to Lambda console → open your function → click Test.

Create a test event (any name).

Click Test → check:

EC2 instance should start (if it was stopped).

You receive an email from SNS saying the instance started.

Logs appear in CloudWatch Logs → confirm success.

✅ Manual test complete — now it’s safe to rely on automation.

🔄 Step 8: Automatic Operation

Now, EventBridge automatically triggers Lambda at the scheduled time.

Lambda automatically starts or stops your EC2.

SNS automatically sends you an email notification.

CloudWatch automatically logs every execution.

You don’t need to click anything — it’s 100% automatic after setup 🎉





