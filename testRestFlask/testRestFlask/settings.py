# -*- coding: utf-8 -*-

import os

# blueprint
from apps.testRest.views import testRest

# config
SYSTEM_CONFIG_NAME = "testRestFlask".upper() + "_CONFIG"
SYSTEM_CONFIG_PATH = "testRestFlask.configs.base.BaseConfig"

env_config = os.environ.get(SYSTEM_CONFIG_NAME)
if env_config:
    SYSTEM_CONFIG_PATH = "testRestFlask.configs." + env_config


# blueprint
SYSTEM_BLUEPRINTS = (
    #(myapp, None),
    (testRest, None),
)
