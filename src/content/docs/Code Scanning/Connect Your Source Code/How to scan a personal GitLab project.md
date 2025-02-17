---
title: How to scan a personal GitLab project
---

**Table of contents:**
  - [Step 1. Create a new group in GitLab](#step-1-create-a-new-group-in-gitlab)
  - [Step 2. Transfer your personal projects to the newly created group](#step-2-transfer-your-personal-projects-to-the-newly-created-group)
  - [Step 3. Connect the group to Aikido](#step-3-connect-the-group-to-aikido)


At this moment, Aikido only allows to scan projects which are linked to a group. Projects linked to your GitLab user are currently not supported. \
​\
If you'd like to enable code scanning on your personal GitLab projects, we recommend you create a personal group and transfer the projects there. To accomplish this, we recommend you follow the steps below.

### Step 1. Create a new group in GitLab

Login to your GitLab account, navigate to "Groups" in the left-hand side navigation and click on "New group". Follow the steps to create a group.

![Image](https://ucarecdn.com/6f7e4107-4a83-44b6-ae5c-f858a3b4ac78/)

### Step 2. Transfer your personal projects to the newly created group

Now, you can transfer your personal projects to the newly created group. To do this, navigate to the project's detail page and go to it's "General settings", which you can see in the left-hand side navigation. At the bottom you can expand the "Advanced" settings section.

![Image](https://ucarecdn.com/12819150-cf77-456d-95fc-21fcad9de857/)

\
At the bottom of this section, you can transfer this project to a different namespace.\
​

![Image](https://ucarecdn.com/968e99ba-c1be-4ccd-ac56-e243c658c35f/)

### Step 3. Connect the group to Aikido

Now that you transferred your new project to the new namespace aka "group", you can connect Aikido to that group and allow read-only acces to start scanning for vulnerabilities. \
​\
In Aikido, select the Group dropdown picker in the left-hand side navigation, and click on "Add another workspace".

![Image](https://ucarecdn.com/75339182-b6b1-4078-a9d1-e7d549c7bdc2/)

You will now go through the flow of connecting your newly created GitLab group to Aikido to grant read-only access to your personal projects.