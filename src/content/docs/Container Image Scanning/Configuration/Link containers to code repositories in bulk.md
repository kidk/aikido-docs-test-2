---
title: Link containers to code repositories in bulk
---


Linking your container images to your code repositories is helpful to centralize all related vulnerabilities in one place. When you manage a lot of code repositories and container images, this might become a tedious job.

Aikido can now link container images to repositories based on the tags of the AWS ECR repositories that are being scanned in Aikido. Aikido will inspect the ECR repository tags during scanning for a special identifier and link it to the proper code repository.

To make use of the feature, make sure that your ECR repository has a tag with a key called: **aik:repository.** The value of the tag should then be the GitHub repository url that you want to link the containers to eg: 

[https://github.com/AikidoSec/demo-app-1](https://github.com/AikidoSec/demo-app-1)

During the next scan, Aikido will then automatically link the container images to that repository.

---