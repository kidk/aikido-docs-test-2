---
title: GraphQL API Scanning
---


Aikido can scan your GraphQL API endpoints to uncover endpoint vulnerabilities specifically related to GraphQL. One of the methods we use is API fuzzing, which essentially includes spamming dangerous payloads to each field in your API. 

> NEVER do this setup on a production environment, but always on staging to avoid potential downtime or interference.

### Main Use Cases

You can see all checks in the [Aikido app here](https://app.aikido.dev/domains/checks?scanner=graphql). 

### Setting up GraphQL API Scanning

**Step 1:** Click **Add Domain** in the [Domain Overview ](https://app.aikido.dev/domains)and select **GraphQL** scanning

![Image](https://ucarecdn.com/e3b66d94-162f-414b-bd36-87a4641556de/)

**Step 2.** Enter the domain name of your **staging environment**. Ensure this is the base URL for your GraphQL APIs (e.g., `https://example.io/graphql`)

![Image](https://ucarecdn.com/7d9ed9dd-97d3-4063-8a12-d15534fa4430/)

**Step 3:** Click save, Aikido will now scan your GraphQL API. 

**Step 4. Authorization:** Note that you can also add authorization information if this is required to talk to your API. You can do this by clicking the triple dots action menu on the domain, and then '**Authenticate Domain**'

![Image](https://ucarecdn.com/93e28303-bdd8-43f4-ad11-ed62a73d5cc7/)

This will trigger the modal where you can fill in the authentication details.

![Image](https://ucarecdn.com/fd6fe4c4-64a7-4f4d-a031-118eafd83dc0/)