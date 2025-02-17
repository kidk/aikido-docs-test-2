---
title: Poetry - Private packages
---


When letting Aikido update your dependencies in repositories with private packages, Aikido would need to also have access to the private packages so that we can properly update your lockfiles. For Poetry, you can provide private either a **Google Artifact Registry** configuration service key or provide environment varaibles in Aikido for this.

## Adding credentials with environment variables

When the credentials to connect to the private registry are static, you can provide environment variables for this in the private registry connection modal. The environment variables should be created in the following format:\
- `POETRY_HTTP_BASIC_[SOURCE_NAME]_USERNAME`\
- `POETRY_HTTP_BASIC_[SOURCE_NAME]_PASSWORD`

Where the `[SOURCE_NAME]` is the name of the data source which you specified in your pyproject.toml file.\
\
When creating a PR via Autofix, Aikido will include these environment variables when running poetry commands.

## Adding credentials for GCP Artifact Registry

For some registries, the credentials can not be generated statically, such as for GCP Artifact registry. In this case you can follow the steps below.

### 1. Create a Service Account

First, create a service account in your Google Cloud project:

1. Go to the Google Cloud Console.
2. Navigate to **IAM & Admin** &gt; **Service Accounts**.
3. Click **Create Service Account**.
4. Fill in a **Service account name** such as `Aikido Artifact Registry Reader` and click **Create And Continue**.
5. Grant the service account with the **Artifact Registry Reader** role.

   ![Image](https://ucarecdn.com/8d6db05a-1848-4c9e-8d0a-5bd824229aa9/)
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
3. Select **Poetry** from the tab bar

   ![Image](https://ucarecdn.com/c6c873de-7657-49ef-8b22-69bd99a8be02/)
4. Paste your saved **JSON Key** content in the **Private registry service account key** field
5. Click **Save** to save the configuration.