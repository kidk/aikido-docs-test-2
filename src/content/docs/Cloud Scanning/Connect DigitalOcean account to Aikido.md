---
title: Connect DigitalOcean account to Aikido
---


### Why connect my DigitalOcean cloud?

Securing your cloud infrastructure is crucial to protecting your user data. You can leverage Aikido's security checks to detect and address any misconfigurations in your infrastructure.

**Main Use Cases**

- Aikido surfaces critical cloud misconfigurations that allow hackers to get into your DigitalOcean cloud, such as the risk highlighted in [this blog post](https://www.aikido.dev/blog/how-a-startups-cloud-got-taken-over-by-a-simple-form-that-sends-an-email). All configuration checks can be found [here (filter on DigitalOcean)](https://app.aikido.dev/clouds/checks)
- If you store Docker images in repo, Aikido looks for most known vulnerabilities in Apache, Nginx etc.

Aikido performs a daily compliancy scans on the above.

### Getting started

To get started, head to the [cloud overview page](https://app.aikido.dev/clouds) on Aikido and click 'Connect cloud.' Follow the step-by-step setup wizard to connect your DigitalOcean account to Aikido.

![Image](https://ucarecdn.com/da5026d7-4995-4a84-bc85-64295105fa51/)

To connect your account, you will need to create an access token that Aikido can use in DigitalOcean. Click on "API" in the left-hand navigation to go to the following screen.

![Image](https://ucarecdn.com/4996db5b-f814-410c-a88e-77ed990b0114/)

On this page, click on "Generate New Token" to create a new token.

![Image](https://ucarecdn.com/44e23ed1-bfe4-4e94-853b-68f78eac4440/)

Enter a descriptive name for your token, and set the expiration to "No expire". Aikido only needs 'Read' access. Click on "Generate Token".

Once your token is created in DigitalOcean, you can copy it and enter it in Aikido's setup wizard, together with the token name you chose.

Finally, you can name your connected project in Aikido and specify the environment it operates in. This information helps Aikido prioritize findings based on the severity and impact to your business.

![Image](https://ucarecdn.com/09b2e048-f427-40c2-9b47-e8ae568b3e92/)

Within 1-2 minutes after connecting your account, Aikido will report misconfigurations that could pose a threat.

---

### Set Up DigitalOcean Cloud Integration →

### Discover Integration Details →

---