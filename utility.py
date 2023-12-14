import time
vending = {
    'C1': {'name': 'Chippy', 'price': '5', 'amount': '5'},
    'C2': {'name': 'Nova', 'price': '7', 'amount': '2'},
    'C3': {'name': 'Piatos', 'price': '2', 'amount': '3'},
    'D1': {'name': 'Cherifer', 'price': '6', 'amount': '1'},
    'D2': {'name': 'Royal', 'price': '5', 'amount': '4'},
    'D3': {'name': 'Milo', 'price': '3', 'amount': '7'}
}

print(f"""██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝   """) # Title
print("┏━✦❘༻༺❘✦━━┓")
while True:
    start = input("𝙏𝙮𝙥𝙚 '𝙔' 𝙩𝙤 𝙨𝙩𝙖𝙧𝙩: ").upper() # Start of the Vending Machine Simulation
    if start == "Y":
        time.sleep(0.5)
        print("⋘ 𝑙𝑜𝑎𝑑𝑖𝑛𝑔 𝑑𝑎𝑡𝑎... ⋙") # A loading screen to convey that the Vending Machine takes time to boot up
        time.sleep(1)
        print("▒▒▒▒▒▒▒▒▒▒")
        time.sleep(1.1)
        print("█▒▒▒▒▒▒▒▒▒")
        time.sleep(1.2)
        print("███▒▒▒▒▒▒▒")
        time.sleep(1.3)
        print("█████▒▒▒▒▒")
        time.sleep(1.4)
        print("███████▒▒▒")
        time.sleep(1.5)
        print("██████████")
        time.sleep(0.5)
        print("ᴄᴏᴍᴘʟᴇᴛᴇ!")
        time.sleep(0.5)
        print(f"""──────────────────────────────────────────┐ 
█▀ █▄░█ ▄▀█ █▀▀ █▄▀ █▀
▄█ █░▀█ █▀█ █▄▄ █░█ ▄█

C1: {vending['C1']['name']} - ${vending['C1']['price']} // Stock: {vending['C1']['amount']}
C2: {vending['C2']['name']} - ${vending['C2']['price']} // Stock: {vending['C2']['amount']}
C3: {vending['C3']['name']} - ${vending['C3']['price']} // Stock: {vending['C3']['amount']}


█▀▄ █▀█ █ █▄░█ █▄▀ █▀
█▄▀ █▀▄ █ █░▀█ █░█ ▄█   

D1: {vending['D1']['name']} - {vending['D1']['price']} // Stock: {vending['D1']['amount']}
D2: {vending['D2']['name']} - {vending['D2']['price']} // Stock: {vending['D2']['amount']}
D3: {vending['D3']['name']} - {vending['D3']['price']} // Stock: {vending['D3']['amount']}     
──────────────────────────────────────────┘""") # Vending Machine
        break
def vending_machine(): # Function is used to make an endless loop
    def vending_process(): # Name is self-explanatory
        while True:
            selection = input("Select an item: ").upper() # Input to select the item

            if int(vending[selection]['amount']) > 0:
                pass

                if selection in vending:
                    selected = input(f"Selected {vending[selection]['name']}. Do you want to buy the item for ${vending[selection]['price']}? ").upper() # Confimration of selection

                    if selected == "YES":
                        amount = input(f"How many {vending[selection]['name']} do you want to buy? Stock: {vending[selection]['amount']}. ") # Amount of selection

                        if int(amount) <= int(vending[selection]['amount']):
                            price = (int(vending[selection]['price']) * int(amount)) # Calculation of initial price times the inputted amount to make a full price
                            price_total = input(f"Ok that will be ${price}. Please insert cash: ") # Input the cash needed to buy the item

                            if int(price_total) >= int(vending[selection]['price']):
                                amount_taken = (int(vending[selection]['amount']) - int(amount)) # Subtracts the given amount to the max amount

                                if amount_taken >= 0:
                                    price_change = (int(price_total) - price)
                                    print(f"Change: ${price_change}")
                                    print(f"Left in stock: {amount_taken}")
                                    vending[selection]['amount'] = str(amount_taken) # Updates the dictionary after successful purchase
                                    break
                            else:
                                print(f"That is not enough to cover ${price}")

                        else: # If amount inputted is bigger than the max stock, else will print 
                            print(f"We only have {vending[selection]['amount']} left in stock.")
                else:
                    print("That's not a valid option.")

            else:
                print("That is out of stock!")
    vending_process() 
    time.sleep(1)
    print(f"""──────────────────────────────────────────┐ 
    █▀ █▄░█ ▄▀█ █▀▀ █▄▀ █▀
    ▄█ █░▀█ █▀█ █▄▄ █░█ ▄█
    
    C1: {vending['C1']['name']} - {vending['C1']['price']} // Stock: {vending['C1']['amount']}
    C2: {vending['C2']['name']} - {vending['C2']['price']} // Stock: {vending['C2']['amount']}
    C3: {vending['C3']['name']} - {vending['C3']['price']} // Stock: {vending['C3']['amount']}
    
    
    █▀▄ █▀█ █ █▄░█ █▄▀ █▀
    █▄▀ █▀▄ █ █░▀█ █░█ ▄█   
    
    D1: {vending['D1']['name']} - {vending['D1']['price']} // Stock: {vending['D1']['amount']}
    D2: {vending['D2']['name']} - {vending['D2']['price']} // Stock: {vending['D2']['amount']}
    D3: {vending['D3']['name']} - {vending['D3']['price']} // Stock: {vending['D3']['amount']}     
──────────────────────────────────────────┘""")
    vending_process()

vending_machine()