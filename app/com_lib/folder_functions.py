# -*- coding: utf-8 -*-
import json
import csv
import os
from typing import (
    List,
    Dict,
    Tuple,
    Sequence,
    Mapping,
    Iterable,
    TypeVar,
    Generic,
    Sized,
    Union,
    Any,
    Optional,
)
from pathlib import Path
from datetime import datetime, timedelta
import time
import random
from com_lib.logging_config import config_logging

# remove loguru and place your favorite logging mechanism
from loguru import logger

config_logging()

# Directory Path
directory_to__files: str = "data"
file_directory = f"{directory_to__files}/csv"  # /{directory}"
directory_path = Path.cwd().joinpath(file_directory)


def last_data_files_changed(directory_path):
    # print(directory_path)
    try:
        time, file_path = max((f.stat().st_mtime, f) for f in directory_path.iterdir())
        time_stamp = datetime.fromtimestamp(time)
        # print(time_stamp, file_path)
        logger.info(f"directory checked for last change: {file_directory}")
        return time_stamp, file_path
    except Exception as e:
        time_stamp = time.time()
        # log error if
        logger.error(e)
        # error: dict = {"error": f"{e}"}
        # return time_stamp, error


def get_directory_list(file_directory):
    """ getting a list of directories"""
    direct_list = []
    file_path = Path.cwd().joinpath(file_directory)
    try:
        # loop through directory
        for x in file_path.iterdir():
            # check if it is a directory
            if x.is_dir():
                # add to list
                direct_list.append(x)
        # return list of items in directory
        logger.info(f"getting a list of directories: {file_directory}")
        return direct_list
    # exception handling
    except Exception as e:
        # log error if
        logger.error(e)
        # return error information
        # error: dict = {"error": f"{e}"}
        # return error


def make_folder(file_directory):
    """ making a folder in a specific directory"""
    try:
        os.makedirs(file_directory)
        logger.info(f"directory created: at {file_directory}")
    except Exception as e:
        # log error if
        logger.error(e)
        # error: dict = {"error": f"{e}"}
        # return error


def remove_folder(file_directory):
    """ making a folder in a specific directory"""
    try:
        os.rmdir(file_directory)
        logger.info(f"direct removed: at {file_directory}")
    except Exception as e:
        # log error if
        logger.error(e)
        # error: dict = {"error": f"{e}"}
        # return error


# if __name__ == '__main__':
#     one()
