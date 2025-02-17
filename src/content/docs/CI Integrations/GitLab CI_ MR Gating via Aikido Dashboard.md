---
title: GitLab CI_ MR Gating via Aikido Dashboard
---


### Introduction

You can easily configure GitLab MR Gating via the Aikido interface. This doc focusses on managing configurations in bulk - multiple repos at the same time - without code. 

### Use Cases

- **Bulk Repository Management**: Easily specify and manage configurations for multiple repositories at once through the Aikido interface.
- **Zero Code Integration**: Install the Aikido app on GitLab to manage checks without embedding any code, simplifying the setup process.
- **Cost Efficiency**: By managing GitLab Checks through Aikido, avoid using CI minutes on GitLab, leading to significant cost savings.

### Setting up GitLab CI

**Step 1.** Go to the [Integrations Page](https://app.aikido.dev/settings/integrations) and select GitLab in the CI gating section.

![Image](https://ucarecdn.com/2f0e7a7f-bb4a-491e-95cf-35001889e1ac/)

**Step 2.** Select **MR Gating Configuration Via Aikido Dashboard** in the modal that pops up. This will open up a new tab with GitLab to install the MR Checks App.

![Image](https://ucarecdn.com/12df3e46-cfd4-4081-ad3d-6c298d931845/)

**Step 3.** Consent to the **Aikido MR Checks OAuth app** in GitLab. Make sure that you select the GitLab group that is currently being used in your workspace.

![Image](https://ucarecdn.com/19535aec-3659-4ea5-9906-5d723f2d5101/)

**Step 4.** Aikido redirects you to the [GitLab CI page](https://app.aikido.dev/settings/integrations/github/checks) with an overview of your repos. You can start configuring your repos. We recommend starting out with 1 repo to make sure everything works well.

![Image](https://ucarecdn.com/d2ff314a-20db-481a-bbde-8e691095b720/)

**Step 5. Select repos in bulk** and click **Configure Scans** button in the top right. 

![Image](https://ucarecdn.com/1846d93c-03dd-414b-b7c1-cdd46f8d5d4c/)

**Step 6**.This will trigger the modal to choose the severity level for failure and the scans you want to execute.

![Image](https://ucarecdn.com/05ed4818-d19a-4cc9-a112-7985d1ec517e/)

> If you've added new repositories after the initial setup, you'll need to configure those repos as well.

### Adding Exceptions for specific repos

You might want to have 1 specific repo where the configuration slightly differs. You can easily add exceptions by clicking the triple dots on a repo item or just select 1 or more items and go through the **Configure Scans** process again.

![Image](https://ucarecdn.com/0d8004d4-730b-4ea7-9e18-f5be65fa85ed/)

### Full Flow

We have recorded a Loom video showing you the full flow, both within Aikido and GitLab. This can be [viewed here](https://www.loom.com/share/403f5b70b9c5403f8d105c7b046a9161?sid=58428224-85a5-4b68-a5b8-95c62a886265). 