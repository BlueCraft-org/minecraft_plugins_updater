class Version:
    major: int
    minor: int
    patch: int
    tuple_version: tuple

    def get_version(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __repr__(self):
        return f"<Version {self.get_version()}>"

    def __init__(self, version):
        version_part = version.split(".")
        self.major = int(version_part[0])
        self.minor = int(version_part[1])
        self.patch = int(version_part[2])

        self.tuple_version = (self.major, self.minor, self.patch)

    @staticmethod
    def __op_dif(version_a, version_b, operator):
        if version_a.major != version_b.major:
            return operator(version_a.major, version_b.major)

        elif version_a.minor != version_b.minor:
            return operator(version_a.minor, version_b.minor)

        return operator(version_a.patch, version_b.patch)

    def __eq__(self, other):
        if isinstance(other, Version):
            return (self.major, self.minor, self.patch) == (
                other.major,
                other.minor,
                other.patch,
            )
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.__op_dif(self, other, lambda a, b: a < b)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Version):
            return self.__op_dif(self, other, lambda a, b: a <= b)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return self.__op_dif(self, other, lambda a, b: a > b)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Version):
            return self.__op_dif(self, other, lambda a, b: a >= b)
        return NotImplemented
