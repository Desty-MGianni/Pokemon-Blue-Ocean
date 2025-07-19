import csv
from time import sleep
from Classes.clearscreen import clearscreen
from Classes.trainer import Player

class Shop:
    
    def load_price_table(name: str):
        path = f"Shop_prices/{name.lower()}.csv"
        with open(path,newline='') as price_table_csv:
            price_table_temp = dict(csv.reader(price_table_csv,delimiter=';'))
            price_table = {item: int(price) for item,price in price_table_temp.items() }
        return price_table

        
    def __repr__(self):
        dict_in_str: str = ''
        for item , price in self.price_table.items():
            dict_in_str += f"\t{item:<13}\t{price} Poké $\n"
        return dict_in_str

    def __init__(self, rank_shop: str,city_name:str):
        self.city_name = city_name
        self.rank = Shop.verify_rank(rank= rank_shop)
        if self.rank != None:
            self.price_table = Shop.load_price_table(self.rank)
        
    sell_price = load_price_table(name= "selling_prices")
    
    def verify_rank(rank: str):
        match rank:
            case "Beginner" | "Intermediate" | "Advanced" | "Max":
                return rank.capitalize()
            case _:
                print("Error when determining the rank of the shop!")
                return None
        
    
    def shop(self, player: Player):
        while True:
            clearscreen()
            print(f"Welcome to {self.city_name}'s shop!")
            player_action_input = input("Do you want to buy or sell items? (Type buy or sell or exit) ")
            match player_action_input:
                case 'buy' | 'b' | 'Buy':
                    self.__purchase_item(player= player)
                case 'sell' | 's' | 'Sell':
                    self.__sell_item(player= player)
                case 'exit' | 'e' | 'Exit':
                    break
                case _:
                    print(f"Error in {self.city_name}'s shop method")

    def __purchase_item(self, player:Player):
        while True:
            sleep(1)
            clearscreen()
            print('To buy')
            print(self)
            print(f"\tYour money: {player.inventory.money}")
            player_choice_item = input("What do you want to purchase ? (Type the name of the item. To exit the shop, Type exit) ").title()
            if player_choice_item in self.price_table:
                if self.price_table[player_choice_item] < player.inventory.money:
                    print(f"\t{player_choice_item} : {self.price_table[player_choice_item]} Poké $")
                    print(f"\tYou have {player.inventory.money} Poké $")
                    try:
                        quantity = int(input("How many do you want to purchase? "))
                    except ValueError:
                        quantity = 0
                    total_price = quantity * self.price_table[player_choice_item]
                    if quantity > 0 and total_price <= player.inventory.money:
                        print(f"{quantity} {player_choice_item} for {total_price} Poké $")
                        confirmation_input = input(f"Confirm ? y/N ")
                        match confirmation_input:
                            case 'y' | 'yes':
                                sleep(1)
                                print(f"You bought {quantity} {player_choice_item}")
                                player.inventory.money -= total_price
                                player.inventory.update_inventory(item= player_choice_item, quantity= quantity)
                                print("Thank you for your purchase!")
                                sleep(1)
                            case _:
                                pass
                    elif quantity == 0:
                        pass
                    else:
                        print("you have not enough money! Decrease the amount of item.")
                else:
                    print("You don't have enough money!")

            elif player_choice_item =="Exit":
                sleep(1)
                break
            else:
                print("The item you entered doesn't exist in this shop!")

    def __sell_item(self,player: Player):
        def selling_transaction(dict_to_lookup: dict):
            if player.inventory.verify_name_in_dict(item= item_to_sell, dict_looked= dict_to_lookup):
                if dict_to_lookup[item_to_sell] > 0:
                    print(f"\t{item_to_sell}: {Shop.sell_price[item_to_sell]} Poké $")
                    try:
                        quantity_to_sell = int(input("How many do you want to sell? "))
                    except ValueError:
                        quantity_to_sell = 0
                    if quantity_to_sell <= dict_to_lookup[item_to_sell] and quantity_to_sell > 0:
                        total_amount_money = quantity_to_sell * Shop.sell_price[item_to_sell]
                        final_choice = input(f"\t{quantity_to_sell} {item_to_sell} will be {total_amount_money}. Continue? (Y/n)").lower()
                        sleep(0.5)
                        match final_choice:
                            case 'n' | 'no':
                                pass
                            case _:
                                player.inventory.update_inventory(item= item_to_sell, quantity= -quantity_to_sell)
                                player.inventory.manage_money(total_amount_money)
                                print(f"You earned {total_amount_money} Poké $")
                                sleep(1)
                    else:
                        pass
                else:
                    print(f"You don't have any {item_to_sell}")
            else:
                print("This type of ball doesn't exist in your inventory!")

        while True:
            sleep(1)
            clearscreen()
            print(player.inventory)
            item_to_sell = input("Enter item you want to sell: (To leave: type exit.)" ).title()
            if item_to_sell.__contains__('Ball'):
                selling_transaction(dict_to_lookup= player.inventory.balls)
            elif item_to_sell.__contains__('Potion'):
                selling_transaction(dict_to_lookup= player.inventory.potions)
            elif item_to_sell.__contains__('Rappel'):
                selling_transaction(dict_to_lookup= player.inventory.revives)
            elif item_to_sell.__contains__('Pierre'):
                selling_transaction(dict_to_lookup= player.inventory.stones)
            elif item_to_sell == 'Exit':
                sleep(1)
                break
            else:
                pass
