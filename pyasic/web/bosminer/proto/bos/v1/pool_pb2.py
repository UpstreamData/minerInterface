# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bos/v1/pool.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...bos.v1 import common_pb2 as bos_dot_v1_dot_common__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11\x62os/v1/pool.proto\x12\x0e\x62raiins.bos.v1\x1a\x13\x62os/v1/common.proto"\x16\n\x05Quota\x12\r\n\x05value\x18\x01 \x01(\r" \n\x0f\x46ixedShareRatio\x12\r\n\x05value\x18\x01 \x01(\x01"\xe4\x01\n\x16PoolGroupConfiguration\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\x05quota\x18\x03 \x01(\x0b\x32\x15.braiins.bos.v1.QuotaH\x00\x12<\n\x11\x66ixed_share_ratio\x18\x04 \x01(\x0b\x32\x1f.braiins.bos.v1.FixedShareRatioH\x00\x12\x30\n\x05pools\x18\x05 \x03(\x0b\x32!.braiins.bos.v1.PoolConfigurationB\x17\n\x15load_balance_strategy"\x81\x01\n\x11PoolConfiguration\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x15\n\x08password\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07\x65nabled\x18\x05 \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_passwordB\n\n\x08_enabled"\xb0\x01\n\tPoolGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x05quota\x18\x02 \x01(\x0b\x32\x15.braiins.bos.v1.QuotaH\x00\x12<\n\x11\x66ixed_share_ratio\x18\x03 \x01(\x0b\x32\x1f.braiins.bos.v1.FixedShareRatioH\x00\x12#\n\x05pools\x18\x04 \x03(\x0b\x32\x14.braiins.bos.v1.PoolB\n\n\x08strategy"\x88\x01\n\x04Pool\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\r\n\x05\x61live\x18\x05 \x01(\x08\x12\x0e\n\x06\x61\x63tive\x18\x06 \x01(\x08\x12(\n\x05stats\x18\x07 \x01(\x0b\x32\x19.braiins.bos.v1.PoolStats"\x98\x01\n\tPoolStats\x12\x17\n\x0f\x61\x63\x63\x65pted_shares\x18\x01 \x01(\x04\x12\x17\n\x0frejected_shares\x18\x02 \x01(\x04\x12\x14\n\x0cstale_shares\x18\x03 \x01(\x04\x12\x17\n\x0flast_difficulty\x18\x04 \x01(\x04\x12\x12\n\nbest_share\x18\x05 \x01(\x04\x12\x16\n\x0egenerated_work\x18\x06 \x01(\x04"\x16\n\x14GetPoolGroupsRequest"G\n\x15GetPoolGroupsResponse\x12.\n\x0bpool_groups\x18\x01 \x03(\x0b\x32\x19.braiins.bos.v1.PoolGroup"\x80\x01\n\x16\x43reatePoolGroupRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x35\n\x05group\x18\x02 \x01(\x0b\x32&.braiins.bos.v1.PoolGroupConfiguration"P\n\x17\x43reatePoolGroupResponse\x12\x35\n\x05group\x18\x01 \x01(\x0b\x32&.braiins.bos.v1.PoolGroupConfiguration"\x80\x01\n\x16UpdatePoolGroupRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x35\n\x05group\x18\x02 \x01(\x0b\x32&.braiins.bos.v1.PoolGroupConfiguration"P\n\x17UpdatePoolGroupResponse\x12\x35\n\x05group\x18\x01 \x01(\x0b\x32&.braiins.bos.v1.PoolGroupConfiguration"V\n\x16RemovePoolGroupRequest\x12/\n\x0bsave_action\x18\x01 \x01(\x0e\x32\x1a.braiins.bos.v1.SaveAction\x12\x0b\n\x03uid\x18\x02 \x01(\t"\x19\n\x17RemovePoolGroupResponse2\x97\x03\n\x0bPoolService\x12\\\n\rGetPoolGroups\x12$.braiins.bos.v1.GetPoolGroupsRequest\x1a%.braiins.bos.v1.GetPoolGroupsResponse\x12\x62\n\x0f\x43reatePoolGroup\x12&.braiins.bos.v1.CreatePoolGroupRequest\x1a\'.braiins.bos.v1.CreatePoolGroupResponse\x12\x62\n\x0fUpdatePoolGroup\x12&.braiins.bos.v1.UpdatePoolGroupRequest\x1a\'.braiins.bos.v1.UpdatePoolGroupResponse\x12\x62\n\x0fRemovePoolGroup\x12&.braiins.bos.v1.RemovePoolGroupRequest\x1a\'.braiins.bos.v1.RemovePoolGroupResponseb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "bos.v1.pool_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_QUOTA"]._serialized_start = 58
    _globals["_QUOTA"]._serialized_end = 80
    _globals["_FIXEDSHARERATIO"]._serialized_start = 82
    _globals["_FIXEDSHARERATIO"]._serialized_end = 114
    _globals["_POOLGROUPCONFIGURATION"]._serialized_start = 117
    _globals["_POOLGROUPCONFIGURATION"]._serialized_end = 345
    _globals["_POOLCONFIGURATION"]._serialized_start = 348
    _globals["_POOLCONFIGURATION"]._serialized_end = 477
    _globals["_POOLGROUP"]._serialized_start = 480
    _globals["_POOLGROUP"]._serialized_end = 656
    _globals["_POOL"]._serialized_start = 659
    _globals["_POOL"]._serialized_end = 795
    _globals["_POOLSTATS"]._serialized_start = 798
    _globals["_POOLSTATS"]._serialized_end = 950
    _globals["_GETPOOLGROUPSREQUEST"]._serialized_start = 952
    _globals["_GETPOOLGROUPSREQUEST"]._serialized_end = 974
    _globals["_GETPOOLGROUPSRESPONSE"]._serialized_start = 976
    _globals["_GETPOOLGROUPSRESPONSE"]._serialized_end = 1047
    _globals["_CREATEPOOLGROUPREQUEST"]._serialized_start = 1050
    _globals["_CREATEPOOLGROUPREQUEST"]._serialized_end = 1178
    _globals["_CREATEPOOLGROUPRESPONSE"]._serialized_start = 1180
    _globals["_CREATEPOOLGROUPRESPONSE"]._serialized_end = 1260
    _globals["_UPDATEPOOLGROUPREQUEST"]._serialized_start = 1263
    _globals["_UPDATEPOOLGROUPREQUEST"]._serialized_end = 1391
    _globals["_UPDATEPOOLGROUPRESPONSE"]._serialized_start = 1393
    _globals["_UPDATEPOOLGROUPRESPONSE"]._serialized_end = 1473
    _globals["_REMOVEPOOLGROUPREQUEST"]._serialized_start = 1475
    _globals["_REMOVEPOOLGROUPREQUEST"]._serialized_end = 1561
    _globals["_REMOVEPOOLGROUPRESPONSE"]._serialized_start = 1563
    _globals["_REMOVEPOOLGROUPRESPONSE"]._serialized_end = 1588
    _globals["_POOLSERVICE"]._serialized_start = 1591
    _globals["_POOLSERVICE"]._serialized_end = 1998
# @@protoc_insertion_point(module_scope)