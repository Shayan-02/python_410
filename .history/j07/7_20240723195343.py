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
                    "name" :
                    {
                        "firstname" : "jack",
                        "lastname" : "smith"
                    },
                    "age" : 5
                },
            "girl" :
                {
                    "name" : "jully",
                    "age" : 3
                }
        }
}

print(
    family["children"]["son"]["name"]["firstname"],
    family["children"]["son"]["name"]["lastname"],
)

print(len)