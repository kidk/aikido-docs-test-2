---
title: Cursor IDE
---


[Cursor](https://cursor.com/) is a code editor built for programming with AI. By integrating Aikido into your Cursor IDE you can scan your codebase for **secrets, API keys** and **SAST** code issues as you develop. It runs scans whenever you open or save a file.

Every time you make and save changes in a file, a scan runs. If any issues are detected, they are highlighted in the editor and also displayed in the Problems panel. When you hover over a detected SAST issue, additional context about the problem is provided.

### How to Install

> This plugin is only available on paid plans.

Cursor supports installing Visual Studio Code extensions. Follow the steps below:\
\
**Step 1.** Open the Extensions view in Cursor, type 'Aikido' in the search bar. Click install on the Aikido Extension page. After installation, you will be asked to add your personal access token (step 2).

**Step 2.** In Aikido, go to the [Cursor IDE integration page](https://app.aikido.dev/settings/integrations/ide/cursor) and create your token. 

**Step 3.** Check out the examples in our docs on the [Open VSIX marketplace to test ](https://open-vsx.org/extension/AikidoSecurity/aikido)whether everything works well.