---
title: Autofix for Open Source Dependencies
---


Aikido Autofix is a tool you can use to **automatically fix vulnerabilities in open source dependencies** in your projects. It will do this by creating pull requests that remove the vulnerability via package updates or by other means. In some cases an Aikido Autofix can remove a whole class of vulnerabilities instead of just 1 issue.

***Note.*** If you are using Aikido Local Scanner, you will not have access to this functionality and this will be hidden in sidebar.

### Autofix Overview Page

Aikido allows you to easily create PRs for multiple version upgrades and fixes at the same time. By grouping per repo and lockfile, we ensure that PRs never get to large and are able to be merged without breaking certain parts of the app.

**Important.** By default, Aikido will always give you the minimum version required to do the fix, never a higher one. This means we prioritise minor version bumps always over the major ones, ensuring there are not too many breaking changes on your side. If a major upgrade is proposed, it is because a minor version upgrade would not fix the issue at hand.

![Image](https://ucarecdn.com/6b1cd879-9709-4df0-8f9f-23855e0f9d38/)

### Autofix options

When creating an autofix, multiple options will be presented to you.

- **Upgrade all packages**: upgrades all packages and will contain major, minor and patch upgrades.
- **Minor and Patch Versions Only:** upgrades minor and patch versions only
- **Critical Issues only:** these are the critical issues as defined by Aikido. These can contain major, minor and patch upgrades.

![Image](https://ucarecdn.com/3c94580b-c7a2-48cd-a31c-c45b72dcea99/)

After you will be shown with a progress window (bottom right) on the state of the PR creation. You will receive an update once the PR is ready.

![Image](https://ucarecdn.com/16361918-0a43-4db3-b7ff-f250361d5fae/)

### Example of setting up autofix and creating your first PR

[Video](https://ucarecdn.com/4d1a26c8-3ccf-4762-818c-e3430058f9a9/)
