---
title: GitHub Registry - Private packages
---


When letting Aikido update your dependencies in repositories with private packages, Aikido would need to also have access to the private packages so that we can properly update your lockfiles. You can now provide private package configuration in Aikido for this.

For now only this is only supported for JavaScript dependencies.

## Prerequisites

### NPM

For NPM and PNPM package managers, your repository must include an `.npmrc` file at the root of the repository with some configuration to tell npm which packages to download from your private registry.

If your private package names look like this: `@pied-piper/***` and are hosted on GitHub's npm registry, your file should look something like this:

```
@pied-piper:registry=https://npm.pkg.github.com
```

Aikido can then inject the token when its updating the dependencies. You can find more info about it from NPM [here](https://yarnpkg.com/configuration/yarnrc#npmScopes).

### YARN

We currently only support Yarn 3 and up versions when updating dependencies in projects with private packages. This means that your repository must include a `.yarnrc.yml` configuration file containing some basic configuration to download the private packages.

If your private package names look like this: `@pied-piper/***` and are hosted on GitHub's npm registry, your `.yarnrc.yml` file should already contain the following snippet:

```
npmScopes:
  pied-piper:
    npmRegistryServer: "https://npm.pkg.github.com"
```

Aikido can then inject the token when its updating the dependencies. You can find more information from Yarn [here](https://yarnpkg.com/configuration/yarnrc#npmScopes).

## Configuration in Aikido

Once the prerequisites are fulfilled, you can configure aikido to authenticate with your private registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on "Manage private registry connection", the configuration modal will now be shown\
   ​

   ![Image](https://ucarecdn.com/363f11da-763a-4c1f-a6a7-dd93c268d4a3/)
3. First fill in the host. Eg: If you are using GitHub's npm registry you need to fill in the host, being: `npm.pkg.github.com` without the url scheme.
4. Fill in the token used to authenticate. In case of GitHub's npm registry, you will need to create a Personal Access Token and enter that. Aikido securely encrypts any tokens until just before they are used. Find more information about GitHub's registry [here](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-npm-registry#authenticating-to-github-packages).
5. Click "Save" to save the configuration

---

###

