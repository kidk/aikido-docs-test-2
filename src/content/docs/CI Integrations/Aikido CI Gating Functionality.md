---
title: Aikido CI Gating Functionality
---


### Introduction

CI gating is available for all of Aikido's CI integrations. With Aikido's CI Gating feature you can scan your feature branches for known vulnerabilities in **open-source software packages (CVE),** **IaC, Secrets** and **SAST**. 

> PR gating is mostly supported via native integrations. Release gating can be done with our CLI tool

### How does it work

**Setup configuration via Aikido dashboard or via Code**

Aikido supports 1-click configuration and management for [GitHub](https://help.aikido.dev/doc/github-ci-pr-gating-via-aikido-dashboard/docZayPeps1j) and [Azure](https://help.aikido.dev/doc/azure-pipelines-ci-pr-gating-via-aikido-dashboard/docVU0nLa09W) accounts via our Aikido dashboard. We recommend using this functionality as it allows for easy configuration, better overview and **does not** use CI minutes.

You can also set up CI gating **via code** for [GitLab](https://help.aikido.dev/doc/gitlab-ci-setting-up-gating-for-merge-requests/doco2l9FLm2k) and [Bitbucket Pipes](https://help.aikido.dev/doc/bitbucket-pipes-setting-up-gating-for-pull-requests/docl8wXHhcmn). If your integration is not in the list, you can still integrate by using our [Public CI API](https://help.aikido.dev/en/articles/8711075-aikido-ci-api).

**Checking results**

After running inside of your CI, Aikido will display a link with the scan results for this specific branch. Given we scan the specific branch (and **not** the entire repo again), **Aikido tells you about both fixed and newly introduced issues for this specific change**.

![Image](https://ucarecdn.com/406eb96c-3e89-4acb-9396-7cc60469b0e8/)

If Aikido detects an issue is fixed inside of a feature branch, it will be marked inside of Aikido's feed as "**PR open**", so you can easily verify an issue will be fixed even before merging a feature branch.

![Image](https://ucarecdn.com/8e9a6629-93f8-4f78-a264-732e5ff5351f/)

### Bypassing a failed state

In case you would like to bypass a failed state, this is possible by ignoring the issues that caused the CI gate to fail. You can do this by clicking the issue and in the top right **Actions menu** select Ignore or Snooze. This issue will then be ignored/snoozed in any future branches in your CI.

> Only users that have the permission to snooze or ignore issues can bypass the CI gate.

---