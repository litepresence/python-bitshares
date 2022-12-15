# -*- coding: utf-8 -*-
from .exceptions import HtlcDoesNotExistException
from .blockchainobject import BlockchainObject


class Htlc(BlockchainObject):
    """
    Read data about an HTLC contract on the chain.

    :param str id: id of the HTLC
    :param bitshares blockchain_instance: BitShares() instance to use when
        accesing a RPC
    """

    type_id = 16

    def refresh(self):
        if data := self.blockchain.rpc.get_object(self.identifier):
            super(Htlc, self).__init__(data)
        else:
            raise HtlcDoesNotExistException(self.identifier)
