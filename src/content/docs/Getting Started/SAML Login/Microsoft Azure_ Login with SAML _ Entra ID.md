---
title: Microsoft Azure_ Login with SAML _ Entra ID
---


### Setting up SAML in your account

> This feature is not by default enabled for all accounts. If you'd like to enable this feature, let us know via the chat at the bottom right within Aikido.

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Image](https://ucarecdn.com/226233e4-b7ed-4614-a3c7-2316aa00830e/)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![Image](https://ucarecdn.com/af05c8a1-f44f-499c-85a3-40090e79ede6/)

### Continue in Azure

**Step 1.** Go to **Microsoft Entra ID**.

**Step 2.** Click the **Add** dropdown and select **Enterprise application**.

![Image](https://ucarecdn.com/e2b0c97b-cd57-473d-a88b-ae86bae5f17e/)

**Step 3.** Click **Create your own application**, choose a name for your app and select 'Non-gallery'.

![Image](https://ucarecdn.com/34300cbc-6836-46d3-bcda-326d3726eaac/)

**Step 4.** Select **Set up single sign on**.

![Image](https://ucarecdn.com/041ab86f-83f5-4f7d-b318-3a5e4b8a4fdb/)

**Step 5.** Click the **SAML** option.

![Image](https://ucarecdn.com/1659ec2c-7283-426d-894c-48ef502505ec/)

**Step 6.** On **step 1**, click **Edit.**

![Image](https://ucarecdn.com/62185eb3-6a97-427b-b914-3a1ec840b54c/)

**Step 7.** Fill in the **Entity ID** and **ACS URL** as shown in Aikido.

![Image](https://ucarecdn.com/b29695e0-9d2a-4f64-9a88-e30172e85348/)

**Step 8.** At **step 2**, click **Edit.**

![Image](https://ucarecdn.com/0cc0859a-2fbd-4ca9-9442-c8114c034d3b/)

**Step 8.** Click the **Unique User Identifier (Name ID)**.\
Optional: clicking 'Add new claim' at the top of this page allows you to add [custom attributes](https://help.aikido.dev/doc/saml-user-rights-using-custom-attributes/doc6Jm7BYzwg) to SAML

![Image](https://ucarecdn.com/c58d21d6-7556-43db-96eb-3f2b81663b8d/)

**Step 9.** Make sure to set **Source attribute** to `user.mail` here.

![Image](https://ucarecdn.com/7359629d-6b9b-4c7a-822a-46ddb14ae30e/)

**Step 10.** At step 3 you can download the **Certificate (Base64)** & at step 4 you'll see the **Login URL** and **Mircosoft Entra Identifier**. These should be copy and pasted to Aikido.

### Go back to Aikido

- Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in Azure.
- Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![Image](https://ucarecdn.com/ecd63576-b9c5-464a-ae53-3bbb1494f534/)

> Success! People having access to your Azure SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![Image](https://ucarecdn.com/bf7e0490-bc80-42f3-8517-805537105a8d/)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![Image](https://ucarecdn.com/a72d4e17-3465-4a72-bd1b-5b15115eb4da/)

![Image](https://ucarecdn.com/9ad5fafb-e1f7-4ac8-b3b7-37d4639c046d/)