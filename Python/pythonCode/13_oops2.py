class Main:
    x=123
    def __init__(self):
        name="farhan"
        self.y="7899"
       
    def pala(self):
        print(self.y)
        print(self.x)
        print(self.z)
        # print(self.name) #It will throw error as it is a local variable
    z=122

main=Main()
main.pala()
# 7899
# 123
# 122

from pprint import pprint

class Country:
    def __init__(self):
        self.countries=[
            {
                "Country":"India",
                "Short":"IN",
                "Code":"91"
            },
            {
                "Country":"Pakistan",
                "Short":"PAK",
                "Code":"92"
            },
            {
                "Country":"Nepal",
                "Short":"NEP",
                "Code":"977"
            }
        ]

#OOPs doesnt recomend this, it recommends inheritance 
# class Access:
#     def __init__(self):
#         Nation= Country()
#         pprint(Nation.countries)



#This isn't possible in constructor function
class Access(Country):
    def getCountries(self):
        pprint(self.countries)
country=Access()
country.getCountries()