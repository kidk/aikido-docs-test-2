---
title: Azure Pipelines_ Setting up gating for pull requests via code
---


> We do not recommend using this functionality anymore, but use the PR gating via the Aikido Dashboard instead as it does not use CI minutes, easier management in bulk and less error-prone.

Aikido's integration with Azure Pipelines allows you to flag or block risky code from being merged. Our CI scans target **IaC**, **SAST**, and **dependency issues**.

If you're on the Aikido Pro plan, you can also use this integration for [CI Gating](https://help.aikido.dev/en/articles/7945775-setting-up-feature-branch-scanning).

> Note: this integration is not available for TFVC repos.

## Set up integration

**Step 1.** Go to our [CI Integrations page](https://app.aikido.dev/settings/integrations/continuous-integration).

**Step 2.** Generate an authentication token. You will need to expose this in your CI environment for the integration. Make sure to copy the token in this step.

**Step 3.** Click on Azure Pipelines. You will be redirected to the Aikido Azure Extension Page

![Image](https://ucarecdn.com/8787fd95-f430-4ceb-9a6a-2e9c085d81fe/)

## Install the extension

Click the green "Get it free"-button

![Image](https://ucarecdn.com/e1fd7298-e234-4057-8943-57499e60f98d/)

Select the organisation where you want to install the extension and click install

![Image](https://ucarecdn.com/6efd326d-b1e8-418e-a951-b29c06ca06c1/)

The extension is now installed. You can verify this by going to "Organisation Settings &gt; Extensions" In your Azure Organisation

![Image](https://ucarecdn.com/d2df10f4-1aa6-4e57-8f3c-687214412530/)

## Set up the pipeline for PRs

We recommend creating a separate Pipeline for this, but it can be integrated in existing build

Go to Pipelines and create a new azure pipeline. At the configure step select "Starter pipeline"

![Image](https://ucarecdn.com/cd05ea44-e92e-485a-b9f8-6923a4e03341/)

In the yml-file use following content.

```
pool:
  vmImage: ubuntu-latest
steps:
  - task: AikidoScanTask@1 
    inputs: 
      secretKey: $(AIKIDO_SECRET) 
      minimumSeverity: 'LOW'
      failOnDependencyScan: true
      failOnSastScan: false
      failOnIacScan: false
      failOnTimeout: true
      timeoutSeconds: 180
```

For the secretKey we recommend using a variable to avoid the secretKey from being exposed. 

Add a new variable for the AIKIDO_SECRET. This is the token that you generated earlier in the Aikido app.

Click the Variables button.

![Image](https://ucarecdn.com/d440d9d8-440a-4e85-9aab-86e8da0dbfd7/)

Click the button with the Plus icon.

![Image](https://ucarecdn.com/f9adf410-9c08-4a7b-8638-76c4c89faf69/)

Give your Variable the name "AIKIDO_SECRET". The value should be the token that you generated earlier in the Aikido app. Check the "Keep this value secret option" to fully secure this secret. Click "OK" to save the variable.

![Image](https://ucarecdn.com/6a107e4a-5cb0-478f-92a6-dc995520276c/)

Under the input section there are some required field.

- **secretKey:** This is the token generated in **step2** of [Set up integration](https://help.aikido.dev/en/articles/9099968-setting-up-gating-for-pull-requests-with-azure-pipelines#h_1a95ad3e70). We recommend saving this in an ENV Variable for your pipeline.
- **minimumSeverity:** When issues of this severity are found the pipeline should fail. Possible options are "LOW", "MEDIUM", "HIGH" & "CRITICAL"

Some optional fields are:

- **failOnDependencyScan:** Boolean value that determines whether the scan should fail on the dependency scan. Default is false
- **failOnSastScan:** Boolean value that determines whether the scan should fail on the SAST scan. Default is false
- **failOnIacScan:** Boolean value that determines whether the scan should fail on the IaC scan. Default is false
- **timeoutSeconds:** Integer value that determines when the task should stop running: Default is 180
- **failOnTimeout:** Boolean value that determines whether the scan should fail on timeout. Default is false

Save and Run the pipeline.

Once your pipeline appears in Azure Pipelines. Go to "Branches" And Select "Branch policies" for the target branches of your PRs where you want run the scan.

![Image](https://ucarecdn.com/25e06f66-3bf0-4cfa-a2bd-890e9a864940/)

Go to Build Validation and click the add icon

![Image](https://ucarecdn.com/58ab5e0c-f40e-4906-bea5-f68cb4824a3b/)

Select your new Aikido Scan pipeline. Fill in your preferred options and make sure to give this build policy a display name.

![Image](https://ucarecdn.com/353f1374-3eaf-4b95-8561-c004feabb423/)

Aikido will now scan new PRs where the target branch is this branch. You can set this up for multiple branches

---