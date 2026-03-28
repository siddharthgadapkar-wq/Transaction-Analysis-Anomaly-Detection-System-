#import file first from the folder
import csv

# we created a class and object to represent a transaction structure
class Transaction:
    def __init__(self,date,category,amount):
        self.date=date
        self.category=category
        self.amount=amount

    def showdetails(self):
        print("Date:",self.date)
        print("category:",self.category)
        print("amount:",self.amount)
        print("--------------------")

#STEP 5:Store all transactions so we can analyze them and find fraud
class FraudDetector:
    def __init__(self,transactions):#here we give the data,that we store in the list, named transactions
        self.transactions=transactions

    def detect_high_transaction(self):
        total=0

        for t in self.transactions:
            total +=t.amount
        
        average = total/len(self.transactions)
        print("Average Transaction Amount:",average)
        print("\nHigh Transaction:")

        for t in self.transactions:
            if t.amount > average*5:
                t.showdetails()
                print("TRANSACTIONS DETECTED")

    def Duplicate_Detector(self):
        seen =[]

        print("\n---Duplicate Transactions---")

        for t in self.transactions:
            key=(t.date,t.category,t.amount)

            if key in seen:
                print("Duplicate Transaction Detected !!!")
                t.showdetails()
            else:
                seen.append(key)

    def Category_Analysis(self):
        category_total={}
        for t in self.transactions:
            if t.category in category_total:
                category_total[t.category] += t.amount
            else:
                category_total[t.category] = t.amount
        print("\nCategory Spending:")
            
        for category in category_total:
            print(category,":",category_total[category])

        max_category=""
        max_amount= 0

        for category in category_total:
            if category_total[category] > max_amount:
                max_amount=category_total[category]
                max_category=category
        print("Highest Money Spending Category:",max_category)

    def search_by_category(self):
        category_input=input("Enter the category to search:")
        print(f"\n Transaction for {category_input}:")
        found = False
        for t in self.transactions:
            if t.category.lower()==category_input.lower():
                t.showdetails()
                found=True
        if not found:
            print("No Transactions found for this category..")        


def load_data():
    transactions =[]  #empty list  
#STEP 1: Read CSV
    with open("transactions.csv","r") as file:
        reader=csv.reader(file)
        data=list(reader)


# STEP 3: converts rows into objects
    for i in range(1,len(data)):
        date=data[i][0]
        category=data[i][1]
        amount=float(data[i][2])         #float because the transaction value can be decimal value

        t=Transaction(date,category,amount)     #Here we pass a variable in the bracket Take values from CSV and make a Transaction object
        transactions.append(t)

    return transactions


# STEP 4: Prints all object
transactions = load_data()
detector=FraudDetector(transactions)

#menu for user to display the analysis
while True:
    print("\n ===TRANSACTION ANALYSIS SYSTEM===")
    print("1.Show High Transactions")
    print("2.Duplicate Transactions")
    print("3.Show category Analysis")
    print("4.Search By Category")
    print("5.Exit program.")

    choice=input("Enter the choice:")

    if choice=="1":
        detector.detect_high_transaction()
    elif choice=="2":
        detector.Duplicate_Detector()
    elif choice=="3":
        detector.Category_Analysis()
    elif choice=="4":
        detector.search_by_category()
    elif choice=="5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice,try again!")
       
detector.detect_high_transaction()
detector.Duplicate_Detector()
detector.Category_Analysis()
detector.search_by_category()
