# Deliverr-exercise

Program file: shipment.py

Test File: test_shipment.py

To test, run command : python test_shipment.py

To find the cheapest shipment
1. I attempt to find one warehouse that can allow me to ship the entire order
2. If not possible, look accross warehouse and find possible shipments
3. Return the one with the cheapest cost 

I would love to hear about any optimal approache to solve this question!

Other approach I attempted:
I tried a more optimal greedy approach that greedly takes items from warehouses with max inventory. This approach guarenteed to get a shipment with least warehouses involved but did not guarenteed the cheapest cost in term of warehouse position in the array. For example it would choose [4,5] warehouse to ship order rather than [1,3]  

