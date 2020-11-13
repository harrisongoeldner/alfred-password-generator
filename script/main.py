#import modules
import random
import string
import sys

# import user input
try:
    query = sys.argv[1]
except:
    query = 15

# function to generate password
def generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(int(length)))
    return password

# save fucntion output to query
query = generate(query)

# output from python
sys.stdout.write(query)
