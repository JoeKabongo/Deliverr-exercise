def get_cheapest_shipment(order, warehouses):
    """
        Find cheapest shipment in these steps
        1. Try to find one warehouse that can ship the entire order, if not go to step two
        2. Do recursive path that get possibles shipments across warehouses(see find_possible_shipment function)
        3. if multiples shipments were found, get the cheapest one(see get_cheapest_option function )
    """
    
    order_item_count = sum(order.values())

    #check if one warehouse can take the entire order
    for index, warehouse in enumerate(warehouses):

        inventory = warehouse.get('inventory')
        name = warehouse.get('name')
        
        #count number of items acquired from warehouse
        item_count = 0 

        #update quantity of item if any found in this warehouse
        possible_remaining_order = order.copy()

        #item we can get from this warehouse
        items_found = {} 

        for  item, quantity in order.items():

            #item was found in warehouse, take the maximum we can for this order
            if item in inventory and quantity != 0:
                number_taken = min(quantity, inventory.get(item))
                item_count += number_taken
                possible_remaining_order[item] = quantity - number_taken
                items_found[item] = number_taken
        
        if item_count == order_item_count:
            return [{name: items_found}]
    
    final_results = []
    find_possible_shipment(order, order_item_count, warehouses, 0, [], final_results)

    n = len(final_results)
    if n == 0: return []
    if n == 1: return final_results[0]

    return get_cheapest_option(final_results, warehouses)

def find_possible_shipment(order, items_left, warehouses, index, current_result, final_result):
    """
        Recursively go through each warehouses
        1. recursive call two options, grab items from this warehouse or dont grab them
        2. if at any path we found all items, we dont continue any longer with that recursive path

    """
    #base case, we have considered all warehouses 
    if index >= len(warehouses): return 

    warehouse = warehouses[index]
    warehouse_inventory = warehouse.get('inventory')
    warehouse_name = warehouse.get('name')

    #count number of items acquired from this warehouse
    item_count = 0 

    #item found from this warehouse
    items_found = {} 
    possible_remaining_order = order.copy()


    for  item, quantity in order.items():

        #item was found in warehouse
        if item in warehouse_inventory and quantity != 0:
            number_taken = min(quantity, warehouse_inventory.get(item))
            item_count += number_taken
            possible_remaining_order[item] = quantity - number_taken
            items_found[item] = number_taken

    #if some items were collected, add it to our resursive path result
    if item_count > 0:
        current_result.append({warehouse_name: items_found})
    
    # we found all items to complete order, add to final result and break recursive path 
    if item_count == items_left: 
        final_result.append(current_result)
        return 
    
    
    #recusive path that consider this warehouse result
    find_possible_shipment(possible_remaining_order, items_left-item_count, warehouses, index + 1, current_result[:], final_result)

    #recursive path that does not considere this warehouse, if items were taken from this warehouse
    if item_count > 0:
        find_possible_shipment(order, items_left, warehouses, index + 1, current_result[:-1], final_result)



def get_cheapest_option(shipment_lists, warehouses):
    """
        Given list of shipment, find cheapest one
        1. Find the shipment with the least warehouses
        2. If more than one, take the shipment whose sums of warehouse index 
        is smallest since warehourse are presort by shipping cost
    """

    #find shipmennts with the least involved warehouses
    least_warehouse_shipments = [shipment_lists[0]]
    lenght = len(shipment_lists[0])

    n = len(shipment_lists)

    for i in range(1, n):

        shipment = shipment_lists[i]
        l = len(shipment)

        if l < lenght:
            lenght = l
            least_warehouse_shipments = [shipment]
        elif l == lenght:
            least_warehouse_shipments.append(shipment)
    
    #if we found one shipment option with the least number of warehourses
    if least_warehouse_shipments == 1:
        return least_warehouse_shipments[0]
    
    #get index of each warehouse
    indexes = {}
    for index, warehouse in enumerate(warehouses):
        name = warehouse.get('name')
        indexes[name] = index
    
    #keep track of the shipment with the minimum index sum
    minumum_sum = sum(indexes.values())
    min_index = -1
    for index, shipment in enumerate(least_warehouse_shipments):
        index_sum = 0
        for warehouse in shipment:
            index_sum += indexes[list(warehouse.keys())[0]] 
        
        if index_sum < minumum_sum:
            min_index = index 
            minumum_sum = index_sum
    
    return least_warehouse_shipments[min_index]
