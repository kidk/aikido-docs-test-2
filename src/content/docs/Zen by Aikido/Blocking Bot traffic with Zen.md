---
title: Blocking Bot traffic with Zen
---


Zen by Aikido helps you identify and block various types of automated traffic accessing your application. This feature enhances your security measures by providing control over unwanted bot activity.

> **Important**: Bot blocking operates independently of the global "[Blocking/Detection Mode](https://help.aikido.dev/doc/blocking-vs-detection-mode-in-zen/docG796GDsFs)" setting. When you enable bot blocking, it will always be enforced, even if Zen is in Detection Mode.

## Use Cases

- 🛡️ **Protect Server Resources**: Prevent bots from overwhelming your infrastructure with excessive requests
- 💰 **Reduce Costs**: Lower bandwidth and computing expenses by blocking unnecessary bot traffic
- 🔒 **Secure Content**: Protect your intellectual property from automated scraping and copying
- ⚡ **Improve Performance**: Enhance site speed by reducing bot-related server load

## Bot Categories We Detect

- **AI Data Scrapers**: Automated tools that collect data for AI training purposes

- **Archivers**: Services that create cached copies of web pages

- **SEO Crawlers**: Bots that analyze websites for search engine optimization

- **Search Engines**: Traditional web crawlers from search engines

- **AI Search Crawlers**: New generation of AI-powered search engine bots

- **AI Assistants**: Automated tools that interact with websites for user queries

- **Vulnerability Scanners**: Tools that probe for security weaknesses

- **Headless Browsers**: Automated browsers running without a GUI

- **Social Media Bots**: Automated tools that scrape social media content

> **Tip**: Consider carefully which bot categories to block, as some legitimate services (like Google's search crawler) might be necessary for your site's functionality.

## How to block bot traffic

Select a specific app and continue to the **Firewall** tab. Click the "**Manage Bots**" next to "**Block Bots**" to configure Bot blocking. 

![Image](https://ucarecdn.com/34e50c67-dca6-4e60-bf4a-b98825823def/)

Use the **Bots** dropdown to select the lists you want to enable and click on "**Block bots**"

![Image](https://ucarecdn.com/b0b4d8bd-c758-4389-bf09-5cbbc18fae8e/)

> Note that bot blocking is not immediate; it takes up to a minute for the block to take effect.