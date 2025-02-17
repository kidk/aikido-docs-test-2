---
title: Setup Configuration in Azure
---


Log into your [**Azure Portal**](https://portal.azure.com/) and navigate to the **Microsoft Entra ID service**.

Click on **Add** and select **App registration**

![Image](https://ucarecdn.com/e77457d8-318c-4766-947f-86a94c8b0e1a/)

Give the application a meaningful name, we need this name later. 

Leave the **Supported account types** default: **Accounts in this organizational directory only**.

Click on **Register**.

![Image](https://ucarecdn.com/4690d5db-e42d-4d8d-93a0-b978333c1364/)

You get redirected to the detail page of the newly created application. Here you can find and copy the **Application (client) ID** and the **Directory (tenant) ID**

![Image](https://ucarecdn.com/4ce56e1e-0436-430e-8492-e4e85120a1d3/)

At the client credentials field, click "Add a certificate or secret"

![Image](https://ucarecdn.com/a250622e-201f-4711-a957-e3aba87db480/)

Click the "New client secret"-button, give a description for the secret and set the expiration date to 2 years (730 days / 24 months)

![Image](https://ucarecdn.com/121cb5f1-e88a-4223-b42d-a4c8333dc37c/)

Copy the **Secret's Value**

![Image](https://ucarecdn.com/bbbbcc21-57d0-4f74-a64a-094a79016cfe/)

You now have all the required values to add the Azure Cloud via the Public API once the application setup is complete in Azure Portal.

Go to the subscription detail page. Now we need to make sure we grant access to the roles we need.

Navigate to **Subscriptions**, find the relevant Subscription for your Virtual Machines

Click on **"Access Control (IAM)"**.

![Image](https://ucarecdn.com/fd91dcbc-023d-4561-a357-f7baf02fb925/)

Go to the Role assignments tab & Click on **"Add"**, then **"Add role assignment"**.

![Image](https://ucarecdn.com/8065aeb7-37b7-46fb-b253-d4a811d5e136/)

In the **"Role"** tab, search and select **"VM Scanner Operator"** & Click **"Next"**.

![Image](https://ucarecdn.com/891c0d87-d666-4c75-8199-ed8d65d7bbf2/)

Leave the **"Assign access to**"default value.

Click on **"Select Members"**, search for the name of the app registration (e.g. "AikidoSecurity") you created and select it.

Click **"Select"**

Click **"Review + assign"** twice

![Image](https://ucarecdn.com/5ca67420-976c-4fc1-b366-bc67a3920b68/)

Repeat the role assignment process for the role **"Disk Snapshot Contributor"**.

The App Registration now has the required roles to scan your Virtual Machines.