---
title: Scanning Frequencies
---


Aikido provides default scanning frequencies for various components to ensure security and performance. Here, you'll learn about these defaults and how to change them.

### Scanning Frequencies

- By default, for all paid plans, Aikido does **daily** scans for open-source dependencies, SAST, IaC, secrets, cloud, containers, and ZAP domains. 
- Domains scanned with Nuclei are by default **twice a week** as this has a higher load on your system.


- In case you quickly want to verify whether a fix was implemented correctly, you can trigger a **manual scan** by clicking 'Start Scan' in the UI.

  ![Image](https://ucarecdn.com/e678ed08-9cb8-4f4f-a651-7ca041202b17/)

> Workspaces on a free plan are scanned every 3 days, and users cannot trigger scans manually. Nuclei domains are scanned once a week.

### Changing Scanning Frequency

In case you want to change your scanning frequency, you can do this by going to [General Settings ](https://app.aikido.dev/settings/account)(admins only) and click **Change Scanning Frequency**.

![Image](https://ucarecdn.com/e91e1100-9205-4824-af06-f00bf304e481/)

 