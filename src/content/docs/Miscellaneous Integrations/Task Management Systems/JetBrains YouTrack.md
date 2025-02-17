---
title: JetBrains YouTrack
---


*📋 Setting up automated task creation in JetBrains YouTrack*

## Introduction

This one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in YouTrack.

Following use cases are supported :

- **Automated Ticket Creation**: Automatically create and push tickets to specified YouTrack projects for seamless tracking of security issues.
- **Manual Ticket Addition**: Manually add security issue tickets to YouTrack, ensuring targeted attention for critical vulnerabilities.

## Connecting the Aikido App to YouTrack

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'YouTrack'\
   A modal will request the **Service URL** (of your YouTrack space) and the **Permanent Token**. The permanent token can be generated inside Profile -&gt; Account Security in YouTrack.\
   ​

   ![Image](https://ucarecdn.com/4b2cd46d-fffe-4903-8c91-3b2f596a08d0/)
3. When you have filled in the credentials correctly, the 'Connected' status will appear.\
   ​

   ![Image](https://ucarecdn.com/6e0c61d5-f127-47e0-b0ba-79421e6a7dc6/)
4. Close the modal & open the YouTrack Integration page.\
   ​

![Image](https://ucarecdn.com/25cdca08-8e72-4031-af44-301e755dc12c/)

## Options for Task Creation in YouTrack via Aikido

There are two different options to create new tasks from Aikido into YouTrack.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

### 1. Manual Task Creation

1. Hover over any issue in your feed and click the ***+*** in the **assignee column.** \
   ​

   ![Image](https://ucarecdn.com/fd1bad1c-19b7-41d9-ba08-683817d37328/)

   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Image](https://ucarecdn.com/8642287d-0d10-46bf-9d0d-d25cf159d51d/)

   \
   ​
2. Fill in the required details in the popup modal.\
   ​

   ![Image](https://ucarecdn.com/98ce3ad1-5aca-4912-b986-17f2e2dc385c/)
3. The newly created task in YouTrack will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).\
   ​

   ![Image](https://ucarecdn.com/df00a756-237c-4b53-949c-a66b981c5a56/)

### 2. Automated Task Creation

1. Go to the [YouTrack Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings page
2. Make sure to enable '**Autocreation**' by clicking the toggle to **On.**
3. Define the criteria for automatic task creation.\
   ​

   ![Image](https://ucarecdn.com/664f2728-c619-4a8c-8cde-32b8a1abaf16/)

   ​
4. Aikido will then autonomously generate YouTrack tickets based on these settings 🚀\
   ​