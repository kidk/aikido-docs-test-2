---
title: PR and release gating using Local Image Scanner
---


In addition to using the local scanner for identifying and reporting security issues in your images, you can also use the Aikido Local Scanner for gating in your CI. We provide two types of gating, **release gating** and **PR gating**.

## Release Gating

You can also run the scanner in release gating mode by using the `--fail-on <severity>` flag. This feature is helpful when scanning your image prior to publishing it to an image library, as it ensures there are no open issues before release. When running in release gating mode, the scanner process will fail when there are any open issues of the chosen severity or higher after the scan is finished.\
\
Example release gating command:

```
./aikido-local-scanner image-scan your-image-name --apikey AIK_CI_xxx --fail-on critical
```

## PR Gating

The PR gating mode ensures that the new code meets specific security criteria before merging into your default branch. This mode scans the changes introduced in the PR. If any new issues that match or exceed your chosen severity are introduced, the CI pipeline will fail.

To enable release gating, add the `--fail-on <severity>` option to select your preferred severity level. Then, add the `--gating-mode pr` option to signify that you wish to perform PR gating. You must also specify the base (`--base-commit-id <commit-id>`) and head commit (`--head-commit-id <commit-id>`). If there a scan was previously performed on the base commit id, the scan results will be compared to those. If not, the results will be compared to the most recent scan on your image.

Example PR gating command:

```
./aikido-local-scanner image-scan your-image-name --apikey AIK_CI_xxx --fail-on critical --gating-mode pr --base-commit-id abc123 --head-commit-id def456 
```