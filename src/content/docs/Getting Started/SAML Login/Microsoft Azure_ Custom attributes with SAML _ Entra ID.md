---
title: Microsoft Azure_ Custom attributes with SAML _ Entra ID
---


First, make sure you have SAML login working using following guide:

[https://help.aikido.dev/doc/microsoft-azure-login-with-saml--entra-id/doc74BfKR60Z](https://help.aikido.dev/doc/microsoft-azure-login-with-saml--entra-id/doc74BfKR60Z)


### Setting up Azure Group based SAML custom attributes

1. Fetch the Azure group id. 

   ![Image](https://ucarecdn.com/3ac909ca-d62b-4575-b6d0-94f46731f20c/)
2. In your 'Single sign-on' section of your app, edit 'Attributes & Claims'.\
   (To get there, follow [this guide](https://help.aikido.dev/doc/microsoft-azure-login-with-saml--entra-id/doc74BfKR60Z#continue-in-azure) until step 8)

   ![Image](https://ucarecdn.com/e0a00d40-b3a7-4829-91c5-65aca18ca858/)
3. Create a group claim.\
   This example is to set the user role of all members in the group as `admin`. Regex pattern is the group ID we copied in step 1.\
   Other supported claims can be found [here](https://help.aikido.dev/doc/saml-user-rights-using-custom-attributes/doc6Jm7BYzwg).

   ![Image](https://ucarecdn.com/6bf9ab78-74e7-4b3d-bc75-735305afbc9c/)
4. In Aikido, log out & log in to see the effects. (Microsoft Azure has a small delay after save)