family = {
    "father" :
        {
            "name" : "John",
            "age" : 30
        },
    "mother" :
        {
            "name" : "Jane",
            "age" : 28
        },
    "children" :
        {
            "son" :
                {
                    "name" : {
                        "firstname" : "jack",
                        "lastname"
                    }
                    "age" : 5
                },
            "girl" :
                {
                    "name" : "jully",
                    "age" : 3
                }
        }
}

print(family["children"]["son"]["name"])