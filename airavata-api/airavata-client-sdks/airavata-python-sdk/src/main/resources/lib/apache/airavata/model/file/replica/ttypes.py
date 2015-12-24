#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import apache.airavata.model.data.movement.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class FileModelType:
  FILE = 0
  DIRECTORY = 1

  _VALUES_TO_NAMES = {
    0: "FILE",
    1: "DIRECTORY",
  }

  _NAMES_TO_VALUES = {
    "FILE": 0,
    "DIRECTORY": 1,
  }

class StorageResourceType:
  GATEWAY_DATA_STORE = 0
  BACKUP_GATEWAY_DATA_STORE = 1
  COMPUTE_RESOURCE = 2
  LONG_TERM_STORAGE_RESOURCE = 3
  OTHER = 4

  _VALUES_TO_NAMES = {
    0: "GATEWAY_DATA_STORE",
    1: "BACKUP_GATEWAY_DATA_STORE",
    2: "COMPUTE_RESOURCE",
    3: "LONG_TERM_STORAGE_RESOURCE",
    4: "OTHER",
  }

  _NAMES_TO_VALUES = {
    "GATEWAY_DATA_STORE": 0,
    "BACKUP_GATEWAY_DATA_STORE": 1,
    "COMPUTE_RESOURCE": 2,
    "LONG_TERM_STORAGE_RESOURCE": 3,
    "OTHER": 4,
  }

class ReplicaPersistentType:
  TRANSIENT = 0
  PERSISTENT = 1

  _VALUES_TO_NAMES = {
    0: "TRANSIENT",
    1: "PERSISTENT",
  }

  _NAMES_TO_VALUES = {
    "TRANSIENT": 0,
    "PERSISTENT": 1,
  }


class FileCollectionModel:
  """
  Attributes:
   - collectionId
   - gatewayId
   - username
   - sharedUsers
   - sharedPublic
   - collectionName
   - collectionDescription
   - fileIdList
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'collectionId', None, None, ), # 1
    (2, TType.STRING, 'gatewayId', None, None, ), # 2
    (3, TType.STRING, 'username', None, None, ), # 3
    (4, TType.LIST, 'sharedUsers', (TType.STRING,None), None, ), # 4
    (5, TType.BOOL, 'sharedPublic', None, None, ), # 5
    (6, TType.STRING, 'collectionName', None, None, ), # 6
    (7, TType.STRING, 'collectionDescription', None, None, ), # 7
    (8, TType.LIST, 'fileIdList', (TType.STRING,None), None, ), # 8
  )

  def __init__(self, collectionId=None, gatewayId=None, username=None, sharedUsers=None, sharedPublic=None, collectionName=None, collectionDescription=None, fileIdList=None,):
    self.collectionId = collectionId
    self.gatewayId = gatewayId
    self.username = username
    self.sharedUsers = sharedUsers
    self.sharedPublic = sharedPublic
    self.collectionName = collectionName
    self.collectionDescription = collectionDescription
    self.fileIdList = fileIdList

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
          self.collectionId = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.gatewayId = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.username = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.sharedUsers = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString()
            self.sharedUsers.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.sharedPublic = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.collectionName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.collectionDescription = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.fileIdList = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readString()
            self.fileIdList.append(_elem11)
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
    oprot.writeStructBegin('FileCollectionModel')
    if self.collectionId is not None:
      oprot.writeFieldBegin('collectionId', TType.STRING, 1)
      oprot.writeString(self.collectionId)
      oprot.writeFieldEnd()
    if self.gatewayId is not None:
      oprot.writeFieldBegin('gatewayId', TType.STRING, 2)
      oprot.writeString(self.gatewayId)
      oprot.writeFieldEnd()
    if self.username is not None:
      oprot.writeFieldBegin('username', TType.STRING, 3)
      oprot.writeString(self.username)
      oprot.writeFieldEnd()
    if self.sharedUsers is not None:
      oprot.writeFieldBegin('sharedUsers', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.sharedUsers))
      for iter12 in self.sharedUsers:
        oprot.writeString(iter12)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.sharedPublic is not None:
      oprot.writeFieldBegin('sharedPublic', TType.BOOL, 5)
      oprot.writeBool(self.sharedPublic)
      oprot.writeFieldEnd()
    if self.collectionName is not None:
      oprot.writeFieldBegin('collectionName', TType.STRING, 6)
      oprot.writeString(self.collectionName)
      oprot.writeFieldEnd()
    if self.collectionDescription is not None:
      oprot.writeFieldBegin('collectionDescription', TType.STRING, 7)
      oprot.writeString(self.collectionDescription)
      oprot.writeFieldEnd()
    if self.fileIdList is not None:
      oprot.writeFieldBegin('fileIdList', TType.LIST, 8)
      oprot.writeListBegin(TType.STRING, len(self.fileIdList))
      for iter13 in self.fileIdList:
        oprot.writeString(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.collectionId)
    value = (value * 31) ^ hash(self.gatewayId)
    value = (value * 31) ^ hash(self.username)
    value = (value * 31) ^ hash(self.sharedUsers)
    value = (value * 31) ^ hash(self.sharedPublic)
    value = (value * 31) ^ hash(self.collectionName)
    value = (value * 31) ^ hash(self.collectionDescription)
    value = (value * 31) ^ hash(self.fileIdList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class FileModel:
  """
  Attributes:
   - fileId
   - gatewayId
   - username
   - sharedUsers
   - sharedPublic
   - fileName
   - fileDescription
   - sha256Checksum
   - fileType
   - fileSize
   - dataType
   - creationTime
   - lastModifiedTime
   - fileReplicas
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'fileId', None, None, ), # 1
    (2, TType.STRING, 'gatewayId', None, None, ), # 2
    (3, TType.STRING, 'username', None, None, ), # 3
    (4, TType.LIST, 'sharedUsers', (TType.STRING,None), None, ), # 4
    (5, TType.BOOL, 'sharedPublic', None, None, ), # 5
    (6, TType.STRING, 'fileName', None, None, ), # 6
    (7, TType.STRING, 'fileDescription', None, None, ), # 7
    (8, TType.STRING, 'sha256Checksum', None, None, ), # 8
    (9, TType.I32, 'fileType', None, None, ), # 9
    (10, TType.I32, 'fileSize', None, None, ), # 10
    (11, TType.STRING, 'dataType', None, None, ), # 11
    (12, TType.I64, 'creationTime', None, None, ), # 12
    (13, TType.I64, 'lastModifiedTime', None, None, ), # 13
    (14, TType.LIST, 'fileReplicas', (TType.STRUCT,(FileReplicaModel, FileReplicaModel.thrift_spec)), None, ), # 14
  )

  def __init__(self, fileId=None, gatewayId=None, username=None, sharedUsers=None, sharedPublic=None, fileName=None, fileDescription=None, sha256Checksum=None, fileType=None, fileSize=None, dataType=None, creationTime=None, lastModifiedTime=None, fileReplicas=None,):
    self.fileId = fileId
    self.gatewayId = gatewayId
    self.username = username
    self.sharedUsers = sharedUsers
    self.sharedPublic = sharedPublic
    self.fileName = fileName
    self.fileDescription = fileDescription
    self.sha256Checksum = sha256Checksum
    self.fileType = fileType
    self.fileSize = fileSize
    self.dataType = dataType
    self.creationTime = creationTime
    self.lastModifiedTime = lastModifiedTime
    self.fileReplicas = fileReplicas

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
          self.fileId = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.gatewayId = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.username = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.sharedUsers = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = iprot.readString()
            self.sharedUsers.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.sharedPublic = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.fileName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.fileDescription = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.sha256Checksum = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.fileType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.fileSize = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.STRING:
          self.dataType = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I64:
          self.creationTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.I64:
          self.lastModifiedTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.LIST:
          self.fileReplicas = []
          (_etype23, _size20) = iprot.readListBegin()
          for _i24 in xrange(_size20):
            _elem25 = FileReplicaModel()
            _elem25.read(iprot)
            self.fileReplicas.append(_elem25)
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
    oprot.writeStructBegin('FileModel')
    if self.fileId is not None:
      oprot.writeFieldBegin('fileId', TType.STRING, 1)
      oprot.writeString(self.fileId)
      oprot.writeFieldEnd()
    if self.gatewayId is not None:
      oprot.writeFieldBegin('gatewayId', TType.STRING, 2)
      oprot.writeString(self.gatewayId)
      oprot.writeFieldEnd()
    if self.username is not None:
      oprot.writeFieldBegin('username', TType.STRING, 3)
      oprot.writeString(self.username)
      oprot.writeFieldEnd()
    if self.sharedUsers is not None:
      oprot.writeFieldBegin('sharedUsers', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.sharedUsers))
      for iter26 in self.sharedUsers:
        oprot.writeString(iter26)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.sharedPublic is not None:
      oprot.writeFieldBegin('sharedPublic', TType.BOOL, 5)
      oprot.writeBool(self.sharedPublic)
      oprot.writeFieldEnd()
    if self.fileName is not None:
      oprot.writeFieldBegin('fileName', TType.STRING, 6)
      oprot.writeString(self.fileName)
      oprot.writeFieldEnd()
    if self.fileDescription is not None:
      oprot.writeFieldBegin('fileDescription', TType.STRING, 7)
      oprot.writeString(self.fileDescription)
      oprot.writeFieldEnd()
    if self.sha256Checksum is not None:
      oprot.writeFieldBegin('sha256Checksum', TType.STRING, 8)
      oprot.writeString(self.sha256Checksum)
      oprot.writeFieldEnd()
    if self.fileType is not None:
      oprot.writeFieldBegin('fileType', TType.I32, 9)
      oprot.writeI32(self.fileType)
      oprot.writeFieldEnd()
    if self.fileSize is not None:
      oprot.writeFieldBegin('fileSize', TType.I32, 10)
      oprot.writeI32(self.fileSize)
      oprot.writeFieldEnd()
    if self.dataType is not None:
      oprot.writeFieldBegin('dataType', TType.STRING, 11)
      oprot.writeString(self.dataType)
      oprot.writeFieldEnd()
    if self.creationTime is not None:
      oprot.writeFieldBegin('creationTime', TType.I64, 12)
      oprot.writeI64(self.creationTime)
      oprot.writeFieldEnd()
    if self.lastModifiedTime is not None:
      oprot.writeFieldBegin('lastModifiedTime', TType.I64, 13)
      oprot.writeI64(self.lastModifiedTime)
      oprot.writeFieldEnd()
    if self.fileReplicas is not None:
      oprot.writeFieldBegin('fileReplicas', TType.LIST, 14)
      oprot.writeListBegin(TType.STRUCT, len(self.fileReplicas))
      for iter27 in self.fileReplicas:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.fileId)
    value = (value * 31) ^ hash(self.gatewayId)
    value = (value * 31) ^ hash(self.username)
    value = (value * 31) ^ hash(self.sharedUsers)
    value = (value * 31) ^ hash(self.sharedPublic)
    value = (value * 31) ^ hash(self.fileName)
    value = (value * 31) ^ hash(self.fileDescription)
    value = (value * 31) ^ hash(self.sha256Checksum)
    value = (value * 31) ^ hash(self.fileType)
    value = (value * 31) ^ hash(self.fileSize)
    value = (value * 31) ^ hash(self.dataType)
    value = (value * 31) ^ hash(self.creationTime)
    value = (value * 31) ^ hash(self.lastModifiedTime)
    value = (value * 31) ^ hash(self.fileReplicas)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class FileReplicaModel:
  """
  Attributes:
   - replicaName
   - replicaDescription
   - storageHostname
   - storageResourceId
   - filePath
   - creationTime
   - validUntilTime
   - storageResourceType
   - replicaPersistentType
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'replicaName', None, None, ), # 1
    (2, TType.STRING, 'replicaDescription', None, None, ), # 2
    (3, TType.STRING, 'storageHostname', None, None, ), # 3
    (4, TType.STRING, 'storageResourceId', None, None, ), # 4
    (5, TType.STRING, 'filePath', None, None, ), # 5
    (6, TType.I64, 'creationTime', None, None, ), # 6
    (7, TType.I64, 'validUntilTime', None, None, ), # 7
    (8, TType.I32, 'storageResourceType', None, None, ), # 8
    (9, TType.I32, 'replicaPersistentType', None, None, ), # 9
  )

  def __init__(self, replicaName=None, replicaDescription=None, storageHostname=None, storageResourceId=None, filePath=None, creationTime=None, validUntilTime=None, storageResourceType=None, replicaPersistentType=None,):
    self.replicaName = replicaName
    self.replicaDescription = replicaDescription
    self.storageHostname = storageHostname
    self.storageResourceId = storageResourceId
    self.filePath = filePath
    self.creationTime = creationTime
    self.validUntilTime = validUntilTime
    self.storageResourceType = storageResourceType
    self.replicaPersistentType = replicaPersistentType

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
          self.replicaName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.replicaDescription = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.storageHostname = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.storageResourceId = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.filePath = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.creationTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.validUntilTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.storageResourceType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.replicaPersistentType = iprot.readI32()
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
    oprot.writeStructBegin('FileReplicaModel')
    if self.replicaName is not None:
      oprot.writeFieldBegin('replicaName', TType.STRING, 1)
      oprot.writeString(self.replicaName)
      oprot.writeFieldEnd()
    if self.replicaDescription is not None:
      oprot.writeFieldBegin('replicaDescription', TType.STRING, 2)
      oprot.writeString(self.replicaDescription)
      oprot.writeFieldEnd()
    if self.storageHostname is not None:
      oprot.writeFieldBegin('storageHostname', TType.STRING, 3)
      oprot.writeString(self.storageHostname)
      oprot.writeFieldEnd()
    if self.storageResourceId is not None:
      oprot.writeFieldBegin('storageResourceId', TType.STRING, 4)
      oprot.writeString(self.storageResourceId)
      oprot.writeFieldEnd()
    if self.filePath is not None:
      oprot.writeFieldBegin('filePath', TType.STRING, 5)
      oprot.writeString(self.filePath)
      oprot.writeFieldEnd()
    if self.creationTime is not None:
      oprot.writeFieldBegin('creationTime', TType.I64, 6)
      oprot.writeI64(self.creationTime)
      oprot.writeFieldEnd()
    if self.validUntilTime is not None:
      oprot.writeFieldBegin('validUntilTime', TType.I64, 7)
      oprot.writeI64(self.validUntilTime)
      oprot.writeFieldEnd()
    if self.storageResourceType is not None:
      oprot.writeFieldBegin('storageResourceType', TType.I32, 8)
      oprot.writeI32(self.storageResourceType)
      oprot.writeFieldEnd()
    if self.replicaPersistentType is not None:
      oprot.writeFieldBegin('replicaPersistentType', TType.I32, 9)
      oprot.writeI32(self.replicaPersistentType)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.replicaName)
    value = (value * 31) ^ hash(self.replicaDescription)
    value = (value * 31) ^ hash(self.storageHostname)
    value = (value * 31) ^ hash(self.storageResourceId)
    value = (value * 31) ^ hash(self.filePath)
    value = (value * 31) ^ hash(self.creationTime)
    value = (value * 31) ^ hash(self.validUntilTime)
    value = (value * 31) ^ hash(self.storageResourceType)
    value = (value * 31) ^ hash(self.replicaPersistentType)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
