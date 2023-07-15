from dataclasses import dataclass, field
from typing import List, Dict

from core.post_processor import PluginPostProcessor
from core.source import PluginSource
from core.version.version import Version
from core.version.target_version import TargetVersion
from core.version.type_version import TypeVersion


@dataclass
class Plugin:
    name: str
    url: str
    source: PluginSource
    post_processors: List[PluginPostProcessor]
    target_version: List[Dict[TypeVersion, TargetVersion]] = field(default=None)

    current_version: Version = field(default=None)
    list_version: List[Version] = field(default=None)

    @staticmethod
    def unserealize(plugin_dict):
        plugin_dict["source"] = PluginSource[plugin_dict["source"].upper()].value
        plugin_dict["post_processors"] = [
            PluginPostProcessor[key.upper()].value
            for key in plugin_dict["post_processors"]
        ]

        if "target_version" in plugin_dict.keys():
            plugin_dict["target_version"] = [
                {
                    TypeVersion[key.upper()].value: TargetVersion(value)
                    if value is not None
                    else None
                    for key, value in target_version.items()
                }
                for target_version in plugin_dict["target_version"]
            ]
        return Plugin(**plugin_dict)
