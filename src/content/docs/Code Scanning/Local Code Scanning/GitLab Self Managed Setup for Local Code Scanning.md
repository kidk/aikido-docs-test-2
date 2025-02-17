---
title: GitLab Self Managed Setup for Local Code Scanning
---

**Table of contents:**
- [How to set up Local Scanning](#how-to-set-up-local-scanning)
- [1. Get your authentication token](#1-get-your-authentication-token)
- [2. Running the Local Scanner](#2-running-the-local-scanner)
  - [Using Docker](#using-docker)
- [3. Check your scanning results](#3-check-your-scanning-results)


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your code never leaves your premises. The scans take place locally, and the results are then uploaded to the Aikido Security platform. This setup allows easy integration of the Local Scanner into your GitLab project for reporting purposes.

## How to set up Local Scanning

**Prerequisite**: make sure to have created an account that allows for Local Scanning.\
[More information on creating a Local Scanning Account](https://help.aikido.dev/en/articles/9070345-how-to-create-an-account-for-local-scanning-on-aikido).

## 1. Get your authentication token

1. Go to the [Local Scanner setup page](https://app.aikido.dev/settings/integrations/localscan)
2. Generate an authentication token and copy. Note that you will only be able to view this token once.
3. Add the authentication token to the CI/CD variables in Gitlab to make it available for use in the pipeline.\
   To do this, you need to go to your group's Settings page and then navigate to the **CI/CD** sub-page.

   ![Image](https://ucarecdn.com/3f45755f-a3dc-4613-a557-54d49e142418/)

   Click on 'Expand' next to variables and click on 'Add variable'. You can then add the authentication token with `AIKIDO_LOCAL_SCANNER_TOKEN` as the key and the copied token contents as the value.

## 2. Running the Local Scanner

Make sure that the local scanner is only triggered for your default branch. By default, Aikido supports scanning one branch in your repository for dependency and code issues, typically the main or master branch. Therefore, we recommend running the local scanner exclusively on that branch to avoid mixing scan results on the Aikido platform. You can specify this in the rules section of your workflow file.

### Using Docker

The easiest way to use our local scanner in your Gitlab pipelines is by using our Docker image. \
​\
Example `.gitlab-ci.yml`:

```
default:
  image:
    name: aikidosecurity/local-scanner:latest
    entrypoint: [""]

run_aikido_selfscanner:
  script:
  - aikido-local-scanner scan ./ --apikey $AIKIDO_LOCAL_SCANNER_TOKEN --repositoryname $CI_PROJECT_NAME --branchname main
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

Specify your preferred branch using the `--branchname` option when executing the command.

If this is the first scan for this repository, Aikido will create a repository with the name you specified, containing all the scanning results. Subsequent scan results will be collected under this repository name in Aikido.

By default all scanners will be executed, if you'd like to run only a selection of scanners, you can do so by supplying the scanner names `--scanners` option. More information on CLI options can be found [here](https://help.aikido.dev/en/articles/9027526-local-scanner-cli-options).\
\
You can also run the scanner in release or PR gating mode. Release gating mode is helpful when scanning your repository prior to releasing, as it ensures there are no open issues before a potential release. When running in release gating mode, the scanner process will fail when there are any open issues of the chosen severity or higher after the scan is finished. PR gating mode can be used to scan for any potentially newly introduced issues in a PR.

More information about release or PR gating mode can be found in [this article](https://help.aikido.dev/doc/pr-and-release-gating-using-local-scanner/doctrfqR4ZlP).

## 3. Check your scanning results

After your first scan is done, you can go to the Aikido Feed to check out your results. A repository with the name you specified will have been created, containing all results from the scanning.