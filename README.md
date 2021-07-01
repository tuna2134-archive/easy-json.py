#easy_json

this can easy for json

How to use

usually version

```py
import easy_json

e=easy_json.mjson("data.json")

data=e.read()

print(data["test"])
#test
```

async version

```py
import async_easy_json
import asyncio

e=easy_json.async_json("data.json")

async def main():
  data=await e.read()
  print(data["test"])
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```