try:
   number_1=int(input("enter the numerator:"))
   number_2=int(input("enter the denominator:"))
   result=number_1/number_2

except ValueError:
   print("invalid value!!")

except ZeroDivisionError:
   print("cannot divide by zero!!")

else:
   print("result:",result)

finally:
   print("Task complited!!")