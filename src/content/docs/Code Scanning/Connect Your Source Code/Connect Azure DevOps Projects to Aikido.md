---
title: Connect Azure DevOps Projects to Aikido
---

**Table of contents:**
- [Select Google or O365 to authenticate](#select-google-or-o365-to-authenticate)
- [Insert your organization's name](#insert-your-organizations-name)
- [Create a Personal Access Token](#create-a-personal-access-token)
- [Select the project and repos you'd like to secure](#select-the-project-and-repos-youd-like-to-secure)
  - [Get Started → ](#get-started--)
  - [Discover Integration Details → ](#discover-integration-details--)
  - [](#)


Aikido allows you to connect your Azure DevOps projects to secure your code. To connect your Azure DevOps projects to Aikido, you will need to follow the steps below. 

Note that each Azure Project with one or more repos will map to one Aikido workspace.

## Select Google or O365 to authenticate

**Step 1.** To connect your Azure DevOps project, you first need to authenticate via Google or Office 365 to create a user in Aikido. On the [signup screen](https://app.aikido.dev/login), click on 'Microsoft / Google' to continue.

**Step 2.** Once you are authenticated via Google/Microsoft, you can go ahead and select 'Connect Azure' on the page like below.

![Image](https://ucarecdn.com/8fece096-ffc3-4775-bd8d-52b44b022ee8/)

**Step 3.** Enter the details to connect the Azure Devops project of your choosing. We'll explain how to obtain the required information right below.

![Image](https://ucarecdn.com/3b1a2af6-64ef-4b33-b436-5e61e388e8dc/)

## Insert your organization's name

Enter the name of the Azure DevOps organization you'd like to connect. You can find this name by going to [https://dev.azure.com](https://dev.azure.com/) and copying it from the left-side navigation.

## Create a Personal Access Token

Next up, you need to create a Personal Access Token to give us access to the resources you want.

- Log in to your Azure DevOps account
- In the upper-right corner, click the user settings icon next to your avatar. It looks like this:

  ![Image](https://ucarecdn.com/8ac6922c-38e0-481b-a9e7-0be293fa315a/)
- Select **Personal Access Token** in the dropdown.
- Click on the **+New Token** button in the top left corner
- Enter a name for the token, eg: 'Aikido Security Access Token'
- Make sure to select the same organization as the one you entered in the previous step
- Make sure to select an expiration date in the future, the max should be 1 year.
- Next, we need the following scopes to be selected (click 'show all scopes'):
  - **Code: Read**
  - **Member Entitlement Management: Read**
  - **Project and Team: Read**
  - **User Profile: Read**
- Click the **Create** button at the bottom.

![Image](https://ucarecdn.com/06457a8f-e8dd-47b3-a629-8cb8cff94338/)

- Copy the token being shown on the following screen and enter it in the input field .

**Important**: You will no longer be able to view the value of the token once you hit continue. Make sure you copied it first.

Aikido will now check the connection to your Azure DevOps organization. If the connection was not successful, make sure to double-check the organization name and personal access token you provided.

## Select the project and repos you'd like to secure

On the next screen, you can select which project you'd like to start with. You'll always be able to connect more of your projects to Aikido.

In the final step you can select all the repos you would like us to monitor.

> Note: Aikido supports the integration of both Git and Team Foundation Version Control (TFVC) repositories. For TFVC repositories, Aikido does not perform secret scanning.

---

### Get Started →

### Discover Integration Details →

---

###

