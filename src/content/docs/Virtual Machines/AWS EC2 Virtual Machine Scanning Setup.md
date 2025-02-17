---
title: AWS EC2 Virtual Machine Scanning Setup
---


> This functionality is available for Pro and Scale plans only. [Contact us](https://www.aikido.dev/contact) for more information.

### Why should I scan my virtual machines?

With virtual machine scanning, Aikido can scan the hard drives of your virtual machines for vulnerable packages, outdated runtimes and risky licenses. 

### Getting started

To enable the scanning of your virtual machines on AWS EC2, you should first start by connecting your AWS Cloud to Aikido. To do this you can follow the steps outlined in [this article](https://help.aikido.dev/doc/connect-aws-account-to-aikido/doc4i7uR2stY).\
\
Once your cloud is connected, you'll see a tab appear on the detail page called 'Virtual Machines'.

![Image](https://ucarecdn.com/5009bb66-9945-408a-a7c5-37fd3c8bc531/)

When you click on 'Set Up VM Scanning' we'll take you to the following page:

![Image](https://ucarecdn.com/c0f27d23-d8bc-4379-85d1-d6b3ac77d3ab/)

On this page, you can set up the virtual machine scanning via an AWS CloudFormation template that should be applied in the account of the virtual machines that you'd like to have scanned. The CloudFormation template will create a role with limited access to your AWS account. It's important to **KEEP** any permissions from the role as this is the absolute minimum that Aikido needs to perform the scans. 

Once the CloudFormation resources have been created, you'll see the ARN of the role in AWS that was created. Copy it and add into the input field on the set up screen. Once you click 'save', Aikido will immediately start to discover any virtual machines in your account and scan them. 