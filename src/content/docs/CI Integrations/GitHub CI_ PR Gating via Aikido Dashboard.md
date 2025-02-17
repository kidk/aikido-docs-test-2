---
title: GitHub CI_ PR Gating via Aikido Dashboard
---


### Introduction

You can easily configure GitHub PR Gating via the Aikido interface. This doc focusses on managing configurations in bulk - multiple repos at the same time - without code. 

### Use Cases

- **Bulk Repository Management**: Easily specify and manage configurations for multiple repositories at once through the Aikido interface.
- **Zero Code Integration**: Install the Aikido app on GitHub to manage checks without embedding any code, simplifying the setup process.
- **Cost Efficiency**: By managing GitHub Checks through Aikido, avoid using CI minutes on GitHub, leading to significant cost savings.

### Setting up GitHub CI

**Step 1.** Go to the [Integrations Page](https://app.aikido.dev/settings/integrations) and select GitHub in the CI gating section.

![Image](https://ucarecdn.com/43344e10-d830-4b16-9304-117e86c3a68e/)

**Step 2.** Select **PR Gating Configuration Via Aikido Dashboard** in the modal that pops up. This will open up a new tab with GitHub to install the PR Checks App.

![Image](https://ucarecdn.com/6dd239df-679e-47db-8da9-a2c507f22f1d/)

**Step 3.** Install the **Aikido PR Checks app** in GitHub. Make sure that you select the GitHub organisation that is currently being used in your workspace. Choose which repos that Aikido is allowed to access. We recommend giving access to all repos so these can easily be managed from within Aikido.

![Image](https://ucarecdn.com/b27aae05-4bb2-427a-86e3-358be281878b/)

**Step 4.** Aikido redirects you to the [GitHub CI page](https://app.aikido.dev/settings/integrations/github/checks) with an overview of your repos. You can start configuring your repos. We recommend starting out with 1 repo to make sure everything works well.

![Image](https://ucarecdn.com/997c66c0-515b-4e7c-b9a5-b5e2867cab6c/)

**Step 5. Select repos in bulk** and click **Configure Scans** button in the top right. 

![Image](https://ucarecdn.com/e866e586-c104-4453-bdda-a64debd62651/)

**Step 6**.This will trigger the modal to choose the severity level for failure and the scans you want to execute.

![Image](https://ucarecdn.com/c826fb12-225c-4ed3-9b01-bc86b10aa845/)

> If you've added new repositories after the initial setup, you'll need to configure those repos as well.

### Adding Exceptions for specific repos

You might want to have 1 specific repo where the configuration slightly differs. You can easily add exceptions by clicking the triple dots on a repo item or just select 1 or more items and go through the **Configure Scans** process again.

![Image](https://ucarecdn.com/86da3769-0a5e-4012-ad5e-c1b6e53233f7/)

### Automatic Configuration for Newly Added Repos

It is possible to auto-enable any new repos with a default configuration. This is helpful when new repos are frequently added to your codebase, and you do not want to configure these new repos each time manually.

### Prerequisite

- Make sure that on the [repository settings](https://app.aikido.dev/settings/integrations/repositories) page, the option to automatically **activate new repos** has been activated. This can be done by clicking the 'Configure' button on that page.

  ![Image](https://ucarecdn.com/9f6bbfd8-0825-4e4f-8f84-0c46e4ee54d7/)

### Steps

**Step 1.** On the GitHub CI page, Click 'Settings' 

![Image](https://ucarecdn.com/dd99be6e-d167-45b2-9ec0-ff909fc34b57/)

**Step 2.** Enable the switch to **automatically activate scan configuration for new repos**

![Image](https://ucarecdn.com/7b1d5caa-602a-4a3a-b525-cc884ddb38b2/)

**Step 3.** Set the configuration that should be applied to all new repos

![Image](https://ucarecdn.com/2f0ee6a7-516a-48d2-b6fe-b53025e64d89/)