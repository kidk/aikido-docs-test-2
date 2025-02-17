---
title: CLI options for Local Scanner
---


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your code never leaves your premises. Below you can find the options that can be passed when running the local scanner.

### Repository scanning

```markdown
Usage: aikido-local-scanner scan [options] <path>

Run a scan.

Arguments:
  path                                     The path you want to scan.

Options:
  --apikey <apikey>                        Apikey to send scanning results to Aikdo.  (env: AIKIDO_API_KEY)
  --repositoryname <repositoryname>        Repo name to create or send results to.
  --branchname <branchname>                Branch name that is being scanned.
  --tmpdirectory <tmpdirectory>            Temporary directory to use during scanning. (default: "./.aikidotmp")
  --debug                                  Add additional debug information to command output.
  --disable-artifact-scanning              Disable trivy rootfs scanning. Use to speed up scanning at the cost of not scanning artifacts such as .jar files.
  --secrets-scanning-full-git-history      Enable scanning the full Git history for secrets.
  --secrets-scanning-one-week-git-history  Enable scanning only the last 7 days of the Git history for secrets.
  --scan-types [types...]                  Specify which types of scans should be executed. This will overwrite the --scanners flag (cf below). (choices: "code", "dependencies", "iac", "secrets", default: [])
  --scanners [scanners...]                 Specify which of the scanners should be executed. (choices: "trivy", "semgrep", "checkov", "syft", "gitleaks")
  --exclude <exclude_path>                 Specify a file or folder path that should be excluded from the scan. This option may be specified multiple times. (default: [])
  --fail-on <severity>                     Runs scanner in gating mode and fails on the given severity or higher. (choices: "low", "medium", "high", "critical")
  --gating-mode <mode>                     Indicate whether the scanner should run in release or PR gating mode. Release gating mode scans your main branch and waits to see if there are any issues that should prevent release, in pull request mode, Aikido seeks ONLY new vulnerabilities introduced in a branch. You must supply a base and head commit for the comparison to work. Should be combined with the --fail-on flag (choices: "release", "pr", default: "release")
  --base-commit-id <commit-id>             Base commit id, this is the commit that Aikido will compare against to determine if a finding is new. Only used for PR gating mode.
  --head-commit-id <commit-id>             Head commit id, the commit that is being scanned. Only used for PR gating mode.
  --gating-result-output <output>          JSON file to write issues to when running in gating mode only
  --no-fail-on-timeout                     Do not fail the process in case the scan result polling times out (gating mode only)
  --max-polling-attempts <amount>          Amount of times to poll for scan results, increase this if the default value of 20 is not enough (gating mode only)
  --no-snippets                            Use this mode to not share any code snippets with Aikido.
  --checkov-skip-extension <extension>     Specify an extension to be skipped by Checkov scans specifically. This option may be specified multiple times. Example: If you want to ignore JSON files, pass .json as the value for this option. (default: [])
  --no-lockfiles-cache                     Do not allow caching of dependency- and lockfiles to enable automated rescans
  -h, --help                               display help for command
```

### Image scanning

```markdown
Usage: aikido-local-scanner image-scan [options] <image>

Run an image scan.

Arguments:
  image                            The image you want to scan.

Options:
  --apikey <apikey>                Apikey to send scanning results to Aikdo.  (env: AIKIDO_API_KEY)
  --platform <platform>            Set platform (to pull arm64 image on a amd64 system for example)
  --image-name <name>              Specify a name for the scanned image. This overwrites the default behaviour of deducting the image name from the <image> argument. Can be used to specify a descriptive name if the image name is not.
  --debug                          Add additional debug information to command output.
  --fail-on <severity>             Runs scanner in gating mode and fails on the given severity or higher. (choices: "low", "medium", "high", "critical")
  --gating-mode <mode>             Indicate whether the scanner should run in release or PR gating mode. Release gating mode scans your main branch and waits to see if there are any issues that should prevent release, in pull request mode, Aikido seeks ONLY new vulnerabilities introduced in a branch. You must supply a base and head commit for the comparison to work. Should be combined with the --fail-on flag (choices: "release", "pr", default: "release")
  --base-commit-id <commit-id>     Base commit id, this is the commit that Aikido will compare against to determine if a finding is new. Only used for PR gating mode.
  --head-commit-id <commit-id>     Head commit id, the commit that is being scanned. Only used for PR gating mode.
  --gating-result-output <output>  JSON file to write issues to (when running in gating mode only)
  --no-fail-on-timeout             Do not fail the process in case the scan result polling times out (release gating mode only)
  --max-polling-attempts <amount>  Amount of times to poll for scan results, increase this if the default value of 20 is not enough (release gating mode only)
  -h, --help                       display help for command
```

## Common use cases

Below you can find some example configurations of common use cases.

**I want to run a scan on a repository**

> The api key can also be passed as an environment variable *AIKIDO_API_KEY*

```
aikido-local-scanner scan ./ 
--apikey AIK_CI_xxx 
--repositoryname DemoApp 
--branchname main
```

**I want to run only SCA scanning on my repository**

```
aikido-local-scanner scan ./ 
--apikey AIK_CI_xxx 
--repositoryname DemoApp 
--branchname main 
--scan-types dependencies
```

**I want to run only secrets scanning on my repository**

```
aikido-local-scanner scan ./ 
--apikey AIK_CI_xxx 
--repositoryname DemoApp 
--branchname main 
--scan-types secrets
```

**I want to run only SAST scanning on my repository**

```
aikido-local-scanner scan ./ 
--apikey AIK_CI_xxx 
--repositoryname DemoApp 
--branchname main 
--scan-types sast
```

**I want to run only IaC scanning on my repository**

```
aikido-local-scanner scan ./ 
--apikey AIK_CI_xxx 
--repositoryname DemoApp 
--branchname main 
--scan-types iac
```

**I want to exclude my /staging and /development folder from being scanned**

```
aikido-local-scanner scan ./ 
--apikey AIK_CI_xxx 
--repositoryname DemoApp 
--branchname main 
--exclude staging 
--exclude development
```

**I want to run only secrets and SAST scanning and I want to exclude my /staging folder.**

```
aikido-local-scanner scan ./ 
--apikey AIK_CI_xxx 
--repositoryname DemoApp 
--branchname main 
--scan-types secrets sast
--exclude staging
```