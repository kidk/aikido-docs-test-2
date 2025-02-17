---
title: Gitlab (Server) CI_ MR Gating via Aikido Dashboard with a Personal Access Token (PAT)
---


### Introduction

You can easily configure GitLab MR Gating via the Aikido interface. This doc focusses on managing configurations in bulk - multiple repos at the same time - without code. 

### Use Cases

- **Bulk Repository Management**: Easily specify and manage configurations for multiple repositories at once through the Aikido interface.
- **Zero Code Integration**: Install the Aikido app on GitLab to manage checks without embedding any code, simplifying the setup process.
- **Cost Efficiency**: By managing GitLab Checks through Aikido, avoid using CI minutes on GitLab, leading to significant cost savings.

### Creating a Personal Access Token

Gitlab Server and Gitlab cloud support several different personal access tokens, which all work the same way. We usually recommend to create a group PAT, but for Gitlab cloud this is only possible for premium customers.

1. Navigate to the "Personal Access Token" settings page
   1. For a group access token: Go to you group page &gt; Settings &gt; Access Tokens
   2. For a personal access token: Go to your profile page &gt; User settings &gt; Access Tokens

      ![Image](https://ucarecdn.com/9e58d61d-ee8e-4c49-8f0d-e3e081aff7d0/)
2. Click on "**Add new token**"
3. Enter a name for the token, remove the expiration date and select the **api** scope

   ![Image](https://ucarecdn.com/9a75454e-da0b-4827-ac1f-4a0913af28b6/)
4. Click on "**Create token**"

   ![Image](https://ucarecdn.com/c616c3d2-a6c5-4387-b1fc-d8cd18965584/)
5. Copy the token and keep it for the next step

### Setting up GitLab CI

**Step 1.** Go to the [Integrations Page](https://app.aikido.dev/settings/integrations) and select GitLab in the CI gating section.

![Image](https://ucarecdn.com/1d5f2c3c-cad7-4bb3-a087-395d4171185b/)

**Step 2.** Select **MR Gating Configuration Via Aikido Dashboard** in the modal that pops up. This will open up a new tab with GitLab to install the MR Checks App.

![Image](https://ucarecdn.com/d24322f3-0111-4dc7-ac40-f6d3868e5ac4/)

**Step 3.** Enter the access token from the previous part into the input field and click "**Update token**"

![Image](https://ucarecdn.com/d9d15044-0b55-4529-bae2-5b8e491487f7/)

**Step 4.** Aikido redirects you to the [GitLab CI page](https://app.aikido.dev/settings/integrations/github/checks) with an overview of your repos. You can start configuring your repos. We recommend starting out with 1 repo to make sure everything works well.

![Image](https://ucarecdn.com/45ca5e3f-45b9-43ec-89cb-c6e393736067/)

**Step 5. Select repos in bulk** and click **Configure Scans** button in the top right. 

![Image](https://ucarecdn.com/571a4e22-8dfa-48c9-8a2a-ab11fce4ad35/)

**Step 6**.This will trigger the modal to choose the severity level for failure and the scans you want to execute.

![Image](https://ucarecdn.com/92e75089-13f0-42bc-b147-a3cc310b55ec/)

> If you've added new repositories after the initial setup, you'll need to configure those repos as well.

### Adding Exceptions for specific repos

You might want to have 1 specific repo where the configuration slightly differs. You can easily add exceptions by clicking the triple dots on a repo item or just select 1 or more items and go through the **Configure Scans** process again.

![Image](https://ucarecdn.com/3a87b0e4-7624-4650-a651-53f5b288d6a8/)

### Full Flow

We have recorded a Loom video showing you the full flow, both within Aikido and GitLab. This can be [viewed here](https://www.loom.com/share/403f5b70b9c5403f8d105c7b046a9161?sid=58428224-85a5-4b68-a5b8-95c62a886265). 