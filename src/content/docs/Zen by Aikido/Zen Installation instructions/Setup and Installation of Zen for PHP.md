---
title: Setup and Installation of Zen for PHP
---


This guide will walk you through installing and setting up Zen by Aikido for your application. Follow the steps below to protect your application.

We have first class support for multiple frameworks and database drivers, for the full list please check our [README on GitHub](https://github.com/AikidoSec/firewall-php?tab=readme-ov-file#supported-libraries-and-frameworks).

## 1. Install Zen by Aikido

Zen for PHP comes as a single package that needs to be installed on the system to be protected. Prerequisites:

- Ensure you have sudo privileges on your system.
- Check that you have a supported PHP version installed (PHP version &gt;= 7.3 and test up to 8.3).
- Make sure to use the appropriate commands for your system or cloud provider.

**Manual install**

#### For Red Hat-based Systems (RHEL, CentOS, Fedora)

```
rpm -Uvh --oldpackage https://github.com/AikidoSec/firewall-php/releases/download/v1.0.102/aikido-php-firewall.x86_64.rpm
```

#### For Debian-based Systems (Debian, Ubuntu)

```
curl -L -O https://github.com/AikidoSec/firewall-php/releases/download/v1.0.102/aikido-php-firewall.x86_64.deb
dpkg -i -E ./aikido-php-firewall.x86_64.deb
```

For [other platforms check out our Github readme](https://github.com/AikidoSec/firewall-php?tab=readme-ov-file#install).

## 2. Create an app in the dashboard and generate a token

1\. Go to the [**Zen** section](https://app.aikido.dev/runtime/services) in Aikido.

2\. Click on **Add app**.

3\. Choose a name for your app and click **Generate token**.

4\. Copy the generated token.

![Image](https://ucarecdn.com/f6e917c2-2ce0-462b-b726-ecf754579c4f/)

## 3. Start Zen in dry / detection-only mode

Set the token as an environment variable, `AIKIDO_TOKEN`. Start your app in dry mode `AIKIDO_BLOCK=false` to ensure it works as expected without blocking any requests:

Tip: You can use `AIKIDO_DEBUG=true` to enable debug mode (To verify that you set `AIKIDO_TOKEN` correctly)

## 4. Test your app

Browse to your application and perform a couple of actions or open a couple of pages. Zen will automatically discover the routes in your application.

> Don't forget to restart PHP-FPM or your webserver to reload PHP with Zen

## 5. Enable Rate limiting and User blocking

Enable additional features like [Rate limiting](https://help.aikido.dev/doc/setting-up-rate-limiting-for-endpoints/docFzLop0bgw) and [User blocking](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1) from within your code by using the snippet below or the [more specific framework examples on Github](https://github.com/AikidoSec/firewall-php/blob/main/docs/should_block_request.md). 

```
// Check if Aikido extension is loaded
if (extension_loaded('aikido')) {
    
    // Get the user from your authentication middleware
    // or wherever you store the user
    \aikido\set_user("123", "John Doe");

    // Check blocking decision from Aikido
    // and decide on what to do
    $decision = \aikido\should_block_request();
    if ($decision->block) {
        if ($decision->type == "blocked") {
            if ($decision->trigger == "user") {
                return response('Your user is blocked!', 403);
            }
            else if ($decision->trigger == "ip") {
                return response("Your IP ({$decision->ip}) is blocked due to: {$decision->description}!", 403);
            }
        } else if ($decision->type == "ratelimited") {
            if ($decision->trigger == "user") {
                return response('Your user exceeded the rate limit for this endpoint!', 429);
            }
            else if ($decision->trigger == "ip") {
                return response("Your IP ({$decision->ip}) exceeded the rate limit for this endpoint!", 429);
            }
        }
    }
}
```

## 6. Setup rate limiting in the dashboard

If you've added the rate-limiting feature, you can test it out by logging in to your Aikido account and navigating to the Zen dashboard. Click on the created app and check the **Events** tab to verify that a “started” event was recorded:

![Image](https://ucarecdn.com/0c965b70-2d46-4dfe-be76-6116db049253/)

To protect a route from brute force attacks, set up rate limiting in the Aikido Dashboard:

1\. Click on the created app.

2\. Go to the **Routes** tab.

3\. Find the route you would like to limit and click **Setup rate limiting**.

4\. Follow the instructions to configure the rate limit (e.g., 5 requests per minute).

![Image](https://ucarecdn.com/42a385f3-327d-4390-a4c6-47bfc174185c/)

![Image](https://ucarecdn.com/69751c22-0703-4254-82b3-40ec315d0072/)

## 7. Verify Rate Limiting

Start your app and try to access the route you've rate limited 5 times within a minute. After the fifth attempt, you should receive a rate limit error:

```
You are rate limited by Aikido firewall. (Your IP: 1.2.3.4)
```