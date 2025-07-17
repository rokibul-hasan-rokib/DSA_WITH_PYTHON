from abc import ABC, abstractmethod
class PluginBase(ABC):
    @abstractmethod
    def run(self):
        pass

class MyPlugin(PluginBase):
    def run(self):
        print("Plugin running!")

def execute(plugin: PluginBase):
    plugin.run()

execute(MyPlugin())
