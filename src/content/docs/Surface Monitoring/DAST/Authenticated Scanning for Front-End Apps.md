---
title: Authenticated Scanning for Front-End Apps
---


This guide will walk you through the steps to set up authenticated domain scanning in Aikido, ensuring thorough and secure assessments. 

> This feature is only available on **Pro** and **Scale** Plans.\
> Option is only available for Front-End application types.

### Use Cases

- Ensure comprehensive security assessments for protected areas of your website.
- Identify vulnerabilities in authenticated sections of your domain.

### Setting up authentication on a domain

**Step 1:** Go to the [Domains Overview](https://app.aikido.dev/settings/domains) and open the action menu for a domain of your choice by clicking the triple dots. Select **Authenticate Domain.**

![Image](https://ucarecdn.com/73e3a4bd-4171-4010-a569-83aadd2f0994/)

**Step 2:** Fill in the URL and email/password for the domain authentication. Click **Test** to let Aikido check whether it can access the domain with those credentials.

![Image](https://ucarecdn.com/cef8d27b-529c-4fab-829d-a2df670c99ba/)

**Step 3.** Once the test has been succeeded, you can **Confirm Authentication.** Aikido will do a thorough scan and all results will appear in Aikido.

### Supported Cases

- Email or username and password login forms
- Multi step login forms with email or username and password (forms where the password field is not visible until an email address is provided)
- **2FA** is currently **not** supported.

> Is your case not supported? Let us know via chat and we will look into it!

### Identifiers

Our scanner looks for a few things on the pages to recognize the email/username input field and login buttons. You can find a list of identifiers here.\
\
Username/Email input field:\
We look for input fields with one of these **ids**:

```javascript
"email", "username", "Username", "login-email", "EmailOrUsername", "UserNameOrEmail", "username_login", "txtUsername", "user_email", "email-input'
```

If no input field is found, we look for any input field with one of these **names**:

```javascript
"email", "username", "userid", "userName", "uid", "uname"
```