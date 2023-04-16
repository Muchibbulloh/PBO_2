class CountUp:
 
 def __init__(self, stop):
  self.i = 0
  self.stop = stop

 def __iter__(self):
  return self
 
 def __next__(self):
  if self.i >= self.stop:
   raise StopIteration
  else:
   self.i += 1
  return self.i - 1
try:
# Membuat objek iterator dari kelas CountUp dengan argumen 5
  counter = iter(CountUp(5))

# Mencetak nilai dari setiap item pada iterator
  while True:
   print(next(counter))

except StopIteration as e:
 print("Iterasi berhenti")