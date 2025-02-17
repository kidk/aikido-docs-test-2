---
title: Setup and Installation of Zen for Dotnet
---


This guide will walk you through installing and setting up Zen by Aikido for your application. Follow the steps below to protect your application.

We have first class support for multiple frameworks and database drivers, for the full list check our [README on GitHub](https://github.com/AikidoSec/firewall-dotnet).

## 1. Install Zen by Aikido

Zen for Dotnet comes as a [NuGet packages for Core and Framework](https://www.nuget.org/profiles/AikidoSecurity) that need to be installed together with your code so your application can be protected. 

--------
#### Dotnet Core
--------

Install the package from NuGet:

```
dotnet add package Aikido.Zen.DotNetCore
```


--------
#### Dotnet Framework
--------

Install the package from NuGet:

```
dotnet add package Zen.Aikido.DotNetFramework
```

or

```
Install-Package Zen.Aikido.DotNetFramework
```


--------
#### Untitled Tab
--------



Configure your application to initiate the Zen firewall. 

--------
#### Untitled Tab
--------

In your `global.asax.cs` file, add the following:

```
protected void Application_Start()
{
    // ...
    Zen.Start();
}
```

If you're using **OWIN**, add the following to your `Startup.cs` file:

```
public void Configuration(IAppBuilder app)
{
    // ...
    Zen.Start();
}
```


--------
#### Untitled Tab
--------

If you are using a startup class, you can add the following to your `Startup.cs` file:

```
using Aikido.Zen.DotNetCore;

public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.AddZenFirewall(Configuration);
    // ...
}

public void Configure(IApplicationBuilder app)
{
    // ...
    // Place this after use routing, or after 
    // authorization, but high enough in 
    // the pipeline to catch all requests
    app.UseZenFirewall(); 
    // ...
}
```



## 2. Create an app in the dashboard and generate a token

1\. Go to the [**Zen**](https://app.aikido.dev/runtime/services) section in Aikido.

2\. Click on **Add app**.

3\. Choose a name for your app and click **Generate token**.

4\. Copy the generated token.

![Image](https://ucarecdn.com/f85939dd-63cb-4b71-bd77-8dfb9c42833b/)

## 3. Start Zen in dry / detection-only mode

Set the token as an environment variable, in `appsettings.json` or `Web.config` `appSettings` depending on your environment.

--------
#### appsettings.json
--------

```
{
  "Aikido": {
    "AikidoToken": "your-api-key"
  }
}
```


--------
#### Web.config
--------

```
<appSettings>
    ...
    <add key="Aikido:AikidoToken" value="your-api-key" />
    ...
</appSettings>
```


--------
#### Untitled Tab
--------



Start your app in dry mode `AIKIDO_BLOCK=false` to ensure it works as expected without blocking any requests:

Tip: You can use `AIKIDO_DEBUG=true` to enable debug mode (To verify that you set `AIKIDO_TOKEN` correctly)

## 4. Test your app

Browse to your application and perform a couple of actions or open a couple of pages. Zen will automatically discover the routes in your application.

## 5. Enable Rate limiting and User blocking

Enable additional features like [Rate limiting](https://help.aikido.dev/doc/setting-up-rate-limiting-for-endpoints/docFzLop0bgw) and [User blocking](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1) from within your code. Check out these examples below. Keep in mind that your specific setup might need adjustments based on your framework and configuration.

--------
#### Dotnet Core
--------

```
.UseRouting()
.Use((context, next) =>
{
    // Identify users to the Zen platform
    var id = context.User?.Identity?.Name ?? "-1";
    var name = context.User?.Identity?.Name ?? "Anonymous";
    if (!string.IsNullOrEmpty(id))
        Zen.SetUser(id, name, context);
    return next();
})
.UseZenFireWall()
```


--------
#### Dotnet Framework
--------

In your `global.asax.cs` file

```
public void Application_Start()
{
    // ...
    Zen.SetUser(context => new User(context.User.Identity.Name, context.User.Identity.Name));
    Zen.Start();
}
```

If you're using OWIN, add the following to your Startup.cs file:

```
public void Configuration(IAppBuilder app)
{
    // ...
    Zen.SetUser(context => new User(context.User.Identity.Name, context.User.Identity.Name));
    Zen.Start();
}
```


--------
#### Untitled Tab
--------



## 6. Setup rate limiting in the dashboard

If you've added the rate-limiting feature, you can test it out by logging in to your Aikido account and navigating to the Zen dashboard. Click on the created app and check the **Events** tab to verify that a “started” event was recorded:

![Image](https://ucarecdn.com/8d0d5d72-855b-4085-8b7a-d7df670eb2b6/)

To protect a route from brute force attacks, set up rate limiting in the Aikido Dashboard:

1\. Click on the created app.

2\. Go to the **Routes** tab.

3\. Find the route you would like to limit and click **Setup rate limiting**.

4\. Follow the instructions to configure the rate limit (e.g., 5 requests per minute).

![Image](https://ucarecdn.com/4f437e18-1f29-4e43-8ca5-5ca116c58fc3/)

![Image](https://ucarecdn.com/3a82744b-67f9-4429-9ea7-e26f6565ac12/)

## 7. Verify Rate Limiting

Start your app and try to access the route you've rate limited 5 times within a minute. After the fifth attempt, you should receive a rate limit error:

```
You are rate limited by Aikido firewall. (Your IP: 1.2.3.4)
```