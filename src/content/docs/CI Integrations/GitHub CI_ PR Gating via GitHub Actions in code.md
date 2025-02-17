---
title: GitHub CI_ PR Gating via GitHub Actions in code
---


> We do not recommend using this functionality anymore, but use the PR gating via the Aikido Dashboard instead as it does not use CI minutes, easier management in bulk and less error-prone.

Aikido's integration with GitHub actions allows you to flag or block risky code from being merged. Our CI scans target **IaC**, **SAST**, and **dependency issues**.

If you're on the Aikido Pro plan, you can also use this integration for setting up [CI Gating](https://help.aikido.dev/en/articles/7945775-setting-up-feature-branch-scanning).

### Set up integration

**Step 1.** Go to our [CI Integrations page](https://app.aikido.dev/settings/integrations/continuous-integration).

![Image](https://ucarecdn.com/57916740-54b9-41de-9f37-134250ceccd7/)

**Step 2.** Generate an authentication token. You will need to expose this in your CI environment for the integration. Make sure to copy the token in this step.

![Image](https://ucarecdn.com/a4860c4c-56c5-48c8-9953-a954060a0d0c/)

**Step 3.** Click on GitHub Actions

![Image](https://ucarecdn.com/a4797078-38f0-4c70-a018-a0a4b5b45bad/)

### Add the Github action to your project(s)

Next, its time to install the action in your projects. You can follow the instructions on the readme of the action, [found here](https://github.com/marketplace/actions/aikido-security-github-action).

This readme includes an explanation of all the options you can pass to the action as well as what they do. It also includes an example of the yaml file you need to include in your project's `.github/workflows` folder.

---