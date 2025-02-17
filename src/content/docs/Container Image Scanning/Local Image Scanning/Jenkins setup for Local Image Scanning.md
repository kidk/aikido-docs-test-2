---
title: Jenkins setup for Local Image Scanning
---


The Aikido Security Local Scanner is a tool that enables you to perform Aikido Security scans within your environment, ensuring your data never leaves your premises. The scans take place locally, and the results are then uploaded to the Aikido Security platform. This setup allows you to scan any images locally on your own machine or in your CI/CD pipeline before they get sent to the registry.

## How to set up Local Scanning for images

### 1. Get your authentication token

1. Go to the [Local Scanner Image setup page](https://app.aikido.dev/settings/container-image-registry/add/localscan)
2. Generate an authentication token and copy. Note that you will only be able to view this token once.
3. Add this token as argument `--apikey` when running the Local Scanner in your project .
4. Store this token in your Jenkins. To do this, navigate to the "Credentials" page in the Jenkins settings.

![Image](https://ucarecdn.com/5ee149ff-1adb-483d-8e26-62b92a78544d/)

### 2. Adding the Local Scanner to your project

Download the local scanner binary from the Aikido UI. In Jenkins, add it on your build node and add it to /usr/local/bin to access it by name. Make sure the binary is executable (example: `chmod +x -R aikido-local-scanner`). If you are using a runner that has Docker installed, it is possible to skip this step and use the Local Scanner docker image to perform the scan (see below).

### 3. Running the Local Scanner

Now all that is left to run the scanner on your repository.\
​\
Make sure that the local scanner is only triggered for your default branch. By default, Aikido supports scanning one branch in your repository for dependency and code issues, typically the main or master branch. Therefore, we recommend running the local scanner exclusively on that branch to avoid mixing scan results on the Aikido platform. If you use git, you can specify this in the *Branches to build* section.

![Image](https://ucarecdn.com/065da2fc-d249-4a71-b0ce-01219ecfa118/)

Now, make the API key available to use in the project by adding it to your build environment.

![Image](https://ucarecdn.com/2e86c5ed-ea49-4d84-9911-226c55aa5547/)

\
Add an 'Execute shell' step to your project with the following content. You can either use name of your image or use the path of a tar artifact of your image.

```
aikido-local-scanner image-scan your-image --apikey $AIKIDO_API_KEY
```

Or if you are using our docker image

```
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aikidosecurity/local-scanner image-scan your-image --apikey $AIKIDO_API_KEY
```

\
To run a release gated scan before pushing to your registry, you can add `--fail-on critical` to the commands above. Adjust the severity to meet your specific gating needs.

### 4. Check your scanning results

After your first scan is done, you can go to the Aikido Feed to check out your results. A image with the name you specified will have been created in the Aikido UI, containing all results from the scanning.