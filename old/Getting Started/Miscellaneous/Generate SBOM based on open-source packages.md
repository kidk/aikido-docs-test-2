# Generate SBOM based on open-source packages

If you are looking for a full overview of your packages & licenses and want to extract the SBOM, this is possible on the [Licenses & SBOM Report](https://app.aikido.dev/licenses) page.

## Where to find the SBOM {#where-to-find-the-sbom}

**Step 1.** Go to Reports &gt; [Licenses & SBOM](https://app.aikido.dev/licenses)

**Step 2.** Download SPDX, CycloneDX  or CSV SBOM via the top right action

![Image](https://ucarecdn.com/74772dd0-d436-4829-9063-800bb19bb697/)

**Optional.** Filter licenses on different parameters and export the SBOM after. The export takes into account the chosen filter values.

![Image](https://ucarecdn.com/b57e32eb-c238-4d10-9009-4645493f305b/)

> If you have multi-branch scanning enabled, you can get different SBOMs per legacy branch by selecting the specific legacy branch repo in the dropdown. Contact us via in-app chat for more info.

### Generate and Export via API {#generate-and-export-via-api}

Aikido also supports generation and download of SBOM via API. More information can be found in our [Apidocs.](https://apidocs.aikido.dev/reference/exportcoderepolicenses)