'''Accept string from the user and display only those characters which are present at an even index'''
def string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
print(string('abcdef'))
