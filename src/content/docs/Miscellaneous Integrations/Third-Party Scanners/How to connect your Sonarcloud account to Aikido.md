---
title: How to connect your Sonarcloud account to Aikido
---


With Aikido's Sonarcloud integration you can combine the powers of Sonarcloud's scanners with Aikido's de-noising engine to get a single dashboard to see all your relevant security issues.

Aikido will only import security-related findings from SonarCloud. No styling-related advice will be imported.

To set up the integration, follow these steps:

## 1. Create an access token

To be able to connect to your Sonarcloud instance, Aikido needs to have an access token to make the API calls. To create this, login to your [Sonarcloud](https://sonarcloud.io/) your environment and then follow these steps:

1. Navigate to "My Account", via the avatar in the top-right corner.
2. Click on "[Security](https://sonarcloud.io/account/security)" in the tabs in the header of the page, which should take you to the page below.
3. Enter a name for the token, use something descriptive like "AikidoSecurity integration token".
4. Copy this token and keep it for the next step

![Image](https://ucarecdn.com/3f157c0f-0a86-4555-a34d-2dfb801ff5e1/)

## 2. Grab your organization's key

Next, you need to find your organization's key in Sonarcloud. This key is shown on the organization's overview page. \
​\
This page can be found by again opening the menu that's shown after clicking the avatar in the top-right, and then clicking on the organization you'd like to connect.

The organization's key is shown in the header of the page on the right-hand side.

![Image](https://ucarecdn.com/21c31221-8dc7-4d51-9604-823800b6ed45/)

## 3. Enable the integration

Go to the [integration settings page](https://app.aikido.dev/settings/integrations/3rd-party-scanners/sonarqube) in your Aikido account and scroll down to the "Third-Party Scanners" section. Click on the SonarQube integration card and click on "Connect SonarQube" on the next page.

## 4. Connect your instance

From the dropdown select "Hosted on sonarcloud.io" for the instance kind. To connect your Sonarcloud environment Aikido needs 2 things:

1. The access token you created in the first step
2. The key of your organization collected on step 2

Fill both in their respective input fields and click on "Create". We'll let you know if we are able to connect to your environment. If this is the case we'll start scanning your environment for relevant vulnerabilities and report them in your "Feed" in Aikido.

![Image](https://ucarecdn.com/adf965c5-3297-4fcf-b765-35ab43b54558/)

---

### Set Up Sonar Integration →

### Discover Integration Details →

---