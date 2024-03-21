def sort_by_price(items) :
    from copy import deepcopy
    sorted_items = []
    copied_items = deepcopy(items)
    for i in range(len(copied_items)) :
        best_item_index = 0
        for j in range(len(copied_items)) :
            if(copied_items[j]["price"] > copied_items[best_item_index]["price"]) :
                best_item_index = j
        sorted_items.append(copied_items[best_item_index])
        del copied_items[best_item_index]
    return sorted_items

def sort_by_weight(items) :
    from copy import deepcopy
    sorted_items = []
    copied_items = deepcopy(items)
    for i in range(len(copied_items)) :
        best_item_index = 0
        for j in range(len(copied_items)) :
            if(copied_items[j]["weight"] < copied_items[best_item_index]["weight"]) :
                best_item_index = j
        sorted_items.append(copied_items[best_item_index])
        del copied_items[best_item_index]
    return sorted_items

def sort_by_ratio(items) :
    from copy import deepcopy
    sorted_items = []
    copied_items = deepcopy(items)
    for i in range(len(copied_items)) :
        best_item_index = 0
        for j in range(len(copied_items)) :
            ratio_i = copied_items[j]["price"]/copied_items[j]["weight"]
            ratio_j = copied_items[best_item_index]["price"]/copied_items[best_item_index]["weight"]
            if(ratio_i > ratio_j) :
                best_item_index = j
        sorted_items.append(copied_items[best_item_index])
        del copied_items[best_item_index]
    return sorted_items

def greedy_kp(items, bag):
   items_in_bag = []
   for item in items:
       if bag >= item['weight']:
           items_in_bag.append(item)
           bag -= item['weight']
   return items_in_bag