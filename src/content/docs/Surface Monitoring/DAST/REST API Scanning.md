---
title: REST API Scanning
---


Aikido can scan your REST API endpoints to uncover critical endpoint vulnerabilities, such as SQL injection or path traversal. Aikido uses API fuzzing, which essentially includes spamming dangerous payloads to each field in your API. 

> NEVER do this setup on a production environment, always on staging to avoid potential downtime.

### Main Use Cases

**Critical Vulnerability Detection**:

- SQL injection
- NoSQL injection
- Path traversal
- Shell injection
- IDOR/BOLA: cross-tenant data leakage in SaaS apps

You can see all checks in the [Aikido app here](https://app.aikido.dev/domains/checks?scanner=rest). 

### Setting up REST API Scanning

**Step 1:** Click **Add Domain** in the [Domain Overview ](https://app.aikido.dev/domains)and **select REST API** 

![Image](https://ucarecdn.com/a17b35a6-5a34-4d70-988a-534580278782/)

**Step 2.** Enter the domain name of your **staging environment**. Ensure this is the base URL for your REST APIs (e.g., `https://example.io/api`)

![Image](https://ucarecdn.com/ba74a958-2462-4a6c-88b5-40f2fe05d53d/)

**Step 3:** Add your OpenAPI specification using one of these options:

- **Connect to Zen App (recommended)**: Integrate with Zen to automatically discover and update API endpoints for continuous scanning. More info about Zen [can be found here](https://help.aikido.dev/section/zen-by-aikido/sgIt4HRxlrFr). No manual work nor maintenance!
- **Manual Upload**: Upload a Swagger file to define your API endpoints. You will be required to manually update and upload your swaggerfile each time new API endpoints are added to your application.

![Image](https://ucarecdn.com/92f0ecb9-5065-45a1-9e0b-42bba818c4c3/)

**Step 4:** Add authorization information to your API to make sure Aikido can access endpoints that require login. You can do this by clicking the triple dots action menu on the domain, and then '**Authenticate Domain**'

![Image](https://ucarecdn.com/b352fba8-9a02-4c8d-84e7-60b6d94e5b9d/)

This will trigger the modal where you can fill in the authentication details. Multiple authentication types are available: **Login via Form** and **Custom Headers** support

![Image](https://ucarecdn.com/42a1f3d3-08d5-4a6b-a142-aeaaeda72705/)