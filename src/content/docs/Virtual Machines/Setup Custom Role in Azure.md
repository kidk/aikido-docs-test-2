---
title: Setup Custom Role in Azure
---


This document will guide you through creating a new App Registration with client credentials inside of the Azure Portal. 

The credentials will be used by Aikido to make the necessary API requests to scan your Virtual Machines. Access to scan your Virtual Machines will be granted to the App Registration using a custom role.

These permissions are limited to the minimum required for Virtual Machine scanning:

Use the following steps to create 

Log into your [**Azure Portal**](https://portal.azure.com/) and navigate to the **Microsoft Entra ID service**.

Click on **Add** and select **App registration**

![Image](https://ucarecdn.com/ce278464-2951-4d84-877f-6afdae8ed902/)

Give the application a meaningful name, we need this name later. 

Leave the **Supported account types** default: **Accounts in this organizational directory only**.

Click on **Register**.

![Image](https://ucarecdn.com/8272b7b3-4bb3-4aec-af7e-437beeaf6095/)

You get redirected to the detail page of the newly created application. Here you can find and copy the **Application (client) ID** and the **Directory (tenant) ID**

![Image](https://ucarecdn.com/f3cb08fa-a0ae-4773-9c9f-6139ef215f3d/)

At the client credentials field, click "Add a certificate or secret"

![Image](https://ucarecdn.com/5d26a68d-fa9c-4e54-b7ae-90c784fca251/)

Click the "New client secret"-button, give a description for the secret and set the expiration date to 2 years (730 days / 24 months)

![Image](https://ucarecdn.com/95171d9f-5f07-4498-81dd-3199d5c941ef/)

Copy the **Secret's Value**

![Image](https://ucarecdn.com/04e75758-4d58-4f1f-bacd-bac394368b76/)

You now have all the required values to configure VM scanning in Aikido, once the application setup is complete in Azure Portal. Next, we need to make sure we grant the application access for VM scanning.

Navigate to **Subscriptions**, find the relevant Subscription for your Virtual Machines

Click on **"Access Control (IAM)"**.

![Image](https://ucarecdn.com/1c719e05-4e24-4386-b2dd-8f82e0bbf7a9/)

Click on the **"Add"** button.

Select **"Add custom role"**

![Image](https://ucarecdn.com/97a45405-cabc-4575-86d3-b35a8b2aac04/)

Go to the **"JSON"** tab and open the editor by clicking on **"Edit"**

![Image](https://ucarecdn.com/fa9c2c19-3293-47ef-8456-1812dd0f03a8/)

Copy generated JSON config from the Aikido setup screen, paste it into the editor

Click **"Save"**

![Image](https://ucarecdn.com/bbaca41f-78ff-4e71-80d3-ec6d355db585/)

At the bottom, click **"Review + assign"**, then **"Create"**

![Image](https://ucarecdn.com/de6a89f8-a12b-4afd-a892-c92843c530ff/)

Now that the custom role is created, we can assign it to the App Registration we created at the start.

Navigate to **Subscriptions**, find the relevant Subscription for your Virtual Machines

Click on **"Access Control (IAM)"**.

![Image](https://ucarecdn.com/bcfd2d55-34c9-4434-8f09-502937183174/)

Go to the Role assignments tab & Click on **"Add"**, then **"Add role assignment"**.

![Image](https://ucarecdn.com/4feba3fe-538d-4b7e-b1f7-615bda664244/)

In the **"Role"** tab, search and select the custom role you created (”Aikido VM Scanner”) & Click **"Next"**.

![Image](https://ucarecdn.com/edc34946-a7a6-449d-a0f1-68ec447af894/)

Leave the **"Assign access to"** default value.

Click on **"Select Members"**, search for the name of the app registration (e.g. "AikidoSecurity") you created and select it.

Click **"Select"**

Click **"Review + assign"** twice

![Image](https://ucarecdn.com/4ee31542-c6c9-40da-a557-b264660a458d/)

The App Registration now has the required permissions to scan your Azure Virtual Machines.