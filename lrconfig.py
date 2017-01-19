from traitlets.config.manager import BaseJSONConfigManager
path = "/Users/orecchia/anaconda/etc/jupyter/nbconfig"
cm = BaseJSONConfigManager(config_dir=path)
cm.update('livereveal', {
              'height': 200, 
              'width': 1024,
              'scroll': True,
})
