---
title: Aikido Scanner for AWS ECR
---


## Introduction

Aikido supports scanning Elastic Container Registry (ECR) images through both **AWS Inspector** and the **Aikido Scanner**. Opting for the Aikido Scanner provides several benefits:

- **Extended Scanning Capabilities**: Scans for licenses and end-of-life (EOL) runtimes for comprehensive security insights.
- **Quicker Results**: Delivers scan results promptly to accelerate development and deployment processes.
- **Targeted Scanning Efficiency**: Allows scanning based on specific tags, enhancing relevance and efficiency.
- **Continuous Scanning:** Unlike AWS Inspector, which scans once at the moment of push, Aikido performs daily scans—even if your image hasn't been updated in 100 days. This means Aikido can identify new Common Vulnerabilities and Exposures (CVEs) in the meantime, which AWS Inspector might miss.
- **Inclusive Pricing**: Included in every paid plan, offering unlimited scans without the additional costs associated with AWS Inspector's pay-per-push model.

## Installing the Aikido Scanner

1. **Navigate to [Containers Page](https://app.aikido.dev/containers)**
2. **Connect Registry**: Click on 'Connect registry' and select the first option: *'AWS Elastic Container Registry'*.
3. **Select Aikido Scanner**.

   ![Image](https://ucarecdn.com/18e955f3-6e54-4def-af72-a453301d42e2/)
4. **Fill in the Details**: Follow the instructions to create an IAM Role and Policy for the necessary permissions, then enter a name of your registry name (you can choose this yourself) and the AWS Role Amazon Resource Name (ARN). This step encompasses setting up the IAM role and policy, as well as providing registry specifics for a complete setup.

   ![Image](https://ucarecdn.com/73c33666-3f7c-4dd8-824e-dad07bafc5d0/)
5. **Completion**: Once the setup is complete, Aikido will scan the connected registry with the Aikido scanner on a nightly basis..

> *Note.* If AWS Inspector was previously enabled during the AWS Cloud setup, Aikido will notify you to switch to Aikido scanning without any problems after filling in all the details in Step 4.

![Image](https://ucarecdn.com/5378222c-fcd5-4470-aeef-c3f39c83e140/)

---