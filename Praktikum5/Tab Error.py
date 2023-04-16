try:
# Contoh kode program yang menyebabkan TabError
 for i in range(5):
  print(i)

except TabError as e:
  print("Terjadi kesalahan:", e)