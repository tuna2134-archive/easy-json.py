import async_easy_json
import asyncio

e=async_easy_json.async_json("data.json")

async def main():
  data=e.read()
  data["t"]="a"
  await e.write(data)
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())