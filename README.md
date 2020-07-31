# bloxapi

![](https://img.shields.io/github/stars/darealzz/bloxapi) ![](https://img.shields.io/github/forks/darealzz/bloxapi) ![](https://img.shields.io/github/license/darealzz/bloxapi) ![](https://img.shields.io/github/issues/darealzz/bloxapi)

A modern & simple to use API wrapper that handles ROBLOX interactions

### Key Features

- Covers a large majority of the ROBLOX API.
- Modern Pythonic API using `async` and `await`.
- Easy and super simple to use.

### Installing

**Python 3.6.0 or higher is required**
```py
# Upgrade pip
# If 'python' does not work try 'py'
$ python -m pip install --upgrade pip

# Install the Module
$ pip install git+https://github.com/darealzz/bloxapi.git
```

### Basic Example

```py
import bloxapi
import asyncio

client = bloxapi.Client(None)

async def main():
    user_object = await client.get_user_by_id(1) # This returns the user object.
    if user_object: # Checking if this user exists.
        print('This user exists!')
        print(user_object.name, user_object.id, user_object.status, user_object.about) 

asyncio.run(main())
```

More examples can be found in the examples directory.

### Links

 - [Documentation (Comming Soon)](http://www.google.com "google")
 - [ROBLOX API](https://api.roblox.com/docs)
