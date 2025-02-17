---
title: Setting up image scanning with Local Scanner
---


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your data never leaves your premises. The scans take place locally, and the results are then uploaded to the Aikido Security platform. This setup allows you to scan any images locally on your own machine or in your CI/CD pipeline before they get sent to the registry.

## How to set up Local Scanning for images

### 1. Get your authentication token

1. Go to the [Local Scanner Image setup page](https://app.aikido.dev/settings/container-image-registry/add/localscan)
2. Generate an authentication token and copy. Note that you will only be able to view this token once.
3. Add this token as argument `--apikey` when running the Local Scanner in your project .

   ![Image](https://ucarecdn.com/6376840b-120d-43e5-a42f-92cd51ee0ce8/)

### 2. Adding the Local Scanner to your project

Download the local scanner binary from the Aikido UI.

### 3. Running the Local Scanner

**Prerequisite:** You need to have a running Docker daemon. \
​\
Now all that is left to run the scanner on your image.

```
./aikido-local-scanner image-scan your-image-name --apikey AIK_CI_xxx
```

Or if you are using our docker image

```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aikidosecurity/local-scanner image-scan your-image-name --apikey AIK_CI_xxx
```

\
If you are running this in your CI, be careful to not run scan on images that are based on feature branches, to prevent production and feature results being mixed together in Aikido.

You can also run the scanner in release or PR gating mode, check out [this article](https://help.aikido.dev/doc/untitled-document/docM6vhIJ5KI) for more info.

### 4. Check your scanning results

After your first scan is done, you can go to the Aikido Feed to check out your results. A image with the name you specified will have been created in the Aikido UI, containing all results from the scanning.

---