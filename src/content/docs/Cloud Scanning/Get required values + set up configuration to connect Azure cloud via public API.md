---
title: Get required values + set up configuration to connect Azure cloud via public API
---


Log into your [**Azure Portal**](https://portal.azure.com/) and navigate to the **Microsoft Entra ID service** (Formerly known as Azure Active Directory).

Select **App registration**

![Image](https://ucarecdn.com/7272798b-6ece-4bc5-9e40-df364a5e7a1f/)

Give the application a meaningful name, we need this name later. 

Leave the "Supported account types" default: "Accounts in this organizational directory only".

Click "Register"

![Image](https://ucarecdn.com/a59aca40-8623-4b87-a76b-06ed42ea2ba4/)

You get redirected to the detail page of the newly created application. Here you can find and copy the **Application (client) ID** and the **Directory (tenant) ID**

![Image](https://ucarecdn.com/f919c8fa-39ae-4cb0-9bec-2d25b03306b4/)

At the client credentials field, click "Add a certificate or secret"

![Image](https://ucarecdn.com/5d15f5a3-597a-473f-87d0-733e9859afaa/)

Click the "New client secret"-button, give a description for the secret and set the expiration date to 2 years (730 days / 24 months)

![Image](https://ucarecdn.com/d12ff208-e713-46a2-a2a0-c637ff7c9f21/)

Copy the **Secret's Value**

![Image](https://ucarecdn.com/4859aaf5-4ea3-4395-afb6-fda023ffdae2/)

Navigate to Subscriptions, Copy the **Subscription ID** of the relevant subscription.

![Image](https://ucarecdn.com/ba21e769-470f-45ac-8943-e91e79e38637/)

You now have all the required values to add the Azure Cloud via the Public API once the application setup is complete in Azure Portal.

Go to the subscription detail page. Now we need to make sure we grant access to the roles we need.

Click on **"Access Control (IAM)"**.

![Image](https://ucarecdn.com/4b484f3d-1809-4a49-aab8-73b3c23cdcbd/)

Go to the Role assignments tab & Click on **"Add"**, then **"Add role assignment"**.

![Image](https://ucarecdn.com/0d132105-5281-4e43-a5df-068e79afe0d1/)

In the **"Role"**-list, search and select **"Security Reader"** & Click **"Next"**.

![Image](https://ucarecdn.com/2db28119-d664-4080-9e28-5871d87b0111/)

Leave the **"Assign access to**"default value.

Click on **"Select Members"**, search for the name of the app registration (e.g. "AikidoSecurity") you created and select it.

Click **"Select"**

Click **"Review + assign"** twice

![Image](https://ucarecdn.com/c423fb1d-21e0-43ed-b243-f26cf556418a/)

Repeat the role assignment process for the role **"Log Analytics Reader"**.

Now the application has the required roles to do the security scanning. You can now add this cloud using the public API.