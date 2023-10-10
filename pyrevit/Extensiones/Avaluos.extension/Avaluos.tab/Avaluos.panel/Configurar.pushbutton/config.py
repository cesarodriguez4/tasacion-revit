from pyrevit import script

class Config:
    def set_config_value(self, key, value):
       # Save the value of the config 
        script.store_data(key, value)
    def get_config_value(self, key):
        # Get the value of the config
        return script.load_data(key)