#
# PySNMP MIB module NETOPTICS-XFAM-PORTS-MIB (http://pysnmp.sf.net)
# ASN.1 source file://C:\MIBS\text_mibs\NETOPTICS-XFAM-PORTS-MIB.mib
# Produced by pysmi-0.0.6 at Tue Mar 07 16:47:00 2017
# On host ? platform ? version ? by user ?
# Using Python version 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)]
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
( TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
nETOPTICS_XFAM_PORTS_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3)).setLabel("nETOPTICS-XFAM-PORTS-MIB").setRevisions(("2015-11-20 00:00",))
class UnsignedShort(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)

class ConfdString(OctetString, TextualConvention):
    displayHint = '1t'

class String(OctetString, TextualConvention):
    displayHint = '1t'

class AutoNegotiationType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1,)
    namedValues = NamedValues(("off", 0), ("on", 1),)

class PortRateLimitType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,40000)

class PortNameType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,63)

class PortModeType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3,)
    namedValues = NamedValues(("loopback", 0), ("simplex", 1), ("standard", 2), ("loopbackTxOn", 3),)

class PortConfigSpeedType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 1000, 10000, 40000,)
    namedValues = NamedValues(("auto", 1), ("a1000", 1000), ("a10000", 10000), ("a40000", 40000),)

class PortLinkFaultDetectPeerType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,64)

class UtilAlertType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("na", 0), ("alertRising", 1), ("alertFalling", 2),)

class PortDuplexType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("na", 0), ("half", 1), ("full", 2),)

class PortDescriptionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,511)

class PortPktParseType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("l2", 0), ("l3", 1), ("l4", 2),)

class PortInlineSpanModeType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4,)
    namedValues = NamedValues(("na", 0), ("inlineFailOpen", 1), ("span", 2), ("tap", 3), ("inlineFailClose", 4),)

class EgressVlanTagType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3,)
    namedValues = NamedValues(("keep-outer", 0), ("remove-outer", 1), ("keep-added", 2), ("remove-added", 3),)

class IngressVlanTagType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("keep", 0), ("stack", 1), ("replace", 2),)

class AutoNegotiationStatusType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,63)

class EnetInterfaceModeType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5,)
    namedValues = NamedValues(("disabled", 0), ("a40GBase-SR4", 1), ("a10GBase-CR", 2), ("sGMII", 3), ("a1000Base-X", 4), ("other", 5),)

class StatsTableType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("statsNa", 1), ("statsRealTime", 2),)

class PortIfg(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("optimized", 1), ("standard", 2),)

class PortConfigAdminType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("enable", 1), ("disable", 2),)

class LinkStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3,)
    namedValues = NamedValues(("na", 0), ("linkUp", 1), ("linkDown", 2), ("linkRxDown", 3),)

class PortStatusSpeedType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 10, 100, 1000, 10000, 40000, 100000,)
    namedValues = NamedValues(("na", 0), ("a10", 10), ("a100", 100), ("a1000", 1000), ("a10000", 10000), ("a40000", 40000), ("a100000", 100000),)

class PortAdminForcedStateType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("na", 0), ("ha-stdby", 1), ("lfd-down", 2),)

class TpidType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 3,)
    namedValues = NamedValues(("a8100", 1), ("a9100", 3),)

class PortStatusAdminType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("na", 0), ("enable", 1), ("disable", 2),)

class TxStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("na", 0), ("tx-disabled", 1), ("tx-enabled", 2),)

class PortDebugFlagsType(Bits, TextualConvention):
    namedValues = NamedValues(("autonegTrace", 0), ("linkDebounceTrace", 1), ("phyPollTrace", 2),)

class PortHeartbeatPeerType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,64)

class PortStatusBypassType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("na", 0), ("enable", 1), ("disable", 2),)

stats = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3))
statsAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 1))
statsAdminStatsTableReset = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 1, 1), StatsTableType()).setMaxAccess("readwrite")
statsBrief = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2))
statsBytes = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3))
statsDrops = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4))
statsErrs = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5))
statsOthers = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6))
statsPrio = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7))
statsProto = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8))
statsSize = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9))
statsUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10))
portGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 1))
portGlobalCrc = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 1, 1), TruthValue()).setMaxAccess("readwrite")
portGlobalCutThrough = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
portGlobalJumbo = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
portGlobalBpduDrop = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
portGlobalUtilAlert = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 1, 5), TruthValue()).setMaxAccess("readwrite")
portsStatsBriefTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1), )
portsStatsBriefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsBriefPortNum"))
portsStatsBriefPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsBriefRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsBriefRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsBriefRxJumboPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsBriefTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
portsStatsBriefTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
portsStatsBriefTxJumboPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
portsStatsBriefLastSampleTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 8), ConfdString()).setMaxAccess("readonly")
portsStatsBriefLastSampleDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 9), String()).setMaxAccess("readonly")
portsStatsBriefEnetInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 10), EnetInterfaceModeType()).setMaxAccess("readonly")
portsStatsBriefLastSampleTimestampCntrUsec = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
portsStatsBriefRxBytesWithIFG = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 12), Counter64()).setMaxAccess("readonly")
portsStatsBriefTxBytesWithIFG = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
portsStatsBriefRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 2, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsBytesTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3, 1), )
portsStatsBytesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsBytesPortNum"))
portsStatsBytesPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsBytesRxNonIpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsBytesRxIpv4Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsBytesRxIpv6Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsBytesRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 3, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsDropsTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1), )
portsStatsDropsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsDropsPortNum"))
portsStatsDropsPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsDropsRxParseErrDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsDropsFilterDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsDropsCorruptedDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsDropsCongestionDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 5), Counter64()).setMaxAccess("readonly")
portsStatsDropsTxCongestionDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 6), Counter64()).setMaxAccess("readonly")
portsStatsDropsRxSecureDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 7), Counter64()).setMaxAccess("readonly")
portsStatsDropsRxVlanTagDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 8), Counter64()).setMaxAccess("readonly")
portsStatsDropsTxVlanBvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 9), Counter64()).setMaxAccess("readonly")
portsStatsDropsRxVlanBvPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 10), Counter64()).setMaxAccess("readonly")
portsStatsDropsRxOverrunPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 11), Counter64()).setMaxAccess("readonly")
portsStatsDropsStpDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 12), Counter64()).setMaxAccess("readonly")
portsStatsDropsTtlDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 13), Counter64()).setMaxAccess("readonly")
portsStatsDropsPauseDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 14), Counter64()).setMaxAccess("readonly")
portsStatsDropsCounterDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 15), Counter64()).setMaxAccess("readonly")
portsStatsDropsTxUnderrunPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 16), Counter64()).setMaxAccess("readonly")
portsStatsDropsTxErrorDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 17), Counter64()).setMaxAccess("readonly")
portsStatsDropsTxTimeOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 18), Counter64()).setMaxAccess("readonly")
portsStatsDropsTxLoopbackDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 19), Counter64()).setMaxAccess("readonly")
portsStatsDropsRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 4, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsErrsTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1), )
portsStatsErrsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsErrsPortNum"))
portsStatsErrsPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsErrsTxErrBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsErrsTxFcsErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsErrsRxFcsErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsErrsRxSizeErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1, 5), Counter64()).setMaxAccess("readonly")
portsStatsErrsRxSymbolErrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1, 6), Counter64()).setMaxAccess("readonly")
portsStatsErrsRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 5, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsOthersTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6, 1), )
portsStatsOthersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsOthersPortNum"))
portsStatsOthersPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsOthersRxCpuTrappedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsOthersFidFwdPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsOthersFloodedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsOthersRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 6, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsPrioTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1), )
portsStatsPrioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsPrioPortNum"))
portsStatsPrioPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsPrioRxPrio0Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio1Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio2Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio3Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 5), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio4Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 6), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio5Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 7), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio6Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 8), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio7Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 9), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio0Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 10), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio1Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 11), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio2Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 12), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio3Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 13), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio4Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 14), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio5Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 15), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio6Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 16), Counter64()).setMaxAccess("readonly")
portsStatsPrioRxPrio7Bytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 17), Counter64()).setMaxAccess("readonly")
portsStatsPrioRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 7, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsProtoTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1), )
portsStatsProtoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsProtoPortNum"))
portsStatsProtoPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsProtoTxUcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxUcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsProtoTxBcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxBcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 5), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxNonIpBcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 6), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxIpv4BcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 7), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxIpv6BcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 8), Counter64()).setMaxAccess("readonly")
portsStatsProtoTxMcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 9), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxMcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 10), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxNonIpMcstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 11), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxIpv4McstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 12), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxIpv6McstPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 13), Counter64()).setMaxAccess("readonly")
portsStatsProtoTxPausePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 14), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxPausePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 15), Counter64()).setMaxAccess("readonly")
portsStatsProtoTxIpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 16), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxIpPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 17), Counter64()).setMaxAccess("readonly")
portsStatsProtoTxNonIpUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 18), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxNonIpUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 19), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxIpv4UcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 20), Counter64()).setMaxAccess("readonly")
portsStatsProtoRxIpv6UcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 21), Counter64()).setMaxAccess("readonly")
portsStatsProtoRx802dot3PauseClassPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 22), Counter64()).setMaxAccess("readonly")
portsStatsProtoRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 8, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsSizeTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1), )
portsStatsSizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsSizePortNum"))
portsStatsSizePortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsSizeRxUndersizedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 2), Counter64()).setMaxAccess("readonly")
portsStatsSizeTxMin64Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 3), Counter64()).setMaxAccess("readonly")
portsStatsSizeRxMin64Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 4), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx65to127Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 5), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx65to127Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 6), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx128to255Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 7), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx128to255Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 8), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx256to511Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 9), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx256to511Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 10), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx512to1023Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 11), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx512to1023Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 12), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx1024to1522Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 13), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx1024to1522Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 14), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx1523to2047Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 15), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx1523to2047Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 16), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx2048to4095Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 17), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx2048to4095Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 18), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx4096to8191Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 19), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx4096to8191Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 20), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx8192to10239Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 21), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx8192to10239Pkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 22), Counter64()).setMaxAccess("readonly")
portsStatsSizeTx10240MaxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 23), Counter64()).setMaxAccess("readonly")
portsStatsSizeRx10240MaxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 24), Counter64()).setMaxAccess("readonly")
portsStatsSizeRxOversizedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 25), Counter64()).setMaxAccess("readonly")
portsStatsSizeRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 9, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portsStatsUtilTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1), )
portsStatsUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portsStatsUtilPortNum"))
portsStatsUtilPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portsStatsUtilTxUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 2), String()).setMaxAccess("readonly")
portsStatsUtilTxUtilPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 3), String()).setMaxAccess("readonly")
portsStatsUtilTxPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 4), String()).setMaxAccess("readonly")
portsStatsUtilRxUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 5), String()).setMaxAccess("readonly")
portsStatsUtilRxUtilPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 6), String()).setMaxAccess("readonly")
portsStatsUtilRxPeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 7), String()).setMaxAccess("readonly")
portsStatsUtilTxUtilBps = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 8), ConfdString()).setMaxAccess("readonly")
portsStatsUtilTxUtilPeakBps = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 9), ConfdString()).setMaxAccess("readonly")
portsStatsUtilRxUtilBps = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 10), ConfdString()).setMaxAccess("readonly")
portsStatsUtilRxUtilPeakBps = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 11), ConfdString()).setMaxAccess("readonly")
portsStatsUtilTxUtilPct = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 12), ConfdString()).setMaxAccess("readonly")
portsStatsUtilTxUtilPeakPct = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 13), ConfdString()).setMaxAccess("readonly")
portsStatsUtilRxUtilPct = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 14), ConfdString()).setMaxAccess("readonly")
portsStatsUtilRxUtilPeakPct = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 15), ConfdString()).setMaxAccess("readonly")
portsStatsUtilTxUtilPctTimes1e4 = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 16), Counter64()).setMaxAccess("readonly")
portsStatsUtilTxUtilPeakPctTimes1e4 = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 17), Counter64()).setMaxAccess("readonly")
portsStatsUtilRxUtilPctTimes1e4 = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 18), Counter64()).setMaxAccess("readonly")
portsStatsUtilRxUtilPeakPctTimes1e4 = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 19), Counter64()).setMaxAccess("readonly")
portsStatsUtilRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 3, 10, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
portTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2), )
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1), ).setIndexNames((0, "NETOPTICS-XFAM-PORTS-MIB", "portPortNumber"))
portPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
portRxDescrip = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 2), PortDescriptionType()).setMaxAccess("readcreate")
portTxDescrip = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 3), PortDescriptionType()).setMaxAccess("readcreate")
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 4), PortNameType().clone('Unnamed port')).setMaxAccess("readcreate")
portAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 5), PortConfigAdminType().clone('enable')).setMaxAccess("readcreate")
portSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 6), PortConfigSpeedType().clone('auto')).setMaxAccess("readcreate")
portMode = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 7), PortModeType().clone('standard')).setMaxAccess("readcreate")
portLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 8), PortStatusSpeedType()).setMaxAccess("readonly")
portLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 9), LinkStatusType()).setMaxAccess("readonly")
portLinkPhyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 10), LinkStatusType()).setMaxAccess("readonly")
portAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 11), AutoNegotiationType().clone('on')).setMaxAccess("readcreate")
portLinkAutoNegotiationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 12), AutoNegotiationStatusType()).setMaxAccess("readonly")
portMirror = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 13), TruthValue()).setMaxAccess("readcreate")
portMirrorGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,4))).setMaxAccess("readcreate")
portUtilAlertDetectionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 27), TruthValue()).setMaxAccess("readcreate")
portUtilAlertAlertInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3,360)).clone(10)).setMaxAccess("readcreate")
portUtilAlertTxAlertRisingThresRate = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,100)).clone(80)).setMaxAccess("readcreate")
portUtilAlertTxAlertFallingThresRate = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,100)).clone(75)).setMaxAccess("readcreate")
portUtilAlertTxAlertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 31), UtilAlertType()).setMaxAccess("readonly")
portUtilAlertTxAlertUtilRate = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 32), Integer32()).setMaxAccess("readonly")
portUtilAlertRxAlertRisingThresRate = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 33), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,100)).clone(80)).setMaxAccess("readcreate")
portUtilAlertRxAlertFallingThresRate = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 34), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,100)).clone(75)).setMaxAccess("readcreate")
portUtilAlertRxAlertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 35), UtilAlertType()).setMaxAccess("readonly")
portUtilAlertRxAlertUtilRate = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 36), Integer32()).setMaxAccess("readonly")
portUtilAlertAlertEnabledStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 37), TruthValue()).setMaxAccess("readonly")
portIfg = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 15), PortIfg().clone('optimized')).setMaxAccess("readcreate")
portVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 16), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(2,4094))).setMaxAccess("readcreate")
portIngressTag = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 17), IngressVlanTagType().clone('keep')).setMaxAccess("readcreate")
portEgressTag = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 18), EgressVlanTagType().clone('keep-outer')).setMaxAccess("readcreate")
portTpid = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 19), TpidType().clone('a8100')).setMaxAccess("readcreate")
portEgressRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 20), PortRateLimitType()).setMaxAccess("readcreate")
portTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 21), TruthValue()).setMaxAccess("readcreate")
portTimestampFcs = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 22), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1,)).clone(namedValues=NamedValues(("append", 0), ("replace", 1),))).setMaxAccess("readcreate")
portTimestampKeyframe = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 23), String().subtype(subtypeSpec=ValueSizeConstraint(1,32))).setMaxAccess("readcreate")
portHa = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 24), TruthValue()).setMaxAccess("readcreate")
portAdminForced = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 25), PortAdminForcedStateType()).setMaxAccess("readonly")
portParse = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 26), PortPktParseType().clone('l4')).setMaxAccess("readcreate")
portPcapture = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 38), TruthValue()).setMaxAccess("readcreate")
portTxDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 39), TruthValue()).setMaxAccess("readcreate")
portTxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 40), TxStatusType()).setMaxAccess("readonly")
portRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 3, 3, 2, 1, 99), RowStatus()).setMaxAccess("readcreate")
mibBuilder.exportSymbols("NETOPTICS-XFAM-PORTS-MIB", portsStatsProtoTxUcstPkts=portsStatsProtoTxUcstPkts, StatsTableType=StatsTableType, PortModeType=PortModeType, PortStatusBypassType=PortStatusBypassType, portPcapture=portPcapture, PortRateLimitType=PortRateLimitType, UtilAlertType=UtilAlertType, statsBrief=statsBrief, portsStatsErrsTxFcsErrPkts=portsStatsErrsTxFcsErrPkts, portRxDescrip=portRxDescrip, portsStatsUtilRxUtilPeakBps=portsStatsUtilRxUtilPeakBps, AutoNegotiationType=AutoNegotiationType, portsStatsPrioRxPrio3Pkts=portsStatsPrioRxPrio3Pkts, portsStatsPrioPortNum=portsStatsPrioPortNum, portsStatsErrsPortNum=portsStatsErrsPortNum, portGlobalCrc=portGlobalCrc, portsStatsSizeTx4096to8191Pkts=portsStatsSizeTx4096to8191Pkts, PortHeartbeatPeerType=PortHeartbeatPeerType, PortPktParseType=PortPktParseType, portAdminForced=portAdminForced, portsStatsDropsTxUnderrunPkts=portsStatsDropsTxUnderrunPkts, ConfdString=ConfdString, portUtilAlertTxAlertStatus=portUtilAlertTxAlertStatus, portsStatsUtilPortNum=portsStatsUtilPortNum, portsStatsErrsTxErrBytes=portsStatsErrsTxErrBytes, portsStatsSizeTx128to255Pkts=portsStatsSizeTx128to255Pkts, portLinkAutoNegotiationStatus=portLinkAutoNegotiationStatus, PortNameType=PortNameType, portsStatsBriefTxPackets=portsStatsBriefTxPackets, portsStatsUtilRxUtilPeakPctTimes1e4=portsStatsUtilRxUtilPeakPctTimes1e4, portsStatsBriefTxBytes=portsStatsBriefTxBytes, portsStatsSizeTxMin64Pkts=portsStatsSizeTxMin64Pkts, portSpeed=portSpeed, portsStatsDropsTxCongestionDropPkts=portsStatsDropsTxCongestionDropPkts, PortDescriptionType=PortDescriptionType, PortInlineSpanModeType=PortInlineSpanModeType, portsStatsPrioRxPrio2Bytes=portsStatsPrioRxPrio2Bytes, statsProto=statsProto, stats=stats, portsStatsProtoRxIpPkts=portsStatsProtoRxIpPkts, portsStatsUtilTxUtil=portsStatsUtilTxUtil, statsAdmin=statsAdmin, portsStatsUtilRowstatus=portsStatsUtilRowstatus, portsStatsErrsRowstatus=portsStatsErrsRowstatus, portsStatsErrsRxSymbolErrPkts=portsStatsErrsRxSymbolErrPkts, portPortNumber=portPortNumber, portTimestampKeyframe=portTimestampKeyframe, portEgressRateLimit=portEgressRateLimit, portRowstatus=portRowstatus, portGlobalBpduDrop=portGlobalBpduDrop, portsStatsBriefTxBytesWithIFG=portsStatsBriefTxBytesWithIFG, portsStatsSizeTx8192to10239Pkts=portsStatsSizeTx8192to10239Pkts, portsStatsOthersRxCpuTrappedPkts=portsStatsOthersRxCpuTrappedPkts, portsStatsErrsEntry=portsStatsErrsEntry, portsStatsProtoRx802dot3PauseClassPkts=portsStatsProtoRx802dot3PauseClassPkts, portTable=portTable, portsStatsProtoRxIpv4UcastPkts=portsStatsProtoRxIpv4UcastPkts, portsStatsPrioEntry=portsStatsPrioEntry, portsStatsBytesPortNum=portsStatsBytesPortNum, portsStatsSizeRx1024to1522Pkts=portsStatsSizeRx1024to1522Pkts, portUtilAlertAlertInterval=portUtilAlertAlertInterval, portsStatsDropsRxParseErrDropPkts=portsStatsDropsRxParseErrDropPkts, portsStatsUtilTxUtilPeak=portsStatsUtilTxUtilPeak, portUtilAlertTxAlertFallingThresRate=portUtilAlertTxAlertFallingThresRate, PortConfigSpeedType=PortConfigSpeedType, portTxDescrip=portTxDescrip, portsStatsBytesRxIpv6Bytes=portsStatsBytesRxIpv6Bytes, portsStatsSizeTx2048to4095Pkts=portsStatsSizeTx2048to4095Pkts, portUtilAlertDetectionEnabled=portUtilAlertDetectionEnabled, portsStatsSizeRx512to1023Pkts=portsStatsSizeRx512to1023Pkts, portsStatsPrioRxPrio3Bytes=portsStatsPrioRxPrio3Bytes, portsStatsPrioRxPrio7Pkts=portsStatsPrioRxPrio7Pkts, portsStatsBriefPortNum=portsStatsBriefPortNum, portsStatsPrioRxPrio0Pkts=portsStatsPrioRxPrio0Pkts, statsErrs=statsErrs, portsStatsDropsRxVlanTagDropPkts=portsStatsDropsRxVlanTagDropPkts, portsStatsErrsTable=portsStatsErrsTable, nETOPTICS_XFAM_PORTS_MIB=nETOPTICS_XFAM_PORTS_MIB, portsStatsSizeRx65to127Pkts=portsStatsSizeRx65to127Pkts, portUtilAlertRxAlertFallingThresRate=portUtilAlertRxAlertFallingThresRate, portsStatsOthersTable=portsStatsOthersTable, portsStatsSizeTx256to511Pkts=portsStatsSizeTx256to511Pkts, portsStatsBytesRxNonIpBytes=portsStatsBytesRxNonIpBytes, portsStatsProtoTxBcstPkts=portsStatsProtoTxBcstPkts, portsStatsBriefRowstatus=portsStatsBriefRowstatus, portsStatsUtilTxUtilPct=portsStatsUtilTxUtilPct, portsStatsSizeTable=portsStatsSizeTable, IngressVlanTagType=IngressVlanTagType, portsStatsProtoRxIpv6McstPkts=portsStatsProtoRxIpv6McstPkts, portsStatsUtilRxPeakTime=portsStatsUtilRxPeakTime, portsStatsProtoRxNonIpBcstPkts=portsStatsProtoRxNonIpBcstPkts, portsStatsProtoRxMcstPkts=portsStatsProtoRxMcstPkts, portsStatsDropsFilterDropPkts=portsStatsDropsFilterDropPkts, portUtilAlertTxAlertUtilRate=portUtilAlertTxAlertUtilRate, portsStatsProtoRxIpv6BcstPkts=portsStatsProtoRxIpv6BcstPkts, portsStatsPrioRxPrio7Bytes=portsStatsPrioRxPrio7Bytes, portsStatsPrioTable=portsStatsPrioTable, portsStatsUtilTxUtilPeakPct=portsStatsUtilTxUtilPeakPct, portsStatsUtilRxUtilPeakPct=portsStatsUtilRxUtilPeakPct, portsStatsSizeRxUndersizedPkts=portsStatsSizeRxUndersizedPkts, portsStatsPrioRxPrio4Bytes=portsStatsPrioRxPrio4Bytes, portUtilAlertRxAlertUtilRate=portUtilAlertRxAlertUtilRate, portLinkSpeed=portLinkSpeed, portsStatsErrsRxSizeErrPkts=portsStatsErrsRxSizeErrPkts, portsStatsBytesRowstatus=portsStatsBytesRowstatus, portsStatsDropsStpDropPkts=portsStatsDropsStpDropPkts, portsStatsOthersFidFwdPkts=portsStatsOthersFidFwdPkts, portsStatsBriefEntry=portsStatsBriefEntry, portsStatsBriefLastSampleTimestampCntrUsec=portsStatsBriefLastSampleTimestampCntrUsec, statsOthers=statsOthers, portsStatsPrioRxPrio1Pkts=portsStatsPrioRxPrio1Pkts, portVlan=portVlan, portEntry=portEntry, portsStatsBriefRxBytesWithIFG=portsStatsBriefRxBytesWithIFG, portsStatsDropsRxOverrunPkts=portsStatsDropsRxOverrunPkts, portsStatsSizeRx2048to4095Pkts=portsStatsSizeRx2048to4095Pkts, portsStatsDropsPauseDropPkts=portsStatsDropsPauseDropPkts, statsUtil=statsUtil, portsStatsDropsPortNum=portsStatsDropsPortNum, portName=portName, portsStatsBriefRxPackets=portsStatsBriefRxPackets, portLinkPhyStatus=portLinkPhyStatus, statsDrops=statsDrops, portParse=portParse, portAutoNegotiation=portAutoNegotiation, portsStatsBriefRxBytes=portsStatsBriefRxBytes, portGlobal=portGlobal, portMirror=portMirror, portsStatsPrioRxPrio1Bytes=portsStatsPrioRxPrio1Bytes, EnetInterfaceModeType=EnetInterfaceModeType, portUtilAlertRxAlertStatus=portUtilAlertRxAlertStatus, portsStatsUtilTxUtilPeakBps=portsStatsUtilTxUtilPeakBps, portsStatsDropsTxTimeOutPkts=portsStatsDropsTxTimeOutPkts, portUtilAlertRxAlertRisingThresRate=portUtilAlertRxAlertRisingThresRate, portsStatsDropsTxLoopbackDropPkts=portsStatsDropsTxLoopbackDropPkts, portsStatsProtoTxPausePkts=portsStatsProtoTxPausePkts, portsStatsSizeTx65to127Pkts=portsStatsSizeTx65to127Pkts, statsAdminStatsTableReset=statsAdminStatsTableReset, portsStatsUtilRxUtilPctTimes1e4=portsStatsUtilRxUtilPctTimes1e4, portUtilAlertAlertEnabledStatus=portUtilAlertAlertEnabledStatus, portsStatsUtilTxUtilPeakPctTimes1e4=portsStatsUtilTxUtilPeakPctTimes1e4, portsStatsProtoTxNonIpUcastPkts=portsStatsProtoTxNonIpUcastPkts, portsStatsBytesTable=portsStatsBytesTable, portsStatsUtilRxUtilBps=portsStatsUtilRxUtilBps, portsStatsProtoRowstatus=portsStatsProtoRowstatus, portsStatsSizeRxOversizedPkts=portsStatsSizeRxOversizedPkts, portGlobalCutThrough=portGlobalCutThrough, portsStatsDropsTxVlanBvPkts=portsStatsDropsTxVlanBvPkts, portsStatsSizeEntry=portsStatsSizeEntry, portsStatsBriefTxJumboPackets=portsStatsBriefTxJumboPackets, portsStatsDropsCorruptedDropPkts=portsStatsDropsCorruptedDropPkts, portsStatsBytesRxIpv4Bytes=portsStatsBytesRxIpv4Bytes, PortDebugFlagsType=PortDebugFlagsType, AutoNegotiationStatusType=AutoNegotiationStatusType, portsStatsProtoRxNonIpMcstPkts=portsStatsProtoRxNonIpMcstPkts, portsStatsPrioRxPrio4Pkts=portsStatsPrioRxPrio4Pkts, portIfg=portIfg, portsStatsProtoRxIpv4McstPkts=portsStatsProtoRxIpv4McstPkts, portsStatsOthersFloodedPkts=portsStatsOthersFloodedPkts, portsStatsSizeRxMin64Pkts=portsStatsSizeRxMin64Pkts, portLinkStatus=portLinkStatus, portsStatsUtilRxUtil=portsStatsUtilRxUtil, PortConfigAdminType=PortConfigAdminType, portsStatsUtilEntry=portsStatsUtilEntry, portsStatsSizeTx1024to1522Pkts=portsStatsSizeTx1024to1522Pkts, LinkStatusType=LinkStatusType, portsStatsDropsEntry=portsStatsDropsEntry, portsStatsBytesEntry=portsStatsBytesEntry, portsStatsDropsRowstatus=portsStatsDropsRowstatus, portsStatsProtoTable=portsStatsProtoTable, PortStatusAdminType=PortStatusAdminType, portsStatsDropsRxSecureDropPkts=portsStatsDropsRxSecureDropPkts, portsStatsBriefRxJumboPackets=portsStatsBriefRxJumboPackets, TpidType=TpidType, portsStatsSizePortNum=portsStatsSizePortNum, portsStatsPrioRxPrio6Pkts=portsStatsPrioRxPrio6Pkts, statsPrio=statsPrio, portsStatsBriefEnetInterfaceMode=portsStatsBriefEnetInterfaceMode, portsStatsPrioRowstatus=portsStatsPrioRowstatus, portGlobalJumbo=portGlobalJumbo, portUtilAlertTxAlertRisingThresRate=portUtilAlertTxAlertRisingThresRate, portsStatsPrioRxPrio5Pkts=portsStatsPrioRxPrio5Pkts, portsStatsBriefLastSampleDateTime=portsStatsBriefLastSampleDateTime, portsStatsPrioRxPrio2Pkts=portsStatsPrioRxPrio2Pkts, portsStatsProtoRxIpv6UcastPkts=portsStatsProtoRxIpv6UcastPkts, portsStatsSizeRx128to255Pkts=portsStatsSizeRx128to255Pkts, portsStatsSizeTx1523to2047Pkts=portsStatsSizeTx1523to2047Pkts, UnsignedShort=UnsignedShort, PortStatusSpeedType=PortStatusSpeedType, portsStatsDropsCongestionDropPkts=portsStatsDropsCongestionDropPkts, portsStatsPrioRxPrio5Bytes=portsStatsPrioRxPrio5Bytes, statsBytes=statsBytes, portsStatsUtilTxPeakTime=portsStatsUtilTxPeakTime, portTimestamp=portTimestamp, portsStatsProtoTxMcstPkts=portsStatsProtoTxMcstPkts, portsStatsPrioRxPrio0Bytes=portsStatsPrioRxPrio0Bytes, portEgressTag=portEgressTag, portTpid=portTpid, portTimestampFcs=portTimestampFcs, portsStatsSizeRx4096to8191Pkts=portsStatsSizeRx4096to8191Pkts, portGlobalUtilAlert=portGlobalUtilAlert, portsStatsProtoRxIpv4BcstPkts=portsStatsProtoRxIpv4BcstPkts, portsStatsProtoRxUcstPkts=portsStatsProtoRxUcstPkts, portsStatsBriefTable=portsStatsBriefTable, portsStatsSizeRx10240MaxPkts=portsStatsSizeRx10240MaxPkts, portsStatsSizeRx256to511Pkts=portsStatsSizeRx256to511Pkts, portsStatsSizeTx512to1023Pkts=portsStatsSizeTx512to1023Pkts, PortAdminForcedStateType=PortAdminForcedStateType, portsStatsUtilRxUtilPeak=portsStatsUtilRxUtilPeak, portsStatsProtoRxPausePkts=portsStatsProtoRxPausePkts, portsStatsProtoRxBcstPkts=portsStatsProtoRxBcstPkts, portsStatsPrioRxPrio6Bytes=portsStatsPrioRxPrio6Bytes, portsStatsDropsTable=portsStatsDropsTable, portsStatsErrsRxFcsErrPkts=portsStatsErrsRxFcsErrPkts, portTxDisable=portTxDisable, portsStatsProtoRxNonIpUcastPkts=portsStatsProtoRxNonIpUcastPkts, portAdmin=portAdmin, portsStatsUtilRxUtilPct=portsStatsUtilRxUtilPct, PortLinkFaultDetectPeerType=PortLinkFaultDetectPeerType, TxStatusType=TxStatusType, portsStatsSizeRx8192to10239Pkts=portsStatsSizeRx8192to10239Pkts, portsStatsOthersRowstatus=portsStatsOthersRowstatus, portHa=portHa, portIngressTag=portIngressTag, portsStatsDropsRxVlanBvPkts=portsStatsDropsRxVlanBvPkts, portsStatsSizeRx1523to2047Pkts=portsStatsSizeRx1523to2047Pkts, portsStatsDropsTtlDropPkts=portsStatsDropsTtlDropPkts, PortIfg=PortIfg, portsStatsBriefLastSampleTimestamp=portsStatsBriefLastSampleTimestamp, EgressVlanTagType=EgressVlanTagType, portsStatsSizeTx10240MaxPkts=portsStatsSizeTx10240MaxPkts, portsStatsUtilTxUtilPctTimes1e4=portsStatsUtilTxUtilPctTimes1e4, portsStatsUtilTable=portsStatsUtilTable, portsStatsSizeRowstatus=portsStatsSizeRowstatus, portMirrorGroup=portMirrorGroup, portsStatsProtoTxIpPkts=portsStatsProtoTxIpPkts, PYSNMP_MODULE_ID=nETOPTICS_XFAM_PORTS_MIB, portsStatsOthersPortNum=portsStatsOthersPortNum, portTxStatus=portTxStatus, portsStatsDropsCounterDropPkts=portsStatsDropsCounterDropPkts, PortDuplexType=PortDuplexType, portsStatsOthersEntry=portsStatsOthersEntry, portsStatsProtoEntry=portsStatsProtoEntry, portsStatsProtoPortNum=portsStatsProtoPortNum, portsStatsUtilTxUtilBps=portsStatsUtilTxUtilBps, String=String, portMode=portMode, portsStatsDropsTxErrorDropPkts=portsStatsDropsTxErrorDropPkts, statsSize=statsSize)
