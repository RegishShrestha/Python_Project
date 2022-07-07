from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

ans = "yes"
bidder_list = []
bidder = {}
greatest = 0
while ans != 'no':
    bidder_name = input("Enter the name: ")
    bidder["name"] = bidder_name
    bidder_price = int(input("Enter your price: "))
    bidder["price"] = bidder_price
    bidder_list.append(bidder)
    ans = input("Is there anyother bidders: ").lower()
    clear()
    if greatest < bidder_price:
        greatest = bidder_price
        name = bidder_name
    if ans == 'no':
        print(f'The higest bid is {greatest} from {name}')
