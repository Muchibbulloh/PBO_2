def count_down(n):
   print(n)
   count_down(n-1)

try:
# Memanggil fungsi count_down dengan argumen 5

 count_down(5)
except RecursionError as e:
   print("Terjadi ketika kedalaman rekursi maksimum terlampaui maximum recursion depth exceeded whilecalling a Python object")