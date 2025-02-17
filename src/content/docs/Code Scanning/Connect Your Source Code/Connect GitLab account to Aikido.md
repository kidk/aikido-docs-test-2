---
title: Connect GitLab account to Aikido
---

**Table of contents:**
  - [Step 1. Logging in using GitLab](#step-1-logging-in-using-gitlab)
  - [Step 2. Creating a workspace, join an existing workspace or create a demo](#step-2-creating-a-workspace-join-an-existing-workspace-or-create-a-demo)
  - [Step 3. Connect a GitLab group to Aikido](#step-3-connect-a-gitlab-group-to-aikido)
  - [Step 4. Selecting groups & selecting repos](#step-4-selecting-groups--selecting-repos)
  - [5. Checking results](#5-checking-results)


Aikido requests read-only access to your GitLab group to analyze your projects. After analysis, your code is always wiped from the system. 

Aikido currently only supports scanning of projects which are linked to a group. Repositories not linked to a group, but linked to just your user can currently not be scanned. If you do have personal repositories which you'd like to have scanned, we recommend to create a personal group, or transfer them to a group you own.

### Step 1. Logging in using GitLab

To get started, navigate to <https://app.aikido.dev> and log in with GitLab. This will look like the screenshot below. Here, Aikido only requests access to your identity on GitLab and the associated email address.

![Image](https://ucarecdn.com/dd58925f-aa33-4b89-9e02-bd75cc1009ad/)

### Step 2. Creating a workspace, join an existing workspace or create a demo

After authorizing Aikido to read your personal GitLab information you get the following screen.

![gitlab_signup](https://ucarecdn.com/143adfc1-c0c6-4c71-8a3d-1bed03e7ca6a/)

On this page you can do one of 3 things:

- **Create a new workspace:** select this option if you want to connect a GitLab group to Aikido and start scanning your code repositories and clouds.
- **Join your team:** select this option if someone in your organization already connected a GitLab group to Aikido, and you'd like to get access to it
- **Use sample repo:** want to have a sneak peak of what Aikido looks like and what it can do? Create a demo account to get a taste of Aikido. You can always connect your GitLab group at a later moment

### Step 3. Connect a GitLab group to Aikido

If you would like to create a new workspace, Aikido will need **read-only access** to your projects and groups. We will therefore redirect you back to GitLab so you can authorize Aikido.

**Note.** This does *not* give access to the actual repos yet. Selecting which ones you want to have scanned is in the step after this one.

![Image](https://ucarecdn.com/b461947a-bf2e-4a4e-936a-84efb59a1f48/)

### Step 4. Selecting groups & selecting repos

After authorizing Aikido to read your groups and projects, you can select which group you'd like to connect to Aikido.

**Note:** Aikido will include any subgroups of the GitLab group you selected in the workspace

![Image](https://ucarecdn.com/f0dad506-48d9-4216-a102-80051d6019b3/)

\
​After selecting the groups of choice, you can choose which repositories you want to give access to.

![Image](https://ucarecdn.com/b7b4ee31-ffac-48a6-8c1e-282fe833ca81/)

### 5. Checking results

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in!