zander_length = float(input("Enter the length of the zander in centimeters: "))

minimum_length = 42

if zander_length >= minimum_length:
  print("Congratulations! You can keep the zander.")
else:
  difference_from_minimum = minimum_length - zander_length
  print(f"The zander is too small. Release it back into the lake. It's {difference_from_minimum:.2f} centimeters below the minimum length.")
