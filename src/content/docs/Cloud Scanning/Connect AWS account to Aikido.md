---
title: Connect AWS account to Aikido
---


### Why connect my AWS cloud?

Securing your cloud infrastructure is crucial to protecting your user data. You can leverage Aikido's security checks to detect and address any misconfigurations in your infrastructure.

Aikido will surface critical cloud misconfigurations that allow hackers to get into your AWS cloud, such as the risk highlighted in [this blog post](https://www.aikido.dev/blog/how-a-startups-cloud-got-taken-over-by-a-simple-form-that-sends-an-email). We focus on the risks that can have a truly big impact on your company's business and cut the noise.

To view the list of security checks performed by Aikido on your cloud environment, go to the 'checks' tab on the [cloud overview page](https://app.aikido.dev/clouds) at. Filter to AWS to see specific checks performed on your connected AWS account.

Assuming you're using multiple AWS accounts via 'AWS Organizations' to separate staging from production, we recommend trying out Aikido on your staging account first, to get a feel for the process.

### Features

After connecting, Aikido will perform the following monitoring:

- Perform a daily compliance scan on all checks listed here: <https://app.aikido.dev/clouds>
- Ingest, deduplicate and filter all Docker CVE findings from AWS inspector
- Monitor your route53 domains for subdomain takeover attacks

### Getting started

To get started, head to the [cloud overview page](https://app.aikido.dev/clouds) on Aikido and click 'Connect cloud.' Follow the step-by-step setup wizard to connect your AWS account to Aikido.

![Image](https://ucarecdn.com/73ee3b40-2ba5-40d4-9c9f-b3d509e05c74/)

Aikido will require the creation of new role in your AWS account. The permissions for this role enable us to do a security audit of your cloud, but not edit your cloud infrastructure. This works by giving the Aikido AWS account a trust relationship with the newly created role in your account

To view the exact Cloudformation template used to create this role, [click here](https://aikido-production-staticfiles-public.s3.eu-west-1.amazonaws.com/minimal-policy.json). Inside the wizard, Aikido can also generate an equivalent Terraform template for you. Note that the policy includes 2 specific access rights to enable AWS inspector for you ( "iam:CreateServiceLinkedRole" and "inspector2:\*"), which you may remove if you have already enabled Inspector yourself.

After creation of the role, Aikido only needs the specific ARN to get started. No access keys or passwords are ever shared with Aikido.

Finally, you can name your connected project in Aikido and specify the environment it operates in. This information helps Aikido prioritize findings based on the severity and impact to your business.

![Image](https://ucarecdn.com/28703034-b615-4b25-a639-8fa336bc27a9/)

Within 1-2 minutes after connecting your account, Aikido will report misconfigurations that could pose a threat.

---

### Set Up AWS Cloud Integration →

### Discover Integration Details →

---