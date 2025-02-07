---
title: GitLab Self-Managed Integration for Authentication and User Management
---


### Introduction

If your organization uses GitLab self-managed, it's not possible to authenticate via the Git provider. In those cases, we allow Gmail and Office365 logins.

### Onboarding of Users

**Manually invite via email (default)**: You can invite users via the Aikido platform on the specified email, and the user will be able to access Aikido directly.

---

**Auto-onboarding**: Aikido can check whether the email that is being used for login is available in the GitLab instance. This is based on adding trusted domains. **Contact us** to help in setting this up or go to your Workspace settings and click 'Add Trusted Domain'.

![Image](https://ucarecdn.com/d7cc579b-0475-45a3-9120-f05797054408/)

> ​Important notes on auto-onboarding
>
> - All users will need to have their 'public email' field exposed. Currently, GitLab does not allow yet to force this upon all users ([more info](https://gitlab.com/gitlab-org/gitlab/-/issues/9828)).
> - The email used for login and the email in the 'public email' field need to be exactly the same. Aliases are currently not supported.