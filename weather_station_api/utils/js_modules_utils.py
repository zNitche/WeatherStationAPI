from flask import url_for
import os
from config import ModulesConfig


def get_lib_src(lib_name):
    lib_address = ""
    module_config = ModulesConfig.MODULES_CONFIG.get(lib_name)

    if module_config:
        if os.path.exists(module_config[ModulesConfig.MODULE_LOCAL_KEY]):
            lib_address = module_config[ModulesConfig.MODULE_LOCAL_STATIC_KEY]
            lib_address = url_for("static", filename=lib_address)

        else:
            lib_address = module_config[ModulesConfig.MODULE_CDN_KEY]

    return lib_address
