# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tfet.proto\x12\x12\x63om.groupseven.fet\"$\n\x10ReceivedResponse\x12\x10\n\x08response\x18\x01 \x01(\x08\"I\n$GetRandomSplitValueFromClientRequest\x12\x0f\n\x07\x66\x65\x61ture\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\"M\n%GetRandomSplitValueFromClientResponse\x12\x10\n\x08\x63lientId\x18\x01 \x01(\x05\x12\x12\n\nsplitValue\x18\x02 \x01(\x01\"]\n$GetAggregatedValuesFromClientRequest\x12\x0f\n\x07\x66\x65\x61ture\x18\x01 \x01(\t\x12\x10\n\x08\x63lientId\x18\x02 \x01(\x05\x12\x12\n\nsplitValue\x18\x03 \x01(\x01\"\xac\x01\n%GetAggregatedValuesFromClientResponse\x12@\n\x13\x61ggregatedValueLeft\x18\x01 \x01(\x0b\x32#.com.groupseven.fet.AggregatedValue\x12\x41\n\x14\x61ggregatedValueRight\x18\x02 \x01(\x0b\x32#.com.groupseven.fet.AggregatedValue\"=\n\x0f\x41ggregatedValue\x12\x14\n\x0c\x61pprovedLoan\x18\x01 \x01(\x05\x12\x14\n\x0c\x64\x65\x63linedLoan\x18\x02 \x01(\x05\"d\n)BroadcastTreeNodesBasedOnBestSplitRequest\x12\x0f\n\x07\x66\x65\x61ture\x18\x01 \x01(\x05\x12\x12\n\nsplitValue\x18\x02 \x01(\x01\x12\x12\n\ntreeHeight\x18\x03 \x01(\x05\x32\xdc\x03\n MasterClientCommunicationService\x12\x94\x01\n\x1dGetRandomSplitValueFromClient\x12\x38.com.groupseven.fet.GetRandomSplitValueFromClientRequest\x1a\x39.com.groupseven.fet.GetRandomSplitValueFromClientResponse\x12\x94\x01\n\x1dGetAggregatedValuesFromClient\x12\x38.com.groupseven.fet.GetAggregatedValuesFromClientRequest\x1a\x39.com.groupseven.fet.GetAggregatedValuesFromClientResponse\x12\x89\x01\n\"BroadcastTreeNodesBasedOnBestSplit\x12=.com.groupseven.fet.BroadcastTreeNodesBasedOnBestSplitRequest\x1a$.com.groupseven.fet.ReceivedResponseb\x06proto3')



_RECEIVEDRESPONSE = DESCRIPTOR.message_types_by_name['ReceivedResponse']
_GETRANDOMSPLITVALUEFROMCLIENTREQUEST = DESCRIPTOR.message_types_by_name['GetRandomSplitValueFromClientRequest']
_GETRANDOMSPLITVALUEFROMCLIENTRESPONSE = DESCRIPTOR.message_types_by_name['GetRandomSplitValueFromClientResponse']
_GETAGGREGATEDVALUESFROMCLIENTREQUEST = DESCRIPTOR.message_types_by_name['GetAggregatedValuesFromClientRequest']
_GETAGGREGATEDVALUESFROMCLIENTRESPONSE = DESCRIPTOR.message_types_by_name['GetAggregatedValuesFromClientResponse']
_AGGREGATEDVALUE = DESCRIPTOR.message_types_by_name['AggregatedValue']
_BROADCASTTREENODESBASEDONBESTSPLITREQUEST = DESCRIPTOR.message_types_by_name['BroadcastTreeNodesBasedOnBestSplitRequest']
ReceivedResponse = _reflection.GeneratedProtocolMessageType('ReceivedResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDRESPONSE,
  '__module__' : 'fet_pb2'
  # @@protoc_insertion_point(class_scope:com.groupseven.fet.ReceivedResponse)
  })
_sym_db.RegisterMessage(ReceivedResponse)

GetRandomSplitValueFromClientRequest = _reflection.GeneratedProtocolMessageType('GetRandomSplitValueFromClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRANDOMSPLITVALUEFROMCLIENTREQUEST,
  '__module__' : 'fet_pb2'
  # @@protoc_insertion_point(class_scope:com.groupseven.fet.GetRandomSplitValueFromClientRequest)
  })
_sym_db.RegisterMessage(GetRandomSplitValueFromClientRequest)

GetRandomSplitValueFromClientResponse = _reflection.GeneratedProtocolMessageType('GetRandomSplitValueFromClientResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRANDOMSPLITVALUEFROMCLIENTRESPONSE,
  '__module__' : 'fet_pb2'
  # @@protoc_insertion_point(class_scope:com.groupseven.fet.GetRandomSplitValueFromClientResponse)
  })
_sym_db.RegisterMessage(GetRandomSplitValueFromClientResponse)

GetAggregatedValuesFromClientRequest = _reflection.GeneratedProtocolMessageType('GetAggregatedValuesFromClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAGGREGATEDVALUESFROMCLIENTREQUEST,
  '__module__' : 'fet_pb2'
  # @@protoc_insertion_point(class_scope:com.groupseven.fet.GetAggregatedValuesFromClientRequest)
  })
_sym_db.RegisterMessage(GetAggregatedValuesFromClientRequest)

GetAggregatedValuesFromClientResponse = _reflection.GeneratedProtocolMessageType('GetAggregatedValuesFromClientResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAGGREGATEDVALUESFROMCLIENTRESPONSE,
  '__module__' : 'fet_pb2'
  # @@protoc_insertion_point(class_scope:com.groupseven.fet.GetAggregatedValuesFromClientResponse)
  })
_sym_db.RegisterMessage(GetAggregatedValuesFromClientResponse)

AggregatedValue = _reflection.GeneratedProtocolMessageType('AggregatedValue', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATEDVALUE,
  '__module__' : 'fet_pb2'
  # @@protoc_insertion_point(class_scope:com.groupseven.fet.AggregatedValue)
  })
_sym_db.RegisterMessage(AggregatedValue)

BroadcastTreeNodesBasedOnBestSplitRequest = _reflection.GeneratedProtocolMessageType('BroadcastTreeNodesBasedOnBestSplitRequest', (_message.Message,), {
  'DESCRIPTOR' : _BROADCASTTREENODESBASEDONBESTSPLITREQUEST,
  '__module__' : 'fet_pb2'
  # @@protoc_insertion_point(class_scope:com.groupseven.fet.BroadcastTreeNodesBasedOnBestSplitRequest)
  })
_sym_db.RegisterMessage(BroadcastTreeNodesBasedOnBestSplitRequest)

_MASTERCLIENTCOMMUNICATIONSERVICE = DESCRIPTOR.services_by_name['MasterClientCommunicationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECEIVEDRESPONSE._serialized_start=33
  _RECEIVEDRESPONSE._serialized_end=69
  _GETRANDOMSPLITVALUEFROMCLIENTREQUEST._serialized_start=71
  _GETRANDOMSPLITVALUEFROMCLIENTREQUEST._serialized_end=144
  _GETRANDOMSPLITVALUEFROMCLIENTRESPONSE._serialized_start=146
  _GETRANDOMSPLITVALUEFROMCLIENTRESPONSE._serialized_end=223
  _GETAGGREGATEDVALUESFROMCLIENTREQUEST._serialized_start=225
  _GETAGGREGATEDVALUESFROMCLIENTREQUEST._serialized_end=318
  _GETAGGREGATEDVALUESFROMCLIENTRESPONSE._serialized_start=321
  _GETAGGREGATEDVALUESFROMCLIENTRESPONSE._serialized_end=493
  _AGGREGATEDVALUE._serialized_start=495
  _AGGREGATEDVALUE._serialized_end=556
  _BROADCASTTREENODESBASEDONBESTSPLITREQUEST._serialized_start=558
  _BROADCASTTREENODESBASEDONBESTSPLITREQUEST._serialized_end=658
  _MASTERCLIENTCOMMUNICATIONSERVICE._serialized_start=661
  _MASTERCLIENTCOMMUNICATIONSERVICE._serialized_end=1137
# @@protoc_insertion_point(module_scope)
