---
title: AWS Inspector for AWS ECR
---

**Table of contents:**
  - [Step 1: Connect your AWS Environment](#step-1-connect-your-aws-environment)
  - [Step 2: Enable the Amazon Inspector](#step-2-enable-the-amazon-inspector)
- [Step 3: Push the latest version of your images to ECR again](#step-3-push-the-latest-version-of-your-images-to-ecr-again)
  - [Step 4. Start a Scan in Aikido to process the results](#step-4-start-a-scan-in-aikido-to-process-the-results)
  - [Step 5. Link Images](#step-5-link-images)
  - [Discover Integration Details → ](#discover-integration-details--)


Aikido can seamlessly integrate with AWS ECR. Docker image findings are extracted via the AWS Inspector2 API or via our own [**Aikido Scanner**](https://help.aikido.dev/en/articles/8911170-scanning-aws-ecr-images-with-the-aikido-scanner) (recommended). 

Aikido will use the findings reported by Inspector and run them through the same deduplication and de-noising engine you are familiar with. Let's dive into the details of this new functionality and how to enable it.

### Step 1: Connect your AWS Environment

As a prerequisite, your AWS environment must be connected to Aikido. If you have not done this already, navigate to the[ cloud overview](https://app.aikido.dev/clouds) in Aikido. Click on "Connect cloud" and follow the steps to get set up. More information in [this article.](https://help.aikido.dev/en/articles/6976671-connecting-your-aws-account-to-aikido)

### Step 2: Enable the Amazon Inspector

Log in to your AWS console and navigate to the [Amazon inspector](https://console.aws.amazon.com/inspector/v2/home) service in the region(s) where your images are stored. Click on "Get Started" and activate the inspector.

![Image](https://ucarecdn.com/d4d7c270-43b9-47c8-8686-31b4009b2afc/)

Alternatively, you enable this from within Aikido during the setup.

![Image](https://ucarecdn.com/3c5f299a-e45e-40d0-92e5-4ef27e35dd08/)

## Step 3: Push the latest version of your images to ECR again

Amazon Inspector will only scan newly pushed imags for vulnerabilities. So for the analysis to start on your images, you should push the latest version of your images again to their respective ECR repositories.

> Important note. Amazon uses a pay-per-push modal, so for every push a fee will be incurred.

### Step 4. Start a Scan in Aikido to process the results

Once Amazon inspector is enabled for the region, AWS will automatically scan all your latest images for vulnerabilities and make them accessible to acquire via the API.

### Step 5. Link Images

**Link images:** The last step is to link a cloud image to a code repository. Go to the 'Images' tab on the cloud detail page and link the images to the code repository where the source code is hosted.

![Image](https://ucarecdn.com/c5f17432-0673-4f0c-858c-c5674a5f560c/)

Once the cloud images are linked to the code repositories, Aikido will assess and score the findings from AWS Inspector/ECR and link them to the related cloud environment and code repository.

> **Important note:** If you are using AWS Inspector, be aware that scanning costs on a pay-per-push basis. Depending on the number of pushes you are doing on a weekly basis, this cost can go up. Feel free to check out the [**Aikido Scanner**](https://help.aikido.dev/en/articles/8911170-scanning-aws-ecr-images-with-the-aikido-scanner) which has a broader coverage and allows for unlimited scans on any free plan.

---

### Discover Integration Details →

---