import unittest
from src import validate_ip
import ipaddress

class UnitTests(unittest.TestCase):

    def test_validIP(self):
        inp = "223.10.10.10"
        self.assertEqual("IP address 223.10.10.10 is valid", validate_ip.validate_ip_address(inp))

    def test_validate_classC(self):
        inp = "223.10.10.10"
        self.assertEqual("The ip address 223.10.10.10 belongs to class C", validate_ip.get_ip_class(inp))

    def test_validate_classB(self):
        inp = "191.10.10.10"
        self.assertEqual(f"The ip address {inp} belongs to class B", validate_ip.get_ip_class(inp))

    def test_validate_classA(self):
        inp = "127.10.10.10"
        self.assertEqual(f"The ip address {inp} belongs to class A", validate_ip.get_ip_class(inp))

    def test_validate_classnotA(self):
        inp = "128.10.10.10"
        self.assertNotEqual(f"The ip address {inp} belongs to class A", validate_ip.get_ip_class(inp))

    def test_validate_classnotB(self):
        inp = "195.10.10.10"
        self.assertNotEqual(f"The ip address {inp} belongs to class B", validate_ip.get_ip_class(inp))

    def test_validate_classnotC(self):
        inp = "225.10.10.10"
        self.assertNotEqual(f"The ip address {inp} belongs to class C", validate_ip.get_ip_class(inp))

    def test_invalid_class(self):
        inp = "255.10.10.10"
        self.assertEqual(f"The ip address {inp} does not belongs to class A, B or C", validate_ip.get_ip_class(inp))

    def test_validate_invalidIP(self):
        inp = ".10.10.10"
        self.assertRaises(ValueError,validate_ip.validate_ip_address,inp)


if __name__ == "__main__":
    unittest.main()



