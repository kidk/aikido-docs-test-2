---
title: Gitlab Container Registry
---


You can now integrate your (cloud) Gitlab Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Gitlab account to gather some data.

We'll have to gather your username (see screenshot)

![Image](https://ucarecdn.com/7a56ad48-6f3c-4291-97c1-b36896ef0de0/)

\
**Step 2:** Copy the group ID where the container registry resides (see screenshot)

![Image](https://ucarecdn.com/d24c6206-b2dc-46f9-9853-088e55e58f1f/)

**Step 3:** Under personal preferences, Access tokens, create a new token for Aikido (direct link: <https://gitlab.com/-/profile/personal_access_tokens>).

The scopes included must be: read_api, read_registry

See screenshot:

![Image](https://ucarecdn.com/3517ec50-78f0-4a11-b196-5c0652c97a93/)

**Step 4:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/gitlab>)

![Image](https://ucarecdn.com/88cde87d-a1da-4a9a-9443-f1befbf61c9f/)

**Step 5:** Aikido will now find all container repositories you can access and list them.

**Step 6:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 7:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---