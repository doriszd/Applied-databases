# importing pymysql, ConnectMysql, ConnectMongo
import pymysql
import ConnectMysql
import ConnectMongo


# defining main function
def main():
    # displaying menu - 7 options
    display_menu()
    # while loop
    while True:
        # user is asked to select a number from 1 to 7
        choice = input("Enter choice: ")
        # OPTION 1
        # if the input is 1 people's names will be listed 2 by 2
        if (choice == "1"):
            # calling view_people function from document ConnectMysql
            person = ConnectMysql.view_people()
            # displaying menu again to enter a new choice
            display_menu()
            
        # OPTION 2
        # if a user chooses 2, countries by independance year will be printed
        elif (choice == "2"):
            print("Countries by Independence Year")
            # while loop
            while True:
                # user is asked to enter a year
                try:
        
                    year = int(input("Enter Year: "))
                    break
                # printing value error "Invalid year entered"
                except ValueError:
                    print("Invalid year entered. Please enter a valid number for the year")
            # calling independence_year function from document ConnectMysql
            independence = ConnectMysql.independence_year(year)
            # for loop to go through all countries in variable independence 
            for country in independence:
                # printing name, continent and independence year
                print (country["Name"],":",country["Continent"],":",country["IndepYear"])
            # diplaying main menu again
            display_menu()
            
        # OPTION 3
        # if a user chooses 3, add new person will be printed
        elif (choice == "3"):
            print("Add new person")
            # while loop
            while True:
                # user is asked to enter name and age
                try:
        
                    name = str(input("Name: "))
                    age = int(input("Age: "))
                    break
                # printing all exceptions as "error - please try again"
                except Exception as e:
                    print("Error - please try again.", e)
            # calling add_your_name function from document ConnectMysql
            add_person = ConnectMysql.add_your_name(name,age)
            # displaying main menu again
            display_menu()
            
            
        # OPTION 4 
        # if user chooses 4, countries by name will be printed
        elif (choice == "4"):
            print("countries by Name")
            # user is asked to enter country name
            country = input("Enter Country Name: ")
            # calling country_by_name function from ConnectMysql document
            countries = ConnectMysql.country_by_name(country)
            # looping through each row and printing results in requested format
            for country in countries:     
                print(country["Name"], "|", country["Continent"], "|", country["Population"], "|", country["HeadOfState"])
            # diplaying main menu 
            display_menu()
            
            
        # OPTION 5
        # if user chooses 5, countries by pop will be printed    
        elif (choice == "5"):
            print("Countries by Pop")
            # user is asked to enter symbol <, > or :
            symbol = input("Enter < > or =: ")
            # if the symbol is not <, >, : user is again asked to enter a symbol
            while symbol not in("<",">",'='):
                symbol = input("Enter < > or = : ")
                # if a user enters a correct symbol a while loop breaks
                if x in("<",">",'='):
                    break
            # user is asked to enter population number    
            population = int(input("Enter population: "))
            # calling countries_by_pop function from ConnectMysql document
            get_pop = ConnectMysql.countries_by_pop(symbol, population)
            # for loop to iterate through all countries 
            for country in get_pop: 
                # if a user chooses "<" 
                if symbol == "<":
                    # convert to integers and print code, name, continent and population of the country
                    if int(country["Population"]) < int(population):   
                        print(country["Code"],"|", country["Name"], "|", country["Continent"], "|", country["Population"])
                        # if a user chooses "=" printing all countries with population equal to that number
                    elif symbol == "=":                  
                        if int(country["Population"]) == int(population):
                            print(country["Code"],"|", country["Name"], "|", country["Continent"], "|", country["Population"])
                    # returning countries with pop greater than user input 
                    elif symbol == ">":                   
                        if int(country["Population"]) > int(population):
                            print(country["Code"],"|", country["Name"], "|", country["Continent"], "|", country["Population"])
                    
            
            display_menu()
            
        # OPTION 6
        # if user chooses 6, user will be asked to find students by address
        elif (choice == "6"):
            print("")
            print("Find Students by Address")
            print("------------------")
            # user is asked to enter address
            Address = input("Enter Address: ") 
            # calling the find function from ConnectMongo document
            result = ConnectMongo.find(Address)   
            # looping to print results 
            for x in result: 
                print(x["_id"], "|", x["details"] ["name"], "|",  x["details"] ["age"], "|", x["qualifications"])
            # displaying the menu
            display_menu()

        # OPTION 7        
        # if user chooses 7, he will be asked to add new course
        elif (choice == "7"): 
            print("")
            print("Add New Course")
            print("------------------")
            # user will be asked to enter id, name and level
            ID = input("_id: ")   
            Name = input("Name: ")
            Level = input("Level: ")
            # calling function insert from MongoConnect document
            ConnectMongo.insert(ID, Name, Level)   
            # displaying main menu
            display_menu()
            
        # if user wants to quit, press x    
        elif (choice == "x"):
            break;        

        else:
            # displaying main menu
            display_menu()  

# defining function to display main menu. There are 7 different options        
def display_menu():
    print("MENU")
    print("====")
    print("1 - View People")
    print("2 - View Countries by Independence Year")
    print("3 - Add New Person")
    print("4 - View Countries by name")
    print("5 - View Countries by population")
    print("6 - Find Students by Address")
    print("7 - Add New Course")
    print("x - Exit application")  



    
if __name__ == "__main__":
    main()    