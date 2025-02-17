---
title: GitHub Container Registry
---


You can now integrate your Github Container Registry with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Github account to gather some data.

We'll have to gather your username (see screenshot)

![Image](https://ucarecdn.com/bcdcbd95-3e97-4fa5-823a-23e54cc5005d/)

\
**Step 2:** Copy the organisation name where the container registry resides. This is visible in the github-url (see screenshot)

![Image](https://ucarecdn.com/42637ec3-0ed2-4016-9418-29470dee6e88/)

**Step 3:** Under profile settings, developer settings, Personal access tokens, Tokens (classic), generate a new classic token for Aikido

(direct link: <https://github.com/settings/tokens>).

the scope includes: `read:packages`

![Image](https://ucarecdn.com/65b9dd8b-d552-46cc-b265-c9e0da804f01/)

\
**Step 4:** Enter the collected data in Aikido (direct link: <https://app.aikido.dev/settings/container-image-registry/add/github>)

![Image](https://ucarecdn.com/1030004f-c2f0-436e-9e0b-e1af4dbaa814/)

\
**Step 5:** Aikido will now find all container repositories you can access and list them.

**Step 6:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 7:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---

### Set Up GitHub Container Registry Scanning →

### Discover Integration Details →

---