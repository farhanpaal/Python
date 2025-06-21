def wholeFamily():
    family ={
        "person":"Farhan",
        "wife":"Maahi",
        "children":[
            {
                "person":"ahmed",
                "wife":"zariqa",
                "children":[
                    {
                        "name":"mehveet"
                    },
                    {
                        "name":"simran"
                    }
                ]
            },
            {
                "person":"Mehmed",
                "wife":"Yameena",
                "children":[
                    {
                        "name":"Marshiq"
                    },
                    {
                        "name":"Kim"
                    }
                ]
            }
        ]
    }

    index=0
    print("House person",family["person"],sep=(" = "))
    print("House Wife",family["wife"],sep=(" = "))
    print("===============")
    for children in family["children"]:
        
        print("person",children["person"], sep=(" : "))
        print("wife",children["wife"], sep=(" : "))
        for children2 in children["children"]:
            index= index+1
            print(f"child {index}",children2["name"],sep=(" = "))
        index=0

        print("-------------------")
wholeFamily()