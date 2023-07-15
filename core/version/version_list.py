from core.version.version import Version
from core.version.target_version import TargetVersion


class VersionList:
    version_list = []

    def __init__(self, *args):
        self.version_list = [
            version if isinstance(version, Version) else Version(version)
            for arg in args
            for version in arg
        ]
        self.version_list.sort(reverse=True)

    @staticmethod
    def filter_major(version_list, major_version):
        return filter(lambda version: version.major == major_version, version_list)

    @staticmethod
    def filter_minor(version_list, minor_version):
        return filter(lambda version: version.minor == minor_version, version_list)

    @staticmethod
    def filter_patch(version_list, patch_version):
        return filter(lambda version: version.patch == patch_version, version_list)

    def filter(self, major_version, minor_version=None, patch_version=None):
        filtered_list = self.filter_major(self.version_list, major_version)
        if minor_version is not None:
            filtered_list = self.filter_minor(filtered_list, minor_version)
        if patch_version is not None:
            filtered_list = self.filter_patch(filtered_list, patch_version)
        return list(filtered_list)

    def get_targeted_lastest_version(self, target_version: TargetVersion):
        return self.filter(*target_version.tuple_version)[0]

    def __repr__(self):
        return f"<ListVersion version_list={self.version_list}>"
