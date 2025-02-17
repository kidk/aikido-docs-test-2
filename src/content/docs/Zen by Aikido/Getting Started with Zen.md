---
title: Getting Started with Zen
---


### Introduction

Zen by Aikido is a powerful Application Firewall that embeds directly into your code to protect your applications against attacks.

It protects your apps by preventing user input containing dangerous strings, which usually allow for **injection** and **path traversal** attacks. Zen protects your apps from common attacks by: 

- ✨ Preventing dangerous user input that enables injection and path traversal 
- 🛡️ Automatically blocking critical injection attacks 
- 🚦 Rate limiting routes and users 
- 🤖 Blocking malicious traffic (bots, TOR, known attackers) 
- 🌍 Controlling access by country 
- 🔍 Monitoring outbound traffic

> Zen by Aikido operates autonomously on the same server as your app to secure your app like a classic web application firewall (WAF), but **without the infrastructure or cost**. 

### Languages

- **Supported:** 
  - [Node.js ](https://github.com/AikidoSec/firewall-node)
  - [Python](https://github.com/AikidoSec/firewall-python?tab=readme-ov-file)
  - [PHP ](https://github.com/AikidoSec/firewall-php)
  - [Java](https://github.com/AikidoSec/firewall-java)
  - [.NET Core and Framework](https://github.com/AikidoSec/firewall-dotnet)
- **In Beta**:
  - Ruby

### How to install

> We do **not send** any data back to the cloud to do security checks. The token is only used to communicate when attacks are detected to show in the dashboard.

Follow the setup instructions in the [Aikido app](https://app.aikido.dev/runtime/services) and check out our [docs.](https://help.aikido.dev/category/installation-instructions/sgmzFX3rLYqv)

### Functionality Support Matrix

|  | **SQLi Protection** | **NoSQLi Protection** | **Path Traversal** | **Shell Injection** | **SSRF Protection** | **Rate Limiting by IP** | **Rate Limiting by User** | **Block Users** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Java** | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Node.js** |  |  |  |  |  |  |  |  |
| Hono | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Hapi | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Next.js | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Express | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Google Cloud Functions | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Google Cloud Pub/Sub | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Lambda | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Micro | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **PHP** | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Python** |  |  |  |  |  |  |  |  |
| Django | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Flask | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| gUnicorn | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Quart | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Scarlette | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Ruby** | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
