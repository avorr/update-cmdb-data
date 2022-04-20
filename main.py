#!/usr/bin/python3

import sys
from vm_passport import PassportsVM
from os_passport import PassportsOS
from os_labels import LabelsOS
from app_versions import gtp_app_versions
from view_settings import visible_settings


# from gtp_releases import releases

def main() -> None:
    # LabelsOS(sys.argv[1])
    # visible_settings()
    # gtp_app_versions(sys.argv[1])
    # return

    try:
        all_objects: tuple = PassportsVM(sys.argv[1])
    except EOFError as error:
        print(error)
    exit()

    try:
        PassportsOS(sys.argv[1], all_objects)
    except EOFError as error:
        print(error)

    try:
        LabelsOS(sys.argv[1])
    except EOFError as error:
        # except:
        #     pass
        print(error)

    if sys.argv[1] in ('PD15', 'PD20'):
        gtp_app_versions(sys.argv[1])
    # releases()
    # gtp_app_versions(sys.argv[1])

    visible_settings()


if __name__ == '__main__':
    main()
    # if 0 != 5:
    # raise TypeError("Type not serializable")
    # raise EOFError("asasa")
