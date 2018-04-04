from .agent import Agent
from .properties import get_valid_input
from .properties_payment import *
# #  Properties
# bld = properties.Apartment.prompt_init()
# print(bld)
#
# apt = properties.Apartment(**bld)
# apt.display()
#
#
# bld_2 = properties.House.prompt_init()
# print(bld_2)
# hse = properties.bld_2
# hse.display()


# # Payment
# pay_type = payment.Rental.prompt_init()
# print(pay_type)
#
# prop_type = properties.House.prompt_init()
# print(prop_type)



# Properties Payment
a1 = HouseRental.prompt_init()
print(a1)

house = HouseRental(**a1)
house.display()


# # Agent
# agent = Agent()
# agent.add_property()
#
# response = get_valid_input("Would you like to add another property?: ",
#                            ("yes", "no"))
# while response == "yes":
#     agent.add_property()
#     response = get_valid_input("Would you like to add another property?: ",
#                                ("yes", "no"))
#
#
# agent.display_properties()
