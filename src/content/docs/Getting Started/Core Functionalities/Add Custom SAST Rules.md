---
title: Add Custom SAST Rules
---


## Introduction

With these custom rules you can make Aikido scan for specific risks in your codebase, especially those risks that are particularly relevant for your environment. This way you can detect vulnerabilities that broader SAST rules might overlook.

## Step-by-Step Guide

**Step 1:** Go to the [repositories checks](https://app.aikido.dev/repositories/checks) page.

**Step 2:** Click on "[Create Custom Rule](https://app.aikido.dev/repositories/sast/custom/add)" in the SAST section\
​

![Image](https://ucarecdn.com/bdfc2dff-94ec-4dce-b75d-371457b06f62/)

\
​**Step 3:** Enter the following details for your rule:

- **Semgrep rule:** Define the rule Aikido will search for. **Tip:** Use the [Semgrep documentation](https://semgrep.dev/docs/writing-rules/overview) to get to know the syntax and the [Semgrep playground ](https://semgrep.dev/playground)to test your rule's effectiveness before saving.
- **Title:** Name your rule for easy identification.
- **TL;DR:** Provide a concise description of the issue. This will show up in the sidebar.
- **How to fix it:** Let your team know the best way to fix this issue.
- **Language:** Specify the programming language.
- **Aikido Score:** Set the priority level for issue reporting in the main Feed.

![Image](https://ucarecdn.com/87ebcf53-81c6-4514-a9b0-8a89cd1cd045/)

**Step 4:** Once you're satisfied with the rule's configuration, click "Save" to add it to your Aikido SAST checks. Your custom rule is now active and will be automatically applied in future scans.

### Extra Info

- Overall, the language attribute in the semgrep rule will always prevail. This can be helpful when you are looking to implement a custom rule that needs to be applied to all languages and files at once.
- If you want to create IaC rules, you can do this by setting the language to yaml/terraform/...

## Examples

- **SAST Rule:** Looking for use of the weak MD5 hashing algorithm in javascript.

  ```
  rules:
    - id: md5-used
      message: It looks like MD5 is used 
      languages:
        - javascript
      severity: WARNING
      pattern-either:
        - pattern: $CRYPTO.createHash("md5")
        - pattern: CryptoJS.MD5(...)
  ```
- **IaC Rule:** A custom rule for detecting lambda functions that might be dangerous. 

  ```
  rules:
     - id: CUSTOM-RULE-530
       languages:
         - hcl
       severity: WARNING
       message: >
         A Lambda function was found with the "type:monitored" tag, but without a "service" tag.
       patterns:
         - pattern: |-
             resource "aws_lambda_function" $ANYTHING {
               ...
               tags = {..., type = "monitored", ...}
             }
         - pattern-not: |-
             resource "aws_lambda_function" $ANYTHING {
               ...
               tags = {..., service= "...", ...}
             }
  ```