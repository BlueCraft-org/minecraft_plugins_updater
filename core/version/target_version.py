from core.version.error import TargetVersionError


class TargetVersion:
    major: int
    minor: int
    patch: int
    tuple_version: tuple

    def get_version(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __repr__(self):
        return f"<TargetVersion {self.get_version()}>"

    def __init__(self, version):
        version_part = version.split(".")
        try:
            self.major = int(version_part[0])
        except ValueError:
            raise TargetVersionError(version)
        self.minor = None if version_part[1] == "*" else int(version_part[1])
        self.patch = None if version_part[2] == "*" else int(version_part[2])

        self.tuple_version = (self.major, self.minor, self.patch)

    def __eq__(self, other):
        if isinstance(other, TargetVersion):
            return self.tuple_version == other.tuple_version
        return False
