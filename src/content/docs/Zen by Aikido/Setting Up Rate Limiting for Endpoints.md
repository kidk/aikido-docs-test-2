---
title: Setting Up Rate Limiting for Endpoints
---


### Introduction

Zen by Aikido allows you to **set up rate limiting on route endpoints** to protect your application from abuse, such as preventing excessive password reset requests. You can rate limit, webpages, REST API endpoints as well as GraphQL APIs. 

> Check the [functionality support matrix](https://help.aikido.dev/doc/getting-started-with-zen/doccLOR8KzO0#functionality-support-matrix) to see if your framework supports rate limiting.

### Supported Functionality

- Set rate limiting on specific endpoints
- Set rate limiting on multiple endpoints by adding a wildcard\* endpoint
- Set rate limiting on IP address or [user ID](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1#how-to-identify-and-block-users)
- Disable protection for a specific endpoint instead disabling protection for your entire app.
- [Localhost](http://Localhost) or 127.0.0.1 is never rate limited

> Rate limiting is based on individual IP addresses or [user identification](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1#how-to-identify-and-block-users). \
> For example, if the limit is 10 requests per minute:
>
> - ❌ **Blocked**: A single IP making 11 requests will be 
> - ✅ **Allowed:** 11 different IPs making one request each
>
> This helps prevent abuse while allowing normal traffic from multiple users.

### How to set up rate limiting

**Step 1**: Navigate to a **specific app** and open **the Endpoints tab**

![Image](https://ucarecdn.com/9abaeced-29fa-466a-b14f-ff77318d94d8/)

**Step 2: Open Action Menu** of the specific endpoint you wish to apply rate limiting to. Clicking **Setup rate limiting** will open a modal.

![Image](https://ucarecdn.com/c5a6dbc9-bb88-4e67-9915-2ef591062e7a/)

**Step 3**: **Enable Rate Limiting** and specify the number of requests allowed per timeframe. Save by updating the endpoint.

![Image](https://ucarecdn.com/2e32beb2-b722-4251-a180-1abcc28ea8b4/)

> Config changes take up to 1 minute to take effect.

### Setting up rate limiting for multiple endpoints at once

You can set up rate limiting for multiple endpoints at once by adding a wildcard endpoint. 

**Step 1.** On the endpoints page, click **Add Endpoint.**

![Image](https://ucarecdn.com/43445b15-3762-4af8-a93e-af05f5c978cd/)

**Step 2.** Add a wildcard endpoint by adding an `*` in the route.

![Image](https://ucarecdn.com/3f33efaa-cda8-4895-b0d6-1720d72f6748/)

**Step 3.** The wildcard will appear now in the list. Proceed to set up rate limiting the same way as above.

![Image](https://ucarecdn.com/745e8921-2d2d-40a9-b778-3248b8e25557/)

## Algorithm - Sliding window

Tracks events using a moving time frame that continuously slides forward. Unlike fixed windows that reset at specific times, sliding windows maintain a rolling count of the most recent period (e.g., last 60 seconds). This prevents edge cases where brief traffic spikes could bypass limits at window boundaries.