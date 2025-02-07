**Table of contents:**
  - [Introduction](#introduction)
  - [How to ignore an issue group or subissue](#how-to-ignore-an-issue-group-or-subissue)
  - [Check out all (auto-) ignored issues](#check-out-all-auto--ignored-issues)

# Ignore Issues to Remove Issues from Main Feed

### Introduction {#introduction}

While Aikido boasts advanced detection capabilities with auto-ignore (see the [ignore criteria](https://app.aikido.dev/issues/ignored/criteria)), the occasional false positive may slip through, or an issue may be irrelevant to your specific context. The ignore functionality is designed to address this, ensuring your security overview remains accurate. 

### How to ignore an issue group or subissue {#how-to-ignore-an-issue-group-or-subissue}

**Step 1:** Navigate to the **issue group**, or **subissue** in Aikido you wish to ignore and select the "Ignore" option in the actions menu (triple dots).

![Image](https://ucarecdn.com/ff7d2590-2d08-42c5-b7a1-464dac520f01/)

**Step 2:** For subissues, you will be asked about how Aikido should treat this subissue and potential similar detections in the future.

![Image](https://ucarecdn.com/b8de9c2c-c625-4a45-9c92-09c72c786b24/)

You have a few options available to ignore the current and future issues. The options available depend on the context in which you are ignoring an issue (single issue or issue group), but also on the issue type (e.g., Surface Monitoring and Cloud Issues show different options).

Below are all the ignore options listed that you might see

- **Only this issue/only this issue group**\
  This option will only ignore this subissue, or this issue group and all its sub issues, depending on the context.\
  ​\
  If you decide to ignore an issue group, please be aware that if we find a new issue for group, this issue will not be auto-ignored and will re-open the group, but not all previously ignored sub issues.\
  ​
- **Ignore by path**\
  When choosing this option, you create an issue rule which will ignore all current and future file based issues (open source, SAST, IAC and exposed secrets) under a certain path. You can edit the path there for convenience to make the rule as specific as you'd like. \
  ​\
  This can be helpful when there are testing frameworks in a specific path that you do not want Aikido to scan.

  ![Image](https://ucarecdn.com/fe887c2a-204b-412b-9854-dbe96beff936/)

  \
  ​
- **Ignore all findings related to CVE**\
  This option creates an issue rule which ignores all current and future open source dependencies linked to that CVE. This ignore rule is global and is applied to all repositories.\
  ​
- **Ignore all findings related to rule**\
  Most issues in Aikido are related to a specific rule code such as SAST, IAC and Cloud issues. When selecting this option, you create an issue rule which ignores all current and future issues related to that specific rule. This ignore rule is global and is applied to all repositories.

**Step 3:** Confirm your choice to ignore the issue, effectively removing it from your main feed in Aikido.

### Check out all (auto-) ignored issues {#check-out-all-auto--ignored-issues}

The [ignore view](https://app.aikido.dev/issues/ignored) consolidates all issues ignored by Aikido's triaging algorithm, as well as those manually ignored by users. Here, you can review the rationale behind each automatically ignored issue (see the [ignore criteria](https://app.aikido.dev/issues/ignored/criteria)). Your manually ignored issues will also be displayed here, providing a comprehensive overview of all exclusions made within Aikido.

![Image](https://ucarecdn.com/65ba19ef-aa73-4a9f-aa79-50f391560e04/)