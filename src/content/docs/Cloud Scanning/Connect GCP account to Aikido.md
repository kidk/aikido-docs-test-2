---
title: Connect GCP account to Aikido
---


Securing your cloud infrastructure is crucial to protecting your data. You can leverage Aikido's security checks to detect and address any misconfigurations in your infrastructure.

To view the list of security checks performed by Aikido on your cloud environment, go to the 'checks' tab on the [cloud overview page](https://app.aikido.dev/clouds) at. Filter to GCP to see specific checks performed on your connected GCP project(s).

To get started, head to the [cloud overview page](https://app.aikido.dev/clouds) on Aikido and click 'Connect cloud.' Follow the step-by-step setup wizard to connect your GCP project with Aikido.

![Image](https://ucarecdn.com/b9f682f2-011c-4c18-bfd2-2fd2a8e5d6b0/)

First, you'll need to provide the project ID to help identify the correct project. Then, you'll be prompted to enable API access to specific GCP services. This is a critical step that enables Aikido to inspect the security of your cloud resources through API requests.

After enabling API access, the setup wizard will guide you through creating a service account with limited, read-only access to specific services in your GCP project. This account will be associated with the necessary roles and permissions, all of which are read-only. This ensures that Aikido can perform its security checks without the risk of unintended modifications to your resources.

If you do not want to assign the suggested roles during the setup. You can ensure the service account includes the following permissions to perform the scans:

```
bigtable.instances.list,
cloudasset.assets.listResource,
cloudfunctions.functions.list,
cloudkms.cryptoKeys.list,
cloudkms.keyRings.list,
cloudkms.cryptoKeys.getIamPolicy,
cloudsql.instances.list,
cloudsql.users.list,
compute.autoscalers.list,
compute.backendServices.list,
compute.disks.list,
compute.firewalls.list,
compute.healthChecks.list,
compute.instanceGroupManagers.list,
compute.instanceGroups.list,
compute.instances.getIamPolicy,
compute.instances.list,
compute.images.list,
compute.networks.list,
compute.projects.get,
compute.resourcePolicies.list,
compute.securityPolicies.list,
compute.snapshots.list,
compute.subnetworks.list,
compute.targetHttpProxies.list,
compute.urlMaps.list,
container.clusters.list,
dns.managedZones.list,
iam.serviceAccountKeys.list,
iam.serviceAccounts.list,
logging.logMetrics.list,
logging.sinks.list,
monitoring.alertPolicies.list,
spanner.instances.list,
storage.buckets.getIamPolicy,
storage.buckets.list,
deploymentmanager.deployments.list,
dataproc.clusters.list,
artifactregistry.repositories.list,
composer.environments.list
```

Once the service account is created, you'll need to generate an access key and upload it to Aikido. This key will be used by Aikido to make the necessary API requests to scan your resources.

Finally, you can name your connected project in Aikido and specify the environment it operates in. This information helps Aikido prioritize findings based on the severity and impact to your business.

![Image](https://ucarecdn.com/355246ac-82c7-438a-a675-3dbd9eb7d1a5/)

Within 1-2 minutes after connecting your account, Aikido will report misconfigurations that could pose a threat.

---

### Set Up GCP Cloud Integration →

### Discover Integration Details →

---