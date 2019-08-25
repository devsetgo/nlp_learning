# -*- coding: utf-8 -*-
""" Starting point of the application """

"""
Load configuration settings
"""
from com_lib.logging_config import config_logging

from settings import (
    APP_VERSION,
    OWNER,
    WEBSITE,
    LICENSE_TYPE,
    LICENSE_LINK,
    HOST_DOMAIN,
    RELEASE_ENV,
    SQLALCHEMY_DATABASE_URI,
    SECRET_KEY,
    LOGURU_BACKTRACE,
    LOGURU_RETENTION,
    LOGURU_ROTATION,
)


"""
Init logging
"""
# config_logging()
# logger.info("API Logging inititated")


def main():
    thing = [
        APP_VERSION,
        OWNER,
        WEBSITE,
        LICENSE_TYPE,
        LICENSE_LINK,
        HOST_DOMAIN,
        RELEASE_ENV,
        SQLALCHEMY_DATABASE_URI,
        SECRET_KEY,
        LOGURU_BACKTRACE,
        LOGURU_RETENTION,
        LOGURU_ROTATION,
    ]
    for t in thing:
        print(t)


if __name__ == "__main__":
    main()
