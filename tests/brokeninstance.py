# -*- coding: utf-8 -*-
class BrokenBitsharesInstance:
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, name):
        raise ValueError("Attempting to use BrokenBitsharesInstance")


class BitsharesIsolator(object):
    enabled = False

    @classmethod
    def enable(cls):
        if not cls.enabled:
            from bitshares.instance import set_shared_bitshares_instance

            broken = BrokenBitsharesInstance()
            set_shared_bitshares_instance(broken)
            cls.enabled = True
