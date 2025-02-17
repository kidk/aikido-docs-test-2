---
title: Scaleway Container Registry
---


You can now integrate your Scaleway Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Scaleway account to gather some data.

We'll have to create an API key. Direct URL: <https://console.scaleway.com/iam/api-keys> (see screenshots below)

![Image](https://ucarecdn.com/3f7b7754-adbc-4804-94ef-440983cfddc7/)

![Image](https://ucarecdn.com/450023c8-2142-4d95-adf4-3a04e5fc81a6/)

![Image](https://ucarecdn.com/8372224e-4e80-46b1-9b6d-6cfb559de972/)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/scaleway>)

![Image](https://ucarecdn.com/4cab47d9-c92e-4555-9c51-ac0766b728f6/)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---