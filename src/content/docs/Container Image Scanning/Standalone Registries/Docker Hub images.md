---
title: Docker Hub images
---


You can now integrate your Docker Hub with Aikido to scan your containers for known vulnerabilities.

Follow the simple steps below to activate this feature:

**Step 1:** Log into your Docker Hub account and navigate to account settings, then security (direct link: <https://hub.docker.com/settings/security>)

**Step 2:** Create an access token with scope 'Read-only'.

**Step 3:** Back in Aikido, go to settings, then [containers](https://app.aikido.dev/settings/container-image-registry). Click 'Connect registry' and pick Docker Hub. Enter your organization namespace and your username, in case you want to scan your personal repositories and the access token from the previous step.\
​\
You can find you username by hovering over the avatar in the top navigation on the right, your username will then be shown in the selected text. In this case it's `aikidotestaccount`.

**Step 4:** Aikido will now find all container repositories you can access and list them.

**Step 5:** Repositories can be linked to a code repository in order to perform better deduplication of findings. This step is optional!

**Step 6:** In the action menu next to the registry, click 'scan repos in registry' to get started. Results will appear in the Feed!

---

### Set Up Docker Hub Integration →

### Discover Integration Details →

---