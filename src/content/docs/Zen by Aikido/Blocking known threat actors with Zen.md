---
title: Blocking known threat actors with Zen
---


Zen by Aikido helps you control access to your application based on known malicious actors and threats. This feature enhances your security measures by leveraging [CrowdSec's](https://www.crowdsec.net/) comprehensive IP-based threat intelligence to block various types of malicious actors and activities. Unlike content or pattern-based blocking, this feature focuses solely on IP address lists for efficient and reliable traffic filtering.

> Important: Actor blocking operates independently of the global [Blocking/Detection Mode](https://help.aikido.dev/doc/blocking-vs-detection-mode-in-zen/docG796GDsFs) setting. When you enable actor blocks, they will always be enforced, even if Zen is in Detection Mode.

## Use Cases

- 🛡️ Block Malicious Botnets: Prevent access from known botnet infrastructure 
- 🔒 Stop Brute Force Attacks: Protect against credential stuffing and password attacks 
- ⚔️ Prevent DoS Attacks: Block known HTTP DoS attackers 
- 🚫 Reduce Exploitation Risk: Block traffic from known HTTP exploit actors 
- 🕵️ Control Anonymous Access: Manage traffic from known proxy/VPN services 
- 🔍 Prevent Scanning: Block reconnaissance from known internet scanners 
- 🛑 WordPress Protection: Block known WordPress attackers

## How to block known threat actors

Select a specific app and continue to the **Firewall** tab. Click the "**Manage Threat Actors**" next to "**Block IPs used by known threat actors**" to configure known threat actors blocking. 

![Image](https://ucarecdn.com/8f11c6c5-db7c-45af-ac67-89a8f22da21b/)

Use the **Known Threat Actors** dropdown to select the lists you want to enable and click on "**Block Threat Actors**"

> Not all lists are available on all plans. Contact our support team if you have any questions about list availability for your subscription.

![Image](https://ucarecdn.com/d9461057-0e80-4d6f-ab00-7b4a48ea0b4a/)

> Note that threat actors blocking is not immediate; it takes up to a minute for the block to take effect.

## Available threat actor lists

- [Botnet Actors](https://app.crowdsec.net/blocklists/65a56c160469607d9badb813)
- [Bruteforce Attackers](https://app.crowdsec.net/blocklists/66ec368bc0ad850aec9c02d4)
- [HTTP DoS Attackers](https://app.crowdsec.net/blocklists/660fc8d678dc68ae3ef065e4)
- [HTTP Exploit Attackers](https://app.crowdsec.net/blocklists/660fc91ba69671df549e3bec)
- [Proxy/VPN](https://app.crowdsec.net/blocklists/65a56839ec04bcd4f51670be)
- [Public Internet Scanners](https://app.crowdsec.net/blocklists/65f972eb807e06de7a0e3e65)
- [WordPress Attackers](https://app.crowdsec.net/blocklists/65a56c1a0469607d9badb814)