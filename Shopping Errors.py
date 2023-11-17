# CSCI 1301
# Programming Assignment #7
# Program: Create a class that mimics a self checking out line at a store.
         # The main goal of this assignment is to practice code debugging.

# I certify that the code in this Python file, except those provided by the instructor, is entirely my own work.

# Shopping Class definition
class Shopping:
    #Constructor Definition
    def __init__(self, tax_rate):
        self.Item_Cost = {}
        self.subtotal = 0
        self.tax_rate = tax_rate

    #calculate_Total instance method definition.
    def calculate_Total(self):
        return self.getSubtotal() * (1 + self.tax_rate)

    #addItem instance method definition. Add an item to the Item_Cost dictionary
    def addItem(self,item):    
        if item.lower in self.Item_Cost: 
            choice = input('This is a duplicate item. Do you want to add it (Y or N)?: ')
        if choice.lower() == 'y':   
            self.subtotal = self.subtotal + cost
        else:
            self.Item_Cost[item.lower()] = cost
            self.subtotal = self.subtotal + cost

    #Print the receipt. Contains all the items with their corresponding prices and total cost
    def printReceipt(self):
        for key,value in self.Item_Cost.items():
            print(f'{key:10}\t{value:4}') 
        print(f'Total:    ${(self * (1 + self.tax_rate)):.2f}')
    
    #scan_Items instance method reads in the name of the item and cost from the user
    def scan_Items(self):
        item = int(input()).lower()  
        if item.lower() != 'stop':   
            if item == 'stop':
                continue               
            else:
                cost = float(input('Enter cost: '))
                self.addItem(item,cost) 
            print('Scan next item: ', end=' ')
            item = input().lower()

    #Operator overload method to do a multiplication
    def __mult__(self, other):
        if isinstance(other, int): 
            return other * other    
        if isinstance(other, Shopping):
            return self.getSubtotal() * other.getSubtotal()
        
    #Rich comparison method to do greater than operation
    def __gt__(self,other): 
        if isinstance(other, Shopping):
            if self.calculate_Total() < other.calculate_Total():   
                return True
            else:
                return False

# Main starts here
if __name__=='__main__':

    walmart_tax_rate = float(input('Enter walmart tax rate: '))
    walmart_budget = float(input('Enter walmart shopping budget: '))
    walmart = Shopping(walmart_tax_rate) #walmart instance

    print('Scan walmart item: ', end=' ')
    walmart.scan_Items(walmart) #scan the items from walmart
    
    #display walmart receipt
    print('Walmart receipt:')
    walmart.printReceipt()
    print()
    kroger_tax_rate = float(input('Enter kroger tax rate: '))
    kroger_budget = float(input('Enter kroger shopping budget: '))
    kroger = Shopping() #kroger instance 

    print('Scan kroger item: ', end=' ')
    kroger.scan_Items()   #scan the items from kroger 
        
    #display kroger receipt
    print('Kroger receipt:')
    kroger.printReceipt()
    print()
    # Doing a rich comparison to determine if the shopper went over budget at walmart.
    if walmart < walmart_budget:    
        print(f'You went over the walmart budget by ${(walmart.calculate_Total() - walmart.subtotal):.2f}')  
    else:
        print(f'Awesome! You stuck to the walmart budget!')                                                
    
    # Doing a rich comparison to determine if the shopper went over budget at kroger.
    if kroger > kroger_budget:
        print(f'You went over kroger budget by ${(kroger.calculate_Total() - kroger_budget):.2f}')
    else:
        print(f'Awesome! You stuck to the kroger budget!') 
    
    # Doing a rich comparison to determine in which store the most money was spent.
    if walmart > kroger:
        print(f'You spent more money at walmart (${walmart.calculate_Total():.2f}) than kroger (${kroger.calculate_Total():.2f})')
    elif kroger > walmart:
        print(f'You spent more money at kroger (${kroger.calculate_Total():.2f}) than walmart (${walmart.calculate_Total():.2f})')
    else:
        print(f'You spent the same amount of money both stores (${kroger.calculate_Total():.2f})')
    
    input("Press Enter to Exit!")




