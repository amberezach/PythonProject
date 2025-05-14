from logging import exception

ItemsInCart = 0

# 2 items will be added to cart

if ItemsInCart != 2:  # raise Exception("Products cart count is not matching")
    pass

assert(ItemsInCart == 0)


try:
    with open("Text.txt", "r") as reader:
        reader.read()

except:
    print("I have reached this block because of a failure in try block")



try:
    with open("Text.txt", "r") as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")
