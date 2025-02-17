---
title: Configuration via env vars
---


## Token

Use the `AIKIDO_TOKEN` env variable to set the token you generated in Aikido:

```
AIKIDO_TOKEN="token"
```

## Blocking mode

You can use the `AIKIDO_BLOCK` env variable to enable blocking mode.

```
AIKIDO_BLOCK="true"
```

> You can also toggle between blocking mode and detection only mode in the dashboard. The environment variable will be used as starting mode. When the config is retrieved, Zen will switch to the configured mode from the dashboard.

## Disable the agent

You can use the `AIKIDO_DISABLE` env variable to disable Zen entirely. In the unlikely event that Zen causes problems, you can disable Zen without removing any code or environment variables (e.g. `AIKIDO_TOKEN` etc).

```
AIKIDO_DISABLE="true"
```

## Debugging

You can use the `AIKIDO_DEBUG` env variable to output more information:

- Whether certain packages are supported or not
- Whether a token was detected
- Whether Zen is running in detection only mode

```
AIKIDO_DEBUG="true"
```

## Proxy settings

You can use the `AIKIDO_TRUST_PROXY` env variable to [trust proxies](https://help.aikido.dev/doc/proxy-settings/docLY8sBN83Q):

> By default, trust proxy is **enabled**.

```
AIKIDO_TRUST_PROXY="false"
```

## Limit API discovery samples

Limits the number of request samples collected per route. Each sample contains:

- Request body structure and type (for non-GraphQL requests)
- Query parameters
- Authentication methods used

These samples help analyze and document your API's structure, including the expected request format and authentication requirements. 

```
AIKIDO_MAX_API_DISCOVERY_SAMPLES="10"
```

## Maximum request body size (NodeJS)

Sets the maximum size (in MB) for incoming HTTP request bodies. This limit helps protect your application from memory exhaustion due to extremely large requests.

```
AIKIDO_MAX_BODY_SIZE_MB="10" # MB
```