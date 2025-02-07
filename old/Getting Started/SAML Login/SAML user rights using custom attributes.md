# SAML user rights using custom attributes

This guide provides detailed instructions on how to configure and manage user rights within Aikido using SAML custom attributes. By leveraging attributes such as `aikido_role`, `aikido_data_edit_rights`, `aikido_can_ignore`, `aikido_can_change_severity`, `aikido_can_manage_teams`, and `aikido_teams`, you can control user permissions and roles from within your identity provider. This approach ensures that users have the same access in Aikido as set up in your identity provider.

- **aikido_role:** `admin`, `default`, `team_only`

  ```xml
  <saml:Attribute Name="aikido_role">
      <saml:AttributeValue xsi:type="xs:anyType">default</saml:AttributeValue>
  </saml:Attribute>
  ```
- **aikido_data_edit_rights:** `standard`, `read_only`

  ```xml
  <saml:Attribute Name="aikido_data_edit_rights">
      <saml:AttributeValue xsi:type="xs:anyType">standard</saml:AttributeValue>
  </saml:Attribute>
  ```
- **aikido_can_ignore:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_ignore">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```
- **aikido_can_change_severity:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_change_severity">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```
- **aikido_can_manage_teams:** `true`, `false`

  ```xml
  <saml:Attribute Name="aikido_can_manage_teams">
      <saml:AttributeValue xsi:type="xs:anyType">true</saml:AttributeValue>
  </saml:Attribute>
  ```
- **aikido_teams:** You can define the different teams where the user is a part of here. If the team(s) do not exist in Aikido, it will be created. The user will auto-join these given teams. The user will be removed from all other teams if this is set up.

  ```xml
  <saml:Attribute Name="aikido_teams">
      <saml:AttributeValue xsi:type="xs:anyType">team1</saml:AttributeValue>
      <saml:AttributeValue xsi:type="xs:anyType">team2</saml:AttributeValue>
  </saml:Attribute>
  ```


- **aikido_workspace_ids:** You can define the different Aikido workspaces where the user is a part of here. The user will auto-join these given workspaces. The user will be removed from all other workspaces if this field is set up.

  ```xml
  <saml:Attribute Name="aikido_workspace_ids">
      <saml:AttributeValue xsi:type="xs:anyType">1233</saml:AttributeValue>
      <saml:AttributeValue xsi:type="xs:anyType">2511</saml:AttributeValue>
  </saml:Attribute>
  ```