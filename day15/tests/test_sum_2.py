# import unittest
# from test_class import MyClass

# class TestSum(unittest.TestCase):
#     def test_sum(self):
#         self.assertEqual( sum([1,2,3]), 6,  "Should be 6" )


#     def test_sum_tuple(self):
#         self.assertEqual( sum((1,2,3)), 6, "Should be 6" )


#     def test_grid(self):


#         grid = [['#', '.', '@'],['#', '.', '@'],['#', '.', '@']]
#         grid2 = [['#', '.', '@'],['#', '.', '@'],['#', '.', '@']]

#         self.assertEqual(grid, grid2, "grids shuold be equal")

#     def test_myclass(self):
#         mc = MyClass()
#         self.assertEqual(mc.myfunc(), 123, "number should be 123")

# if __name__ == "__main__":
#     unittest.main()