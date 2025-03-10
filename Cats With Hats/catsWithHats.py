# 9.9 - Challenge: Cats With Hats
# solution

def get_cats_with_hats(list_of_cats):
    # variable for storing cats wearing hats
    cats_with_hats = []
    # we want to walk around the circle 100 times
    
    for num in range(1, 101):
        # we want to visit each cat in the circle
        for cat in range(1, 101):
            # determine which cat to visit
            # with the very useful modulo operator
            if cat % num == 0:
                # so if the cat has a hat on, we take it off and if it
                if list_of_cats[cat] is True:
                    list_of_cats[cat] = False
                # and put one on if it dosen't
                else:
                    list_of_cats[cat] = True
                    
    # at this point, it should have the final answer
    # so we need to return all the cats wearing hats
    for cat in range(1, 101):
        if list_of_cats[cat] == True:
            cats_with_hats.append(cat)
    return cats_with_hats


# at this point i was worried about wtiting a list with 100 false values but
# apperently, you can just do this:
cat_list = [False] * 101
print(get_cats_with_hats(cat_list))
        

                
        
