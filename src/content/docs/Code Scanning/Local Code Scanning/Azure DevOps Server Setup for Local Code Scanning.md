---
title: Azure DevOps Server Setup for Local Code Scanning
---


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your code never leaves your premises. The scans take place locally, and the results are then uploaded to the Aikido Security platform. This setup allows easy integration of the Local Scanner into your Azure DevOps Server project for reporting purposes.

## How to set up Local Scanning

**Prerequisite**: make sure to have created an account that allows for Local Scanning.\
[More information on creating a Local Scanning Account](https://help.aikido.dev/en/articles/9070345-how-to-create-an-account-for-local-scanning-on-aikido).

## 1. Setting up a Local Scanner pipeline

Navigate to Pipelines in the left hand navigation, click *Pipelines* and select *New Pipeline* or *Create Pipeline*. In the Configure step, select *Starter Pipeline*. This example pipeline below will trigger a scan on changes on the main branch.

```yaml
trigger:
  branches:
    include:
    - main

pool:
  vmImage: 'ubuntu-latest'

container:
  image: aikidosecurity/local-scanner:latest
  options: --entrypoint=""

steps:
- script: aikido-local-scanner scan $BUILD_SOURCESDIRECTORY --apikey $(AIKIDO_API_KEY) --repositoryname $BUILD_REPOSITORY_NAME --branchname main
```

Now it is time to add the api key as a secret variable. Click variables in the right hand corner and add a new variable. Fill in AIKIDO_API_KEY as the name. Check the *Keep this value secret* checkbox. To find the secret value, move on to step 2.

## 2. Get your authentication token

1. Go to the [Local Scanner setup page](https://app.aikido.dev/settings/integrations/localscan)
2. Generate an authentication token and copy. Note that you will only be able to view this token once.
3. Paste this token as the value for the AIKIDO_API_KEY variable in the pipeline setup.

Now you can create and run your pipeline for the first time.

## 3. Check your scanning results

After your first scan is done, you can go to the Aikido Feed to check out your results. A repository will have been created, containing all results from the scanning.