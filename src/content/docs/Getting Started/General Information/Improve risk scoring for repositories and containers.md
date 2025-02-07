---
title: Improve risk scoring for repositories and containers
---


**Setting repo and container sensitivity to reduce noise**

Aikido allows you to add contextual info to all your repositories and containers to improve noise reduction. This info can help Aikido uncover more security risks and improves issue scoring. For example

- Adding info about the data sensitivity of each repo improves prioritisation and reduces noise. An issue found in a code repo that is responsible for handling personal information will be scored higher than a repo that never touches any sensitive data.
- Adding a domain name can allow Aikido to scan for issues including SSL, cookie misconfiguration, XSS attacks,.. 

### Configure Repository and Container Sensitivity

**Step 1.** Navigate to [Repositories](https://app.aikido.dev/repositories) overview or [Container](https://app.aikido.dev/containers) overview

**Step 2.** Click on the triple dots to open the action menu and select **Configure**

![Image](https://ucarecdn.com/832117bd-88d8-403a-abf1-9745f3379814/)

**Step 3.** A modal pops up with different settings.

![Image](https://ucarecdn.com/7e404a94-3fa2-4f4e-8b21-cac89328170f/)

- **Connection to the internet**: For each repository, you can specify whether the service/repository is connected to the internet via HTTP(S). There are three options:
  - Yes: Select this option if the repository is accessible over the internet using HTTP(S).
  - No: Choose this option if the repository is not connected to the internet.
  - Unknown: If you're unsure about the repository's internet connection status, select this option.

- **Specify the Domain** (if applicable): If the repository is connected to the internet, you can provide the domain of the service (e.g., <https://example.com>). This will activate Aikido's dynamic testing for surface monitoring (DAST). This is powered by OWASP ZAP.
- **Setting Sensitivity Levels**
  - Choose Sensitivity Level: Aikido allows you to define the sensitivity level of the data managed by each service/repository. This helps tailor the scanning process to the importance of the data. Sensitivity levels range from "Not Sensitive at All" to "Extremely Sensitive."
  - For each repository, choose the sensitivity level that best represents the data it manages. Consider the nature of the data, its confidentiality, and potential impact if compromised.
  - Updating the sensitivity level will influence the scoring mechanism of Aikido

    ![Image](https://ucarecdn.com/041e2f1e-c2ad-4d23-bc10-5d2f59d4e45f/)

---