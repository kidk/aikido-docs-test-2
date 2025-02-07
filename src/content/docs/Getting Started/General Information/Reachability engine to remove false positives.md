---
title: Reachability engine to remove false positives
---


Aikido combines 100+ custom rules to reduce false positives and irrelevant alerts. Most of those ground rules are powered by our own reachability analysis engine. In this article we explain how it works.

When Aikido detects a known vulnerability inside of Javascript, Python, etc, it will do a special check to make sure your application can actually reach this vulnerable code. This can result in significant noise suppression of alerts compared to legacy vulnerability scanners.

Aikido will extend this mechanism to more languages to improve noise suppression.

**Example 1:** Aikido knows you're not using the affected function. In the case below, Aikido uses it's internal database to know CVE-2020-7774 only affects the 'setLocale' function. However, it becomes clear you are **not using this function** anywhere in your own codebase. That means you're not affected. Aikido will downgrade the issue. Of course, Aikido will keep on eye out to make sure you don't start using this function in the future.

![Image](https://ucarecdn.com/2ab4f164-e024-42a0-8bf2-d050225cdf03/)

**Example 2:** JS package 'minimatch' is vulnerable, but Aikido notices the parent packages using minimatch are 'eslint' and 'mochajs'. In this case Aikido knows the child package minimatch is **part of your linting or testing stack**, and the code is not being shipped to production. This means your end-users will not be affected, so the issue can be downgraded.

**Example 3:** A package (path-parse) is known to have a defect (CVE). Aikido traces the usage of this package. It turns out it's required by a package called 'Pug'. It turns out however, that Pug is **no longer being used** in your app. That means the CVE can safely be discarded.

![Image](https://ucarecdn.com/fda1c7f6-1cba-439e-af75-38faf58cca3e/)