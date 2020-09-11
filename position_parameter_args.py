def is_item_here (item, *args):
    if item in args : return True
    else: return False
print (is_item_here('item','l',5, 8,90))
