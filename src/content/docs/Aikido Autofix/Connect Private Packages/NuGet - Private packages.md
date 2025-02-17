---
title: NuGet - Private packages
---


When letting Aikido update your dependencies in repositories with private NuGet packages, Aikido would need to also have access to the private packages so we can properly update your lockfiles. You can now provide private NuGet registry configuration in Aikido for this.

## Prerequisites

**Prepare nuget.config**

For private NuGet packages, Aikido uses a nuget.config file to authenticate with the private registry. This file will overwrite the nuget.config in root of the scanned repository. It is possible to configure multiple private registries in this file. 

Example nuget.config for accessing private packages on GitHub's NuGet registry:

```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />
    <add key="github" value="https://nuget.pkg.github.com/AikidoSec/index.json" />
  </packageSources>
  <packageSourceCredentials>
    <github>
      <add key="Username" value="AikidoSec" />
      <add key="ClearTextPassword" value="ghp_ABC123...XYZ" />
    </github>
  </packageSourceCredentials>
</configuration>
```

Take a look at the following docs for more information on authenticating with private NuGet registries.

- [Microsoft - Consuming packages from authenticated feeds ](https://learn.microsoft.com/en-us/nuget/consume-packages/consuming-packages-authenticated-feeds)
- [GitHub - Working with the NuGet registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-nuget-registry)

## Configuration in Aikido

Once the prerequisites are fulfilled, you can configure Aikido to authenticate with your private NuGet registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the Autofix in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on "Manage Private Registry Connection", the configuration modal will now be shown
3. Select "Nuget" as package manager

   ![Image](https://ucarecdn.com/ebfc1c1e-5524-4b4e-a527-6e1e8627b693/)
4. Fill in your nuget.config with authentication information. Aikido securely encrypts your configuration file until just before they are used. 
5. Click "Apply Changes" to save the configuration