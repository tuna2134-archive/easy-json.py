import json
import asyncio

class async_json:
  def __init__(self,name):
    self.name=name
    
  def read(self):
    with open(self.name, mode="r") as f:
      data = json.load(f)
    return data
    
  async def write(self,data):
    with open(self.name, mode="w") as f:
      json.dump(data, f, indent=4)