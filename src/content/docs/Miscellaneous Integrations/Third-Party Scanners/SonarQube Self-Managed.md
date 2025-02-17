---
title: SonarQube Self-Managed
---


With Aikido's SonarQube integration you can combine the powers of SonarQube's scanners with Aikido's de-noising engine to get a single dashboard to see all your relevant security issues.

To install the integration, you can follow the steps below.

### Prerequisite

- Make sure to whitelist our IP addresses. [Get them here.](https://help.aikido.dev/doc/allowing-ip-addresses-for-code--container-scanning/docqMBL9MmdF)

## 1. Create an access token

To be able to connect to your SonarQube instance, Aikido needs to have an access token to make the API calls. To create this, login to your SonarQube your environment and then follow these steps:

1. Navigate to "My Account", via the avatar in the top-right corner.
2. Click on "Security" in the tabs in the header of the page, which should take you to the page below.
3. Enter a name for the token, use something descriptive like "AikidoSecurity integration token".
4. Select "User Token" as the token type
5. Select when the token expires
6. Click on "generate"
7. Copy this token and keep it for the next step

![Image](https://ucarecdn.com/486a0376-d634-4f6e-a4eb-fe7e133412ad/)

## 2. Enable the integration

Go to the [integration settings page](https://app.aikido.dev/settings/integrations/3rd-party-scanners/sonarqube) in your Aikido account and scroll down to the "Third-Party Scanners" section. Click on the SonarQube integration card and click on "Connect SonarQube" on the next page.

## 3. Connect your instance

From the dropdown select "Self managed" for the instance kind. To connect your SonarQube environment Aikido needs 2 things:

1. The access token you created in the first step
2. The URL of your instance eg: <https://example.sonarqube.com>

Fill both in their respective input fields and click on "Create". We'll let you know if we are able to connect to your environment. If this is the case we'll start scanning your environment for relevant vulnerabilities and report them in your "Feed" in Aikido.

![Image](https://ucarecdn.com/d852ef02-14c8-429a-b459-0903e1478844/)

---

### Set Up Sonar Integration →

### Discover Integration Details →

---