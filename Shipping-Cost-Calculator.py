#Shipping Cost Calculator

##Input Package weight and shipping rate
weight = float(input("Enter the package weight in kilograms:"))
rate = float(input("Enter the shipping rate per kilogram:"))

##Calculate shipping cost
shipping-cost = weight * rate

##Display the result
print(f"Shipping Cost: {shipping-cost} USD")