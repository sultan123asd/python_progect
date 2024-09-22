item_greetings = input("greetings!^_^ choose any spray from our list:Lilys whisper. dark vanilla dream. : ")
quantity = int(input("how many would you like to purchase?: "))

lilys_whisper = 399

dark_vanilla_dream = 599

desert_bloom = 766

if item_greetings == "lilys whisper":
    total = lilys_whisper * quantity

    print(f'your total price is: {total} \nThanks for shopping!')
elif item_greetings =="dark vanilla dream":
    total = dark_vanilla_dream * quantity

    print(f'your total price is: {total} \nThanks for shopping!')
