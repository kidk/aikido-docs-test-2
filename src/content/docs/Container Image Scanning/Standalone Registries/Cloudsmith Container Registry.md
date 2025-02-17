---
title: Cloudsmith Container Registry
---


You can now integrate your Cloudsmith's Container Registry with Aikido, to scan your images for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Cloudsmith account. And navigate to API Settings.

See screenshot below.

We'll have to gather an API Key. Direct URL: <https://cloudsmith.io/user/settings/api/>

![Image](https://ucarecdn.com/bb3a1b86-d787-4566-8712-e3ff29a8f9ed/)

You can copy the API key directly from this screen:

![Image](https://ucarecdn.com/bd01d550-c677-423f-9ebd-e9260b2833a2/)

\
**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/cloudsmith>)

![Image](https://ucarecdn.com/794eaef4-1fac-4a30-a710-c00889f12a8f/)

- **Username** can be found in your user account on top (see first screenshot above)
- **Organization Namespace** can be found here:

![Image](https://ucarecdn.com/9043f1ca-03bc-472a-a2b9-51763d085696/)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---