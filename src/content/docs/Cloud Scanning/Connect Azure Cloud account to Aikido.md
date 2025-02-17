---
title: Connect Azure Cloud account to Aikido
---


Securing your cloud infrastructure is crucial to protecting your data. You can leverage Aikido's security checks to detect and address any misconfigurations in your infrastructure.

To view the list of security checks performed by Aikido on your cloud environment, go to the 'checks' tab on the [cloud overview page](https://app.aikido.dev/clouds) at. Filter to Azure to see specific checks performed on your connected Azure project(s).

To get started, head to the [cloud overview page](https://app.aikido.dev/clouds) on Aikido and click 'Connect cloud.' Follow the step-by-step setup wizard to connect your Azure project with Aikido.

![Image](https://ucarecdn.com/f88c44cf-5188-4504-aa2a-6f900ed8a78c/)

The setup wizard will guide you through creating a new 'App registration' inside of the **Microsoft Entra ID service** with an API secret specifically for Aikido. In the last step, you'll assign specific reader roles ("Security reader", "Log analytics reader") to grant limited, read-only access to specific services in your Azure cloud. This ensures that Aikido can perform its security checks without the risk of unintended modifications to your resources.

The API secret will be used by Aikido to make the necessary API requests to scan your resources. Aikido will notify you via email when the secret is about to expire.

Finally, you can name your connected project in Aikido and specify the environment it operates in (development, production,..). This information helps Aikido prioritize findings based on the severity and impact to your business.

![Image](https://ucarecdn.com/6bdf014a-abc6-4d69-9f8d-c90724e58850/)

Within 1-2 minutes after connecting your account, Aikido will report misconfigurations that could pose a threat.

---

### Set Up Azure Cloud Integration →

### Discover Integration Details →

---