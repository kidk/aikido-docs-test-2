# Azure DevOps Integration for Authentication and User Management

If your organization uses Azure DevOps, users can login with Google and Microsoft accounts. Users can auto-onboard in your workspace if Trusted Domains have been set up.

### Understanding Aikido's Azure DevOps Integration {#understanding-aikidos-azure-devops-integration}

- **Manual Onboarding:** invite users manually via email 
- **Auto-onboard via Trusted Domains**: Users can automatically join the Azure DevOps workspace if their login email is part of a trusted domain that you can specify on workspace level. Aikido will verify this user has access to your Azure Devops organization. **Note:** the user needs to be a member on the organisation level in Azure, otherwise they will not be recognised during team sync.
- **Synchronization of Teams and Repositories:** Aikido replicates your Azure DevOps team and project structure. All users will have access to their repos, in line with the permissions set in Azure DevOps. By default, all users will have the **Team Only** role.

### Onboarding of Users with Trusted Domains {#onboarding-of-users-with-trusted-domains}

> If you have multiple workspaces, you need to setup Trusted Domains in each workspace. 

1. Go to [General Settings](https://app.aikido.dev/settings/account) in your workspace
2. In workspace info, click 'Add Trusted Domain'

   ![Image](https://ucarecdn.com/57ed94d1-4c3f-434b-8db6-b92ef76238e1/)
3. Fill in the trusted domain in the modal

   ![Image](https://ucarecdn.com/36b654cd-1d63-4245-b543-c1a62828fc6c/)

> For security reasons, Aikido only allows you to add trusted domains that are the same as the current logged in user. This means that [user@aikido.dev](mailto:user@aikido.dev) can only add [aikido.dev](http://aikido.dev) as trusted domain.

### Manually Inviting Users {#manually-inviting-users}

**Manually invite via email**: You can invite users via the Aikido platform on the specified email, and the user will be able to access Aikido directly. 