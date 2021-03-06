# Copyright 2015-2018 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import struct
from yabgp.message.attribute.linkstate.linkstate import LinkState
from yabgp.tlv import TLV

# https://tools.ietf.org/html/rfc7752#section-3.3.3.2
#  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |              Type             |             Length            |
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# //                    Route Tags (one or more)                 //
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


@LinkState.register()
class IGPRouteTagList(TLV):

    TYPE = 1153  # https://tools.ietf.org/html/rfc7752#section-3.3.3.2
    TYPE_STR = "igp_route_tag_list"

    @classmethod
    def unpack(cls, value):
        """
        """
        results = []
        while value:
            results.append(struct.unpack('!I', value[:4])[0])
            value = value[4:]
        return cls(value=results)
