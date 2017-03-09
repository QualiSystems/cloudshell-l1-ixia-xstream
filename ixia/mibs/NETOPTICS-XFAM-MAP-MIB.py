#
# PySNMP MIB module NETOPTICS-XFAM-MAP-MIB (http://pysnmp.sf.net)
# ASN.1 source file://C:\MIBS\text_mibs\NETOPTICS-XFAM-MAP-MIB.mib
# Produced by pysmi-0.0.6 at Tue Mar 07 16:52:52 2017
# On host ? platform ? version ? by user ?
# Using Python version 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)]
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
( TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
nETOPTICS_XFAM_MAP_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1)).setLabel("nETOPTICS-XFAM-MAP-MIB").setRevisions(("2015-09-28 00:00",))
class ConfdString(OctetString, TextualConvention):
    displayHint = '1t'

class String(OctetString, TextualConvention):
    displayHint = '1t'

class MapDescriptionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class MapNameType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,64)

class MapPortListType(OctetString, TextualConvention):
    displayHint = '1t'

class MapIdType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,64)

map = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1))
mapIdTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1, 1), )
mapIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-MAP-MIB", "mapIdId"))
mapIdId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1, 1, 1, 1), MapIdType())
mapIdInPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1, 1, 1, 2), MapPortListType()).setMaxAccess("readcreate")
mapIdOutPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1, 1, 1, 3), MapPortListType()).setMaxAccess("readcreate")
mapIdPcapture = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
mapIdRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 18, 1, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
mibBuilder.exportSymbols("NETOPTICS-XFAM-MAP-MIB", mapIdOutPorts=mapIdOutPorts, MapDescriptionType=MapDescriptionType, PYSNMP_MODULE_ID=nETOPTICS_XFAM_MAP_MIB, MapNameType=MapNameType, mapIdInPorts=mapIdInPorts, mapIdTable=mapIdTable, nETOPTICS_XFAM_MAP_MIB=nETOPTICS_XFAM_MAP_MIB, MapPortListType=MapPortListType, MapIdType=MapIdType, String=String, map=map, mapIdId=mapIdId, mapIdRowstatus=mapIdRowstatus, mapIdPcapture=mapIdPcapture, mapIdEntry=mapIdEntry, ConfdString=ConfdString)
