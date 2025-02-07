---
title: GitLab Integration for Authentication and User Management
---


### Introduction

When you create an Aikido workspace based on GitLab Cloud version, you select a GitLab Group. The Aikido workspace will consist of the main group and all its subgroups and underlying repositories.

### Benefits

- **Automatic Onboarding:** From that point on, other GitLab members of this group will be able to onboard Aikido automatically. Note: this only on the condition that they have at the least 'reporter', 'developer', 'maintainer' or 'owner' level of access to this group. 'Guests' will not be able to get in.
- **Effortless Offboarding:** When a member is removed from your GitLab Instance, they automatically lose access to the Aikido workspace. Aikido will sync access every night and auto-offboard members that are no longer active in your GitLab instance.

### Adding multiple GitLab Groups in a single Aikido Workspace

By default, a new workspace will be created for every GitLab group. If you want to have multiple GitLab groups inside 1 Aikido workspace, you need to create a root-level group in GitLab that contains all the subgroups.

### Inviting users to Aikido without an organisational GitLab account

You can invite users via Google, Microsoft or using a personal GitLab Account. More information can be [found here.](https://help.aikido.dev/doc/invite-users-to-aikido-without-a-git-account/docqM7btfSwK)