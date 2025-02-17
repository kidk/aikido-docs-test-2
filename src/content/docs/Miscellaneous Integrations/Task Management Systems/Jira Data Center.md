---
title: Jira Data Center
---

**Table of contents:**
- [Introduction ](#introduction-)
- [Prerequisites](#prerequisites)
- [Connecting the Aikido App to Jira](#connecting-the-aikido-app-to-jira)
- [Options for Task Creation in Jira via Aikido](#options-for-task-creation-in-jira-via-aikido)
- [1. Manual Task Creation](#1-manual-task-creation)
- [2. Automated Task Creation](#2-automated-task-creation)
  - [Setup Jira Integration Now→ ](#setup-jira-integration-now-)
  - [Discover Integration Details → ](#discover-integration-details--)


***📋 Setting up automated task creation in Jira Data Center***

## Introduction

This article focuses on those companies that have Jira Data Center running (i.e., Jira on premise, different from [Jira Cloud](https://help.aikido.dev/en/articles/8680218-setting-up-automated-task-creation-in-jira-cloud)). The following one-time setup *per workspace* allows everyone in your Aikido organization to create issues directly in Jira On Prem.

Following use cases are supported :

- Automated Ticket Creation: Automatically create and push tickets to specified Jira projects for seamless tracking of security issues.
- Manual Ticket Addition: Manually add security issue tickets to Jira, ensuring targeted attention for critical vulnerabilities.

## Prerequisites

In order to make the connection to JIRA Data Center, you'll need to create a personal access token. This token will then be used to carry out all requests to your instance.\
​\
Please note that the level of access the integration has will be equal to the person who created the personal access token (PAT). It's therefore advised to let a person with sufficient access rights in the environment to create the PAT.

To create a PAT, you can follow the steps below:

1. Navigate to your JIRA Data Center environment
2. Click on your avatar in the navigation bar on top and navigate to "Profile"
3. Click on "Personal Access Tokens", you should end up on a screen similar to the one below\
   **​**

   ![Image](https://ucarecdn.com/bd8df7ef-3798-4bdb-acac-65a30ef15823/)
4. Click on "Create token" and give it an appropriate name
5. We advise to not set an expiry date, but if you do, you'll have to remind yourself to update the token in Aikido periodically
6. Once the token is created, you'll get to copy it momentarily, copy the token and keep it for the next step

## Connecting the Aikido App to Jira

1. Navigate to [Integration Settings](https://app.aikido.dev/settings/integrations) within the Aikido app.
2. In the 'Task Trackers' section, select 'Jira Data Center'
3. Enter the url of your environment
4. Enter the PAT from the previous step and hit "Save"\
   **​**

   ![Image](https://ucarecdn.com/f6f0b160-29a8-4940-8cd2-0a53e76f1741/)
5. Once authorized, Aikido is successfully connected to Jira, enhancing your task management capabilities 🚀

   ![Image](https://ucarecdn.com/3d9b5e8e-600d-467a-9683-1c80aa0e556f/)

## Options for Task Creation in Jira via Aikido

There are two different options to create new tasks from Aikido into Jira.

1. Manually create tasks from the Aikido interface
2. Automatically create new tasks via Aikido's auto creation functionality.

## 1. Manual Task Creation

1. Hover over any issue in your feed and click the *+* in the assign column. \
   **​**

   ![Image](https://ucarecdn.com/41b48dfa-4002-4038-85ac-35e0f21a5378/)

   \
   Alternatively, you can click the triple dots in the last columns to open up the action menu. If you have grouped issues, the triple dot action menu is available on every subissue.\
   ​

   ![Image](https://ucarecdn.com/8e0eca2d-bd15-4a1a-917e-c22a19b36547/)
2. Fill in the required details in the popup modal.\
   ​

   ![Image](https://ucarecdn.com/2601869d-3437-4823-b410-264c9eb9f8fb/)
3. The newly created task in Jira will be linked in the Aikido Issue Detail under the 'Tasks' tab (sidepanel).

![Image](https://ucarecdn.com/6fd5b53d-a667-4294-b410-5caecbb3552d/)

## 2. Automated Task Creation

1. Go to the [Jira Integration](https://app.aikido.dev/settings/integrations/tasktracker) settings
2. Make sure to enable 'Autocreation' by clicking the toggle to On.
3. Define the criteria for automatic task creation.\
   ​

   ![Image](https://ucarecdn.com/003436a4-f840-40c3-a362-f9f37b377cc1/)

   **​**
4. Aikido will then autonomously generate Jira tickets based on these settings 🚀

---

### Setup Jira Integration Now→

### Discover Integration Details →

---