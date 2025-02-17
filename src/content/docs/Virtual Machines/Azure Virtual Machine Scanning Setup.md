---
title: Azure Virtual Machine Scanning Setup
---


> This functionality is currently behind feature flag and available for Scale plans only. [Contact us](https://www.aikido.dev/contact) for more information.

### Why should I scan my virtual machines?

With virtual machine scanning, Aikido can scan the hard drives of your virtual machines for vulnerable packages, outdated runtimes and risky licenses. 

### Getting started

To enable the scanning of your virtual machines on Azure, you should first start by connecting your Azure Cloud to Aikido. To do this you can follow the steps outlined in [this article](https://help.aikido.dev/doc/connect-azure-cloud-account-to-aikido/docJek8tWcLd).\
\
Once your cloud is connected, you'll see a tab appear on the detail page called 'Virtual Machines'.

![Image](https://ucarecdn.com/73f430a6-1621-4290-b258-dc4d89a3696b/)

When you click on 'Set Up VM Scanning' we'll take you to the following page:

![Image](https://ucarecdn.com/8fe87a31-930a-43ab-a32c-6199bf0d4320/)

The setup wizard will guide you through creating a new App Registration inside of the Azure Portal with an API secret specifically for Aikido.

The API secret will be used by Aikido to make the necessary API requests to scan your resources. Aikido will notify you via email when the secret is about to expire.

Only the bare minimum of permissions are granted to the App Registration. This ensures that Aikido can perform its security checks without the risk of unintended altering of your resources.

Once you click 'save', Aikido will immediately start to discover any virtual machines in your account and scan them.