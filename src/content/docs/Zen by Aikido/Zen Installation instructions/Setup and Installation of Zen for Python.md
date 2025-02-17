---
title: Setup and Installation of Zen for Python
---


This guide will walk you through installing and setting up Zen by Aikido for your application. Follow the steps below to protect your application.

We have first class support for multiple frameworks and database drivers, for the full list check our [README on GitHub](https://github.com/AikidoSec/firewall-python/tree/main?tab=readme-ov-file#supported-libraries-and-frameworks).

## 1. Install Zen by Aikido

Zen for Python comes as a PIP package that needs to be installed together with your code so your application can be protected. 

```
pip install aikido_zen
```

Choose your framework or runtime and follow the specific instructions. 

--------
#### Gunicorn
--------

Use the following template for your `gunicorn_config.py` file:

```
import aikido_zen.decorators.gunicorn as aik

@aik.post_fork
def post_fork(server, worker):
    # If you already have a config file, replace pass with your own code.
    pass
```

Modify your gunicorn starting command to add this configuration file:

```
gunicorn -c gunicorn_config.py --workers ...
```

For more advanced options [check out our Github docs](https://github.com/AikidoSec/firewall-python/tree/main/docs).


--------
#### Quart
--------

In `app.py` add the following snippet to your application

```
import aikido_zen
aikido_zen.protect()
```

> When installing additional middleware, make sure to install it like this and not like `app.asgi_app = my_middleware` as it would remove all other middleware. 
>
> ```
> from quart import Quart
> app = Quart(__name__)
> ...
> app.asgi_app = my_middleware(app.asgi_app)
> ```

For more advanced options [check out our Github docs](https://github.com/AikidoSec/firewall-python/tree/main/docs).


--------
#### Django
--------

In `manage.py` add the following snippet to your application

```
import os
import sys
import aikido_zen

if __name__ == "__main__":
    aikido_zen.protect()
    # ...
```

For more advanced options [check out our Github docs](https://github.com/AikidoSec/firewall-python/tree/main/docs).


--------
#### Flask, Starlette, FastAPI, uWSGI
--------

In `app.py` add the following snippet to your application

```
import aikido_zen
aikido_zen.protect()
```

For more advanced options [check out our Github docs](https://github.com/AikidoSec/firewall-python/tree/main/docs).


--------
#### Untitled Tab
--------



## 2. Create an app in the dashboard and generate a token

1\. Go to the [**Zen** section](https://app.aikido.dev/runtime/services) in Aikido.

2\. Click on **Add app**.

3\. Choose a name for your app and click **Generate token**.

4\. Copy the generated token.

![Image](https://ucarecdn.com/cd5ee773-000e-47fc-943e-98db2b7519ff/)

## 3. Start Zen in dry / detection-only mode

Set the token as an environment variable, `AIKIDO_TOKEN`. Start your app in dry mode `AIKIDO_BLOCK=false` to ensure it works as expected without blocking any requests:

Tip: You can use `AIKIDO_DEBUG=true` to enable debug mode (To verify that you set `AIKIDO_TOKEN` correctly)

## 4. Test your app

Browse to your application and perform a couple of actions or open a couple of pages. Zen will automatically discover the routes in your application.

## 5. Enable Rate limiting and User blocking

Enable additional features like [Rate limiting](https://help.aikido.dev/doc/setting-up-rate-limiting-for-endpoints/docFzLop0bgw) and [User blocking](https://help.aikido.dev/doc/block-users-with-zen/docbO6Nm6Zb1) from within your code by using the relevant framework snippets below.

--------
#### Untitled Tab
--------

In your main file add the following snippet to your application to enable request blocking

```
from starlette.middleware import Middleware
from aikido_zen.middleware import AikidoStarletteMiddleware

app = Starlette(routes=[
    ...
], middleware=[
    ...
    # Authorization middleware here (Make sure aikido middleware runs after this)
    Middleware(AikidoStarletteMiddleware),
    ...
])
```

To more easily identify your users in the Zen UI, use the following helper function within your authentication middleware after you've authenticated your user. 

```
from aikido_zen import set_user

# Set a user (presumably in middleware) :
set_user({"id": "123", "name": "John Doe"})
```


--------
#### Starlette / FastAPI
--------

In your main file add the following snippet to your application to enable request blocking

```
from starlette.middleware import Middleware
from aikido_zen.middleware import AikidoStarletteMiddleware

app = Starlette(routes=[
    ...
], middleware=[
    ...
    # Authorization middleware here (Make sure aikido middleware runs after this)
    Middleware(AikidoStarletteMiddleware),
    ...
])
```

To more easily identify your users in the Zen UI, use the following helper function within your authentication middleware after you've authenticated your user. 

```
from aikido_zen import set_user

# Set a user (presumably in middleware) :
set_user({"id": "123", "name": "John Doe"})
```


--------
#### Django
--------

In `settings.py` add the following snippet to your application to enable request blocking

```
MIDDLEWARE = [
    # Authorization middleware here (Make sure aikido middleware runs after this)
    "aikido_zen.middleware.AikidoDjangoMiddleware",
    # ...
]
```

To more easily identify your users in the Zen UI, use the following helper function within your authentication middleware after you've authenticated your user. 

```
from aikido_zen import set_user

# Set a user (presumably in middleware) :
set_user({"id": "123", "name": "John Doe"})
```


--------
#### Flask
--------

In your main file add the following snippet to your application to enable request blocking

```
from aikido_zen.middleware import AikidoFlaskMiddleware

app = Flask(__name__)
# ...
app.wsgi_app = AikidoFlaskMiddleware(app.wsgi_app)
# Authorization middleware here (Make sure aikido middleware runs after this) 
# Flask runs from bottom to top
# ...
```

To more easily identify your users in the Zen UI, use the following helper function within your authentication middleware after you've authenticated your user. 

```
from aikido_zen import set_user

# Set a user (presumably in middleware) :
set_user({"id": "123", "name": "John Doe"})
```


--------
#### Untitled Tab
--------



## 6. Setup rate limiting in the dashboard

If you've added the rate-limiting feature, you can test it out by logging in to your Aikido account and navigating to the Zen dashboard. Click on the created app and check the **Events** tab to verify that a “started” event was recorded:

![Image](https://ucarecdn.com/8ee62b56-f6df-4143-8d67-52decb746802/)

To protect a route from brute force attacks, set up rate limiting in the Aikido Dashboard:

1\. Click on the created app.

2\. Go to the **Routes** tab.

3\. Find the route you would like to limit and click **Setup rate limiting**.

4\. Follow the instructions to configure the rate limit (e.g., 5 requests per minute).

![Image](https://ucarecdn.com/9fddbbb2-4ce9-49ff-9152-178f356cf77d/)

![Image](https://ucarecdn.com/34b1af76-facb-4b6d-9c87-155236236b8f/)

## 7. Verify Rate Limiting

Start your app and try to access the route you've rate limited 5 times within a minute. After the fifth attempt, you should receive a rate limit error:

```
You are rate limited by Aikido firewall. (Your IP: 1.2.3.4)
```