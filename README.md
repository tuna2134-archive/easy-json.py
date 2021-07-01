#easy_json

this can easy for json

How to use

##usually version

###read

```py
import easy_json

e=easy_json.mjson("data.json")

data=e.read()

print(data["test"])
#test
```

###write

```py
import easy_json

e=easy_json.mjson("data.json")

data=e.read()
data["test"]="test"
e.write(data)

```

##async version

###write

```py
import async_easy_json
import asyncio

e=easy_json.async_json("data.json")
data=e.read()

async def main():
  data["test"]="test"
  await e.write(data)
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```