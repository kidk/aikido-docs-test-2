---
title: Blocking Tor traffic with Zen
---


Zen by Aikido helps you identify and block users who are accessing your application through the [Tor network](https://www.torproject.org/). This feature enhances your security measures by providing visibility and control over [Tor-based traffic](https://www.torproject.org/).

> **Important**: Tor blocking operates independently of the global "[Blocking/Detection Mode](https://help.aikido.dev/doc/blocking-vs-detection-mode-in-zen/docG796GDsFs)" setting. When you enable tor blocking, it will always be enforced, even if Zen is in Detection Mode.

## Use Cases

- 🛡️ **Block Tor Users**: Automatically prevent access from Tor exit nodes when needed for security compliance or risk mitigation

- 🔒 **Meet Compliance**: Satisfy regulatory requirements that mandate blocking anonymous proxy traffic

- 💳 **Protect Transactions**: Ensure financial transactions come from identifiable, non-anonymous sources

## How to block tor traffic

Select a specific app and continue to the **Firewall** tab. Click the toggle next to "**Block Tor Traffic"** to enable Tor blocking.

![Image](https://ucarecdn.com/3c9ef9ec-c1a8-46c7-9343-f45f7a4f18f6/)

> Note that Tor blocking is not immediate; it takes up to a minute for the block to take effect.