---
title: Troubleshoot Jira Task Creation_ Set up Default Issue Types
---


Task creation inside Aikido can fail, **particularly when the issue types that have been setup in Jira include required fields that Aikido are not available in Aikido**. The fix is to create a new issue type in Jira without any required fields, and inform Aikido about this new name.

### 1. Create a new Issue Type in JIRA

**Step 1:** Log in to JIRA and go to Settings &gt; Issues &gt; **Issue Types**

**Step 2: Add a New Issue Type**

Click *Add Issue Type*. Name it something indicative like **Security Fix**, and ensure it does not mandate any field that previously hindered Aikido task creation. This issue type must not include any required fields that Aikido cannot sync.

### 2. Configuring Aikido to Use the New Issue Type

**Step 1:** Go to [**JIRA Integration Settings**](https://app.aikido.dev/settings/integrations/tasktracker) in Aikido

**Step 2: Input the New Issue Type Name** in the default task type entry.

Enter the name of the issue type you created in JIRA (e.g., Security Fix). This links Aikido's ticket creation process with the new JIRA issue type.

![Image](https://ucarecdn.com/4d62afc3-3daa-409f-8c86-127036359b66/)

---