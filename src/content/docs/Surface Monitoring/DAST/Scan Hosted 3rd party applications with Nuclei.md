---
title: Scan Hosted 3rd party applications with Nuclei
---


Aikido's surface monitoring is built on top of [ZAP](https://help.aikido.dev/en/articles/8040614-surface-monitoring-scan-your-domain-names-with-owasp-zap) and Nuclei, a tool designed to provide an attacker's point of view on your hosted infrastructure. It probes your web-available services for known vulnerabilities, enhancing the security of your digital assets.

### What is Surface Monitoring Scanning?

Surface monitoring with Nuclei inspects all the externally-facing components of your infrastructure. It focuses on services like your GitLab server, WordPress website, and hosted Confluence server, among others. This approach helps identify vulnerabilities from an attacker's perspective, ensuring robust security.

### Overview of Checks Performed by Nuclei

To understand the checks performed by Nuclei, visit our [checks overview page](https://app.aikido.dev/domains/checks?scanner=nuclei). Here, you will find a comprehensive list of all the vulnerabilities and misconfigurations that Nuclei can detect.

## Add a domain to be scanned with Nuclei

**Step 1:** Navigate to the [Domains Overview Page](https://app.aikido.dev/domains) or [Domains Settings](https://app.aikido.dev/settings/domains) and select **Hosted App**

![Image](https://ucarecdn.com/698baacd-d5cf-4446-9ca8-4c68e2bf3007/)

**Step 2:** Enter the service URLs of your web-available services in the configuration form. You can specify full paths and subpaths.

**Step 3:** Select technologies that you want to scan for. 

*Example on how to select technologies.* If your webshop is built in Magento, you can select Magento, PHP and nginx. You can select up to 4 technologies to scan for. If you want to have more information on the checks done for each technology group, visit the [checks overview page.](https://app.aikido.dev/domains/checks?scanner=nuclei)

![Image](https://ucarecdn.com/7612a940-577b-4105-ab62-0db6ab39ad29/)

Once you've completed the form. simply start a scan for your this domain. The Surface Monitoring Scanner will then get to work, scanning your software surface for any signs of potential threats and report the issues in your feed. All issues can also be viewed in the domain detail page.

---

### Set Up Surface Monitoring →

