---
title: Blocking vs Detection Mode in Zen
---


Zen by Aikido offers two operational modes for handling attack patterns: **Detection Mode** and **Blocking Mode**. These modes specifically apply to application-level attacks like SQL injection, shell injection, path traversal, and SSRF. 

Other security features like [user blocking](https://help.aikido.dev/doc/blocking-users-with-zen/docbO6Nm6Zb1), [bot protection](https://help.aikido.dev/doc/blocking-bot-traffic-with-zen/dociQ23filsX), [tor blocking](https://help.aikido.dev/doc/blocking-tor-traffic-with-zen/docpysjmqh7e) and [country blocking](https://help.aikido.dev/doc/blocking-traffic-by-country-with-zen/docuvCI1lRzo) are managed separately through their respective settings.

## Understanding the Modes

### Detection Mode (Default)

- 📝 Logs potential attacks without blocking them
- 🔬 Allows you to monitor threats without impacting traffic
- 📊 Helps evaluate security patterns before enabling blocks

### Blocking Mode

- 🛡️ Actively blocks detected attack patterns
- 🚫 Blocks malicious requests before they can execute
- ⚡ Provides real-time protection against threats

## Configuration Options

### Using Environment Variables

```
# Enable Blocking Mode 
AIKIDO_BLOCK="true" 

# Enable Detection Mode (default) 
AIKIDO_BLOCK="false"
```

### Using the Dashboard

1. Navigate to your app's firewall settings
2. Find the "**Block Attacks**" section
3. Toggle between "Detection-Only" and "Blocking-Mode"

![Image](https://ucarecdn.com/eb4fd581-694d-42b4-8c96-ca2a46fcc2a9/)

> Note: The environment variable sets the initial mode, but the dashboard configuration takes precedence once loaded.

## What Gets Blocked?

Blocking mode only affects these attack types:

- SQL Injection attempts
- NoSQL Injection attempts
- Shell Injection attacks
- Path Traversal exploits
- SSRF attempts

Check out our [Functionality Support Matrix](https://help.aikido.dev/doc/getting-started-with-zen/doccLOR8KzO0) for more details. 