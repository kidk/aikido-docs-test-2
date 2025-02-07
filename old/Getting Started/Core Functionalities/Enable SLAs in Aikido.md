**Table of contents:**
  - [Introduction](#introduction)
  - [How to enable SLAs in Aikido](#how-to-enable-slas-in-aikido)
  - [SLA Information in Aikido UI](#sla-information-in-aikido-ui)

# Enable SLAs in Aikido

### Introduction {#introduction}

You can enable SLA settings in Aikido to automatically assign due dates to tickets. This facilitates a structured and timely approach to issue resolution based on their reported time and severity. 

### How to enable SLAs in Aikido {#how-to-enable-slas-in-aikido}

1. Navigate to the Settings -&gt; [SLA settings](https://app.aikido.dev/settings/sla)
2. Ensure the 'Enable SLAs' option is turned on to implement SLA rules.\
   ​

   ![Image](https://ucarecdn.com/1ff28d9b-3344-4de1-bcfd-f50e669ab680/)
3. Input the **number of days** for resolution in the fields for Critical, High, Medium, and Low priority issues to establish SLA time frames.\
   ​

   ![Image](https://ucarecdn.com/c1e31d14-d808-4f55-a853-117c72d67aba/)

   \
   ​
4. Set up the '**Due Soon' notification threshold** by specifying the number of days before the SLA deadline, which will highlight impending due dates on the [SLA Due Soon](https://app.aikido.dev/queue?filter=due_soon) view.\
   ​

   ![Image](https://ucarecdn.com/e8abe17c-281e-4a5f-9947-3caf00ca1536/)
5. Click **'Save'** to apply these configurations.

### SLA Information in Aikido UI {#sla-information-in-aikido-ui}

After setting up your SLA parameters, here's how you can monitor your SLA due dates.

- **Sidebar Information**: Next to each subissue in the sidebar, you will see the SLA information, providing a quick reference to gauge urgency. Hover over the label in order to view the date.\
  ​

  ![Image](https://ucarecdn.com/9b8a2056-6d6a-4314-a7cc-3efff950ad43/)
- **SLA Due Soon Filter**: The [**SLA Due Soon**](https://app.aikido.dev/queue?filter=due_soon) view view displays issues that are close to breaching the SLA, based on the threshold set. **Enable this filtered view** by clicking the Filter Icon on your Feed and select SLA Due Soon.\
  ​

  ![Image](https://ucarecdn.com/b8bdc36a-51a0-4742-9ec8-ce0d1dc6cc90/)
- **Out of SLA View**: The [**Out of SLA**](https://app.aikido.dev/queue?filter=out_of_sla) view lists all issues and subissues that have exceeded their SLA limits. **Enable this filtered view** by clicking the Filter Icon on your Feed and select Out of SLA.\
  ​

  ![Image](https://ucarecdn.com/ba292c16-3b12-456a-b0a4-5e118b7638c8/)

---