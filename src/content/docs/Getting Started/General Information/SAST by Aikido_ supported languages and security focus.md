---
title: SAST by Aikido_ supported languages and security focus
---


### How Aikido SAST currently works

Aikido’s SAST engine is built to find and prioritize security issues in your code. Unlike traditional SAST tools like SonarQube that focus on code readability, style, and maintainability, **Aikido focuses exclusively on security**. No noise, just the vulnerabilities you need to fix.

Aikido SAST engine is based on our **custom risk categorisation model**. Some of these categorisation: -

- Aikido removes findings that are not related to security (eg opinionated code styling rules). 
- Findings that reside in repositories that a user categorized as sensitive will get upgraded. 
- Findings inside of files that are not intended for production (eg unit tests or functions that aren't used in production) might get downgraded and so on.

Our SAST engine also leverage some of the best open-source engines out there, which we have significantly customized and fine-tuned to provide you sharper, relevant results over the years.

To view all individual rules that are active per language, check out our [SAST Checks](https://app.aikido.dev/repositories/sast) or [Infrastructure as Code](https://app.aikido.dev/repositories/iac) checks to view the rules per language.

### Language support

Aikido is not sensitive to the versions of languages. By default, we support all versions.

| **Language** | **Base engine** |
| --- | --- |
| JavaScript | Aikido Engine + Opengrep |
| Typescript | Aikido Engine + Opengrep |
| PHP | Aikido Engine + Opengrep |
| .NET/C# | Aikido Engine + Opengrep |
| Java | Aikido Engine + Opengrep |
| Scala | Aikido Engine + Opengrep |
| C/C++ | Aikido Engine + Opengrep |
| Swift | Aikido Engine + Opengrep |
| Android | Aikido Engine + Opengrep |
| Kotlin | Aikido Engine + Opengrep |
| Dart | Aikido Engine + Opengrep |
| Go | Aikido Engine + Opengrep |
| Ruby | Aikido Engine + Opengrep |
| Python | Aikido Engine + Opengrep |
| Elixir | Aikido Engine + Opengrep |
| Infrastructure-as-code files (Terraform, Cloudformation, Docker,..) | Checkov |
| Exposed secret discovery in all files inside of Git history | Aikido Base Engine with Liveness Checks + Gitleaks |
