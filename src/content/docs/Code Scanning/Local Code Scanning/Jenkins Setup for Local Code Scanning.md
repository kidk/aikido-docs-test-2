---
title: Jenkins Setup for Local Code Scanning
---

**Table of contents:**
- [Requirements](#requirements)
  - [Temporary folder​](#temporary-folder)
- [How to set up Local Scanning](#how-to-set-up-local-scanning)
- [1. Get your authentication token](#1-get-your-authentication-token)
  - [2. Adding the Local Scanner to your project](#2-adding-the-local-scanner-to-your-project)
  - [3. Running the Local Scanner](#3-running-the-local-scanner)
  - [4. Check your scanning results](#4-check-your-scanning-results)


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your code never leaves your premises. The scans take place locally, and the results are then uploaded to the Aikido Security platform. This setup allows easy integration of the Local Scanner into your Jenkins project for reporting purposes. The scanner cannot be used to perform gating on merge requests. 

## Requirements

Your Jenkins Node must meet certain requirements to run the Local Scanner. We currently support the **Linux x86_64** operating system architecture. Additionally, ensure your Node has sufficient resources. We've tested on machines equipped with 4GB RAM, a 2 Core CPU, and 14GB of storage.

The version of glibc is also crucial for running our binary. You'll need version 2.27 or higher, which was released in 2018. Consequently, most newer Linux operating systems have this version or higher. Operating systems that support this include:

- CentOS 8 or higher
- Ubuntu 18.04 or higher
- Debian 10 or higher
- Fedora 28 or higher

To verify the version of glibc on your operating system, you can run

```
$ ldd --version ldd 
(Ubuntu GLIBC 2.30-0ubuntu2.1) 2.30
```

### Temporary folder​

The scanner creates a temporary local folder (default .aikidotmp) to perform certain actions:

- Copy certain lockfiles to run efficient scanning.
- Write the results of the scanners.

This folder is cleaned up after the scanning is finished.

In addition, some files are copied to the temporary operating directory. Ensure that enough space is available; we recommend a minimum of 2GB.​

## How to set up Local Scanning

**Prerequisite**: make sure to have created an account that allows for Local Scanning.\
[More information on creating a Local Scanning Account](https://help.aikido.dev/en/articles/9070345-how-to-create-an-account-for-local-scanning-on-aikido).

## 1. Get your authentication token

1. Go to the [Local Scanner setup page](https://app.aikido.dev/settings/integrations/localscan)
2. Generate an authentication token and copy. Note that you will only be able to view this token once.
3. Add this token as argument `--apikey` when running the Local Scanner in your project.
4. Store this token in your Jenkins. To do this, navigate to the "Credentials" page in the Jenkins settings.

   ![Image](https://ucarecdn.com/79b10ff7-e7e5-4919-aaac-655ffa726b60/)

### 2. Adding the Local Scanner to your project

Download the local scanner binary from the Aikido UI. In Jenkins, add it on your build node and add it to /usr/local/bin to access it by name. Make sure the binary is executable (example: `chmod +x -R aikido-local-scanner`).

### 3. Running the Local Scanner

Now all that is left to run the scanner on your repository.\
​\
Make sure that the local scanner is only triggered for your default branch. By default, Aikido supports scanning one branch in your repository for dependency and code issues, typically the main or master branch. Therefore, we recommend running the local scanner exclusively on that branch to avoid mixing scan results on the Aikido platform. If you use git, you can specify this in the *Branches to build* section.

![Image](https://ucarecdn.com/6a83742e-ecd0-4663-9aaf-01011fa04da1/)

Now, make the API key available to use in the project by adding it to your build environment.

![Image](https://ucarecdn.com/30f94579-a386-4618-8729-12a10ff528c6/)

\
Add an 'Execute shell' step to your project with the following content

```
aikido-local-scanner scan ./ --apikey $AIKIDO_API_KEY --repositoryname DemoApp --branchname main
```

Specify your preferred branch using the `--branchname` option when executing the command.

If this is the first scan for this repository, Aikido will create a repository with the name you specified, containing all the scanning results. Subsequent scan results will be collected under this repository name in Aikido.

More information on CLI options can be found [here](https://help.aikido.dev/en/articles/9027526-local-scanner-cli-options).

You can also run the scanner in release gating mode by using the `--fail-on <severity>` flag. This feature is helpful when scanning your repository prior to releasing, as it ensures there are no open issues before a potential release. When running in release gating mode, the scanner process will fail when there are any open issues of the chosen severity or higher after the scan is finished.\
\
Example release gating command:

```
aikido-local-scanner scan ./ --apikey $AIKIDO_API_KEY --repositoryname DemoApp --branchname main --fail-on critical
```

### 4. Check your scanning results

After your first scan is done, you can go to the Aikido Feed to check out your results. A repository with the name you specified will have been created, containing all results from the scanning.