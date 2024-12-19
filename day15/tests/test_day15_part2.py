import unittest
import os
print("cwd: ", os.getcwd())

from mycode.day15_part2 import Warehouse, Coor

class TestWarehouse(unittest.TestCase):

    def test_load_map(self):
        map_path = "./day15/tests/inputs/load_test_map.txt"
        inst_path = "./day15/tests/inputs/load_test_inst.txt"
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
        inst_path = "./day15/tests/inputs/load_test_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        self.assertEqual(len(wh.wh_map), 10, "wh_map should have 10 rows")
        self.assertEqual(len(wh.wh_map[0]), 20, "wh_map sohuld have 20 columns")

        print("start: ", wh.start)
        print("robot_pos: ", wh.robot_pos())
        self.assertEqual(wh.robot_pos(), (4,10), "robot should start at (4,10)")


    def test_Coor(self):
        map_path = "./day15/tests/inputs/load_test_map.txt"
        inst_path = "./day15/tests/inputs/load_test_inst.txt"
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


    def test_robot_move_left(self):
        map_path = "./day15/tests/inputs/load_test_expanded_map.txt"
        inst_path = "./day15/tests/inputs/load_test_inst.txt"
        wh = Warehouse(map_path, inst_path, False)

        for i in range(8):
            self.assertTrue(wh.move_robot('<'))
            # print(wh.robot_pos())
        # hits wall
        self.assertFalse(wh.move_robot('<'))    

if __name__ == "__main__":
    unittest.main()