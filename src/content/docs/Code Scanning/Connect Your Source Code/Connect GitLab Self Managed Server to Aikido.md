---
title: Connect GitLab Self Managed Server to Aikido
---

**Table of contents:**
  - [Step 1. Select Google or O365 to authenticate](#step-1-select-google-or-o365-to-authenticate)
  - [Step 2. Insert your GitLab server URL](#step-2-insert-your-gitlab-server-url)
  - [Step 3. Create a Personal Access Token](#step-3-create-a-personal-access-token)
  - [Step 4. Select the group and repositories you'd like to secure](#step-4-select-the-group-and-repositories-youd-like-to-secure)
  - [Get Started → ](#get-started--)
  - [Discover Integration Details → ](#discover-integration-details--)


Aikido allows you to connect your self-managed GitLab server to secure your code. In order to connect your GitLab server to Aikido, you will need to follow the steps below.

***Important before you start***

- If your GitLab is behind a firewall, we have a [list of Static IPs](https://help.aikido.dev/en/articles/8731261-allowing-ip-addresses-for-code-scanning) you can whitelist. 
- The person who sets up the account needs to have access rights both to the GitLab instance **and** GitLab group.

### Step 1. Select Google or O365 to authenticate

**Step 1.** To connect your GitLab server, you first need to authenticate via Google or Office 365 to create a user in Aikido. On the [signup screen](https://app.aikido.dev/login), click on 'Google / Microsoft' to continue.

**Step 2.** Once you're authenticated, you can either create a new workspace by clicking the **Self-Managed** button in the GitLab section.

![Image](https://ucarecdn.com/38929d5c-805a-4ee2-9881-67b5a316190d/)

### Step 2. Insert your GitLab server URL

When you decide to create a new workspace, you'll need to provide a few details about your self-managed GitLab instance so Aikido can connect to it.

Enter the URL to your GitLab server in the first input field.

![Image](https://ucarecdn.com/2ea0a4d5-b40f-4887-af1d-9c95003ad321/)

### Step 3. Create a Personal Access Token

Next up, you need to create a Personal Access Token to give us access to the resources you want.

- Log in to your GitLab server
- In the upper-right corner, click your avatar and select **Settings**.
- On the **User Settings** menu, select **Access Tokens**.
- Enter a name for the token, eg: 'Aikido Security Access Token'
- You don't need to select an expiration date
- We need the following scopes to be selected:
  - **read_user**
  - **read_api**
  - **read_repository**
- Click the **Create personal access token** button.

![Image](https://ucarecdn.com/0afbd9e4-64bf-404c-92ba-41e636e6541c/)

- Copy the token being shown on the screen and enter it in the input field.

**Important**: You will no longer be able to view the value of the token once you hit continue. Make sure you copied it first.

Aikido will now check the connection to your GitLab server. If the connection was not successful, make sure to double-check the URL you entered and the personal access token you provided.

### Step 4. Select the group and repositories you'd like to secure

On the next screen, you can select which group you'd like to start with. You'll always be able to connect more of your groups to Aikido.

In the final step you can select all the repositories you would like us to monitor.

---

### Get Started →

### Discover Integration Details →

---