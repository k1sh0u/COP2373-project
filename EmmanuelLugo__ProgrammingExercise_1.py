"""
Write an application to pre-sell a limited number of cinema tickets. Each buyer can buy up to 4 tickets.
No more than 20 tickets can be sold total.
Prompt the user for the desired number of tickets and then display the number of remaining tickets after their purchase.
Repeat until all tickets have been sold. Then display the total number of buyers.

Please use the following in your code:

two functions - your choice how you want to design this
input
output
accumulator
if statement
loop
You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.
"""






"""
What I want my code to check:

Are we sold out?

how many tickets does the customer want

are they exceeding the 4 ticket max per customer rule?

If the customer is requesting 4 or less, do we even have enough?. 

is 
    
_____
"""

ticket_supply = 20

def ticket_sign(ticket_supply):

    if ticket_supply >= 1:
        print(f"Welcome! We have {ticket_supply} tickets left.")
        buy_a_ticket(ticket_supply)
    else:
        print("we are sold out.")








def buy_a_ticket(ticket_supply):
    while True:

        try:
            tickets_to_buy = int(input("How many tickets would you like?: "))
        except ValueError:
            print("Input must be a number.")
            continue
        if tickets_to_buy > 4:
            print("4 tickets Max per customer.")
        elif tickets_to_buy < 1:
            print("You cannot buy less than 1 ticket.")
        elif tickets_to_buy > ticket_supply:
            print(f"there are only {ticket_supply} tickets left.")
        else:
            print(f"You have purchased {tickets_to_buy} tickets.")
            ticket_supply -= tickets_to_buy
            ticket_sign(ticket_supply)
            break




ticket_sign(ticket_supply)




