---
title: Custom config - Private packages
---


When letting Aikido update your dependencies in repositories with private packages, Aikido would need to also have access to the private registries so that we can properly update your lockfiles. You can now provide secure environment variables, which will be encrypted and injected into your workflows. This means when our system detects vulnerabilities in dependencies, it can seamlessly authenticate with private registries, automatically patch the affected packages, and update the lockfiles, all while keeping your credentials safe.

## Configuration in Aikido

Once the prerequisites are fulfilled, you can configure aikido to authenticate with your private registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on "Manage private registry connection", the configuration modal will now be shown

   ![Image](https://ucarecdn.com/e2529564-caf7-4789-ba16-ed169db5c977/)
3. When you select 'Custom' you will now be able to enter the environment variables we need to complete the automated fixes in your repositories. In the example above we show a potential setup for private NPM registries 
4. Fill in the "key" and "value"  and add as many variables which are needed. Aikido will encrypt all values automatically for you.

## Example setups

### .npmrc

A common way to authenticate with private registries for JS libraries, is by including an `.npmrc` file in your repository to tell your package manager where to download a package from.\
\
Ensure that the `.npmrc` file in your repository contains the following example content, Aikido will be able to inject the NPM_TOKEN environment variable which you provided:

```
//npm.pkg.github.com/:_authToken=${NPM_TOKEN}
@pied-piper:registry=https://npm.pkg.github.com
```