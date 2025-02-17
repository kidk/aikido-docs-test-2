---
title: Setup and Installation of Zen for Node.js (Javascript & Typescript)
---


This guide will walk you through installing and setting up Zen by Aikido for your application. Follow the steps below to protect your application.

We have first class support for Javascript and Typescript, including multiple frameworks and database drivers, for the full list check our [README on GitHub.](https://github.com/AikidoSec/firewall-node/blob/main/README.md#supported-libraries-and-frameworks)

## 1. Install Zen by Aikido

First, you need to install the Zen package. Open your terminal and run:

```
# The --save-exact makes sure that you don't automatically install a newer version
$ npm install --save-exact @aikidosec/firewall

# The --exact makes sure that you don't automatically install a newer version
$ yarn add --exact @aikidosec/firewall
```

## 2. Include Zen in app.js

Next, you need to include Zen in your app.js file. This should be done before any other code or imports:

```
require('@aikidosec/firewall'); // <-- Include this before any other code or imports

const express = require('express');

const app = express();

// Your other middleware and routes

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
```

Alternatively, if you are using ESM import style:

```
import '@aikidosec/firewall';

import express from 'express';

const app = express();

// Your other middleware and routes

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
```

> When using esbuild as your bundler, [follow these additional configuration steps](https://github.com/AikidoSec/firewall-node/blob/main/docs/esbuild.md#installing-zen-in-a-nodejs-application-bundled-with-esbuild).

## 3. Create an app in the dashboard and generate a token

1. Go to the [**Zen** section](https://app.aikido.dev/runtime/services) in Aikido.
2. Click on **Add app**.
3. Choose a name for your app and click **Generate token**.
4. Copy the generated token.

![Image](https://ucarecdn.com/06017eb3-bf16-42b0-bb0a-7c80f004935e/)

## 4. Start Zen in dry / detection-only mode

Set the token as an environment variable, `AIKIDO_TOKEN`, using [dotenv](https://github.com/motdotla/dotenv) or another method of your choosing. Start your app in dry mode to ensure it works as expected without blocking any requests:

```
$ AIKIDO_BLOCK=false node app.js
```

Tip: You can use `AIKIDO_DEBUG=true` to enable debug mode (To verify that you set `AIKIDO_TOKEN` correctly)

## 5. Test your app

Browse to GET /auth/login and perform a login as you normally would (e.g., POST /auth/login). Zen will automatically discover the routes in your application:

```
app.get('/auth/login', (req, res) => {
  res.send('Login Page');
});

app.post('/auth/login', (req, res) => {
  // Handle login logic
  res.send('Logged In');
});
```

## 6. Setup rate limiting in the dashboard

Log in to your Aikido account and navigate to the Zen dashboard. Click on the created app and check the **Events** tab to verify that a “started” event was recorded:

![Image](https://ucarecdn.com/2bb3bce0-6314-4de9-b212-f14fc7e440a0/)

To protect your POST /auth/login route from brute force attacks, set up rate limiting in the Aikido Dashboard:

1. Click on the created app.
2. Go to the **Routes** tab.
3. Find the POST /auth/login route and click **Setup rate limiting**.
4. Follow the instructions to configure the rate limit (e.g., 5 requests per minute).

![Image](https://ucarecdn.com/1e6b9251-9b14-477c-8775-45cc18a741b2/)

![Image](https://ucarecdn.com/eafa9223-3340-41ff-ba99-83d27ecd20ed/)

## 7. Verify Rate Limiting

Start your app and try to log in 5 times within a minute. After the fifth attempt, you should receive a rate limit error:

```
You are rate limited by Aikido firewall. (Your IP: 1.2.3.4)
```

> Requests from localhost will not be rate limited when NODE_ENV is "production". When you are developing your app locally, you'll be able to verify the rate limiting.