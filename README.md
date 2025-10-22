HEAD
\# AWS EC2 Auto Start/Stop with Lambda



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




# aws-ec2-scheduler
Automatically start/stop EC2 instances using AWS Lambda and send email via SNS12d87498e4f3269cbe807460a1868f98b4d6eafa
