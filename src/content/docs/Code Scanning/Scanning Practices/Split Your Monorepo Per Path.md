---
title: Split Your Monorepo Per Path
---


> This functionality is **only** available for GitLab (Cloud/On-Prem) and Azure DevOps (Git/TFVC).  For **GitHub and other integrations** we recommend using [this alternative](https://help.aikido.dev/doc/assign-team-responsibilities-by-specific-path-in-repo/docq5lO69L3V).

Aikido allows you to split up your large repositories / monorepositories per path, improving the overall management of your security issues.

## Use Cases

- Ideal for projects with a large main repository containing numerous subdirectories managed by different teams.
- Facilitates a clearer overview within Aikido by dividing large repositories into smaller, more manageable parts.
- Increase scanning speed. Giant repos often take a lot of time to scan.

## Prerequisites

- Only available for **Pro Plans**. Contact Aikido in order to enable this functionality.
- Supports **SCA, SAST,** and **IaC** scans only. Secret scanning is not available for split repositories.

## How to split up your repositories

**Step 1:** Go to the repository detail page and add `/split` to the end of its URL in the browser's address bar (e.g., `https://app.aikido.dev/repositories/330080/split`*).* This will direct you to the page allowing you to split your repository.

![Image](https://ucarecdn.com/1acc303c-9047-47c6-90a4-8997e18de9e1/)

**Step 2:** Enter the split points. These are the paths within your repository that you wish to separate. Input all the paths you want to see as individual entities.\
​\
​

![Image](https://ucarecdn.com/7eb2ed38-070e-4182-9875-dfbb27d99557/)

**Step 3:** Select ***Split repo***. This action deactivates the original repository configuration and divides it into smaller repositories for scanning. You can view all these in the [**repository overview**](https://app.aikido.dev/repositories). All specified paths will be shown with a **tag** next to the original repo name.

![Image](https://ucarecdn.com/da0abeab-31ee-4f9c-ba0b-937d6dd8622e/)

**Step 4.** Assign different subpaths to different teams. More information on how to set up teams and assign responsibilities can be found [here](https://help.aikido.dev/en/articles/9005606-using-teams-for-repository-and-user-management).

> Notes: You can add new paths at a later stage. You can do this by going again to the base repo from where it was split. Do not add the already existing paths, new ones are sufficient.

---