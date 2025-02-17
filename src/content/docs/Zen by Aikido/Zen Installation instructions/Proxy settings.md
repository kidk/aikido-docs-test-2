---
title: Proxy settings
---


We'll automatically use the `x-forwarded-for` header to determine the client's IP address when behind a proxy.

If you're publicly exposing your server without a load balancer in front of it, you should set the `AIKIDO_TRUST_PROXY` env var to `false` to ensure that the correct IP address is used. Otherwise, someone could potentially spoof their IP address by adding the above header and thus bypassing the rate limiting

## Additional configuration for ASP.NET Core

[ASP.NET](http://ASP.NET) core will not automatically pick up `x-forwarded-for` without additional configuration. For more details check out the [Microsoft docs](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-9.0&preserve-view=true).