---
title: Aikido - Forge Integration_ Troubleshooting
---

**Table of contents:**
  - [1. Missing permissions](#1-missing-permissions)
  - [2. Repository not active in Aikido](#2-repository-not-active-in-aikido)
  - [3. Setup for multiple Gits](#3-setup-for-multiple-gits)



### 1. Missing permissions

> A person has a user on aikido, but have not given permission to the current repository in the workspace

All permissions for Aikido can be managed inside your source code manager. This often can be found at App Permissions. A quick way to **grant permissions and activating repos** is through the Aikido UI

**Steps to give permissions and activate repos**

- Go to the [Repository Settings page ](https://app.aikido.dev/settings/integrations/repositories)and click **Add Repo**. This will open up the respective source code manager
- Select repos you want to Aikido to have access to

  ![Image](https://ucarecdn.com/c60a1b0d-3f9c-41ff-b65c-c27c907979e4/)

- Select which repos Aikido should **activate** and scan

  > This is important so Aikido can scan for vulnerabilities and send information to Forge.

  ![Image](https://ucarecdn.com/0231037c-bf20-4269-8702-88cca5d15856/)

### 2. Repository not active in Aikido

> The repository has permission, but was not selected as one of the repos to scan.

It is possible that you have granted permission to Aikido to all repositories, but that only a few were selected for being nightly scanned. By default, Aikido disables these repositories for scanning.

**Steps to activate a single repository in Aikido**

- Go to the [Repository Settings page](https://app.aikido.dev/settings/integrations/repositories)
- Go to the repository that you want to activate and click the triple dots on the right. In the action menu, select  'Activate'.

  ![Image](https://ucarecdn.com/443198a2-31e5-4cd8-a788-2430d4fa5e4f/)

If you need to enable a big number of repos at once, you can click 'add repo' which will take you back through the [initial setup](https://app.aikido.dev/onboarding/github/connect-repositories) page. There you can multiselect which repos you would like to be scanned / activated.

![Image](https://ucarecdn.com/5fdc0e3b-3ab0-47d3-a86f-09beca7245f6/)

### 3. Setup for multiple Gits

> A user has a workspace, but the repository is not in that workspace. This can be the case when a repository is another GitHub organisation.

Aikido supports [connecting multiple Gits](https://help.aikido.dev/doc/account-setup-with-multiple-gits/docQQDljtNwO) (e.g., GitHub combined with Bitbucket) or different organisations within the same Git. If you want to connect a new GitHub organisation to an existing account, **you will need to create a new workspace.**

**Steps to setup a new workspace**

**Step 1:** Add a new workspace by clicking your profile icon in the top right corner.

![Image](https://ucarecdn.com/8622f892-c25d-4192-9d4b-1718d6d954f5/)

**Step 2:** Continue by selecting "Add a New Workspace." 

![Image](https://ucarecdn.com/520e5e25-cbcf-4056-8b41-0a092ce3df96/)

**Step 3:** Switch between different Git accounts using the workspace switcher located in the top left corner.

![Image](https://ucarecdn.com/7e3091ac-77d5-46b6-8712-4568446b068e/)