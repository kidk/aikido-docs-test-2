---
title: Scan Front-End App domains with ZAP
---


Aikido's surface monitoring is built on top of ZAP and [Nuclei](https://help.aikido.dev/en/articles/8880098-surface-monitoring-scan-3rd-party-applications-that-you-host-with-nuclei). Aikido uses these to monitor your app's public attack surface by probing your domain names for weaknesses.

### What is Surface Monitoring Scanning?

Surface monitoring, sometimes better known as Dynamic Application Security Testing (DAST) inspects all the externally-facing components of your software, including the application programming interfaces (APIs), web pages, data transfer protocols, and other user-facing features.

### Overview of checks performed

To see the checks performed by the Surface Monitoring Scanner, visit our [checks overview page](https://app.aikido.dev/domains/checks). Here, you'll find a detailed list of all the checks performed during the scan. Aikido will only perform safe, non-destructive automated test (eg no automated SQL injection attempts,..).

### Add a domain to be scanned with ZAP

**Step 1:** Navigate to the [Domains Overview Page](https://app.aikido.dev/domains) or [Domains Settings](https://app.aikido.dev/settings/domains) and select **Front-End App**

![Image](https://ucarecdn.com/80dde2cc-77cb-4640-80f4-1396cd93f0ee/)

**Step 2:** Fill in the service URL for the repositories which have public-facing domains by filling out the configuration form. You can specify full paths.

**Step 3: Optional**: link your domain to a repository or domain

**Step 4: Optional:** set the sensitivity of the data

![Image](https://ucarecdn.com/a4ab6998-734b-42fe-9329-da2fd7536aa6/)

---

### Set Up Surface Monitoring →

---