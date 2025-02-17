---
title: Bitbucket CI_ PR Gating via Aikido Dashboard
---


You can easily configure Bitbucket PR Gating via the Aikido interface. This doc focusses on managing configurations in bulk - multiple repos at the same time - without code. 

### Use Cases

- **Bulk Repository Management**: Easily specify and manage configurations for multiple repositories at once through the Aikido interface.
- **Zero Code Integration**: Install the Aikido app on Bitbucket to manage checks without embedding any code, simplifying the setup process.
- **Cost Efficiency**: By managing Bitbucket Checks through Aikido, avoid using CI minutes on Bitbucket, leading to significant cost savings.

### Setting up Bitbucket CI

**Step 1.** Go to the [Integrations Page](https://app.aikido.dev/settings/integrations) and select Bitbucket Pipes in the CI gating section.

![Image](https://ucarecdn.com/7348e605-7934-469f-a00c-5357fa002a1c/)

**Step 2.** Select **PR Gating Configuration Via Aikido Dashboard** in the modal that pops up. This will open up a new tab with Bitbucket to install the PR Checks App.

![Image](https://ucarecdn.com/257dddb1-0497-458a-8de8-194a5a90e23a/)

**Step 3.** Consent to the **Aikido PR Checks OAuth app** in Bitbucket. 

![Image](https://ucarecdn.com/38689676-3fa2-4377-8956-63cf7e59345d/)

**Step 4.** Aikido redirects you to the [Bitbucket CI page](https://app.aikido.dev/settings/integrations/github/checks) with an overview of your repos. You can start configuring your repos. We recommend starting out with 1 repo to make sure everything works well.

![Image](https://ucarecdn.com/9944a550-c244-4542-b849-3f95b5f1556c/)

**Step 5. Select repos in bulk** and click **Configure Scans** button in the top right. 

![Image](https://ucarecdn.com/473a6d49-0fcc-40d9-9669-8937e085fece/)

**Step 6**.This will trigger the modal to choose the severity level for failure and the scans you want to execute.

![Image](https://ucarecdn.com/20031398-6e95-4b3d-98e1-da9d5a9a0923/)

> If you've added new repositories after the initial setup, you'll need to configure those repos as well.

### Adding Exceptions for specific repos

You might want to have 1 specific repo where the configuration slightly differs. You can easily add exceptions by clicking the triple dots on a repo item or just select 1 or more items and go through the **Configure Scans** process again.

![Image](https://ucarecdn.com/1a2b51d0-ef1d-4b47-a789-8006e395fbe8/)