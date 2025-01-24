class goa: #declaring class
    name=""
    drink= ""  #declaring variable
    def party(self): #creating function
        print("Let's party")
    def beach(self): #creating function
        print("Enjoying the beach")

ramesh= goa() #object1
suresh= goa() #object2

ramesh.name="Ramesh"
suresh.name="suresh"

ramesh.drink="Drink"
suresh.drink="not drink"

print(ramesh.name)
print(suresh.name)

print("ramesh-drink:?",ramesh.drink)
print("suresh-drink:?",suresh.drink)

ramesh.party()
suresh.beach()
