---
title: Jira Cloud
---


*📋 Setting up automated task creation in Jira Cloud*

## Introduction

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Jira Cloud.

Following use cases are supported :

- **Automated Ticket Creation**: Automatically create and push tickets to specified Jira projects for seamless tracking of security issues.
- **Manual Ticket Addition**: Manually add security issue tickets to Jira, ensuring targeted attention for critical vulnerabilities.

> Note: If the authorisation is linked to a person, we recommend using service accounts.

## Connecting the Aikido App to Jira

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Jira Issues'
3. A prompt will request authorization for Jira.\
   ​

   ![Image](https://ucarecdn.com/7f02a7ff-2d6a-4fd2-859a-690ec2503847/)
4. Login into your Jira account
5. Grant Aikido permission to access your Jira workspace

   ![Image](https://ucarecdn.com/a052e293-4386-42ea-a4ae-4fa3661b2fad/)
6. Once authorized, Aikido is successfully connected to Jira, enhancing your task management capabilities 🚀

![Image](https://ucarecdn.com/51974d9f-c08b-4886-96de-4c635f986a34/)

## ​Options for Task Creation in Jira via Aikido

There are two different options to create new tasks from Aikido into Jira.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation

1. Hover over any issue in your feed and click the ***+*** in the **assign column.** 

   ![Image](https://ucarecdn.com/0001b592-6b4b-4bbf-b3a8-ff8ddff44c51/)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.

   ![Image](https://ucarecdn.com/38576e60-ea82-4442-88d3-db09a3bbd539/)
2. Fill in the required details in the popup modal.\
   ​

   ![Image](https://ucarecdn.com/61e7326b-5183-4741-aaac-891ec98663fc/)
3. The newly created task in Jira will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Image](https://ucarecdn.com/294591ba-6d3d-4cfc-9cee-0fc1b6c880cd/)

## 2. Automated Task Creation

1. Go to the [Jira Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.

   ![Image](https://ucarecdn.com/a2cf62ba-d5ce-4053-a032-2f6f5f0b43ad/)

   ​
4. Aikido will then autonomously generate Jira tickets based on these settings 🚀

### Jira Sync Information

Aikido automatically syncs a couple of fields to Jira

- Severity is mapped to the 'Priority field' in Jira (one way)
- Assignees are synced both ways (so updates in Jira will be reflected in Aikido too)

---

### Setup Jira Integration Now →

### Discover Integration Details →

---