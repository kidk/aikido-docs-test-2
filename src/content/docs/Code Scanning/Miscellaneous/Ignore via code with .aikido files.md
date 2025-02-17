---
title: Ignore via code with .aikido files
---


The `.aikido` file (YAML-formatted) allows you to ignore certain CVE's and exclude certain paths from being scanned by Aikido. The .aikido files are read automatically whenever a scan is initiated.

### Setting up the .aikido file

Create the .aikido file **within the root of your repository**. 

![Image](https://ucarecdn.com/9b2a4a59-3404-4012-be7a-dd43a6374104/)

## Ignore CVEs and exclude specific paths

**Ignore CVEs**

To ignore CVE's, add them to the .aikido yaml file with a reason. The Aikido UI will also show that these specific CVEs are ignored with reference to the .aikido file.

![Image](https://ucarecdn.com/97662102-7431-4590-b26a-53572f1ae18e/)

**Exclude Paths**

The `exclude` key and `paths` subkey allow you to hide specific files and directories from being scanned by Aikido code scanning. This will automatically exclude scans for secrets, SAST issues and lockfiles. 

**Note.** Each path must be a complete path from your repository's root, and wildcards are not supported.

```
ignore:
  cves:
    CVE-2020-8203:
      reason: We do not care about this CVE
exclude:
  paths:
    - src/useless-folder
    - src/index.js
    - package-lock.json
    - package.json 
```