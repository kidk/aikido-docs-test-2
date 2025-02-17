---
title: Image scanning for DigitalOcean Container Registry
---


You can now integrate your DigitalOcean Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your DigitalOcean account to gather some data.

We'll have to gather only a Personal Access Token (PAT). Direct URL: <https://cloud.digitalocean.com/account/api/tokens> (see screenshot below)

![Image](https://ucarecdn.com/34100e62-59be-4a33-902d-20c0ebbd4418/)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/digitalocean>)

![Image](https://ucarecdn.com/937e0175-88c2-4c79-94f8-d015e01bdf18/)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---