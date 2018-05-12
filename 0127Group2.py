#temp2
ini_temp=eval(input("Please enter a temperature:"))
Convert_to=input("Would you like that converted to C or F?")
if Convert_to=="C":
    new_temp=((ini_temp-32)*(5/9))
    print("The converted temp is", new_temp, convert_to)
else:
    new_temp=((ini_temp*(9/5))+32)
    print("The converted temp is",new_temp,convert_to)
    
