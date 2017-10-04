#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: Hive
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class AdjacencyType:
  CONJUNCTIVE = 0
  DISJUNCTIVE = 1

  _VALUES_TO_NAMES = {
    0: "CONJUNCTIVE",
    1: "DISJUNCTIVE",
  }

  _NAMES_TO_VALUES = {
    "CONJUNCTIVE": 0,
    "DISJUNCTIVE": 1,
  }

class NodeType:
  OPERATOR = 0
  STAGE = 1

  _VALUES_TO_NAMES = {
    0: "OPERATOR",
    1: "STAGE",
  }

  _NAMES_TO_VALUES = {
    "OPERATOR": 0,
    "STAGE": 1,
  }

class OperatorType:
  JOIN = 0
  MAPJOIN = 1
  EXTRACT = 2
  FILTER = 3
  FORWARD = 4
  GROUPBY = 5
  LIMIT = 6
  SCRIPT = 7
  SELECT = 8
  TABLESCAN = 9
  FILESINK = 10
  REDUCESINK = 11
  UNION = 12
  UDTF = 13
  LATERALVIEWJOIN = 14
  LATERALVIEWFORWARD = 15
  HASHTABLESINK = 16
  HASHTABLEDUMMY = 17
  PTF = 18
  MUX = 19
  DEMUX = 20
  EVENT = 21
  ORCFILEMERGE = 22
  RCFILEMERGE = 23
  MERGEJOIN = 24

  _VALUES_TO_NAMES = {
    0: "JOIN",
    1: "MAPJOIN",
    2: "EXTRACT",
    3: "FILTER",
    4: "FORWARD",
    5: "GROUPBY",
    6: "LIMIT",
    7: "SCRIPT",
    8: "SELECT",
    9: "TABLESCAN",
    10: "FILESINK",
    11: "REDUCESINK",
    12: "UNION",
    13: "UDTF",
    14: "LATERALVIEWJOIN",
    15: "LATERALVIEWFORWARD",
    16: "HASHTABLESINK",
    17: "HASHTABLEDUMMY",
    18: "PTF",
    19: "MUX",
    20: "DEMUX",
    21: "EVENT",
    22: "ORCFILEMERGE",
    23: "RCFILEMERGE",
    24: "MERGEJOIN",
  }

  _NAMES_TO_VALUES = {
    "JOIN": 0,
    "MAPJOIN": 1,
    "EXTRACT": 2,
    "FILTER": 3,
    "FORWARD": 4,
    "GROUPBY": 5,
    "LIMIT": 6,
    "SCRIPT": 7,
    "SELECT": 8,
    "TABLESCAN": 9,
    "FILESINK": 10,
    "REDUCESINK": 11,
    "UNION": 12,
    "UDTF": 13,
    "LATERALVIEWJOIN": 14,
    "LATERALVIEWFORWARD": 15,
    "HASHTABLESINK": 16,
    "HASHTABLEDUMMY": 17,
    "PTF": 18,
    "MUX": 19,
    "DEMUX": 20,
    "EVENT": 21,
    "ORCFILEMERGE": 22,
    "RCFILEMERGE": 23,
    "MERGEJOIN": 24,
  }

class TaskType:
  MAP = 0
  REDUCE = 1
  OTHER = 2

  _VALUES_TO_NAMES = {
    0: "MAP",
    1: "REDUCE",
    2: "OTHER",
  }

  _NAMES_TO_VALUES = {
    "MAP": 0,
    "REDUCE": 1,
    "OTHER": 2,
  }

class StageType:
  CONDITIONAL = 0
  COPY = 1
  DDL = 2
  MAPRED = 3
  EXPLAIN = 4
  FETCH = 5
  FUNC = 6
  MAPREDLOCAL = 7
  MOVE = 8
  STATS = 9
  DEPENDENCY_COLLECTION = 10
  COLUMNSTATS = 11

  _VALUES_TO_NAMES = {
    0: "CONDITIONAL",
    1: "COPY",
    2: "DDL",
    3: "MAPRED",
    4: "EXPLAIN",
    5: "FETCH",
    6: "FUNC",
    7: "MAPREDLOCAL",
    8: "MOVE",
    9: "STATS",
    10: "DEPENDENCY_COLLECTION",
    11: "COLUMNSTATS",
  }

  _NAMES_TO_VALUES = {
    "CONDITIONAL": 0,
    "COPY": 1,
    "DDL": 2,
    "MAPRED": 3,
    "EXPLAIN": 4,
    "FETCH": 5,
    "FUNC": 6,
    "MAPREDLOCAL": 7,
    "MOVE": 8,
    "STATS": 9,
    "DEPENDENCY_COLLECTION": 10,
    "COLUMNSTATS": 11,
  }


class Adjacency:
  """
  Attributes:
   - node
   - children
   - adjacencyType
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'node', None, None, ), # 1
    (2, TType.LIST, 'children', (TType.STRING,None), None, ), # 2
    (3, TType.I32, 'adjacencyType', None, None, ), # 3
  )

  def __init__(self, node=None, children=None, adjacencyType=None,):
    self.node = node
    self.children = children
    self.adjacencyType = adjacencyType

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.node = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.children = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.children.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.adjacencyType = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Adjacency')
    if self.node is not None:
      oprot.writeFieldBegin('node', TType.STRING, 1)
      oprot.writeString(self.node)
      oprot.writeFieldEnd()
    if self.children is not None:
      oprot.writeFieldBegin('children', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.children))
      for iter6 in self.children:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.adjacencyType is not None:
      oprot.writeFieldBegin('adjacencyType', TType.I32, 3)
      oprot.writeI32(self.adjacencyType)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Graph:
  """
  Attributes:
   - nodeType
   - roots
   - adjacencyList
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'nodeType', None, None, ), # 1
    (2, TType.LIST, 'roots', (TType.STRING,None), None, ), # 2
    (3, TType.LIST, 'adjacencyList', (TType.STRUCT,(Adjacency, Adjacency.thrift_spec)), None, ), # 3
  )

  def __init__(self, nodeType=None, roots=None, adjacencyList=None,):
    self.nodeType = nodeType
    self.roots = roots
    self.adjacencyList = adjacencyList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.nodeType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.roots = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readString();
            self.roots.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.adjacencyList = []
          (_etype16, _size13) = iprot.readListBegin()
          for _i17 in xrange(_size13):
            _elem18 = Adjacency()
            _elem18.read(iprot)
            self.adjacencyList.append(_elem18)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Graph')
    if self.nodeType is not None:
      oprot.writeFieldBegin('nodeType', TType.I32, 1)
      oprot.writeI32(self.nodeType)
      oprot.writeFieldEnd()
    if self.roots is not None:
      oprot.writeFieldBegin('roots', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.roots))
      for iter19 in self.roots:
        oprot.writeString(iter19)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.adjacencyList is not None:
      oprot.writeFieldBegin('adjacencyList', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.adjacencyList))
      for iter20 in self.adjacencyList:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Operator:
  """
  Attributes:
   - operatorId
   - operatorType
   - operatorAttributes
   - operatorCounters
   - done
   - started
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'operatorId', None, None, ), # 1
    (2, TType.I32, 'operatorType', None, None, ), # 2
    (3, TType.MAP, 'operatorAttributes', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.MAP, 'operatorCounters', (TType.STRING,None,TType.I64,None), None, ), # 4
    (5, TType.BOOL, 'done', None, None, ), # 5
    (6, TType.BOOL, 'started', None, None, ), # 6
  )

  def __init__(self, operatorId=None, operatorType=None, operatorAttributes=None, operatorCounters=None, done=None, started=None,):
    self.operatorId = operatorId
    self.operatorType = operatorType
    self.operatorAttributes = operatorAttributes
    self.operatorCounters = operatorCounters
    self.done = done
    self.started = started

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.operatorId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.operatorType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.operatorAttributes = {}
          (_ktype22, _vtype23, _size21 ) = iprot.readMapBegin() 
          for _i25 in xrange(_size21):
            _key26 = iprot.readString();
            _val27 = iprot.readString();
            self.operatorAttributes[_key26] = _val27
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.operatorCounters = {}
          (_ktype29, _vtype30, _size28 ) = iprot.readMapBegin() 
          for _i32 in xrange(_size28):
            _key33 = iprot.readString();
            _val34 = iprot.readI64();
            self.operatorCounters[_key33] = _val34
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.done = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.started = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Operator')
    if self.operatorId is not None:
      oprot.writeFieldBegin('operatorId', TType.STRING, 1)
      oprot.writeString(self.operatorId)
      oprot.writeFieldEnd()
    if self.operatorType is not None:
      oprot.writeFieldBegin('operatorType', TType.I32, 2)
      oprot.writeI32(self.operatorType)
      oprot.writeFieldEnd()
    if self.operatorAttributes is not None:
      oprot.writeFieldBegin('operatorAttributes', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.operatorAttributes))
      for kiter35,viter36 in self.operatorAttributes.items():
        oprot.writeString(kiter35)
        oprot.writeString(viter36)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.operatorCounters is not None:
      oprot.writeFieldBegin('operatorCounters', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.I64, len(self.operatorCounters))
      for kiter37,viter38 in self.operatorCounters.items():
        oprot.writeString(kiter37)
        oprot.writeI64(viter38)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.done is not None:
      oprot.writeFieldBegin('done', TType.BOOL, 5)
      oprot.writeBool(self.done)
      oprot.writeFieldEnd()
    if self.started is not None:
      oprot.writeFieldBegin('started', TType.BOOL, 6)
      oprot.writeBool(self.started)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Task:
  """
  Attributes:
   - taskId
   - taskType
   - taskAttributes
   - taskCounters
   - operatorGraph
   - operatorList
   - done
   - started
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'taskId', None, None, ), # 1
    (2, TType.I32, 'taskType', None, None, ), # 2
    (3, TType.MAP, 'taskAttributes', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.MAP, 'taskCounters', (TType.STRING,None,TType.I64,None), None, ), # 4
    (5, TType.STRUCT, 'operatorGraph', (Graph, Graph.thrift_spec), None, ), # 5
    (6, TType.LIST, 'operatorList', (TType.STRUCT,(Operator, Operator.thrift_spec)), None, ), # 6
    (7, TType.BOOL, 'done', None, None, ), # 7
    (8, TType.BOOL, 'started', None, None, ), # 8
  )

  def __init__(self, taskId=None, taskType=None, taskAttributes=None, taskCounters=None, operatorGraph=None, operatorList=None, done=None, started=None,):
    self.taskId = taskId
    self.taskType = taskType
    self.taskAttributes = taskAttributes
    self.taskCounters = taskCounters
    self.operatorGraph = operatorGraph
    self.operatorList = operatorList
    self.done = done
    self.started = started

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.taskId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.taskType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.taskAttributes = {}
          (_ktype40, _vtype41, _size39 ) = iprot.readMapBegin() 
          for _i43 in xrange(_size39):
            _key44 = iprot.readString();
            _val45 = iprot.readString();
            self.taskAttributes[_key44] = _val45
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.taskCounters = {}
          (_ktype47, _vtype48, _size46 ) = iprot.readMapBegin() 
          for _i50 in xrange(_size46):
            _key51 = iprot.readString();
            _val52 = iprot.readI64();
            self.taskCounters[_key51] = _val52
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.operatorGraph = Graph()
          self.operatorGraph.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.operatorList = []
          (_etype56, _size53) = iprot.readListBegin()
          for _i57 in xrange(_size53):
            _elem58 = Operator()
            _elem58.read(iprot)
            self.operatorList.append(_elem58)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.done = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.started = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Task')
    if self.taskId is not None:
      oprot.writeFieldBegin('taskId', TType.STRING, 1)
      oprot.writeString(self.taskId)
      oprot.writeFieldEnd()
    if self.taskType is not None:
      oprot.writeFieldBegin('taskType', TType.I32, 2)
      oprot.writeI32(self.taskType)
      oprot.writeFieldEnd()
    if self.taskAttributes is not None:
      oprot.writeFieldBegin('taskAttributes', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.taskAttributes))
      for kiter59,viter60 in self.taskAttributes.items():
        oprot.writeString(kiter59)
        oprot.writeString(viter60)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.taskCounters is not None:
      oprot.writeFieldBegin('taskCounters', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.I64, len(self.taskCounters))
      for kiter61,viter62 in self.taskCounters.items():
        oprot.writeString(kiter61)
        oprot.writeI64(viter62)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.operatorGraph is not None:
      oprot.writeFieldBegin('operatorGraph', TType.STRUCT, 5)
      self.operatorGraph.write(oprot)
      oprot.writeFieldEnd()
    if self.operatorList is not None:
      oprot.writeFieldBegin('operatorList', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.operatorList))
      for iter63 in self.operatorList:
        iter63.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.done is not None:
      oprot.writeFieldBegin('done', TType.BOOL, 7)
      oprot.writeBool(self.done)
      oprot.writeFieldEnd()
    if self.started is not None:
      oprot.writeFieldBegin('started', TType.BOOL, 8)
      oprot.writeBool(self.started)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Stage:
  """
  Attributes:
   - stageId
   - stageType
   - stageAttributes
   - stageCounters
   - taskList
   - done
   - started
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'stageId', None, None, ), # 1
    (2, TType.I32, 'stageType', None, None, ), # 2
    (3, TType.MAP, 'stageAttributes', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.MAP, 'stageCounters', (TType.STRING,None,TType.I64,None), None, ), # 4
    (5, TType.LIST, 'taskList', (TType.STRUCT,(Task, Task.thrift_spec)), None, ), # 5
    (6, TType.BOOL, 'done', None, None, ), # 6
    (7, TType.BOOL, 'started', None, None, ), # 7
  )

  def __init__(self, stageId=None, stageType=None, stageAttributes=None, stageCounters=None, taskList=None, done=None, started=None,):
    self.stageId = stageId
    self.stageType = stageType
    self.stageAttributes = stageAttributes
    self.stageCounters = stageCounters
    self.taskList = taskList
    self.done = done
    self.started = started

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.stageId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.stageType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.stageAttributes = {}
          (_ktype65, _vtype66, _size64 ) = iprot.readMapBegin() 
          for _i68 in xrange(_size64):
            _key69 = iprot.readString();
            _val70 = iprot.readString();
            self.stageAttributes[_key69] = _val70
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.stageCounters = {}
          (_ktype72, _vtype73, _size71 ) = iprot.readMapBegin() 
          for _i75 in xrange(_size71):
            _key76 = iprot.readString();
            _val77 = iprot.readI64();
            self.stageCounters[_key76] = _val77
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.taskList = []
          (_etype81, _size78) = iprot.readListBegin()
          for _i82 in xrange(_size78):
            _elem83 = Task()
            _elem83.read(iprot)
            self.taskList.append(_elem83)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.done = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.started = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Stage')
    if self.stageId is not None:
      oprot.writeFieldBegin('stageId', TType.STRING, 1)
      oprot.writeString(self.stageId)
      oprot.writeFieldEnd()
    if self.stageType is not None:
      oprot.writeFieldBegin('stageType', TType.I32, 2)
      oprot.writeI32(self.stageType)
      oprot.writeFieldEnd()
    if self.stageAttributes is not None:
      oprot.writeFieldBegin('stageAttributes', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.stageAttributes))
      for kiter84,viter85 in self.stageAttributes.items():
        oprot.writeString(kiter84)
        oprot.writeString(viter85)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.stageCounters is not None:
      oprot.writeFieldBegin('stageCounters', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.I64, len(self.stageCounters))
      for kiter86,viter87 in self.stageCounters.items():
        oprot.writeString(kiter86)
        oprot.writeI64(viter87)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.taskList is not None:
      oprot.writeFieldBegin('taskList', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.taskList))
      for iter88 in self.taskList:
        iter88.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.done is not None:
      oprot.writeFieldBegin('done', TType.BOOL, 6)
      oprot.writeBool(self.done)
      oprot.writeFieldEnd()
    if self.started is not None:
      oprot.writeFieldBegin('started', TType.BOOL, 7)
      oprot.writeBool(self.started)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Query:
  """
  Attributes:
   - queryId
   - queryType
   - queryAttributes
   - queryCounters
   - stageGraph
   - stageList
   - done
   - started
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'queryId', None, None, ), # 1
    (2, TType.STRING, 'queryType', None, None, ), # 2
    (3, TType.MAP, 'queryAttributes', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.MAP, 'queryCounters', (TType.STRING,None,TType.I64,None), None, ), # 4
    (5, TType.STRUCT, 'stageGraph', (Graph, Graph.thrift_spec), None, ), # 5
    (6, TType.LIST, 'stageList', (TType.STRUCT,(Stage, Stage.thrift_spec)), None, ), # 6
    (7, TType.BOOL, 'done', None, None, ), # 7
    (8, TType.BOOL, 'started', None, None, ), # 8
  )

  def __init__(self, queryId=None, queryType=None, queryAttributes=None, queryCounters=None, stageGraph=None, stageList=None, done=None, started=None,):
    self.queryId = queryId
    self.queryType = queryType
    self.queryAttributes = queryAttributes
    self.queryCounters = queryCounters
    self.stageGraph = stageGraph
    self.stageList = stageList
    self.done = done
    self.started = started

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.queryId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.queryType = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.queryAttributes = {}
          (_ktype90, _vtype91, _size89 ) = iprot.readMapBegin() 
          for _i93 in xrange(_size89):
            _key94 = iprot.readString();
            _val95 = iprot.readString();
            self.queryAttributes[_key94] = _val95
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.queryCounters = {}
          (_ktype97, _vtype98, _size96 ) = iprot.readMapBegin() 
          for _i100 in xrange(_size96):
            _key101 = iprot.readString();
            _val102 = iprot.readI64();
            self.queryCounters[_key101] = _val102
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.stageGraph = Graph()
          self.stageGraph.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.stageList = []
          (_etype106, _size103) = iprot.readListBegin()
          for _i107 in xrange(_size103):
            _elem108 = Stage()
            _elem108.read(iprot)
            self.stageList.append(_elem108)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.done = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.started = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Query')
    if self.queryId is not None:
      oprot.writeFieldBegin('queryId', TType.STRING, 1)
      oprot.writeString(self.queryId)
      oprot.writeFieldEnd()
    if self.queryType is not None:
      oprot.writeFieldBegin('queryType', TType.STRING, 2)
      oprot.writeString(self.queryType)
      oprot.writeFieldEnd()
    if self.queryAttributes is not None:
      oprot.writeFieldBegin('queryAttributes', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.queryAttributes))
      for kiter109,viter110 in self.queryAttributes.items():
        oprot.writeString(kiter109)
        oprot.writeString(viter110)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.queryCounters is not None:
      oprot.writeFieldBegin('queryCounters', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.I64, len(self.queryCounters))
      for kiter111,viter112 in self.queryCounters.items():
        oprot.writeString(kiter111)
        oprot.writeI64(viter112)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.stageGraph is not None:
      oprot.writeFieldBegin('stageGraph', TType.STRUCT, 5)
      self.stageGraph.write(oprot)
      oprot.writeFieldEnd()
    if self.stageList is not None:
      oprot.writeFieldBegin('stageList', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.stageList))
      for iter113 in self.stageList:
        iter113.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.done is not None:
      oprot.writeFieldBegin('done', TType.BOOL, 7)
      oprot.writeBool(self.done)
      oprot.writeFieldEnd()
    if self.started is not None:
      oprot.writeFieldBegin('started', TType.BOOL, 8)
      oprot.writeBool(self.started)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryPlan:
  """
  Attributes:
   - queries
   - done
   - started
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'queries', (TType.STRUCT,(Query, Query.thrift_spec)), None, ), # 1
    (2, TType.BOOL, 'done', None, None, ), # 2
    (3, TType.BOOL, 'started', None, None, ), # 3
  )

  def __init__(self, queries=None, done=None, started=None,):
    self.queries = queries
    self.done = done
    self.started = started

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.queries = []
          (_etype117, _size114) = iprot.readListBegin()
          for _i118 in xrange(_size114):
            _elem119 = Query()
            _elem119.read(iprot)
            self.queries.append(_elem119)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.done = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.started = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QueryPlan')
    if self.queries is not None:
      oprot.writeFieldBegin('queries', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.queries))
      for iter120 in self.queries:
        iter120.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.done is not None:
      oprot.writeFieldBegin('done', TType.BOOL, 2)
      oprot.writeBool(self.done)
      oprot.writeFieldEnd()
    if self.started is not None:
      oprot.writeFieldBegin('started', TType.BOOL, 3)
      oprot.writeBool(self.started)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
