import unittest
from shipment import get_cheapest_shipment


class TestCheapestShipment(unittest.TestCase):
    
    def test_shipment_function(self):
        """
            Test that the  invantory class return the correct shipment
        """

        #Order can only be shipped from one warehouse
        order = { 'banana' : 10, 'apple': 5 }
        warehouses = [ 
            { 'name': 'pk', 'inventory': { 'banana': 10 , 'apple': 5} }, 
            { 'name': 'owd', 'inventory': { 'apple': 10, 'basketball': 2, 'bread': 3 } }, 
            {'name': 'amz', 'inventory': {'bread': 100}}
        ]

        expected_output = [{ 'pk': {'apple': 5, 'banana': 10}}]
        self.assertTrue(
            self.are_equal(get_cheapest_shipment(order, warehouses), expected_output )
        )

        #order can only be shipped using multiple warehouses
        order = { 'banana' : 10, 'apple': 14 }
        warehouses = [ 
            { 'name': 'pk', 'inventory': { 'banana': 10 , 'apple': 5} }, 
            { 'name': 'owd', 'inventory': { 'apple': 10, 'basketball': 8, 'bread': 3 } }, 
            {'name': 'amz', 'inventory': {'bread': 1}}
        ]
        expected_output = [{ 'pk': {'apple': 5, 'banana': 10}}, {'owd': {'apple': 9}}]
        self.assertTrue(
            self.are_equal(get_cheapest_shipment(order, warehouses), expected_output)
        )

        #Not enough inventory for the order (not enough apple)
        order = { 'banana' : 10, 'apple': 25 , 'bread': 12}
        warehouses = [ 
            { 'name': 'pk', 'inventory': { 'banana': 10 , 'apple': 5} }, 
            { 'name': 'owd', 'inventory': { 'apple': 10, 'basketball': 2, 'bread': 3 } }, 
            {'name': 'amz', 'inventory': {'bread': 20}}
        ]
        expected_output = []
        self.assertTrue(
            self.are_equal(get_cheapest_shipment(order, warehouses), expected_output)
        )


        # Order can be made either be made between two warehourse and one warehouse. Choose one warehouse option
        order = { 'banana' : 10, 'apple': 25 }
        warehouses = [ 
            { 'name': 'pk', 'inventory': { 'banana': 10 , 'apple': 5} }, 
            { 'name': 'owd', 'inventory': { 'apple': 10, 'basketball': 2, 'bread': 3 } }, 
            {'name': 'amz', 'inventory': {'bread': 100 , 'apple': 76, 'banana': 100}}
        ]

        expected_output = [{'amz': {'banana': 10, 'apple': 25}}]
        self.assertTrue(
            self.are_equal(get_cheapest_shipment(order, warehouses), expected_output)
        )
        

        # Order can be taken from mutliple combination of warehouses
        # take the cheapest combination 
        
        #this case the first two warehouses will be the cheapest option
        order = { 'banana' : 10, 'apple': 25 }
        warehouses = [ 
            { 'name': 'pk', 'inventory': { 'banana': 4 , 'apple': 5} }, 
            { 'name': 'owd', 'inventory': { 'apple': 23, 'banana': 6} },
            { 'name': 'cmd', 'inventory': { 'apple': 22, 'banana': 10} },
            {'name': 'amz', 'inventory': {'apple': 20, 'banana': 7}}
        ]

        expected_output = [{'pk': {'banana': 4, 'apple': 5}}, {'owd': {'banana': 6, 'apple': 20}}]
        self.assertTrue(
            self.are_equal(get_cheapest_shipment(order, warehouses), expected_output)
        )


        # We can make order with warehouse 1,2 and 3. Or warehouse 4 with any other warehouse
        # Output is warehouse 1 and 4 since they are they cheapest to combination
        order = { 'banana' : 10, 'apple': 25 }
        warehouses = [ 
            { 'name': 'pk', 'inventory': { 'banana': 4 , 'apple': 5} }, 
            { 'name': 'poc', 'inventory': { 'apple': 10, 'banana': 4} },
            { 'name': 'owd', 'inventory': { 'apple': 15, 'banana': 4} },
            {'name': 'amz', 'inventory': {'apple': 20, 'banana': 7}}
        ]

        expected_output = [{'pk': {'banana': 4, 'apple': 5}}, {'amz': {'banana': 6, 'apple': 20}}]
        self.assertTrue(
            self.are_equal(get_cheapest_shipment(order, warehouses), expected_output)
        )


    def are_equal(self, list1, list2):
        """ Test that two lists of dictionary are equals """
        if len(list1) != len(list2): return False

        for element in list2:
            if element not in list1:
                return False 
        return True
    

if __name__ == '__main__':
    unittest.main()







