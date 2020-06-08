temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C) : ")
input_value = int(temp[:-1])
input_unit = temp[-1]
if input_unit.upper() == "C":
  result = int(round((9 * input_value) / 5 + 32))
  output_unit = "Fahrenheit"
elif input_unit.upper() == "F":
  result = int(round((input_value - 32) * 5 / 9))
  output_unit = "Celsius"
else:
  print("Input proper Unit.")
  quit()
print(temp ,"is", result, "in", output_unit)
