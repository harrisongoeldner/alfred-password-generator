#import
import random
import string
import sys

query = sys.argv[1]

def generate(query):
    characters = string.ascii_letters + string.digits + string.punctuation
    query = ''.join(random.choice(characters) for i in range(length))
    return query

query = generate(20)
sys.stdout.write(query)
