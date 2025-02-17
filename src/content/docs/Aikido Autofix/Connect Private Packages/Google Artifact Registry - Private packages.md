---
title: Google Artifact Registry - Private packages
---


When letting Aikido update your dependencies in repositories with private packages, Aikido would need to also have access to the private packages so that we can properly update your lockfiles. You can provide private **Google Artifact Registry** configuration in Aikido for this.

For now only this is only supported for JavaScript dependencies.

### 1. Create a Service Account

First, create a service account in your Google Cloud project:

1. Go to the Google Cloud Console.
2. Navigate to **IAM & Admin** &gt; **Service Accounts**.
3. Click **Create Service Account**.
4. Fill in a **Service account name** such as `Aikido Artifact Registry Reader` and click **Create And Continue**.
5. Grant the service account with the **Artifact Registry Reader** role.

   ![Image](https://ucarecdn.com/9f0adb2d-d03b-4da9-a164-32e6d0e18237/)
6. Click **Continue** and **Done**.

### 2. Create a Key for the Service Account

1. On the **Service Accounts** page, find the service account you just created.
2. Click on the three dots on the right and select **Manage Keys**.
3. Click **Add Key** &gt; **Create New Key**.
4. Choose **JSON** and click **Create**.
5. Save the JSON key file to a secure location.

### 3. Configuration in Aikido

Once the prerequisites are fulfilled, you can configure aikido to authenticate with your private registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/settings/integrations/autofix).
2. Click on **Manage private registry connection**, the configuration modal will now be shown
3. Fill in your **Private registry host**. Should look like `https://<region>-npm.pkg.dev/<project-id>/<repository-name>/`
4. Paste your saved **JSON Key** content in the **Private registry token** field

   ![Image](https://ucarecdn.com/238fb0d1-05b5-447f-9e6c-ba52d015c1ac/)
5. Click **Save** to save the configuration.