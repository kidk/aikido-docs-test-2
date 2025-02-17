---
title: Azure Pipelines CI_ PR Gating via Aikido Dashboard
---


> Make sure the person who sets up the integration has enough permissions in Azure to manage all repos.

### Introduction

You can easily configure Azure DevOps PR Gating via the Aikido interface. This doc focusses on managing configurations in bulk - multiple repos at the same time - without code. 

### Use Cases

- **Bulk Repository Management**: Easily specify and manage configurations for multiple repositories at once through the Aikido interface.
- **Zero Code Integration**: Install the Aikido app on Azure DevOps to manage checks without embedding any code, simplifying the setup process.
- **Cost Efficiency**: By managing Azure DevOps Checks through Aikido, you avoid using CI minutes on Azure DevOps, leading to significant cost savings.

### Setting up Azure DevOps CI

**Step 1.** Go to the [Integrations Page](https://app.aikido.dev/settings/integrations) and select Azure Pipelines in the CI gating section.

![Image](https://ucarecdn.com/841b0383-ea8c-4e23-9fd5-b0bfa0f6d7d2/)

**Step 2.** Select **PR Gating Configuration via Aikido Dashboard** in the modal that pops up

![Image](https://ucarecdn.com/73c56e84-849d-49c5-a25d-5ff2636faefe/)

**Step 3.** Grant Aikido the necessary permissions. 

![Image](https://ucarecdn.com/487e813c-5767-4665-9321-dc816361cb16/)

**Step 4.** Aikido redirects you to the [Azure Pipelines page](https://app.aikido.dev/settings/integrations/azure-devops/checks) with an overview of your repos. You can start configuring your repos. We recommend starting out with 1 repo to make sure everything works well.

![Image](https://ucarecdn.com/074b209f-e226-427f-927c-85a7ca9912eb/)

**Step 5. Select repos in bulk** and click **Configure Scans** button in the top right. 

![Image](https://ucarecdn.com/0b3a75a8-de64-4a3b-8d0c-2ec3c2e3e1ce/)

**Step 6**.This will trigger the modal to choose the severity level for failure and the scans you want to execute.

![Image](https://ucarecdn.com/7bb56ec3-0997-4359-907f-0b3193960191/)

> If you've added new repositories after the initial setup, you'll need to configure those repos as well.

When creating or updating PR's, you'll now see the status of the checks on the pull request in Azure DevOps.

![Image](https://ucarecdn.com/0d1e8676-82ce-47a5-a056-edc294e14dd4/)

### Adding Exceptions for specific repos

You might want to have 1 specific repo where the configuration slightly differs. You can easily add exceptions by clicking the triple dots on a repo item or just select 1 or more items and go through the **Configure Scans** process again.

![Image](https://ucarecdn.com/fe4714cf-8f97-4a86-94dd-ccad35a351c7/)

## Configure the PR gating to block pull request

The PR gating functionality can only make its own pipeline fail, but won't block the PR from getting merged. In order to ensure that a failing gate also prevents the PR from merging, you can follow these steps:

1. Go to the project's settings page and navigate to "Repositories" 
2. Select the relevant repository where you'd like to make the PR gate required

   ![Image](https://ucarecdn.com/471ec693-7ab8-4174-9697-bfc923afa627/)
3. Navigate to the "Policies" tab
4. Select the PR's target branch where you'd like to enforce the PR gating to be blocking, this is usually the default branch of the repository called "main" or "master".

   ![Image](https://ucarecdn.com/19105849-1cbb-404a-9c81-2db45b36661c/)
5. Now add a new "Status Check" by clicking the "+" icon
6. Select the Aikido PR checks from the dropdown and make sure that you select "Required"

   ![Image](https://ucarecdn.com/deac7454-ece4-4b5e-8311-ee0dbb87a9c5/)
7. And lastly, hit "Save". The PR gating will now be required to be successful for merging PR's.

This can also be setup in bulk for all repositories in project via the "Policies" and adding a branch protection rule. It might be that the "Aikido Security/check code for vulnerabilities" check is not available in the dropdown, in which case you can add it manually there.