---
title: Autofix for Azure DevOps
---



**Introduction**

Aikdo Autofix is a tool you can use to have Aikido fix vulnerabilities in 3rd party dependencies in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue.

**Setup Autofix for Azure DevOps**

> All users within your workspace will need to setup Autofix individually. 

By default, Aikido only has read access on your Azure DevOps instance. To use Aikido Autofix, a separate access token with write access is required. Please make sure that "Third-party application access via Oauth" is enabled for your organization, by going to "Organization settings" and then clicking "Policies".

![Image](https://ucarecdn.com/de2304d7-85d2-4b8b-8d71-24259117f59d/)

**Step 1. Enable Autofix on the [Autofix Settings](https://app.aikido.dev/settings/integrations/autofix) page or go to [Autofix Page](https://app.aikido.dev/issues/fix) and click on Enable Autofix.**

![Image](https://ucarecdn.com/9ac87091-7eef-4f05-86a1-a137f2ddf68c/)

**Step 2.** Click **Authorize** 

![Image](https://ucarecdn.com/8a0e9ba1-c135-4e5f-a37b-3de7ddee86d0/)

**Step 3.** Grant Aikido permissions to **Write**

![Image](https://ucarecdn.com/ad9f2ecc-7a4f-4c78-8e74-2429a4b8e7a8/)

**Step 4.** Click save and you are all set. You will now be able to execute autofix PRs from the [Autofix page](https://app.aikido.dev/issues/fix) or from the action menu for subissues in the sidebar ([read more here](https://help.aikido.dev/doc/autofix-page/docojS5DmO5M)).