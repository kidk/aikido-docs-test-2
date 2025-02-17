---
title: Allowing IP addresses for code & container scanning
---


If your Git provider only allows specific IP addresses to access your code, you will have to allowlist Aikido's IP addresses for code scanning before you can start scanning.

Add the following IPs:

- **52.214.244.18**
- **18.202.209.180**
- **52.50.198.227**
- **52.51.98.186**

The ports required to be opened are at least port **443** for HTTPS. For Docker container registries, additional ports might be required. For example, the Gitlab Container Registry requires port **4567** to be open.

After adding the IPs, rescan your repositories to confirm connectivity.

---