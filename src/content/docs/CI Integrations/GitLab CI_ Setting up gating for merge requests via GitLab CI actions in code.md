---
title: GitLab CI_ Setting up gating for merge requests via GitLab CI actions in code
---


> We do not recommend using this functionality anymore, but use the MR gating via the Aikido Dashboard instead as it does not use CI minutes, easier management in bulk and less error-prone.

Aikido's integration with GitLab CI allows you to flag or block risky code from being merged. Our CI scans target **IaC**, **SAST**, **dependency issues, secrets** and **malware**.

### 1. Set up integration

**Step 1.** Go to our [CI integrations page](https://app.aikido.dev/settings/integrations/continuous-integration)

**Step 2.** Generate a new authentication token and make sure to copy it.

**Step 3.** Click GitLab CI

![Image](https://ucarecdn.com/6f26060e-c87d-465d-914d-45f31b38149d/)

By clicking on "GitLab CI" you will be redirected to the GitLab repo hosting the code to run the action, in the Readme, we give a few examples on how you can integrate the action into your pipeline.

### 2. Inject token into GitLab's CI environment

​As a final step, you need to make the authentication token available to the CI runner in GitLab.

First, you need to go to your group's Settings page and then navigate to the **CI/CD** sub-page.

![Image](https://ucarecdn.com/1dd37533-82d6-4a65-adba-561c2572416f/)

Click on 'Expand' next to variables and click on 'Add variable'. You can then add the authentication with the following configuration:\
​

![Image](https://ucarecdn.com/57cf3a27-4465-4005-9d1e-62c4f44d3eab/)

Paste the authentication token you copied in the previous step in the 'value' box and click on 'Add variable'.

> Note: it's important to uncheck the 'Protect variable' checkbox, as that will prevent the variable from being available on branches which do not have deletion protection (which would be often the case for CI checks).

> Note. Ensure that the repository you're scanning is part of the GitLab group that's linked with Aikido.

In case of any questions, you can always contact support for more information.

---

###

