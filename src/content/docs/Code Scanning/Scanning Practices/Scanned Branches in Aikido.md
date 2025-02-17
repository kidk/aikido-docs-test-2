---
title: Scanned Branches in Aikido
---


### Single-Branch Scanning

By default, Aikido will scan the default branch in your repository for dependency and code issues. The default branch is usually main/master. **Aikido runs a full scan of all repos, clouds, containers and domains every night**.

If you update the default branch, Aikido will pick up this change during its nightly sync, so no changes are needed on Aikido's end.

In some cases, it might be interesting to scan another branch instead of the default branch. This could be the case if you are developing on another branch for an extended period of time. You can overwrite the branch being scanned on the repository detail page in Aikido by clicking the branch button at the top.

![Image](https://ucarecdn.com/769bdbd4-5ab6-4248-a382-b6e56af0438e/)

A modal will appear that will allow you to change the branch being scanned every night.

![Image](https://ucarecdn.com/b460fe90-cd2f-41b8-bb40-b54fb7f7aaa1/)

## Multi-Branch Scanning

If you are looking to scan multiple branches of the same repo on a regular basis, you can contact us to enable Multi-Branch Scanning for you. This is only available for Paid Plans. Please check whether multi-branch scanning is right for you [by checking the use cases in this article](https://help.aikido.dev/doc/support-for-multi-branch-scanning/docmidd23LFZ).