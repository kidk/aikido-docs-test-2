---
title: Gitlab Self Managed Container Registry
---


You can now integrate your Gitlab Self Managed Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Gitlab account to gather some data.

We'll have to gather your username (see screenshot)

![Image](https://ucarecdn.com/ee118282-ecab-4687-8d5e-9885f6bf5aad/)

\
**Step 2:** Copy the group ID where the container registry resides (see screenshot)

![Image](https://ucarecdn.com/9c7c898a-dc4e-4169-82c2-708df1c479f1/)

\
**Step 3:** Under personal preferences, Access tokens, create a new token for Aikido (direct link: ). <https://gitlab.com/-/profile/personal_access_tokens>

The scopes included must be: read_api, read_registry

See screenshot:

![Image](https://ucarecdn.com/167e7af9-436c-43f9-a585-a6bd0d693234/)

\
**Step 4:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/gitlab-self>)

![Image](https://ucarecdn.com/1d74b1b9-dacb-49e5-840f-1d3e7e38ab6e/)

**Step 5:** Aikido will now find all container repositories you can access and list them.

**Step 6:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 7:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---