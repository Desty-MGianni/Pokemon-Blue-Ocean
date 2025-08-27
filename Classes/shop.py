import csv
import logging
import beaupy
from time import sleep
from Classes.clearscreen import clearscreen
from Classes.trainer import Player

class Shop:
    
    def load_price_table(name: str) -> dict:
        path = f"Shop_prices/{name.lower()}.csv"
        with open(path,newline='') as price_table_csv:
            price_table_temp = dict(csv.reader(price_table_csv,delimiter=';'))
        return {item: int(price) for item,price in price_table_temp.items()}

    sell_price: dict[str: int] = load_price_table(name= "selling_prices")
        
    def __str__(self) -> str:
        dict_in_str: str = ''
        for item , price in self.price_table.items():
            dict_in_str += f"\t{item:<13}\t{price} Poké $\n"
        return dict_in_str

    def __init__(self, rank_shop: str, city_name:str) -> None:
        self.city_name: str = city_name
        self.rank: str = Shop.verify_rank(rank= rank_shop)
        if self.rank != None:
            self.price_table: dict[str: int] = Shop.load_price_table(self.rank)
        
    # Called in constructor to make sure there is no problem with the .csv files
    def verify_rank(rank: str) -> str | None:
        match rank:
            case "Beginner" | "Intermediate" | "Advanced" | "Max":
                return rank.capitalize()
            case _:
                logging.error("Error loading the corresponding price table: incorrect name parsed to verify_rank method!")
                return None
        
    # loop that we caled in cites.
    def shop(self, player: Player) -> None:
        while True:
            clearscreen()
            print(f"Welcome to {self.city_name}'s shop!")
            options = ["Buy", "Sell", "Exit"]
            choice = beaupy.select(
                options,
                return_index= True,
                cursor= "--->"
            )
            match choice:
                case 0:
                    self.__purchase_item(player= player)
                case 1:
                    self.__sell_item(player= player)
                case 2:
                    break

    def __purchase_item(self, player:Player):
        while True:
            # Need this conversion as beaupy doesn't handle dict data type
            list_items: list[str] = list(self.price_table.keys()) + ["Exit"]

            sleep(0.5)
            clearscreen()
            print('To buy')
            choice: str = beaupy.select(
                options= list_items,
                preprocessor= lambda x: f"{self.price_table[x]}: {x}",
                return_index= False,
                cursor= "--->",
            )
            if choice == "Exit":
                break
            print(f"Money: {player.inventory.money}")
            print(f"You have selected {choice}")
            try:
                quantity: int = beaupy.prompt("Enter how much you want to buy: ",target_type= int)
            except beaupy.ConversionError:
                quantity = 0
            if quantity == 0:
                continue
            total_price: int = self.price_table[choice] * quantity
            if total_price <= player.inventory.money:
                if beaupy.confirm(question= f"Confirm {quantity} {choice} for {total_price} Poké-Dollars ?", cursor= "--->"):
                    player.inventory.money -= total_price
                    player.inventory.update_inventory(item= choice, quantity= quantity)
                    print("Thank you for your purchase!")
                    sleep(0.75)
            else:
                print("You don't have enough money!")
                sleep(1)


    def __sell_item(self, player: Player) -> None:
        def __look_quantity_invetory(item: str) -> int:
            if item in player.inventory.balls_available.keys():
                return player.inventory.balls_available[item]
            elif item in player.inventory.potions_available.keys():
                return player.inventory.potions_available[item]
            elif item in player.inventory.revives_available.keys():
                return player.inventory.revives_available[item]
            elif item in player.inventory.stones_available.keys():
                return player.inventory.stones_available[item]

        while True:
            sleep(1)
            clearscreen()
            player.inventory.update_items_available()
            all_items_available: list[str] = list(player.inventory.balls_available.keys()) + \
                list(player.inventory.potions_available.keys()) + \
                list(player.inventory.revives_available.keys()) + \
                list(player.inventory.stones_available.keys())

            choice = beaupy.select(
                options= all_items_available,
                preprocessor= lambda x: f"{self.sell_price[x]}: {x} x {__look_quantity_invetory(item = x)}",
                return_index= False,
                cursor= "--->"
            )
            try:
                quantity_to_sell: int = beaupy.prompt(
                    prompt= f"How many {choice} do you want to sell ? ", target_type= int)
            except beaupy.ConversionError:
                quantity_to_sell = 0
            if quantity_to_sell == 0:
                continue
            elif quantity_to_sell <= __look_quantity_invetory(item= choice):
                total_earn: int = quantity_to_sell * self.sell_price[choice]
                if beaupy.confirm(question= f"Confirm ? (You will earn {total_earn}$ with this transaction.)", cursor= "--->"):
                    player.inventory.manage_money(total_earn)
                    player.inventory.update_inventory(item= choice, quantity= - quantity_to_sell)
            else:
                print("You don't have enough items (decrease the amount to sell.)")
                sleep(1)