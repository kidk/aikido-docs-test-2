---
title: Okta_ Login with SAML
---


> This feature is not by default enabled for all accounts. If you'd like to enable this feature, let us know via the chat at the bottom right within Aikido. Also make sure you are on a Pro or Scale Plan.

### Setting up SAML in your account

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Image](https://ucarecdn.com/cd9146ff-36d4-4839-a879-0092907a7019/)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![Image](https://ucarecdn.com/01f94720-00dc-4d8f-95a3-887c7546433b/)

### Continue in Okta

**Step 1.** Go to **Applications** &gt; **Applications** in the Admin Console.

**Step 2.** Click **Create App Integration**, select **SAML 2.0** and click **Next**.

**Step 3.** Choose an **App name** and click **Next**.

**Step 4.** Fill the fields **Single sign-on URL**, **Audience URI** and **Name ID format** with the fields visible in Aikido (see above) and click **Next**.

**Step 5.** Now you should be on the tab **Sign On** and you should see **Metadata details**. Click **More details**.

### Go back to Aikido

- Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in Okta. 
- Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![Image](https://ucarecdn.com/bf648fe2-3f42-4490-9067-3840392e84f9/)

> Success! People having access to your Okta SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![Image](https://ucarecdn.com/b6d1fe83-fa12-410c-b6de-77ac12f0f41b/)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![Image](https://ucarecdn.com/c233b6e3-7de6-40fe-b58c-8e6414a89556/)

![Image](https://ucarecdn.com/4e595972-8a51-4473-956b-7da0b4fd41fa/)