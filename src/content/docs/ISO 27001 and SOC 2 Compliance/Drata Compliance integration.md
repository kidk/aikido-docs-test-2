---
title: Drata Compliance integration
---

**Table of contents:**
- [API Key](#api-key)
  - [Details](#details)
  - [Scopes](#scopes)
  - [Save](#save)
- [Done](#done)
  - [Set Up Drata Integration →](#set-up-drata-integration-)
  - [Discover Integration Details →](#discover-integration-details-)


The Drata integration automatically pushes Evidence to Drata for SOC2 and ISO27001:2022.

To activate the Drata integration, in Aikido: Go to [Settings &gt; Integrations &gt; Drata](https://app.aikido.dev/settings/integrations/compliance/drata) and click 'Add Drata integration'.  

## API Key

You'll need to create a Drata API Key. You can generate such key in Drata via [Username &gt; Settings &gt; API Keys &gt; Create API Key](https://app.drata.com/account-settings/api-keys/add). 

### Details

Make sure the Expiration is set to 'Never Expires'.

![Image](https://ucarecdn.com/434c3577-6525-4dd7-bd05-3d8542874506/)

### Scopes

The access for the scopes can be set to 'Custom' with at least following scopes.

**Controls:**

- **Controls list:** Read
- **Add control:** Write
- **Map external evidence:** Read, Write
- **Delete mapped external evidence:** Write

**Workspaces:**

- **List workspaces:** Read

**Frameworks:**

- **List frameworks:** Read
- **List framework requirements:** Read

![Image](https://ucarecdn.com/34731256-9c26-4160-a673-b0c3ab16d664/)

### Save

Next, click 'Save' and copy your generated API Key.

Back in Aikido, paste the API Key and click 'Next'. After that, choose your Drata workspace and click 'Save'.

![Image](https://ucarecdn.com/650bf49f-49d4-4848-8513-f93aaa9f8a47/)

## Done

Aikido will now daily create a PDF report and sync this as 'external evidence' to Drata. We'll create a control with code 'AIKIDO' and link the relevant SOC2 and ISO27001 requirements. You can search for this control [here](https://app.drata.com/compliance/controls/inscope?q=Aikido).

Under 'Control evidence', the Aikido PDF will be attached every month.

---

### Set Up Drata Integration →

### Discover Integration Details →

