# -*- coding: utf-8 -*-
""" Application configuration """

from dotenv import load_dotenv
import os

load_dotenv()
"""
Application description settings
"""
APP_VERSION = os.environ.get("APP_VERSION", default="1.0.0")
OWNER = os.environ.get("OWNER", default="Mike")
WEBSITE = os.environ.get("WEBSITE", default="http://test.com")
LICENSE_TYPE = os.environ.get("LICENSE_TYPE", default="MIT")
LICENSE_LINK = os.environ.get("LICENSE_LINK", default="https://github.com/")


"""
General Application Settings
"""
HOST_DOMAIN = os.environ.get("HOST_DOMAIN", default="http://github.com")
RELEASE_ENV = os.environ.get("RELEASE_ENV", default="prd")
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI", default="sqlite:///data_base/app.db"
)
SECRET_KEY = os.environ.get("", default="secret-key-change-this")

"""
Loguru settings
"""
LOGURU_BACKTRACE = False
if RELEASE_ENV.lower() == "dev":
    LOGURU_BACKTRACE = True
LOGURU_RETENTION = os.environ.get("LOGURU_RETENTION", default="10 days")
LOGURU_ROTATION = os.environ.get("LOGURU_ROTATION", default="10 MB")
