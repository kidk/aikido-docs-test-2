---
title: AI Autofix for SAST and IaC Issues
---


The goal of Aikido has always been to save you time by reducing noise, focusing on the issues that truly matter. With the introduction of the **AI Autofix** feature, Aikido takes this one step further.

### Key Features of AI Autofix

- **Preview Changes:** Review detailed previews of AI-generated fixes before implementing them to ensure alignment with your standards.
- **Create Pull Requests (PRs):** Generate pull requests directly in your Source Control Management (SCM) system from the Autofix interface.
- **Direct IDE Integration:** Apply fixes instantly to your codebase via the VS Code integration, saving even more time.

  ![Image](https://ucarecdn.com/859a9d47-c060-4244-8c32-89fff802c11e/)

---

### Important Info

- **We do not use your code for training / fine-tuning**
  - Code snippets required for generating fixes are securely transmitted to **AWS Bedrock** over encrypted channels. Aikido **nor** [AWS Bedrock](https://aws.amazon.com/bedrock/security-compliance/) use your code for training or fine-tuning AI models.
- **Speed**
  - Simple fixes are typically generated in under 5 seconds. Larger or more complex fixes may take up to 30 seconds, depending on file size and issue complexity.
- **Confidence Levels**
  - Fixes are categorized into confidence levels: **High**, **Medium**, and **Low**. Manual reviews before merging are recommended.

    ![Image](https://ucarecdn.com/2c623f8c-0bb2-444c-8071-d957e38e3f99/)

---

### How to use the AI Autofix functionality

- **Step 1**. Navigate to the [Autofix Page. ](https://app.aikido.dev/issues/fix/sast)All potential fixes are grouped by type and location.

  ![Image](https://ucarecdn.com/2b801f85-4354-421b-b93d-7ff66d316815/)
- **Step 2.** Select one or multiple fixes to preview or create a PR for. 

  ![Image](https://ucarecdn.com/b9f2fa3e-053f-492c-8a1d-3f0ed3b90a2c/)
- **Step 3.** Preview and Apply. 
  - **Create a PR**: Automatically generate a pull request in your SCM.
  - **Apply Directly**: Instantly implement the fix in your codebase via VS Code integration.

![Image](https://ucarecdn.com/f6ac142a-2711-4ce2-b4d4-db6ae64938b2/)

---