#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) 
    for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    
    if password_length <= 0:
        print("Please enter a valid password length.")
    else:
        generated_password = generate_password(password_length)
        print("Generated Password:", generated_password)


# In[ ]:





# In[ ]:




