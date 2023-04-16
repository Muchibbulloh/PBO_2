import asyncio

async def count_up(stop):
  i = 0
  while i < stop:
   yield i
   i += 1
  raise StopAsyncIteration

async def main():
 async for i in count_up(5):
  print(i)

try:
# Menjalankan coroutine main()
 asyncio.run(main())
 
except StopAsyncIteration as e:
 print("Iterasi berhenti:", e)