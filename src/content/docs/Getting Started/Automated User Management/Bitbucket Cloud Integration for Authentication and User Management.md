---
title: Bitbucket Cloud Integration for Authentication and User Management
---


### Introduction

Aikido ensures a one-to-one mapping with this Bitbucket Workspace, including repositories and teams. This streamlines the onboarding and offboarding processes within Aikido.

If you have multiple Bitbucket workspaces, you can connect these by setting up multiple Aikido workspaces.

> For automatic onboarding to work, developers need to have access to all repos. If you want to give access to a developer with limited access to repos in Bitbucket, we suggest inviting them [via Google/Microsoft](https://help.aikido.dev/doc/invite-users-to-aikido-without-a-git-account/docqM7btfSwK).

### Benefits

- **Automatic Onboarding:** After initial connection with Bitbucket, all Bitbucket members of this group will be able to onboard Aikido automatically, on the condition they have access to **all repositories** in this Bitbucket workspace.
- **Effortless Offboarding:** Aikido will sync access every night and auto-offboard members that are no longer active in your Bitbucket Workspace. This means that when a member is removed from the Bitbucket Workspace, they automatically lose access to the Aikido Workspace too.
- **Synchronization of Teams:** Aikido replicates your Bitbucket team structure (i.e. User Groups in Bitbucket). Groups need to have access to repositories in order to connect responsibilities of repositories to the teams in Aikido.
- **Daily Syncing**: Currently, Aikido updates the team structures, repositories and access permissions on a daily basis.

### Inviting users to Aikido without an organisational Bitbucket account

You can invite users via Gmail, Microsoft or using a personal Bitbucket Account. This can be helpful when a developer only has limited access in Bitbucket. More information can be [found here.](https://help.aikido.dev/doc/invite-users-to-aikido-without-a-git-account/docqM7btfSwK)