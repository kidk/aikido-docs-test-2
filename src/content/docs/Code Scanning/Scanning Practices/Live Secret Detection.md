---
title: Live Secret Detection
---


Our Live Secret Detection feature checks if exposed secrets are still active and assesses their potential risks. Based on the outcome, the issue's severity will be changed.

### Use Cases

- Identifying and flagging active secrets in code repositories.
- Reducing noise for secrets that are not active anymore (e.g., already rotated)
- Checking the scope of permissions granted by exposed secrets.
- Enhancing security by marking dangerous secrets for immediate action.

### How Live Secret Detection Works

**Identify and Verify**

Aikido sends the exposed secret to a secure endpoint to check whether it is still active. As a result, you may notice IPs in your logs that are coming from Aikido. Below the list of Aikido IPs:

- **52.214.244.18**
- **18.202.209.180**
- **52.50.198.227**
- **52.51.98.186**

**Assess permissions**

Aikido goes a step further and checks permissions of the active secrets. Based on that, we make an extra distinction in our severity upgrades. We check the following.

- **Expired Secrets**
- **Read-Only Scopes**
- **Write/Delete Scopes**

> We do different checks (e.g., GitHub Access Tokens, Sendgrid tokens, etc). Contact us if there are secrets you want to have checked!