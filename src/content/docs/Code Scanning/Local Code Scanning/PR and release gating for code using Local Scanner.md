---
title: PR and release gating for code using Local Scanner
---


In addition to using the local scanner for identifying and reporting security issues in your codebase, you can also use the Aikido Local Scanner for gating in your CI. We provide two types of gating, **release gating** and **PR gating**.

## Release Gating

Release gating ensures that your software meets specific security criteria before being made available to users or customers. This mode performs a scan on your default branch and pushes the results to the Aikido feed. If there are any open issues that match or exceed your chosen severity after the scan, the CI pipeline will fail.

This mode is **also** available for image scanning and can prevent pushes to image repositories if there are any issues in your image.

To enable release gating add the `--fail-on <severity>` option to the scan command.

## PR Gating

The PR gating mode ensures that the new code meets specific security criteria before merging into your default branch. This mode scans the changes introduced in the PR. If any new issues that match or exceed your chosen severity are introduced, the CI pipeline will fail.

To enable release gating, add the `--fail-on <severity>` option to select your preferred severity level. Then, add the `--gating-mode pr` option to signify that you wish to perform PR gating. You must also specify the base (`--base-commit-id <commit-id>`) and head commit (`--head-commit-id <commit-id>`). If there a scan was previously performed on the base commit id, the scan results will be compared to those. If not, the results will be compared to the most recent scan on your default branch.

## Examples

### GitLab Self Managed

For general information about setting up the Local Scanner in a GitLab environment, check out [this article](https://help.aikido.dev/doc/gitlab-self-managed-setup-for-local-scanner/docFsQvMRCCd).\
\
Example `.gitlab-ci.yml` for release gating:

```
default:
  image:
    name: aikidosecurity/local-scanner:latest
    entrypoint: [""]

run_aikido_selfscanner:
  script:
  - aikido-local-scanner scan ./ --apikey $AIKIDO_LOCAL_SCANNER_TOKEN --repositoryname $CI_PROJECT_NAME --branchname main --fail-on critical
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
```

Example `.gitlab-ci.yml` for PR gating:

```
default:
  image:
    name: aikidosecurity/local-scanner:latest
    entrypoint: [""]

run_aikido_selfscanner:
  script:
  - aikido-local-scanner scan ./ --apikey $AIKIDO_LOCAL_SCANNER_TOKEN --repositoryname $CI_PROJECT_NAME --branchname $CI_COMMIT_REF_NAME --gating-mode pr --fail-on critical --base-commit-id $CI_MERGE_REQUEST_DIFF_BASE_SHA --head-commit-id $CI_COMMIT_SHA
  rules:
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
```

### GitHub

For general information about setting up the Local Scanner in a GitHub environment, check out [this article](https://help.aikido.dev/doc/github-action-setup-for-local-scanner/docn4KpccwdF).\
Example `.github/workflows/aikido-scan.yml` for release gating:

```
on:
  push:
    branches:
      - main

name: Aikido Scan
jobs:
  aikido-local-scan-repo:
    runs-on: ubuntu-latest
    container:
      image: aikidosecurity/local-scanner:latest
    steps: 
      - uses: actions/checkout@v4 
        with: 
          token: ${{ secrets.GITHUB_TOKEN }} 
          path: my-repo 
      - name: Run scan
        run: aikido-local-scanner scan my-repo --apikey ${{ secrets.AIKIDO_API_KEY }} --repositoryname MyRepo --branchname main --fail-on critical
```

Example `.github/workflows/aikido-scan.yml` for PR gating:

```
on:
  pull_request:
    branches:
      - main

name: Aikido Scan
jobs:
  aikido-local-scan-repo:
    runs-on: ubuntu-latest
    container:
      image: aikidosecurity/local-scanner:latest
    steps: 
      - uses: actions/checkout@v4 
        with: 
          token: ${{ secrets.GITHUB_TOKEN }} 
          path: ${{ github.event.repository.name }}
      - name: Run scan
        run: aikido-local-scanner scan ${{ github.event.repository.name }} --apikey ${{ secrets.AIKIDO_API_KEY }} --repositoryname ${{ github.event.repository.name }} --branchname ${{ github.event.pull_request.head.ref }} --gating-mode pr --fail-on critical --base-commit-id ${{ github.event.pull_request.base.sha }} --head-commit-id ${{ github.event.pull_request.head.sha }}
```