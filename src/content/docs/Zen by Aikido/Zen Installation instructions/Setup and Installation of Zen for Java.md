---
title: Setup and Installation of Zen for Java
---


This guide will walk you through installing and setting up Zen by Aikido for your application. Follow the steps below to protect your application.

We have first class support for multiple frameworks and database drivers, for the full list check our [README on GitHub](https://github.com/AikidoSec/firewall-java). The Java agent supports Linux, Windows and Mac OS.

## 1. Install Zen by Aikido

Zen for Java comes as a JAR package that needs to be installed together with your code so your application can be protected. 

Download the [zip file](https://github.com/AikidoSec/firewall-java/releases/latest) and unzip it to a directory (e.g. `/opt/zen`). 

Please ensure you do not alter the structure of this folder and that the process can read & write to it. 

To activate the zen agent you then just have to add the following argument to your Java start command.

```
-javaagent:/opt/zen/agent.jar
```

## 2. Create an app in the dashboard and generate a token

1\. Go to the [**Zen** section](https://app.aikido.dev/runtime/services) in Aikido.

2\. Click on **Add app**.

3\. Choose a name for your app and click **Generate token**.

4\. Copy the generated token.

![Image](https://ucarecdn.com/5c5f1014-4ca4-4013-b642-6bead70dc25e/)

## 3. Start Zen in dry / detection-only mode

Set the token as an environment variable, `AIKIDO_TOKEN`. Start your app in dry mode `AIKIDO_BLOCK=false` to ensure it works as expected without blocking any requests:

Tip: You can use `AIKIDO_DEBUG=true` to enable debug mode (To verify that you set `AIKIDO_TOKEN` correctly)

## 4. Test your app

Browse to your application and perform a couple of actions or open a couple of pages. Zen will automatically discover the routes in your application.

## 5. Enable Rate limiting and User blocking

Enable additional features like [Rate limiting](https://help.aikido.dev/doc/setting-up-rate-limiting-for-endpoints/docFzLop0bgw) and [User blocking](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1) from within your code with Gradle.

```
dependencies {
    # ...
    implementation files('/opt/zen/agent_api.jar')
    # ...
}
```

Additional instructions are needed and depend on the framework used.

- [Spring](https://github.com/AikidoSec/firewall-java/blob/main/docs/spring.md)
- [Webflux](https://github.com/AikidoSec/firewall-java/blob/main/docs/spring_webflux.md)
- [Javalin](https://github.com/AikidoSec/firewall-java/blob/main/docs/javalin.md)

## 6. Setup rate limiting in the dashboard

If you've added the rate-limiting feature, you can test it out by logging in to your Aikido account and navigating to the Zen dashboard. Click on the created app and check the **Events** tab to verify that a “started” event was recorded:

![Image](https://ucarecdn.com/74a95eb3-5fbf-45a0-826a-e46ae996c953/)

To protect a route from brute force attacks, set up rate limiting in the Aikido Dashboard:

1\. Click on the created app.

2\. Go to the **Routes** tab.

3\. Find the route you would like to limit and click **Setup rate limiting**.

4\. Follow the instructions to configure the rate limit (e.g., 5 requests per minute).

![Image](https://ucarecdn.com/466176d4-6bc1-48e1-b820-5cf64777ca56/)

![Image](https://ucarecdn.com/f0ecf04a-31ae-4057-b23d-8c8b18d2f353/)

## 7. Verify Rate Limiting

Start your app and try to access the route you've rate limited 5 times within a minute. After the fifth attempt, you should receive a rate limit error:

```
You are rate limited by Aikido firewall. (Your IP: 1.2.3.4)
```