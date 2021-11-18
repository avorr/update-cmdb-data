#!/usr/bin/python3

from env import portal_info
from vm_passport import PassportsVM
from os_passport import PassportsOS
from view_settings import visiableSetting

if __name__ == '__main__':
    print(portal_info)
    print('######' * 100)
    all_objects = map(PassportsVM, portal_info)
    print('######' * 100)
    print(type(all_objects))
    print(len(all_objects))
    print('######' * 100)
    # all(map(PassportsOS, portal_info, all_objects))
    tuple(PassportsOS(foo, all_objects) for foo in portal_info)
    if next(iter(portal_info)) == 'PD15':
        visiableSetting()
