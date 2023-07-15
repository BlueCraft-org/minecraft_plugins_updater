class TargetVersionError(Exception):
    def __init__(self, version):
        self.version = version
        super().__init__(f"TargetVersion {version} is not supported.")
