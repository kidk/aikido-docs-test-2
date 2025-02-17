---
title: Azure Pipelines CI_ PR Gating via Aikido Dashboard with a Personal Access Token
---


When the installation of the Azure DevOps checks integration does not work via[ the OAuth flow](https://help.aikido.dev/doc/azure-pipelines-ci-pr-gating-via-aikido-dashboard/docVU0nLa09W), you can also configure it to work with a Personal Access Token (PAT).

> Please note that for the integration to work properly, you need to be able to manage service hooks in all of the projects in your organization. This is usually a reserved permission for workspace admins.

**First**, go to the PAT management page in Aikdo, which can be [found here](https://app.aikido.dev/settings/integrations/azure-devops/checks/personal-access-token). 

**Next**, follow the instructions below to generate a PAT in Azure DevOps.

## Generating a PAT

1. Navigate to '**User Settings**' &gt; '**Personal Access Tokens**', via the header icon shown here

   ![Image](https://ucarecdn.com/6a98aaa9-d4dd-439c-8523-1243b85bccd2/)

   Or use the shortcut link '**Generate Access Token here**' on the personal access token management page in Aikido.

   ![Image](https://ucarecdn.com/734148e7-1b81-4ffe-9987-0bcfc390e36e/)
2. You should end up on a page similar to this

   ![Image](https://ucarecdn.com/d9e644dd-79a8-4d81-a3b2-9942a34c5ec9/)
3. Make sure you have selected the same organization as the one in your Aikido workspace via the '**Access scope**' button on the top right
4. Click on "**New token**"
5. Next you need to select the following permissions for the token: **Work Items (Read & Write)**, **Code (Read & Write)**, **Code (Status)** and **Build (Read)**

   ![Image](https://ucarecdn.com/33865be9-0c62-4642-8ae7-b47280f0f4be/)
6. For the expiration, use custom defined and set it to 1 year from now, this is the maximum duration that Azure DevOps allows the token to be valid for. 
7. Click on '**Create**' to create the access token
8. Copy the token on the next screen and insert it on the personal access token management page in Aikido.