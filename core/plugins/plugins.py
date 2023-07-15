from core.plugins.plugin import Plugin


class Plugins(list):
    def __init__(self, plugin_list):
        super().__init__(
            [Plugin.unserealize(plugin_dict) for plugin_dict in plugin_list]
        )
