---
title: GitLab Registry - Private packages
---


When letting Aikido update your dependencies in repositories with private packages, Aikido would need to also have access to the private packages so that we can properly update your lockfiles. You can now provide private package configuration in Aikido for this.

For now only this is only supported for JavaScript dependencies.

## Prerequisites

### NPM

For NPM and PNPM package managers, your repository must include an `.npmrc` file at the root of the repository with some configuration to tell npm which packages to download from your private registry.

If your private package names look like this: `@pied-piper/***` and are hosted on GitLab's npm registry, your file should look something like this:

```
@pied-piper:registry=https://<domain_name>/api/v4/projects/<project_id>/packages/npm
```

Aikido can then inject the token when its updating the dependencies. You can find more info about it from NPM [here](https://yarnpkg.com/configuration/yarnrc#npmScopes).

### YARN

We currently only support Yarn 3 and up versions when updating dependencies in projects with private packages. This means that your repository must include a `.yarnrc.yml` configuration file containing some basic configuration to download the private packages.

If your private package names look like this: `@pied-piper/***` and are hosted on GitLab's npm registry, your `.yarnrc.yml` file should already contain the following snippet:

```
npmScopes:
  pied-piper:
    npmRegistryServer: "https://<domain_name>/api/v4/projects/<project_id>/packages/npm"
```

Aikido can then inject the token when its updating the dependencies. You can find more information from Yarn [here](https://yarnpkg.com/configuration/yarnrc#npmScopes).

## Configuration in Aikido

Once the prerequisites are fulfilled, you can configure aikido to authenticate with your private registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on "Manage private registry connection", the configuration modal will now be shown

   ![Image](https://ucarecdn.com/6e1328d4-8880-41ed-84e5-cfacc415fdc4/)
3. First fill in the host.
4. Fill in the token used to authenticate. Find more information about generating a token in GitLab [here](https://docs.gitlab.com/ee/user/packages/npm_registry/index.html#authenticate-to-the-package-registry).
5. Click "Save" to save the configuration