---
title: Auth0_ Login with SAML
---


> This feature is not by default enabled for all accounts. If you'd like to enable this feature, let us know via the chat at the bottom right within Aikido.

### Setting up SAML in your account

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Image](https://ucarecdn.com/8a58bd39-29d2-432e-92c4-303a82ce2d57/)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![Image](https://ucarecdn.com/2fbe514a-30bd-4b40-89e1-f04a65b94f6b/)

### Continue in Auth0

**Step 1.** Go to [**Applications** &gt; **Applications**](https://manage.auth0.com/#/applications) in the Auth0 navigation.

**Step 2.** Click the **+ Create Application**.

**Step 3.** Choose a **Name** and click **Continue**.

**Step 4.** Select the **Addons** tab and click **SAML2**.

**Step 5.** On the SAML2 modal, select the **Settings** tab, and fill in your `Single Sign-On URL / ACS URL` as shown in Aikido.  Looks like `https://app.aikido.dev/api/saml/saml_auth?samlClientId=...` 

**Step 6.** Fill the settings field with following JSON:\
`{`\
`    "audience": "https://app.aikido.dev/saml",`\
`    "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",`\
`    "mappings": {`\
`        "email": "Email"`\
`    },`\
`    "nameIdentifierProbes": ["Email"]`\
`}`

**Step 7.** Scroll down and click **Enable** / **Save**.

**Step 8.** Within the same SAML2 modal, select the **Usage** tab.

**Step 9.** In **Aikido**, fill the fields with the data shown in Auth0:

- **Entity ID / Issuer:** enter the value of **Issuer**
- **Single Sign-On URL:** enter the value of **Identity Provider Login URL**
- **X.509 Certificate:** enter the value of **Identity Provider Certificate**
- Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![Image](https://ucarecdn.com/fdd2ad9c-5df9-4ecf-93fe-0787f0f64641/)

> Success! People having access to your Auth0 SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![Image](https://ucarecdn.com/ddd8d484-fb7b-4024-8cf0-c39bac91190c/)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![Image](https://ucarecdn.com/55187a98-aecc-42ef-9066-99f41e6f83ab/)

![Image](https://ucarecdn.com/d4d54eb5-cdbc-4ed2-9932-5b6e23ccbd01/)