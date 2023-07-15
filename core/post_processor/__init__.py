from enum import Enum

from core.post_processor.fabricmc_post_processor import FabricMcPostProcessor
from core.post_processor.plugin_post_processor import PluginPostProcessor
from core.post_processor.versionjson_post_processor import VersionJsonPostProcessor


class PluginPostProcessor(Enum):
    PLUGIN = PluginPostProcessor
    FABRICMC = FabricMcPostProcessor
    VERSIONJSON = VersionJsonPostProcessor
