---
title: Support for Multi-Branch Scanning
---

**Table of contents:**
  - [Use Cases](#use-cases)
- [Prerequisites](#prerequisites)
- [Adding multiple branches](#adding-multiple-branches)


Multi-branch scanning in Aikido allows developers to scan multiple legacy branches at the same time or is useful when you want to scan both your staging and production environment at the same time. You can add as many branches as you want. This is typically used when branches exist for months and continuous scanning is needed. 

### Use Cases

- You have old legacy branches that needs nightly scanning (eg branch V3, branch V4), that live in parallel, and you want to scan both as separate projects, even though they are in the same repository. 
- You want to continuously monitor your staging and production environments

> In case you are looking to scan feature branches that get merged within a couple of days or weeks, we suggest looking into our [CI gating functionality](https://help.aikido.dev/section/setting-up-ci-integrations/sg3q6UrIf4qE).

## Prerequisites

Multi-branch scanning needs to be enabled for your account. Contact us.

## Adding multiple branches

**Step 1:** Navigate to your repository's detail page and click on the current branch name (often tagged master). This action will open a modal window.

![Image](https://ucarecdn.com/fa3fe901-f8fd-44ea-8489-e354dcebf016/)

**Step 2:** Click 'Scan multiple branches.’\
​

![Image](https://ucarecdn.com/f32721ac-7cc7-469a-af70-1a47866fcd5a/)

**Step 3:** Enter the name of the branch you wish to add to the scanning process.\
​

![Image](https://ucarecdn.com/15130a0a-8e38-41fd-b271-ac0803c98b65/)

**Result:** Aikido clones the specified repo and scans the repository nightly, or you can trigger a scan manually for instant results. A label will appear next to the cloned repo so you know which repo contains which branch that is being scanned.

**Looking to scan more than 2 branches?** You can go into any of the repositories and go through this process again.

![Image](https://ucarecdn.com/3b2e2e4c-407b-46e4-b4f7-96ba226eb282/)

> Note: It's important to note that secret scanning is conducted only on the initial repository. This is because the secret scanning feature is designed to automatically cover all branches by default.

---