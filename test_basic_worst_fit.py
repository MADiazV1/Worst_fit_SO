# Tests
import unittest
from main import worst_fit

class TestBasicFirstFit(unittest.TestCase):

  def test_pass_empty_map(self):
    work_memory = []
    req = 0
    index = 0
    search = worst_fit(work_memory, req, index)
    self.assertEqual(search, None)

  def test_req_highest(self):
    work_memory = [(0x00A00000, 0x000C0000)]
    req = 0x000D0000
    index = 0
    search = worst_fit(work_memory, req, index)
    self.assertEqual(search, None)

  def test_req_highest_list(self):       
    work_memory = [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000C0000)]
    req = 0x000D0000
    index = 0
    search = worst_fit(work_memory, req, index)
    self.assertEqual(search, None)

  def test_req_highest_list_2(self):
    work_memory = [
      (0xa0000000, 0x00010000),
      (0xb0000000, 0x00010000),
      (0x10000000, 0x00090000),
      (0xc0000000, 0x00060000),
      (0xd0000000, 0x00010000),
      (0x30000000, 0x00040000)
    ]
    req = 0x00030000
    index = 0
    search = worst_fit(work_memory, req, index)
    self.assertEqual(search, (0x10030000, 2))

if __name__ == '__main__':
  unittest.main()
