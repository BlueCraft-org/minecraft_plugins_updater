import unittest

from core.version.target_version import TargetVersion
from core.version.error import TargetVersionError
from core.version.version import Version
from core.version.version_list import VersionList


class TestTargetVersion(unittest.TestCase):
    def test_init(self):
        tv = TargetVersion("1.2.3")
        self.assertEqual(tv.major, 1)
        self.assertEqual(tv.minor, 2)
        self.assertEqual(tv.patch, 3)
        self.assertEqual(tv.tuple_version, (1, 2, 3))

    def test_init_with_wildcard(self):
        tv = TargetVersion("1.*.*")
        self.assertEqual(tv.major, 1)
        self.assertIsNone(tv.minor)
        self.assertIsNone(tv.patch)
        self.assertEqual(tv.tuple_version, (1, None, None))

    def test_get_version(self):
        tv = TargetVersion("1.2.3")
        self.assertEqual(tv.get_version(), "1.2.3")

    def test_repr(self):
        tv = TargetVersion("1.2.3")
        self.assertEqual(repr(tv), "<TargetVersion 1.2.3>")

    def test_init_with_invalid_version(self):
        with self.assertRaises(TargetVersionError) as cm:
            TargetVersion("a.b.c")
        self.assertEqual(str(cm.exception), "TargetVersion a.b.c is not supported.")


class TestVersion(unittest.TestCase):
    def test_init(self):
        v = Version("1.2.3")
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.patch, 3)
        self.assertEqual(v.tuple_version, (1, 2, 3))

    def test_get_version(self):
        v = Version("1.2.3")
        self.assertEqual(v.get_version(), "1.2.3")

    def test_repr(self):
        v = Version("1.2.3")
        self.assertEqual(repr(v), "<Version 1.2.3>")

    def test_eq(self):
        v1 = Version("1.2.3")
        v2 = Version("1.2.3")
        self.assertTrue(v1 == v2)

    def test_ne(self):
        v1 = Version("1.2.3")
        v2 = Version("1.2.4")
        self.assertTrue(v1 != v2)

    def test_lt(self):
        v1 = Version("1.2.3")
        v2 = Version("1.2.4")
        self.assertTrue(v1 < v2)

    def test_le(self):
        v1 = Version("1.2.3")
        v2 = Version("1.2.4")
        self.assertTrue(v1 <= v2)

    def test_gt(self):
        v1 = Version("1.2.4")
        v2 = Version("1.2.3")
        self.assertTrue(v1 > v2)

    def test_ge(self):
        v1 = Version("1.2.4")
        v2 = Version("1.2.3")
        self.assertTrue(v1 >= v2)

    def test_lt_major(self):
        v1 = Version("1.2.3")
        v2 = Version("2.1.1")
        self.assertTrue(v1 < v2)

    def test_lt_minor(self):
        v1 = Version("1.2.3")
        v2 = Version("1.3.1")
        self.assertTrue(v1 < v2)

    def test_le_major(self):
        v1 = Version("1.2.3")
        v2 = Version("2.1.1")
        self.assertTrue(v1 <= v2)

    def test_le_minor(self):
        v1 = Version("1.2.3")
        v2 = Version("1.3.1")
        self.assertTrue(v1 <= v2)

    def test_gt_major(self):
        v1 = Version("2.2.3")
        v2 = Version("1.3.4")
        self.assertTrue(v1 > v2)

    def test_gt_minor(self):
        v1 = Version("1.3.3")
        v2 = Version("1.2.4")
        self.assertTrue(v1 > v2)

    def test_ge_major(self):
        v1 = Version("2.2.3")
        v2 = Version("1.3.4")
        self.assertTrue(v1 >= v2)

    def test_ge_minor(self):
        v1 = Version("1.3.3")
        v2 = Version("1.2.4")
        self.assertTrue(v1 >= v2)


class TestVersionList(unittest.TestCase):
    def test_init(self):
        vl = VersionList(["1.2.3", "1.2.4", "1.3.1"])
        self.assertEqual(len(vl.version_list), 3)
        self.assertEqual(vl.version_list[0].get_version(), "1.3.1")
        self.assertEqual(vl.version_list[1].get_version(), "1.2.4")
        self.assertEqual(vl.version_list[2].get_version(), "1.2.3")

    def test_filter_major(self):
        vl = VersionList(["1.2.3", "1.2.4", "2.3.1"])
        filtered_list = list(vl.filter_major(vl.version_list, 1))
        self.assertEqual(len(filtered_list), 2)
        self.assertEqual(filtered_list[0].get_version(), "1.2.4")
        self.assertEqual(filtered_list[1].get_version(), "1.2.3")

    def test_filter_minor(self):
        vl = VersionList(["1.2.3", "1.2.4", "1.3.1"])
        filtered_list = list(vl.filter_minor(vl.version_list, 2))
        self.assertEqual(len(filtered_list), 2)
        self.assertEqual(filtered_list[0].get_version(), "1.2.4")
        self.assertEqual(filtered_list[1].get_version(), "1.2.3")

    def test_filter_patch(self):
        vl = VersionList(["1.2.3", "1.2.4", "1.3.4"])
        filtered_list = list(vl.filter_patch(vl.version_list, 4))
        self.assertEqual(len(filtered_list), 2)
        self.assertEqual(filtered_list[0].get_version(), "1.3.4")
        self.assertEqual(filtered_list[1].get_version(), "1.2.4")

    def test_filter(self):
        vl = VersionList(["1.2.3", "1.2.4", "1.3.4"])
        filtered_list = vl.filter(1, 2, 4)
        print(filtered_list)
        self.assertEqual(len(filtered_list), 1)
        self.assertEqual(filtered_list[0].get_version(), "1.2.4")

    def test_get_targeted_lastest_version(self):
        vl = VersionList(["1.2.3", "2.3.4", "3.4.5"])
        tv = TargetVersion("2.*.*")
        targeted_version = vl.get_targeted_lastest_version(tv)
        self.assertEqual(targeted_version.get_version(), "2.3.4")

    def test_repr(self):
        vl = VersionList(["1.2.3", "2.3.4", "3.4.5"])
        self.assertEqual(
            repr(vl),
            "<ListVersion version_list=[<Version 3.4.5>, <Version 2.3.4>, <Version 1.2.3>]>",
        )


if __name__ == "__main__":
    unittest.main()
