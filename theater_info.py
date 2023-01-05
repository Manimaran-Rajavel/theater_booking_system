from winreg import EnumValue
import   user_info

class seats:
    global matrix,total_seats_booked
    matrix = []


    def __init__(self):
        self.no_of_rows = int(input("\nEnter the Number of Rows: "))
        self.no_of_columns = int(input("Enter the Number of Columns: "))
       

    def capacity(self):
        for i in range(self.no_of_rows + 1):
            a = []
            for j in range(self.no_of_columns + 1):
                if j >= 9:
                    a.append(" N")
                else:
                    a.append("N")
            matrix.append(a)

        total_seats = self.no_of_columns * self.no_of_rows
        return total_seats, self.no_of_rows,self.no_of_columns

    def show_the_seats(self):

        for i in range(0, self.no_of_rows + 1):
            if i == 0:
                for j in range(0, self.no_of_columns + 1):
                    print(j, end=" ")
            else:
                print(i, end=" ")
                for k in range(self.no_of_columns):
                    print(matrix[i - 1][k], end=" ")
            print()
        print("\nN - Indicate Seat is Not Booked\nB - Incicate seat is Booked\n")


class tickets:
    global price_each_ticket,p

    def __init__(self):
        self.book_row = int(input("\nPlease enter the row no. you want to book: "))
        self.book_column = int(input("Please enter the column no. you want to book: "))


    def buy_ticket(self, total_seats, no_of_rows,total_income ):

        p = tickets.price_per_ticket(self,total_seats, no_of_rows,total_income)

        print("\nThe Price of your ticket will be: ", p, "₹")
        confirmation = input("\nPlease type 'Yes' to Confirm booking 'No' to cancle ticket: ")

        if confirmation == 'Yes' or confirmation=='yes':

            matrix[self.book_row - 1][self.book_column - 1] = "B"
            u=user_info.user_info()
            u.user(self.book_row,self.book_column)
            return True,p

        else:
            print("\nNo ticket booked")
            return None,None

    def price_per_ticket(self, total_seats, no_of_rows,total_income):
        current_income=0
        if total_seats <= 60:
            current_income=100
            total_income=total_income + current_income
            return  100

        else:
            if self.book_row >= (no_of_rows / 2):
                current_income = 80

                return  80
            else:
                current_income = 100

                return 100

class statistics:
    def stats(self,total_seats_booked,total_seats,c,total_income):
        print("Number of Purchased Tickets: ",total_seats_booked)
        print("Percentage of Tickets Booked: ",(total_seats_booked/total_seats)*100)
        print("Current Income: ",c,"₹")
        print("Total_income: ",total_income,"₹")
        print(50*"-")   


# New class created 
class Theater:
    # Method
    def movie_name(self):
        print("\nplease choose the movie:\n")
        movie_list = ["Book 'Movie1'","Book 'Movie2'","Book 'Movie3'"]  # list containg Movie names
        for i,value in enumerate (movie_list):
            print(f"Enter '{i}' to {value}\n")       # Print the movie names
        self.user_movie =  int(input("Enter the Movie number: "))  # Get the input
 
        print(50*"-")   

    # Method
    def movie_language(self):
        print("\nPlease choose the Lanuage\n")

        # Specific language for each movie
        if self.user_movie == 0:
            lang  = ["Tamil","English","Hindi","Kannada","Telugu"] # langugaes for movie Movie1 (can add more languages)
            for i,value in enumerate (lang):
                print(f"Enter '{i}' to {value}\n")
        elif self.user_movie == 1:  # langugaes for movie Movie2 (can add more languages)
            lang  = ["Tamil","English","Kannada","Telugu"]
            for i,value in enumerate (lang):
                print(f"Enter '{i}' to {value} \n")
        else:               
            lang  = ["Tamil","English"]   # langugaes for movie Movie3 (can add more languages)
            for i,value in enumerate (lang):
                print(f"Enter '{i}' to {value}\n")
        
        int(input("choose the number: "))
        self.lang_flag  = True
        print(50*"-")   

    # Method
    def timing(self):
        print("\nPlease choose the Timing\n")
        value_time = ["09:00 AM", "11:00 AM","02:00 PM", "06:00 PM", "10:00 PM"] #Timings
        for i,value in enumerate (value_time):
            print(f"Enter '{i}' to {value}\n")
        int(input("Enter the Time slot: "))
        print(50*"-")   