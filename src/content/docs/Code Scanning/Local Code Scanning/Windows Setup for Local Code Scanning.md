---
title: Windows Setup for Local Code Scanning
---

**Table of contents:**
- [Prerequisites](#prerequisites)
- [How to set up Local Scanning](#how-to-set-up-local-scanning)
  - [1. Get your authentication token](#1-get-your-authentication-token)
  - [2. Running the Local Scanner](#2-running-the-local-scanner)
  - [4. Check your scanning results](#4-check-your-scanning-results)


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your code never leaves your premises. The scans take place locally, and the results are then uploaded to the Aikido Security platform. This setup allows you to scan any repos locally own your own machine. 

## Prerequisites

Ensure that you have [Docker installed](https://docs.docker.com/desktop/) before proceeding.

## How to set up Local Scanning

**Prerequisite**: make sure to have created an account that allows for Local Scanning.\
[More information on creating a Local Scanning Account](https://help.aikido.dev/en/articles/9070345-how-to-create-an-account-for-local-scanning-on-aikido).

### 1. Get your authentication token

1. Go to the [Local Scanner setup page](https://app.aikido.dev/settings/integrations/localscan)
2. Generate an authentication token and copy. Note that you will only be able to view this token once.
3. Add this token as argument `--apikey` when running the Local Scanner in your project .

### 2. Running the Local Scanner

Now all that is left to spin up a container and scan your repository. Navigate to the root of your repository and run the following command; filling in your key, repository name and branch name. 

If you are using the command prompt:

```
docker run --rm -v "%cd%:/my-app" aikidosecurity/local-scanner scan /my-app --apikey AIK_CI_xxx --repositoryname RepoName --branchname main
```

If you are using Powershell:

```
docker run --rm -v "{PWD}:/my-app" aikidosecurity/local-scanner scan /my-app --apikey AIK_CI_xxx --repositoryname RepoName --branchname main
```

By default all scanners will be executed, if you'd like to run only a selection of scanners, you can do so by supplying the scanner names `--scanners` option. More information on CLI options can be found [here](https://help.aikido.dev/en/articles/9027526-local-scanner-cli-options).

### 4. Check your scanning results

After your first scan is done, you can go to the Aikido Feed to check out your results. A repository with the name you specified will have been created, containing all results from the scanning.