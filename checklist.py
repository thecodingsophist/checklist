#Keyboard Shortcuts!!!!
#Control A goes to beginning of the line
#Control E goes to the end of the line

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = "√" + checklist[index]

def select(function_code):
    if function_code == "C":
        input_item = input("Input item:")
        create(input_item)
    elif function_code == "R":
        input_item = input("Input index")
        read(int(input_item))
    elif function_code == "P":
        list_all_items()
    else:
        print("Unknown Option")

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()

    mark_completed(0)

    select("C")

    list_all_items()

    select("R")

    list_all_items()


test()
