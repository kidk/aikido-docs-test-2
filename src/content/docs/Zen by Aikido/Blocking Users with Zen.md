---
title: Blocking Users with Zen
---


Zen by Aikido provides a way to identify and block users who are unwanted or trigger attacks, enhancing your app's security by preventing malicious activity.

> **Important**: User blocking operates independently of the global "[Blocking/Detection Mode](https://help.aikido.dev/doc/blocking-vs-detection-mode-in-zen/docG796GDsFs)" setting. When you enable user blocks, they will always be enforced, even if Zen is in Detection Mode.

### Use Cases

- 🔍 **Monitoring active users:** Track user activity to identify and respond to potential threats.
- 🛡️ **Block Malicious Users**: Prevent access from users who have triggered security events

### How to identify and block users

**Step 1:** Identify current users using the `setUser` function found in our agents.

- [Nodejs](https://github.com/AikidoSec/firewall-node/blob/main/docs/user.md)
- [PHP](https://github.com/AikidoSec/firewall-php/blob/main/docs/user.md)
- [Python](https://github.com/AikidoSec/firewall-python/blob/main/docs/user.md)

Once set, Aikido will display all active users in the dashboard.

![Image](https://ucarecdn.com/10029b34-5b0b-4a20-9fe5-723b57e54ae1/)

**Step 2:** Identify which user to block and open the Action menu by clicking the triple dots.

![Image](https://ucarecdn.com/34cf81d8-9b20-4720-846d-0d5a803eedd6/)

> Note that user blocking is not immediate; it takes up to a minute for the block to take effect.

## Privacy & GDPR

Passing the user's name is optional, but it can help you identify the user in the dashboard. You will be required to list Aikido Security as a subprocessor if you choose to share personal identifiable information (PII).