# Google Workspaces: Login with SAML

> This feature is not by default enabled for all accounts. If you'd like to enable this feature, let us know via the chat at the bottom right within Aikido.

### Setting up SAML in your account {#setting-up-saml-in-your-account}

**Step 1.** Go to [**General Settings**](https://app.aikido.dev/settings/account) and click '**Enable SAML Authentication'**

![Image](https://ucarecdn.com/6bb8581e-5aab-49a3-8ce8-4b5f13a49749/)

**Step 2.** Copy **all details** to your identity provider. See steps below.

![Image](https://ucarecdn.com/131b2923-631f-42e8-af65-87faa35c50e0/)

### Continue in Google {#continue-in-google}

**Step 1.** Go to **Apps** &gt; **Web and mobile apps** in the Google Admin Console.

**Step 2.** Click the **Add app** dropdown and select **Add custom SAML app**.

**Step 3.** Choose an **App name**  and click **Continue**.

**Step 4.** Ignore the metadata page for now, we'll get this information later on. Click **Continue**.

**Step 5.** Fill the fields **ACS URL**, **Entity ID** and **Name ID format** with the fields visible in Aikido (see above) and click **Continue** and click **Finish**.

**Step 6.** Now you should be on the detail page of your newly created app. Click **Download Metadata**.

### Go back to Aikido {#go-back-to-aikido}

- Fill in the **Entity ID / Issuer**, **Single Sign-On URL** and **X.509 Certificate** as shown in the modal in Google. 
- Also fill out the **Company Domain** to make sure people can log in without the need of a Single Sign-On URL.

![Image](https://ucarecdn.com/33ba5a40-204e-4c76-8a85-971b8115c30b/)

> Success! People having access to your Google SAML app will now be able to auto-onboard to your Aikido workspace.

### 2 options for users to login using your SAML client {#2-options-for-users-to-login-using-your-saml-client}

**Option 1. Using SSO Link Directly**

Copy the Login Link and share this internally with other users.

![Image](https://ucarecdn.com/d44ce4f2-726b-4108-b8d5-bb83c49b1490/)

**Option 2.** Going to the Aikido login screen, selecting **Login Via SSO** and filling in the email address **Important**: the email needs to contain the company domain that has been set up.

![Image](https://ucarecdn.com/fa842428-89f5-4aa8-91a4-56cc2a7533eb/)

![Image](https://ucarecdn.com/2ec57086-151e-48f9-ab55-0c1ac60cafb1/)