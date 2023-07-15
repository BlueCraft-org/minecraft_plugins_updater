from core.plugins.plugins import Plugins


class PluginsManager:
    @staticmethod
    async def pipeline(plugin):
        pass

    @staticmethod
    async def execut(plugin_list):
        plugins = Plugins(plugin_list)
        print(plugins)
