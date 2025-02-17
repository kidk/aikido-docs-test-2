---
title: GitLab Setup for Local Image Scanning
---


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your data never leaves your premises. The scans take place locally, and the results are then uploaded to the Aikido Security platform. This setup allows you to scan any images locally on your own machine or in your CI/CD pipeline before they get sent to the registry.

## How to set up Local Scanning for images

### 1. Get your authentication token

1. Go to the [Local Scanner Image setup page](https://app.aikido.dev/settings/container-image-registry/add/localscan)
2. Generate an authentication token and copy. Note that you will only be able to view this token once.
3. Add this token as argument `--apikey` when running the Local Scanner in your project .
4. Add the authentication token to the CI/CD variables in Gitlab to make it available for use in the pipeline.\
   To do this, you need to go to your group's Settings page and then navigate to the **CI/CD** sub-page.

   ![Image](https://ucarecdn.com/0dbf926b-b7ee-4a4c-b154-8f43de26fd68/)

   Click on 'Expand' next to variables and click on 'Add variable'. You can then add the authentication token with `AIKIDO_LOCAL_SCANNER_TOKEN` as the key and the copied token contents as the value.

### 2. Running the Local Scanner

​\
Now all that is left to run the scanner on your image. You can use this example file as a guide:

```
default:
  image: docker:cli
  services:
    - docker:dind

run_aikido_selfscanner:
  script:
  - docker build ...
  - docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aikidosecurity/local-scanner image-scan your-local-image-name --apikey $AIKIDO_LOCAL_SCANNER_TOKEN
    - if: $CI_COMMIT_BRANCH == "main"
```

If you are running this in your CI, be careful to not run scan on images that are based on feature branches, to prevent production and feature results being mixed together in Aikido.\
\
To run a release gated scan before pushing to your registry, you can run a Pipeline like:

```
default:
  image: docker:cli
  services:
    - docker:dind

run_aikido_selfscanner:
  script:
  - docker build ...
  - docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aikidosecurity/local-scanner image-scan your-local-image-name --apikey $AIKIDO_LOCAL_SCANNER_TOKEN --fail-on critical
  - docker push ...
    - if: $CI_COMMIT_BRANCH == "main"
```

Adjust the severity specified in `--fail-on` to match your needs.

### 4. Check your scanning results

After your first scan is done, you can go to the Aikido Feed to check out your results. A image with the name you specified will have been created in the Aikido UI, containing all results from the scanning.