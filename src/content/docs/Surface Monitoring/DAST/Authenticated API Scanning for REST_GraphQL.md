---
title: Authenticated API Scanning for REST_GraphQL
---


\
This guide will walk you through the steps to set up authenticated domain scanning in Aikido, ensuring thorough and secure assessments.

> This feature is only available on Pro and Scale Plans

### Use Cases

- Ensure comprehensive security assessments for protected areas of your website.
- Identify vulnerabilities in authenticated sections of your APIs.

### Setting up authentication on a domain

**Step 1:** Go to the [**Domains Overview**](https://app.aikido.dev/settings/domains) and open the action menu for a REST/ GraphQL API domain of your choice by clicking the triple dots. Select **Authenticate Domain.**

![Image](https://ucarecdn.com/77efc1b9-0cd9-4015-a510-adde377cb2b0/)

**Step 2:** Select your preferred option to authenticate.

![Image](https://ucarecdn.com/c16057a3-f401-440d-be94-2389db62fc45/)

### Authentication Options

> These can serve as alternatives when you want to use MFA for authentication.

**Login via Form**

Fill in the URL and email/password for the domain authentication. Click **Test** to let Aikido check whether it can access the domain with those credentials.

![Image](https://ucarecdn.com/b335a98b-6c66-48a8-8507-96fc7da88beb/)

---

**Custom Headers**

If your API accepts a fixed API key of some sorts which should not change after creation, you can add it as a custom header via this option.

---

**OAuth Client Credentials**

This option can be used when you want to bypass MFA. Aikido makes a request to the provided login URL which follows the OAuth spec for a Client Credentials flow. This means that we'll make a POST request to the configured login url, with `grant_type` set to `client_credentials` and a basic authorization header containing the client_id and client_secret as the username and password respectively.