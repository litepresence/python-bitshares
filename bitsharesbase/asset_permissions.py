# -*- coding: utf-8 -*-
asset_permissions = {
    "charge_market_fee": 1,
    "white_list": 2,
    "override_authority": 4,
    "transfer_restricted": 8,
    "disable_force_settle": 16,
    "global_settle": 32,
    "disable_confidential": 64,
    "witness_fed_asset": 128,
    "committee_fed_asset": 256,
}
whitelist = {
    "no_listing": 0,
    "white_listed": 1,
    "black_listed": 2,
    "white_and_black_listed": 0x1 | 0x2,
}


def toint(permissions):
    permissions_int = 0
    for p in permissions:
        if permissions[p]:
            permissions_int |= asset_permissions[p]
    return permissions_int


def todict(number):
    return {k: bool(number & v) for k, v in asset_permissions.items()}


def force_flag(perms, flags):
    for p in flags:
        if flags[p]:
            perms |= asset_permissions[p]
    return perms


def test_permissions(perms, flags):
    for p in flags:
        if not asset_permissions[p] & perms:
            raise Exception(f"Permissions prevent you from changing {p}!")
    return True
