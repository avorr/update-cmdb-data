#!/usr/bin/python3
# import time

from env import portal_info
from vm_passport import PassportsVM
from os_passport import PassportsOS
from os_labels import LabelsOS

if __name__ == '__main__':
    # print('########' * 30)
    # print(portal_info)
    # print('########' * 30)
    # exit()

    all_objects = max(map(PassportsVM, portal_info))
    # from allObjects import allObjects as all_objects
    # all(map(PassportsOS, portal_info, all_objects))
    tuple(PassportsOS(foo, all_objects) for foo in portal_info)
    tuple(LabelsOS(foo, all_objects) for foo in portal_info)

    if next(iter(portal_info)) == 'PD15':
        from view_settings import visiableSetting
        visiableSetting()