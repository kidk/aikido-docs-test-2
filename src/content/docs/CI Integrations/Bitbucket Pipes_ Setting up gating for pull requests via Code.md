---
title: Bitbucket Pipes_ Setting up gating for pull requests via Code
---


> We do not recommend using this functionality anymore, but use the PR gating via the Aikido Dashboard instead as it does not use CI minutes, easier management in bulk and less error-prone.

Aikido's integration with Bitbucket Pipes allows you to flag or block risky code from being merged. Our CI scans target **IaC**, **SAST**, and **dependency issues**.

Integrate Aikido into your Bitbucket workflow with Aikido's integration for Bitbucket Pipes. The source code for our [Bitbucket Pipe is here.](https://bitbucket.org/aikido-production/bitbucket-pipe/src)

## Prerequisites

### Enable pipelines in your repositories

In order to enable the integration, you first must ensure that pipelines are enabled for the repositories you'd like to secure in Bitbucket. In order to do this, you need to follow these steps:

1. Log in to your Bitbucket account
2. Go to the repository you'd like to enable pipelines for
3. Click on "Repository settings" in the navigation on the left
4. Scroll in the navigation on the left to the section "Pipelines" and click on "Settings"
5. Enable pipelines

![Image](https://ucarecdn.com/95d9dbd1-ca3b-4dd2-806c-41577276cb35/)

### Obtain your Aikido CI integration token

Next, we need to make sure that Aikido's CI integration can connect to your Aikido account. We'll do that via a secret auth token which you can generate in your Aikido account.

1. Go to our [CI Integrations page](https://app.aikido.dev/settings/integrations/continuous-integration).
2. Generate an authentication token. You will need to expose this in your CI environment for the integration. Make sure to copy the token and keep it somewhere secure. You will need it in a next step.
3. Click on Bitbucket Pipes.\
   ​

![Image](https://ucarecdn.com/0330325f-82c1-4f99-a2d3-d20b2ee8c36a/)

## Configuring the integration in your repo

Finally, we'll expose the auth token to your pipelines and create the configuration file which will run the integration.

1. Go to your repository settings in your Bitbucket account
2. Scroll in the navigation on the left to the section "Pipelines" and click on "Repository variables"
3. Add the auth token from the previous step as a repository variable. In this article, we'll name it `AIKIDO_API_KEY`, but you can name it whatever you like.
4. We recommend to keep the `secured` checkbox checked, to make sure the token is not printed to the console in the pipelines.
5. Click on "Add"\
   ​

![Image](https://ucarecdn.com/f0c428b9-419c-4be8-9ae8-2f55b9eb1101/)

\
Now, you need to create a configuration file to tell Bitbucket pipelines which checks to run when and where. Create a file called `bitbucket-pipelines.yml` in your repository root and add the following contents to it.

```
pipelines:
  pull-requests:
    '**':
      - step:
          name: Aikido Security Scan
          script:
          - pipe: aikido-production/bitbucket-pipe:1.0.5
            variables:
              AIKIDO_API_KEY: $AIKIDO_API_KEY
```

\
This configuration will tell Bitbucket the following:

- Run this pipeline on each pull request
- `'**'` is a filter where you can tell Bitbucket to only run it on certain pipelines, in this example we want to run it on all pull requests
- We add a step called "Aikido Security Scan" which will run a script
- We'll run the `aikido-production/bitbucket-pipe` which is our official Bitbucket Pipelines integration with version `1.0.5`. We recommend to keep this version pinned to the latest version that meets your requirements
- We expose the `AIKIDO_API_KEY` environment variable that we added in the previous step to the environment of Aikido's integration so it can connect to your Aikido account

The official integration will by default fail when it finds critical vulnerabilities in the last commit of the pull request. This behaviour, amongst other is configurable through other variables. This is an overview of the variables that you can currently pass to the integration to control its behaviour.

| **name** | **kind** | **default** | **explanation** |
| --- | --- | --- | --- |
| AIKIDO_API_KEY (required) | string | NULL | Your aikido CI auth token |
| MINIMUM_SEVERITY | string | 'CRITICAL' | The severity at which to fail when it finds issues. Can be one of 'CRITICAL', 'HIGH', 'MEDIUM' or 'LOW' |
| FAIL_ON_TIMEOUT | string | false | Whether or not the pipeline should fail when the scans do not complete within a certain amount of time. Can be one of 'true' or 'false'. |
| FAIL_ON_DEPENDENCY_SCAN | string | false | Whether or not the pipeline should fail in case 3rd party dependency issues are detected. Can be one of 'true' or 'false'. |
| FAIL_ON_SAST_SCAN | string | false | Whether or not the pipeline should fail in case sast issues are detected. Can be one of 'true' or 'false'. |
| FAIL_ON_IAC_SCAN | string | false | Whether or not the pipeline should fail in case infrastructure as code issues are detected. Can be one of 'true' or 'false'. |

Push this file with your configuration to your repository's main branch and you'll see that when syncing your pull requests to the main branch, that the pipeline checks will run on each push.