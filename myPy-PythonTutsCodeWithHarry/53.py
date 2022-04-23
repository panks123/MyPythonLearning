# else and finally in try except




try:
    '''Code that may cause an exception is written inside try block'''
    f1=open("Hamad_ex.txt")
    

except IOError as e:
    print("IOError error:",e)

except EOFError as e:
    print("EOF error:",e)

else:
    print("This will execute if except block will not run")
    

finally:
    f1.close()
    print("Cleanup statements")     # inside finally block we write those statements which we
                                    # want to execute anyhow whether exception occurs or not


print("Normal flow of program does not stop if exception occurs, this line is executed")
