#Random Password Generator - www.101computing.net/random-password-generator/
import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def run():
  
  uppercase_letter_1 = chr(random.randint(65, 90)) 
  uppercase_letter_2 = chr(random.randint(65, 90))  

  lowercase_letter_1 = chr(random.randint(97, 122))
  lowercase_letter_2 = chr(random.randint(97, 122)) 

  number_1 = chr(random.randint(48, 57))            
  number_2 = chr(random.randint(48, 57))            

  special_number_1 = chr(random.randint(33, 64))    
  special_number_2 = chr(random.randint(33, 64))    


  
  password = uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + lowercase_letter_2 + number_1 + number_2 + special_number_1 + special_number_2
  password = shuffle(password)

  #Ouput
  print(password)

run()