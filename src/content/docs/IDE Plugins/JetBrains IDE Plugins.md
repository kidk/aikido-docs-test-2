---
title: JetBrains IDE Plugins
---


Aikido integrates with the majority of Jetbrains IDEs and scans your codebases for **secrets, API keys** and **SAST** code issues. It runs scans whenever you open or save a file.

Every time you make and save changes in a file, a scan runs. If any issues are detected, they are highlighted in the editor and also displayed in the Problems panel. When you hover over a detected SAST issue, additional context about the problem is provided.

![Image](https://ucarecdn.com/530564ed-8698-4161-b13e-4aa301e00836/)

### Supported IDEs

We support the majority of Jetbrain IDEs

- IntelliJ IDEA (Java/Kotlin/Spring)
- GoLand (Go/JS/TS)
- PhpStorm (PHP/Laravel/Symfony)
- PyCharm (Python/Django)
- Rider (C#/.NET/ASP.NET)
- WebStorm (JS/TS/React)

### How to Install and Test

> This plugin is only available on paid plans.

**Step 1.** Head over to the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/24993-aikido-security) and click **Get.** After installation, you will be asked to add your personal access token (step 2).

**Step 2.** In Aikido, go to the [JetBrains IDE Integration Screen](https://app.aikido.dev/settings/integrations/ide/jetbrains) and create your token. 

![Image](https://ucarecdn.com/3fefe56c-0d6a-43b6-a61d-6bf47f6c7118/)

**Step 3.** Check out the examples in our docs on the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/24993-aikido-security) to test whether everything works well.