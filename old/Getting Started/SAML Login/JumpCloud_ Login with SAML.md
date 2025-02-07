# JumpCloud: Login with SAML 

> This feature is not by default enabled for all accounts. If you'd like to enable this feature, let us know via the chat at the bottom right within Aikido.

### Setting up SAML in your account {#setting-up-saml-in-your-account}

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Image](https://ucarecdn.com/e1fd0c18-f548-4071-919d-67e1fac297ec/)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![Image](https://ucarecdn.com/09a7d874-2d07-4f24-b41c-83eb4ae62a50/)

### Continue in JumpCloud {#continue-in-jumpcloud}

**Step 1.** Go to **User Authentication** &gt; **SSO Applications** in the JumpCloud Admin Portal navigation.

**Step 2.** Click the **Add New Application** and search for **SAML 2.0**. Click **Next**.

**Step 3.** Choose a **Display Label** and click **Save Application**.

**Step 4.** Click **Configure Application**.

**Step 5.** Click on the **SSO** tab and fill following fields:

- **Idp Entity ID:** `https://console.jumpcloud.com/<appname>`
- **SP Entity ID:** `https://app.aikido.dev/saml` 
- **ACS URLs** - **Default URL:** `https://app.aikido.dev/api/saml/saml_auth?samlClientId=...`  (As shown in Aikido)
- **SAMLSubject NameID:** `email` 
- **SAMLSubject NameID Format:** `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` 
- **Signature Algorithm:** `RSA-SHA256`
- **Default RelayState:** You can leave this empty

![Image](https://ucarecdn.com/05b8da4a-cc77-4099-856c-70e00b369a45/)

**Step 6.** We'll continue in Aikido, but you might as well click **Save** and come back to this screen.

### Go back to Aikido {#go-back-to-aikido}

- Fill in the:
  - **Entity ID / Issuer:** `https://console.jumpcloud.com/<appname>` (Make sure this matches what you've entered as **Idp Entity ID** in JumpCloud. If you're having issues with this, see the Troubleshooting section at the bottom)
  - **Single Sign-On URL:** as shown in JumpCloud under **IDP URL**. (looks like `https://sso.jumpcloud.com/saml2/<appname>`)
  - **X.509 Certificate**: This can be fetched in different ways. One way is to click **Export Metadata** in JumpCloud the config and open the downloaded xml. You'll find your certificate between the `ds:X509Certificate` tags.
- Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![Image](https://ucarecdn.com/282cde57-79ed-4aab-bddb-bd4073327ee6/)

> Success! People having access to your JumpCloud SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client {#2-options-for-users-to-login-using-your-saml-client}

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![Image](https://ucarecdn.com/13d717d7-9d5e-4dd1-ab34-4d5b6455f475/)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![Image](https://ucarecdn.com/ca4791cb-4534-471c-8757-b2dc3ca7e569/)

![Image](https://ucarecdn.com/ff9dd4af-ca57-484d-aacb-ed9cbe5aad7d/)

### Troubleshooting {#troubleshooting}

**Error**

![Image](https://ucarecdn.com/5f7761f9-08db-4072-8559-0567d1bfc719/)

**Solution**

Make sure the **Idp Entity ID** is unique. Perhaps you could change it to `https://console.jumpcloud.com/<samlClientId>`. Note that you'll also need to change it in Aikido in **Entity ID / Issuer** as these should match.