---
title: Autofix for GitHub, BitBucket, GitLab Cloud
---


Aikdo Autofix is a tool you can use to have Aikido fix vulnerabilities in 3rd party dependencies in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue.

### Supported Languages

Support for the auto-fixer at this time is limited to **Javascript** (Yarn, npm, pnpm)**, Java** (pom.xml)**, Go, PHP** (composer)**, Python, .NET** and **Ruby** repositories which are hosted on Github, Bitbucket, GitLab, [GitLab Self-Managed](https://aikido.outverse.com/doc/enable-aikido-autofix-for-gitlab-self-managed/docfdOyiUltZ) or [Azure DevOps](https://help.aikido.dev/doc/autofix-for-azure-devops/doc2EkfEcDFQ).

### Setting Up Autofix

**Step 1. Enable Autofix on the [Autofix Settings](https://app.aikido.dev/settings/integrations/autofix) page or go to [Autofix Page](https://app.aikido.dev/issues/fix) and click on Enable Autofix.**

![Image](https://ucarecdn.com/d1149bda-5055-45e6-afaf-a7b728bc33ef/)

**Step 2.** After installing the Aikido Autofix application, you can instruct Aikido to create these pull requests. This can either be done via the action menu in the **sub-issues table** in the sidebar or manage in bulk on the [Autofix page.](https://app.aikido.dev/issues/fix)\
​

![Image](https://ucarecdn.com/95ee20a4-3001-44f5-b66c-2e2c6beb9deb/)

We'll always explain beforehand what Aikido Autofix will be doing. In some cases, there are multiple ways we can fix an issue. In such a case you will be able to select the option you prefer.

![Image](https://ucarecdn.com/9ea84323-a443-43e6-af11-f2731479e179/)

When a fix is prepared, we'll present you with a modal with the commands we are running to install the requested fix. This way you'll be able to reproduce the creation of the pull request locally if needed. The modal can be closed while the process is still running.

![Image](https://ucarecdn.com/d3828ae3-cb1d-4332-9ee6-47a44c74e150/)

---

### Set Up Autofix →

---