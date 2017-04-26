class Parent():
    def __init__(self,last_name,eye_color):
        print ("parent arg called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("last name - "+self.last_name)
        print("eye color -"+self.eye_color)
        

class Child(Parent):
    def __init__(self,last_name,eye_color,no_of_toys):
        print("child is called")
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys = no_of_toys
    def show_info(self):
        print("last name-"+self.last_name)
        print("eye color-"+self.eye_color)
        print("no of toys -"+str(self.no_of_toys))
    
    


#billy_cyrus = Parent("cyrus","blue")
#print (billy_cyrus.last_name)
#billy_cyrus.show_info()

miley_cyrus= Child("cyrus","blue",5)
miley_cyrus.show_info()
#print(miley_cyrus.last_name)
#print(miley_cyrus.no_of_toys)

    
