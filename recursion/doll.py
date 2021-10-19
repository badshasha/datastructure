
def dall(number_of_dall):
    print("dall open")
    if number_of_dall == 1:
        print("dall find")
    else:
        dall(number_of_dall-1)


dall(8)
