---
title: Harbor Container Registry
---


You can now integrate your Harbor Container Registry with Aikido, to scan your images for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** In Harbor, under Administration, then 'Robot Accounts', create a new Robot Account for Aikido that has access to the 'List repository', 'Pull Repository' and 'List Artifacts' scope. After creation, copy the secret, then the name from the table of robot accounts.

![Image](https://ucarecdn.com/034631db-6fb7-460f-8af3-57c5fa94db85/)

**Step 2:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/harbor>)

![Image](https://ucarecdn.com/22c23924-d0cf-4564-8a8c-97cc8173fcc1/)

**Step 3:** Aikido will now find all container repositories you can access and list them.

**Step 4:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 5:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---