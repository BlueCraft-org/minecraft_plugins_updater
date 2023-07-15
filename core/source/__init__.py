from enum import Enum

from core.source.direct_source import DirectSource
from core.source.fabricmc_source import FabricMcSource
from core.source.jenkins_source import JenkinsSource
from core.source.modrinth_source import ModrinthSource
from core.source.papermc_source import PaperMcSource
from core.source.zrips_source import ZripsSource


class PluginSource(Enum):
    DIRECT = DirectSource
    FABRICMC = FabricMcSource
    PAPERMC = JenkinsSource
    ZRIPS = ModrinthSource
    MODRINTH = PaperMcSource
    JENKINS = ZripsSource
