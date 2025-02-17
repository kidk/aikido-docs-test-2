---
title: Export RAW SBOM of your containers
---


## Introduction

Exporting a RAW SBOM with Aikido enhances software security and transparency. This feature is particularly useful for:

- Identifying the filesystem locations of issue discoveries.
- Tracking the origin of installed components.

## Step-by-Step Guide

**Step 1:** Navigate to any **container detail** page on Aikido.

**Step 2:** Click **Actions** in the top right.\
​

![Image](https://ucarecdn.com/fc079c8a-dbd1-48b2-a52d-788db57184da/)

\
​**Step 3:** Choose **Export RAW SBOM** to generate and download the SBOM for your container.

## Limitations

The RAW SBOM Export is available only for images scanned by Aikido, not for those analyzed through AWS Inspector or GCP Vulnerability Scanning.

More information on setting up your container scanning with the Aikido Scanner can be found [here](https://help.aikido.dev/en/articles/8911170-container-scanning-for-aws-ecr-with-the-aikido-scanner).

### Generate and Export via API

Aikido also supports generation and download of SBOM via API. More information can be found in our [Apidocs](https://apidocs.aikido.dev/reference/exportcontainerrepolicenses)[.](https://apidocs.aikido.dev/reference/exportcoderepolicenses)

---