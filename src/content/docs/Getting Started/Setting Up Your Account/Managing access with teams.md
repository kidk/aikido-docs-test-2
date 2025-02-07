---
title: Managing access with teams
---


## Introduction

Aikido allows the creation of teams within its platform, enabling users to connect multiple repositories and clouds for comprehensive access and management.

## Use Cases

- **Filter Repositories Quickly:** In companies with multiple teams, each team may have access to the entire codebase, but their primary responsibilities are often limited to specific repositories or projects. By creating teams in Aikido, team members **can have a focused overview** of only the repositories relevant to their tasks.\
  ​

  ![Image](https://ucarecdn.com/e47c7d0e-a0e8-40db-9c28-dd5ab925c8c5/)
- **Agency Project Management:** Agencies frequently handle multiple clients, necessitating a structured approach to manage each client's repositories separately. Aikido facilitates this by allowing the creation of teams for each client, making it straightforward to organize and access client-specific repositories. Additionally, this allows for easy generation of client-specific reports.

  ![Image](https://ucarecdn.com/c6d997d8-7fad-4997-9461-3a011cb6f443/)
- **Specify resources connect to an app:** you can use the team functionality to combine resources that are part of the same app (combination of repos, containers and clouds).
- **Selective Access Control:** Assign repository access exclusively to designated team members.
- **Better overview when using a monorepo split.** You can assign team members to specific directories of your monorepo, improving their overview. More information on splitting monorepositories can be found [here](https://help.aikido.dev/en/articles/9026666-splitting-up-your-monorepo-per-directory).

## How To Create Teams

**Step 1:** Navigate to **Settings -&gt; Teams**\
​

![Image](https://ucarecdn.com/eb9c5cc9-fe18-4fda-8040-d68dc275f186/)

**Step 2:** Click **Create Team** and give your team a name\
​

![Image](https://ucarecdn.com/2713e19f-5433-435b-b10b-9f1aa409950e/)

\
**Step 3:** **Add team members** to the newly created team.

![Image](https://ucarecdn.com/59d4a227-bdc5-4880-a1de-4fcb3da51294/)

**Step 4:** Define the **team's responsibilities** by adding **resources via the responsibility tab.** You can add different resources such as clouds, repositories and containers. 

> Note that resource linking is only available for manually created teams (not imported from SCM)

> If you want to link specific domains to a team, you can set this up by linking your domains to a repo or container. It will automatically inherit access permissions.

![Image](https://ucarecdn.com/718b39c3-2119-4d42-8bf1-823fa3913434/)

**Step 5.** Go back to your feed and filter on a specific team. You should only see issues that are related to those repositories and clouds that were attached to the team.

## Syncing with GitHub, Bitbucket or Azure DevOps

If you have existing teams set up in GitHub,Bitbucket or Azure DevOps, Aikido can import them and maintain synchronization on a nightly basis. This ensures that any changes in team structures or access rights managed in GitHub/Bitbucket are accurately reflected in Aikido. Any new teams that are created in GitHub will appear in Aikido. The same applies to when you remove a team in GitHub: Aikido will pick this up and remove the team too. Any repos that are part of the team, will be synced too.

It's important to note that in this scenario, GitHub/Bitbucket acts as the source of truth for access rights, and all management should be conducted within those platforms.

Aikido makes in clear which teams have been Imported from GitHub.

![Image](https://ucarecdn.com/0ab4ee09-6b7d-48ee-a435-b20c98ff18d6/)

## Syncing with Backstage.io

Aikido integrates seamlessly with repositories containing `catalog-info.yaml` files for [Backstage.io](https://backstage.io). This allows for the automatic importing of teams, taking into account the path of where the file is located.

#### How It Works

1. Aikido scans repositories for `catalog-info.yaml` files.

2. Aikido looks for the `spec->owner` field in the file and imports this as team.

3. Aikido records the exact path of each `catalog-info.yaml` file, ensuring the team is responsible for those specific paths (and repositories).

## How to select your team in UI

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams. This filter can be used on basically every page in Aikido (feed, reports, settings etc).

![Image](https://ucarecdn.com/1c6dccbd-d42b-46d0-afb8-741ac1a85163/)