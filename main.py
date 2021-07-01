import async_easy_json
import asyncio

e=async_easy_json.async_json("data.json")

async def main():
  data=await e.read()
  print(data["test"])
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())