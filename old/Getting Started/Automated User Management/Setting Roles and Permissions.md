# Setting Roles and Permissions

## Roles and Permissions Logic {#roles-and-permissions-logic}

Aikido offers three distinct user roles (**admins**, **default** and **team-only** users) to manage access and permissions effectively. Default and team-only users can have **standard editing rights** or can be **read-only**.

<table class="table-light dark:table-dark" style="width: 750px">
<colgroup><col style="width: 407px"><col style="width: 343px"></colgroup><tbody><tr><th colspan="1" rowspan="1" colwidth="407" style="width: 407px;"><p>Role</p></th><th colspan="1" rowspan="1" colwidth="343" style="width: 343px;"><p>Access Level</p></th></tr><tr><td colspan="1" rowspan="1" colwidth="407" style="width: 407px;"><p><strong>Admins</strong></p></td><td colspan="1" rowspan="1" colwidth="343" style="width: 343px;"><p>Full access</p></td></tr><tr><td colspan="1" rowspan="1" colwidth="407" style="width: 407px;"><p><strong>Default Users</strong></p><p></p></td><td colspan="1" rowspan="1" colwidth="343" style="width: 343px;"><p>Global / All Teams</p><p><span data-text-color="text-editor-gray-light dark:text-editor-gray-dark" class="text-editor-gray-light dark:text-editor-gray-dark">Standard rights or read-only</span></p></td></tr><tr><td colspan="1" rowspan="1" colwidth="407" style="width: 407px;"><p><strong>Team-Only Users</strong></p></td><td colspan="1" rowspan="1" colwidth="343" style="width: 343px;"><p>Team-specific</p><p><span data-text-color="text-editor-gray-light dark:text-editor-gray-dark" class="text-editor-gray-light dark:text-editor-gray-dark">Standard rights or read-only</span></p></td></tr></tbody>
</table>

### Default Users vs Team-Only Users {#default-users-vs-team-only-users}

The main difference between the two is that team-only users only have access to those issues for the teams they belong to. They still are able to mostly manage issues.

<table class="table-light dark:table-dark" style="width: 714px">
<colgroup><col style="width: 216px"><col style="width: 180px"><col style="width: 318px"></colgroup><tbody><tr><th colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p>Permission</p></th><th colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>Default Users</p></th><th colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>Team-Only Users</p></th></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Issue Actions</strong></p><p><span data-text-color="text-editor-gray-light dark:text-editor-gray-dark" class="text-editor-gray-light dark:text-editor-gray-dark">Snooze, ignore, severity change, autofix</span></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>✅</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>✅</p></td></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Create Tasks</strong></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>✅</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>✅</p></td></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Add Repos</strong></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>✅</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>❌</p></td></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Add Registries</strong></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>✅</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>❌</p></td></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Add Domains</strong></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>✅</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>Connected to repos only. No standalone.</p></td></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Export Issues</strong></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>✅</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>❌</p></td></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Acces to Settings</strong></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>All settings</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>General Settings <strong>Only</strong></p></td></tr><tr><td colspan="1" rowspan="1" colwidth="216" style="width: 216px;"><p><strong>Acces to Reports</strong></p></td><td colspan="1" rowspan="1" colwidth="180" style="width: 180px;"><p>All Reports</p></td><td colspan="1" rowspan="1" colwidth="318" style="width: 318px;"><p>Trends Over Time <strong>Only</strong></p></td></tr></tbody>
</table>

### Advanced Rights for Users with Standard Rights {#advanced-rights-for-users-with-standard-rights}

Aikido has an extra layer of permissions that can be enabled or disabled (both for default and team-only users). This is helpful in case you still want users to be able to execute certain actions. **Read-only rights block all possible actions.**

- **Snooze/Ignore Issues**: Ability to temporarily or permanently dismiss issues.
- **Change Issue Severity**: Ability to modify the severity level of issues.
- **Manage Teams**: Ability to manage team settings and membership.

## How to change roles and permissions {#how-to-change-roles-and-permissions}

**Step 1.** Go to the user overview in your settings

**Step 2.** Click the triple dots to open up the role and permissions modal for a specific user

![Image](https://ucarecdn.com/3666ec2a-c91c-473f-9352-6c191c51c09b/)

**Step 3.** Set the preferred user role and permissions

![Image](https://ucarecdn.com/cca312e7-d2a2-4d4a-b1fe-c08e130e4d84/)