import unittest

from core.post_processor import PluginPostProcessor
from core.source import PluginSource
from core.version.target_version import TargetVersion
from core.version.type_version import TypeVersion
from core.plugins.plugin import Plugin


class TestPlugin(unittest.TestCase):
    def test_unserealize(self):
        plugin_dict = {
            "name": "PluginTest",
            "target_version": [{"minecraft": "1.19.4", "plugin": None}],
            "url": "https://plugin/test",
            "source": "direct",
            "post_processors": ["versionjson"],
        }
        plugin = Plugin.unserealize(plugin_dict)
        self.assertEqual(plugin.name, "PluginTest")
        self.assertEqual(plugin.url, "https://plugin/test")
        self.assertEqual(plugin.source, PluginSource.DIRECT.value)
        self.assertEqual(
            plugin.post_processors, [PluginPostProcessor.VERSIONJSON.value]
        )
        print(plugin.target_version)
        self.assertEqual(
            plugin.target_version,
            [
                {
                    TypeVersion.MINECRAFT.value: TargetVersion("1.19.4"),
                    TypeVersion.PLUGIN.value: None,
                }
            ],
        )


if __name__ == "__main__":
    unittest.main()
