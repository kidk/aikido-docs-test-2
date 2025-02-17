---
title: Scanning Dev Dependencies for CVEs
---


> Aikido does continuously scan dev dependencies for malware. The following article relates to CVE scanning.

**By default**, Aikido will not report vulnerabilities for dependencies that are only installed on the developer machine. The assumption here is that they will not ship to production and won't impact the security of your live product. 

However, there are some cases in which scanning for dev dependencies might be a valuable addition to the other scans:

- Compliance reasons, including the software that is only available on the developer machines
- Sveltekit: packages are often marked as dev dependency although they make it into production.

We support **Javascript and Java**. 

### Enabling Dev Dependencies Per Repository

It is possible to enable dev depedency scanning on per repo basis. 

**Step 1.** Contact Aikido to enable the functionality. Quickest way to do this is contact us via chat.

**Step 2.** Go to the detail page of a specific repository and click '**Configure**'.

![Image](https://ucarecdn.com/b68f0f11-f4e3-4c53-aa1e-60949980d75e/)

**Step 3.** Scroll down in the modal to enable dev dependency scanning

![Image](https://ucarecdn.com/4c91b233-fb86-4085-b110-18ebc8a54155/)

**Step 4.** Manually trigger a rescan (or wait until the nightly scan) and see new issues coming in.