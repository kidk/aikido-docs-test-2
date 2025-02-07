**Table of contents:**
- [Introduction](#introduction)
- [Aikido's Main Feed](#aikidos-main-feed)
- [Sidebar](#sidebar)
- [Filter Issues](#filter-issues)
- [Export Issues to CSV or PDF](#export-issues-to-csv-or-pdf)
- [Show issues per team or project](#show-issues-per-team-or-project)

# Main Feed

## Introduction {#introduction}

Aikido's Feed is meticulously designed to streamline security management: it groups similar issues for clarity, allows for customizable views to highlight what's currently important. The main feed focusses on open issues only. Snoozed and ignored issues are accessible on a separate page for a clean giving a focused and clean overview. 

## Aikido's Main Feed {#aikidos-main-feed}

The **Feed** is the central hub for monitoring and managing security issues. A similar view can be found all over Aikido when going into details of repositories, clouds and domains.

By default, Aikido enables the **Focus** view, containing all issues that are important to follow-up. By toggling to **All** we will also show issues that have been auto-triaged and ignored.

*Status Column*

Shows the status of the particular issue. 

- *New*: issues that have been around for less than 7 days
- *To Do:* all other issues that are still unresolved
- *Task Open:* only when a task manager is linked
- *PR Open:* clicking will take you to PR / branch scan overview.

![Image](https://ucarecdn.com/e134c1d8-5218-4f06-96d2-2cb099968f41/)

## Sidebar {#sidebar}

Aikido's Feed is equipped with a detailed sidebar, designed to provide users with comprehensive information and actionable options for each security issue. The image below shows the main important actions one can take.

**#1 Group Actions:** these are actions that can be taken on group level of an issue.

**#2 Subissue Actions:** you can also take actions on a subissue separately. This can be important when certain subissues want to be snoozed or ignored, but the overal issue group should remain in the main feed.

**#3 Reachability Analysis:** visualizes accessible code paths for that specific issue.

**#4 Detail Screen**: Separate detail screen with even more information (e.g., CVE information).

![Image](https://ucarecdn.com/7d0dadc8-a23e-4f23-b207-c1710b0ce1df/)

**Reachability Analysis**

![Image](https://ucarecdn.com/1aabe4cf-b6b9-44e5-b953-41f35c7ef824/)

## Filter Issues {#filter-issues}

You can easily adjust the view in order to filter on those issues that are most important to you in the moment. These filters can be found above the issue table in every feed view. You can filter on

- **Issue Type**
- **Predefined filtered views**
  - If you are using the [**SLA functionality**](https://help.aikido.dev/en/articles/8926339-enabling-slas-in-aikido), you will be able to see all upcoming and
  - SLA issues

![Image](https://ucarecdn.com/ac998c65-834e-4bad-b76b-550ca0c2db6b/)

## Export Issues to CSV or PDF {#export-issues-to-csv-or-pdf}

You can export a CSV or PDF of issues. You can configure which issues to export exactly. This can be triggered from the Actions menu in the top right.

![Image](https://ucarecdn.com/fc64121c-f6e4-4e98-87b9-e2c0cedcdf20/)

## Show issues per team or project {#show-issues-per-team-or-project}

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams ([📖 Set Up Teams](https://help.aikido.dev/en/articles/9005606-using-teams-for-repository-and-user-management)).

![Image](https://ucarecdn.com/7d1a69e7-7618-4eae-b374-ee6322f9fd43/)