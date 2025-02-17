---
title: Autofix for GitLab Self Managed
---


**Introduction**

Aikdo Autofix is a tool you can use to have Aikido fix vulnerabilities in 3rd party dependencies in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue.

**Setup Autofix for GitLab Self Managed**

By default, Aikido only has read access on your Gitlab Self Managed instance. To use Aikido Autofix a separate access token with write access is required.

**Step 1. Enable Autofix on the [Autofix Settings](https://app.aikido.dev/settings/integrations/autofix) page or go to [Autofix Page](https://app.aikido.dev/issues/fix) and click on Enable Autofix.**

**Step 2.** Click **Authorize**, and you will see this modal:

![Image](https://ucarecdn.com/847dce22-b557-4a36-8592-c8b97e558f46/)

**Step 3.** Head over to your Self Managed Gitlab account. Click on your personal account icon top left and go to preferences.

![Image](https://ucarecdn.com/1aa79b23-ea0e-473c-beb6-e60b3ff03d73/)

**Step 4.** In the sidebar, select Access Token. Then click the "Add new token"-button

![Image](https://ucarecdn.com/696b35be-f6ea-4bce-978d-0bede8b663ee/)

**Step 5.** Name the token 'Aikido Autofix' and add the following permissions: `api` & `write_repository`

![Image](https://ucarecdn.com/0a39f5aa-0e23-4e69-91a3-c94163f81db7/)

**Step 6.** Copy the newly created token and paste it into the modal in Aikido.

![Image](https://ucarecdn.com/75bb003e-2ebf-4687-8b8c-3c6049717027/)

![Image](https://ucarecdn.com/c1669df1-17da-4e97-b521-c71fc46b8e5d/)

**Step 7.** Click save and you are all set. You will now be able to execute autofix PRs from the [Autofix page](https://app.aikido.dev/issues/fix) or from the action menu for subissues in the sidebar.

---