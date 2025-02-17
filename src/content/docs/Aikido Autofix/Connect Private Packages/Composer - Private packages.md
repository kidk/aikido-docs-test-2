---
title: Composer - Private packages
---


When letting Aikido update your dependencies in repositories with private composer packages, Aikido would need to also have access to the private packages so we can properly update your lockfiles. You can now provide private Composer registry configuration in Aikido for this.

## Prerequisites

**Prepare auth.json**

For private Composer packages, Aikido uses a auth.json file to authenticate with the private registry. This file will overwrite the auth.json in root of the scanned repository. It is possible to configure multiple private registries in this file. 

Example auth.json for accessing private packages on GitHub's Composer registry:

```
{
    "github-oauth": {
        "github.com": "your-github-token"
    }
}
```

## Configuration in Aikido

Once the prerequisites are fulfilled, you can configure Aikido to authenticate with your private NuGet registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the Autofix in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on "Manage Private Registry Connection", the configuration modal will now be shown
3. Select "Composer" as package manager

   ![Image](https://ucarecdn.com/da027140-6320-4263-b008-47f6ec5ddde6/)
4. Fill in your auth.json with authentication information. Aikido securely encrypts your configuration file until just before they are used. 
5. Click "Apply Changes" to save the configuration