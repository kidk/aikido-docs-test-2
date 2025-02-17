---
title: Azure DevOps Boards
---


*📋 Setting up automated task creation in Azure DevOps Boards*

## Introduction

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Azure DevOps Boards.

Following use cases are supported :

- **Automated Ticket Creation**: Automatically create and push tickets to specified Boards projects for seamless tracking of security issues.
- **Manual Ticket Addition**: Manually add security issue tickets to Boards, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to Boards

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Azure DevOps Boards'\
   A modal will request some more information to authenticate:
   - **UserID**​: this is your **email**
   - **Access Token**: Can be found inside Azure DevOps. As scope, under '**Work Items**', you can select '**Read & write**'.
   - **Organisation** ***Name*:** name of the organisation, can be found in the URL

     > Make sure to include the organisation name ONLY, without the prefix of the url https://...

   ![Image](https://ucarecdn.com/d8185da7-4270-4757-983c-2f49135d8433/)
3. After filling in the credentials correctly, press save and Close the modal.\
   ​
4. Open the Azure DevOps Boards Integration page to manage the auto creation settings.\
   ​

![Image](https://ucarecdn.com/57fff758-9b9c-41e1-8312-ee580f8053da/)

## Options for Task Creation in Azure DevOps Boards via Aikido

There are two different options to create new tasks from Aikido into Boards

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.** \
   ​

   ![Image](https://ucarecdn.com/ae1f257e-0299-4349-b6df-4992273bef04/)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Image](https://ucarecdn.com/a9b48cf3-8614-447c-b1dd-252ae08967c8/)
2. Fill in the required details in the popup modal.\
   ​

   ![Image](https://ucarecdn.com/636e8271-d106-4556-9e2f-fb9c1cc51345/)

   ​
3. The newly created task in Boards will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Image](https://ucarecdn.com/803ed3f1-1548-49b0-ba58-64e153b91f1a/)

## 2. Automated Task Creation

1. Go to the [Azure DevOps Boards Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Select '**Change auto creation**'
3. Define the criteria for automatic task creation.\
   ​

   ![Image](https://ucarecdn.com/b847c651-3f59-4660-8350-960a783810d7/)

   ​
4. Aikido will then autonomously generate Boards tickets based on these settings 🚀

---

### Setup Azure DevOps Boards Integration →

### Discover Integration Details →

---