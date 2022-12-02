# # from django.test import TestCase

# # # Create your tests here.
# # from django.db import models
# # from .models import Score

# scores =[ {"username":"CP",
#         "lastLevel":2},
#         {"username":"mike",
#         "lastLevel":21},
#         {"username":"jerry",
#         "lastLevel":12}]
# i = 1

# for score in scores:
#     score.update(rank=i)
#     i+=1

# print(scores)

# name = input('Enter name: ')
# print(name)


supper = ["fish","chicken","fries"]

for i,item in enumerate(supper):
    print(f"{i+1}. {item}")


temp = 10
temp /= 2
print( temp)
import random

print(random.choice(supper))