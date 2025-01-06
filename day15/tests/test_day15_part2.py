import unittest
import os
print("cwd: ", os.getcwd())

from mycode.day15_part2 import Warehouse, Coor

# Test ideas
# 1) Test load of map against the extended map upload
# 2) Identify each type of move, then break point on each of them to check logic. 
#   - do sequences of moves to ege <<<, <>< <^> - this doesn't take into account the terrain of the map
#   - do checks on each combination of code executions. Can I use conditional breakpoints? 





class TestWarehouse(unittest.TestCase):

    def test_real_input(self):
        map_path = "./day15/inputs/day15_input_map.txt"
        inst_path = "./day15/inputs/day15_input_inst.txt"
        wh = Warehouse(map_path, inst_path)

        wh.execute_instructions()

        print("gps score: ", wh.cal_gps())

    def test_dom_input(self):
        map_path = "./day15/tests/inputs/dom_map.txt"
        inst_path = "./day15/tests/inputs/dom_inst.txt"
        wh = Warehouse(map_path, inst_path)

        wh.execute_instructions()

        print("gps score: ", wh.cal_gps())
    
    def test_small_example(self):
        map_path = "./day15/tests/inputs/small_example_map.txt"
        inst_path = "./day15/tests/inputs/small_example_inst.txt"
        wh = Warehouse(map_path, inst_path)

        wh.execute_instructions()

        print("gps score: ", wh.cal_gps())

    def test_large_example_gps(self):

        map_path = "./day15/inputs/day15_test2_map.txt"
        inst_path = "./day15/inputs/day15_test2_inst.txt"
        wh = Warehouse(map_path, inst_path)

        wh.execute_instructions()

        print("gps score: ", wh.cal_gps())
        wh.show_wh_map()
        self.assertEqual(wh.cal_gps(), 9021, "Large example should equal gps of 9021")


    def test_load_map(self):
        map_path = "./day15/tests/inputs/load_test_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path)


        # check grid size
        self.assertEqual(len(wh.original_map), 10, "original_map should have 10 rows")
        self.assertEqual(len(wh.original_map[0]), 10, "original_map should have 10 columns")
        self.assertEqual(len(wh.wh_map), 10, "wh_map should have 10 rows")
        self.assertEqual(len(wh.wh_map[0]), 20, "wh_map sohuld have 20 columns")

        # check start position
        self.assertEqual(wh.start, (4,10), "start position should be (4,10)")

    def test_load_expanded_map(self):
        map_path = "./day15/tests/inputs/load_test_expanded_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        self.assertEqual(len(wh.wh_map), 10, "wh_map should have 10 rows")
        self.assertEqual(len(wh.wh_map[0]), 20, "wh_map sohuld have 20 columns")

        print("start: ", wh.start)
        print("robot_pos: ", wh.robot_pos())
        self.assertEqual(wh.robot_pos(), (4,10), "robot should start at (4,10)")


    def test_load_compared_to_load_extended_map(self):

        map_path = "./day15/tests/inputs/load_vs_load_extended_orig_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh_orig = Warehouse(map_path, inst_path)

        map_path = "./day15/tests/inputs/load_vs_load_extended_ext_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh_ext = Warehouse(map_path, inst_path, False)

        self.assertEqual(wh_orig.wh_map, wh_ext.wh_map, "Maps should be the same.")




    def test_Coor(self):
        map_path = "./day15/tests/inputs/load_test_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path)

        coor00 = Coor((0,0))
        coor22 = Coor((2,2))

        # get values using Warehouse.value()
        self.assertEqual(wh.value(coor00), '#', "value at (0,0) should be '#")
        self.assertEqual(wh.value(coor22), '.', "value at (2,2) should be '.")

        # test offset
        self.assertEqual(coor00.offset(1,2).r, 1, "row offset should be 1")
        self.assertEqual(coor00.offset(1,2).c, 2, "row offset should be 2")
        # test next_pos and __call__()
        self.assertEqual(coor22.next_pos('^')() , (1,2), "'^' should give (1,2)")
        self.assertEqual(coor22.next_pos('>')() , (2,3), "'^' should give (2,3)")
        self.assertEqual(coor22.next_pos('v')() , (3,2), "'^' should give (3,2)")
        self.assertEqual(coor22.next_pos('<')() , (2,1), "'^' should give (2,1)")

    def test_robot_move_up(self):
        map_path = "./day15/tests/inputs/load_test_expanded_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        for i in range(3):
            self.assertTrue(wh.move_robot('^'), "The Robot should be able to move.")
            # print(wh.robot_pos())
        # hits wall
        self.assertFalse(wh.move_robot('^'), "The Robot should not be able to move.")  

    def test_robot_move_left(self):
        map_path = "./day15/tests/inputs/load_test_expanded_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        for i in range(8):
            self.assertTrue(wh.move_robot('<'), "The Robot should be able to move.")
            # print(wh.robot_pos())
        # hits wall
        self.assertFalse(wh.move_robot('<'), "The Robot should not be able to move.")    

    def test_robot_move_down(self):
        map_path = "./day15/tests/inputs/load_test_expanded_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        for i in range(4):
            self.assertTrue(wh.move_robot('v'), "The Robot should be able to move.")
            # print(wh.robot_pos())
        # hits wall
        self.assertFalse(wh.move_robot('v'), "The Robot should not be able to move.")  

    def test_robot_move_right(self):
        map_path = "./day15/tests/inputs/load_test_expanded_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        for i in range(7):
            self.assertTrue(wh.move_robot('>'), "The Robot should be able to move.")
            # print(wh.robot_pos())
        # hits wall
        self.assertFalse(wh.move_robot('>'), "The Robot should not be able to move.")   

    # test pushing single blocks
    def test_block_test1(self):
        map_path = "./day15/tests/inputs/block_test1_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        for i in range(3):
            self.assertTrue(wh.move_robot('^'), "The Robot should be able to move.")
            # print(wh.robot_pos())
        # 4 blocks stack up against top wall
        self.assertFalse(wh.move_robot('^'), "The Robot should not be able to move.")

    # test pushing two blocks with second block blocked
    def test_block_test2(self):
        
        map_path = "./day15/tests/inputs/block_test2_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        
        self.assertFalse(wh.move_robot('^'), "The Robot should not be able to move.")
        self.assertEqual(wh.value(Coor((5,9))), '.', "The left block should not move.")

    # test pushing two blocks with second block blocked
    def test_block_test3(self):
        
        map_path = "./day15/tests/inputs/block_test3_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        
        self.assertFalse(wh.move_robot('^'), "The Robot should not be able to move.")
        self.assertEqual(wh.value(Coor((5,9))), '.', "The left block should not move.")
        self.assertEqual(wh.cal_gps(), 1930)


    # test pushing a pyramid of blocks works
    def test_block_test4(self):
        
        map_path = "./day15/tests/inputs/block_test4_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        
        self.assertTrue(wh.move_robot('^'), "The Robot should be able to move.")
        self.assertFalse(wh.move_robot('^'), "The Robot should not be able to move.")
        
        # test pushing a pyramid of blocks works

    def test_block_test5(self):
        
        map_path = "./day15/tests/inputs/block_test5_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        
        self.assertFalse(wh.move_robot('^'), "The Robot should not be able to move.")
        
    # pushing blocks left    
    def test_block_test6(self):
        
        map_path = "./day15/tests/inputs/block_test6_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        

        for i in range(5):
            self.assertTrue(wh.move_robot('<'), "The Robot should be able to move.")
            # wh.show_wh_map()
        self.assertFalse(wh.move_robot('<'), "The Robot should not be able to move.")
        # wh.show_wh_map()

    
    # pushing blocks right
    def test_block_test7(self):
        
        map_path = "./day15/tests/inputs/block_test7_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        
        for i in range(8):
            self.assertTrue(wh.move_robot('>'), "The Robot should be able to move.")
            # wh.show_wh_map()
        self.assertFalse(wh.move_robot('>'), "The Robot should not be able to move.")
        # wh.show_wh_map()

    # pushing blocks left with obstacles
    def test_block_test8(self):
        
        map_path = "./day15/tests/inputs/block_test8_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        
        for i in range(2):
            self.assertTrue(wh.move_robot('>'), "The Robot should be able to move.")
            wh.show_wh_map()
        self.assertFalse(wh.move_robot('>'), "The Robot should not be able to move.")
        wh.show_wh_map()


    # two blocks pushing one
    def test_block_test9(self):
        
        map_path = "./day15/tests/inputs/block_test9_map.txt"
        inst_path = "./day15/tests/inputs/dummy_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        wh.show_wh_map()
        for i in range(4):
            print('^')
            self.assertTrue(wh.move_robot('^'), "The Robot should be able to move.")
            wh.show_wh_map()
        self.assertFalse(wh.move_robot('^'), "The Robot should not be able to move.")
        wh.show_wh_map()


    # pushing blocks around an obstacle
    def test_path_test1(self):
        
        map_path = "./day15/tests/inputs/path_test1_map.txt"
        inst_path = "./day15/tests/inputs/path_test1_inst.txt"
        wh = Warehouse(map_path, inst_path, False)
        
        wh.execute_instructions()
        print("gps: ",wh.cal_gps())



if __name__ == "__main__":
    unittest.main()