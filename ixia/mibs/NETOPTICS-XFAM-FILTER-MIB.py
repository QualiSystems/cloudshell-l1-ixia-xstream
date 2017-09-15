#
# PySNMP MIB module NETOPTICS-XFAM-FILTER-MIB (http://pysnmp.sf.net)
# ASN.1 source file://C:\MIBS\text_mibs\NETOPTICS-XFAM-FILTER-MIB.mib
# Produced by pysmi-0.0.6 at Tue Mar 07 21:44:46 2017
# On host ? platform ? version ? by user ?
# Using Python version 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)]
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( Ipv6Address, ) = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
( TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
nETOPTICS_XFAM_FILTER_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1)).setLabel("nETOPTICS-XFAM-FILTER-MIB").setRevisions(("2015-11-10 00:00",))
class Byte(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(-128,127)

class UnsignedByte(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,255)

class UnsignedShort(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)

class ConfdString(OctetString, TextualConvention):
    displayHint = '1t'

class String(OctetString, TextualConvention):
    displayHint = '1t'

class HexList(OctetString, TextualConvention):
    displayHint = '1x:'

class FilterDscpType(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,63)

class FilterDescriptionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class FilterMplsLabelType(OctetString, TextualConvention):
    displayHint = '1t'

class FilterTeidType(OctetString, TextualConvention):
    displayHint = '1t'

class FilterMplsEthertypeType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("all", 3),)

class FilterMplsLabelPositionType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3,)
    namedValues = NamedValues(("any", 1), ("first", 2), ("last", 3),)

class IpProtocolType(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,255)

class FilterRangeNameType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,64)

class FilterPrecedenceType(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,7)

class FilterMplsLabelFilterModeType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("basic", 1), ("extended", 2),)

class FilterGtpPayloadType(OctetString, TextualConvention):
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(2,20)

class DecapsulationType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0,)
    namedValues = NamedValues(("nvgre", 0),)

class PortMaskType(OctetString, TextualConvention):
    displayHint = '1t'

class VlanMaskType(OctetString, TextualConvention):
    displayHint = '1t'

class FilterTosType(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,15)

class FilterRangeIndexType(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,6100)

class EthertypeType(OctetString, TextualConvention):
    displayHint = '1t'

class FilterTcpFlagsType(Bits, TextualConvention):
    namedValues = NamedValues(("fin0", 0), ("syn0", 1), ("rst0", 2), ("psh0", 3), ("ack0", 4), ("urg0", 5), ("fin1", 16), ("syn1", 17), ("rst1", 18), ("psh1", 19), ("ack1", 20), ("urg1", 21),)

class FilterModeType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5,)
    namedValues = NamedValues(("general", 0), ("l2", 1), ("v4", 2), ("v4sipdip", 3), ("l2v4", 4), ("v6", 5),)

class FilterFragmentType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("first-fragment", 0), ("other-fragments", 1), ("all-fragments", 2),)

class FilterIdType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,6100)

class FilterMplsMaxTagsType(Integer32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,5)

class FilterGreProtocolType(OctetString, TextualConvention):
    displayHint = '1t'

class FilterMplsStripType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("a1", 1), ("a2", 2),)

class FilterGtpMsgType(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,255)

class UdfValueType(OctetString, TextualConvention):
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,32)

class FilterTunnelType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("gre", 0), ("gtpv1", 1), ("gtpv2", 2),)

class FilterActionType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2, 3, 4,)
    namedValues = NamedValues(("redir", 1), ("lb", 2), ("drop", 3), ("copy", 4),)

class FilterNameType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,64)

class FilterGroupType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,32)

class L4udfValueType(OctetString, TextualConvention):
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,38)

filterGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 3))
filterGlobalMplsParsing = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 3, 1), TruthValue()).setMaxAccess("readwrite")
filterMode = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 2), FilterModeType()).setMaxAccess("readwrite")
filter = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1))
filterRuleStats = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3))
filterRuleStatsAclMax = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 1), Integer32()).setMaxAccess("readonly")
filterRuleStatsAclUsed = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 2), Integer32()).setMaxAccess("readonly")
filterRuleStatsUserRules = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 3), Integer32()).setMaxAccess("readonly")
filterRuleStatsGeneratedRules = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 4), Integer32()).setMaxAccess("readonly")
filterRuleStatsExpandedRules = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 5), Integer32()).setMaxAccess("readonly")
filterRuleStatsCentiUtilization = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 6), Unsigned32()).setMaxAccess("readonly")
filterRuleStatsAclInfo = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 7), String()).setMaxAccess("readonly")
filterRuleStatsCfgRulesExpanded = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 8), Integer32()).setMaxAccess("readonly")
filterRuleStatsMatchBytesAvailable = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 10), Integer32()).setMaxAccess("readonly")
filterRuleStatsMatchBytesUsed = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 9), Integer32()).setMaxAccess("readonly")
filterRuleStatsCentiParamUtilization = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 3, 11), Unsigned32()).setMaxAccess("readonly")
filterStats = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6))
filterRuleTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1), )
filterRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-FILTER-MIB", "filterRuleId"))
filterRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 1), FilterIdType())
filterRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 2), FilterActionType().clone('redir')).setMaxAccess("readcreate")
filterRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 3), FilterNameType()).setMaxAccess("readcreate")
filterRuleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 4), FilterDescriptionType()).setMaxAccess("readcreate")
filterRuleInPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 5), String()).setMaxAccess("readcreate")
filterRuleRedirPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 6), String()).setMaxAccess("readcreate")
filterRuleGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 7), String()).setMaxAccess("readcreate")
filterRuleEthertype = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 8), EthertypeType()).setMaxAccess("readcreate")
filterRuleIp4Dst = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 9), IpAddress()).setMaxAccess("readcreate")
filterRuleIp4DstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
filterRuleIp4Src = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 11), IpAddress()).setMaxAccess("readcreate")
filterRuleIp4SrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 12), IpAddress()).setMaxAccess("readcreate")
filterRuleIp6Dst = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 13), Ipv6Address()).setMaxAccess("readcreate")
filterRuleIp6DstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 14), Ipv6Address()).setMaxAccess("readcreate")
filterRuleIp6Src = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 15), Ipv6Address()).setMaxAccess("readcreate")
filterRuleIp6SrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 16), Ipv6Address()).setMaxAccess("readcreate")
filterRuleIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 17), IpProtocolType()).setMaxAccess("readcreate")
filterRuleL4DstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 18), UnsignedShort()).setMaxAccess("readcreate")
filterRuleL4DstPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 19), PortMaskType()).setMaxAccess("readcreate")
filterRuleL4DstPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 20), UnsignedShort()).setMaxAccess("readcreate")
filterRuleL4DstPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 21), UnsignedShort()).setMaxAccess("readcreate")
filterRuleL4SrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 22), UnsignedShort()).setMaxAccess("readcreate")
filterRuleL4SrcPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 23), PortMaskType()).setMaxAccess("readcreate")
filterRuleL4SrcPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 24), UnsignedShort()).setMaxAccess("readcreate")
filterRuleL4SrcPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 25), UnsignedShort()).setMaxAccess("readcreate")
filterRuleMacDst = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 26), HexList().subtype(subtypeSpec=ValueSizeConstraint(6,6)).setFixedLength(6)).setMaxAccess("readcreate")
filterRuleMacDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 27), HexList().subtype(subtypeSpec=ValueSizeConstraint(6,6)).setFixedLength(6)).setMaxAccess("readcreate")
filterRuleMacSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 28), HexList().subtype(subtypeSpec=ValueSizeConstraint(6,6)).setFixedLength(6)).setMaxAccess("readcreate")
filterRuleMacSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 29), HexList().subtype(subtypeSpec=ValueSizeConstraint(6,6)).setFixedLength(6)).setMaxAccess("readcreate")
filterRuleUdfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 30), UdfValueType()).setMaxAccess("readcreate")
filterRuleUdfValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 31), UdfValueType()).setMaxAccess("readcreate")
filterRuleVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 32), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(2,4094))).setMaxAccess("readcreate")
filterRuleVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 33), VlanMaskType()).setMaxAccess("readcreate")
filterRuleMplsLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 34), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0,1048575))).setMaxAccess("readcreate")
filterRuleMplsType = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 35), FilterMplsEthertypeType()).setMaxAccess("readcreate")
filterRuleMplsFilterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 36), FilterMplsLabelFilterModeType()).setMaxAccess("readcreate")
filterRuleMplsPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 37), FilterMplsLabelPositionType()).setMaxAccess("readcreate")
filterRuleMplsMaxTags = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 38), FilterMplsMaxTagsType()).setMaxAccess("readcreate")
filterRuleDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 39), FilterDscpType()).setMaxAccess("readcreate")
filterRulePrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 40), FilterPrecedenceType()).setMaxAccess("readcreate")
filterRuleTos = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 41), FilterTosType()).setMaxAccess("readcreate")
filterRuleTcpFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 42), FilterTcpFlagsType()).setMaxAccess("readcreate")
filterRuleTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 43), FilterTunnelType()).setMaxAccess("readcreate")
filterRuleInnerIp4Src = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 44), IpAddress()).setMaxAccess("readcreate")
filterRuleInnerIp4SrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 45), IpAddress()).setMaxAccess("readcreate")
filterRuleInnerIp4Dst = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 46), IpAddress()).setMaxAccess("readcreate")
filterRuleInnerIp4DstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 47), IpAddress()).setMaxAccess("readcreate")
filterRuleInnerIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 48), IpProtocolType()).setMaxAccess("readcreate")
filterRuleGtpTeid = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 49), FilterTeidType()).setMaxAccess("readcreate")
filterRuleGtpTeidMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 50), FilterTeidType()).setMaxAccess("readcreate")
filterRuleGtpMsgType = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 51), FilterGtpMsgType()).setMaxAccess("readcreate")
filterRuleGreProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 52), FilterGreProtocolType()).setMaxAccess("readcreate")
filterRuleL4UdfValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 53), L4udfValueType()).setMaxAccess("readcreate")
filterRuleL4UdfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 54), L4udfValueType()).setMaxAccess("readcreate")
filterRuleGtpPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 55), FilterGtpPayloadType()).setMaxAccess("readcreate")
filterRuleGtpPayloadMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 56), FilterGtpPayloadType()).setMaxAccess("readcreate")
filterRuleMplsLabel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 57), FilterMplsLabelType()).setMaxAccess("readcreate")
filterRuleEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 58), TruthValue()).setMaxAccess("readcreate")
filterRuleFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 59), FilterFragmentType()).setMaxAccess("readcreate")
filterRuleVset = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 60), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(2,4094))).setMaxAccess("readcreate")
filterRuleInnerL4SrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 61), UnsignedShort()).setMaxAccess("readcreate")
filterRuleInnerL4SrcPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 62), PortMaskType()).setMaxAccess("readcreate")
filterRuleInnerL4DstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 63), UnsignedShort()).setMaxAccess("readcreate")
filterRuleInnerL4DstPortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 64), PortMaskType()).setMaxAccess("readcreate")
filterRuleFiltergroup = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 65), FilterGroupType()).setMaxAccess("readcreate")
filterRuleHashprofile = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 66), String().subtype(subtypeSpec=ValueSizeConstraint(0,31))).setMaxAccess("readcreate")
filterRulePcapture = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 67), TruthValue()).setMaxAccess("readcreate")
filterRuleRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
filterstatsTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1), )
filterstatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-FILTER-MIB", "filterstatsId"))
filterstatsId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 1), FilterIdType())
filterstatsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 2), Counter64()).setMaxAccess("readonly")
filterstatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 3), Counter64()).setMaxAccess("readonly")
filterstatsLastSampleTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 4), ConfdString()).setMaxAccess("readonly")
filterstatsLastSampleDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 5), String()).setMaxAccess("readonly")
filterstatsRateBps = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 6), ConfdString()).setMaxAccess("readonly")
filterstatsRatePeakBps = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 7), ConfdString()).setMaxAccess("readonly")
filterstatsRatePeakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 8), String()).setMaxAccess("readonly")
filterstatsRatePeakTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 9), Counter64()).setMaxAccess("readonly")
filterstatsRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 6, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
filtergeneratedRuleTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2), )
filtergeneratedRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2, 1), ).setIndexNames((0, "NETOPTICS-XFAM-FILTER-MIB", "filtergeneratedRuleIndex"))
filtergeneratedRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
filtergeneratedRuleBasis = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2, 1, 2), String()).setMaxAccess("readonly")
filtergeneratedRuleRule = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2, 1, 3), String()).setMaxAccess("readonly")
filtergeneratedRulePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
filtergeneratedRuleBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
filtergeneratedRuleRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 2, 1, 99), RowStatus()).setMaxAccess("readcreate")
filterexpandedRuleTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 4), )
filterexpandedRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 4, 1), ).setIndexNames((0, "NETOPTICS-XFAM-FILTER-MIB", "filterexpandedRuleRuleId"), (0, "NETOPTICS-XFAM-FILTER-MIB", "filterexpandedRuleSubruleId"))
filterexpandedRuleRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 4, 1, 1), FilterIdType())
filterexpandedRuleSubruleId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
filterexpandedRuleRule = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 4, 1, 3), String()).setMaxAccess("readonly")
filterexpandedRuleRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 4, 1, 10), RowStatus()).setMaxAccess("readcreate")
filterfiltergroupsTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 5), )
filterfiltergroupsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 5, 1), ).setIndexNames((1, "NETOPTICS-XFAM-FILTER-MIB", "filterfiltergroupsName"))
filterfiltergroupsName = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 12, 1, 1, 5, 1, 1), FilterGroupType()).setMaxAccess("readonly")
mibBuilder.exportSymbols("NETOPTICS-XFAM-FILTER-MIB", FilterTcpFlagsType=FilterTcpFlagsType, filterRuleStatsCfgRulesExpanded=filterRuleStatsCfgRulesExpanded, filterRuleIp6SrcMask=filterRuleIp6SrcMask, filterRuleMplsLabel2=filterRuleMplsLabel2, filterRuleVlan=filterRuleVlan, filterRuleIp4Dst=filterRuleIp4Dst, filterRuleId=filterRuleId, filterRuleStatsGeneratedRules=filterRuleStatsGeneratedRules, filterRuleTable=filterRuleTable, filterRuleVlanMask=filterRuleVlanMask, filterRuleL4DstPortStart=filterRuleL4DstPortStart, FilterMplsStripType=FilterMplsStripType, filterexpandedRuleRule=filterexpandedRuleRule, filterRuleMplsType=filterRuleMplsType, filterRuleIp6Src=filterRuleIp6Src, filterRuleL4SrcPortStart=filterRuleL4SrcPortStart, filterStats=filterStats, filterstatsId=filterstatsId, filterRuleFiltergroup=filterRuleFiltergroup, filtergeneratedRuleRule=filtergeneratedRuleRule, PYSNMP_MODULE_ID=nETOPTICS_XFAM_FILTER_MIB, filterRuleL4SrcPortEnd=filterRuleL4SrcPortEnd, filterstatsRatePeakTime=filterstatsRatePeakTime, filtergeneratedRuleBasis=filtergeneratedRuleBasis, FilterRangeIndexType=FilterRangeIndexType, filterfiltergroupsTable=filterfiltergroupsTable, filterRulePrecedence=filterRulePrecedence, ConfdString=ConfdString, FilterGroupType=FilterGroupType, filtergeneratedRulePackets=filtergeneratedRulePackets, FilterMplsLabelFilterModeType=FilterMplsLabelFilterModeType, filterRuleGtpMsgType=filterRuleGtpMsgType, filterRuleStatsMatchBytesAvailable=filterRuleStatsMatchBytesAvailable, filterMode=filterMode, filterRuleGtpPayloadMask=filterRuleGtpPayloadMask, filterRuleName=filterRuleName, filterRuleL4UdfMask=filterRuleL4UdfMask, filterRuleHashprofile=filterRuleHashprofile, filterRuleGtpTeidMask=filterRuleGtpTeidMask, filterexpandedRuleRowstatus=filterexpandedRuleRowstatus, filterRulePcapture=filterRulePcapture, EthertypeType=EthertypeType, filterstatsLastSampleTimestamp=filterstatsLastSampleTimestamp, FilterMplsMaxTagsType=FilterMplsMaxTagsType, filterRuleL4SrcPortMask=filterRuleL4SrcPortMask, FilterNameType=FilterNameType, filterstatsRateBps=filterstatsRateBps, filterfiltergroupsName=filterfiltergroupsName, filterRuleDescription=filterRuleDescription, filterRuleL4DstPort=filterRuleL4DstPort, filterRuleDscp=filterRuleDscp, FilterGtpPayloadType=FilterGtpPayloadType, filterRuleStatsCentiUtilization=filterRuleStatsCentiUtilization, L4udfValueType=L4udfValueType, filterRuleStatsUserRules=filterRuleStatsUserRules, filterRuleIp6Dst=filterRuleIp6Dst, filterRuleEntry=filterRuleEntry, filterRuleIp4SrcMask=filterRuleIp4SrcMask, filterRuleGtpTeid=filterRuleGtpTeid, DecapsulationType=DecapsulationType, UnsignedByte=UnsignedByte, filterRuleStats=filterRuleStats, FilterGtpMsgType=FilterGtpMsgType, filtergeneratedRuleTable=filtergeneratedRuleTable, filterRuleStatsAclMax=filterRuleStatsAclMax, filterexpandedRuleTable=filterexpandedRuleTable, filterRuleStatsAclInfo=filterRuleStatsAclInfo, FilterGreProtocolType=FilterGreProtocolType, filterRuleMacDstMask=filterRuleMacDstMask, filterstatsTable=filterstatsTable, filterstatsPackets=filterstatsPackets, FilterIdType=FilterIdType, FilterDescriptionType=FilterDescriptionType, Byte=Byte, filterRuleRedirPorts=filterRuleRedirPorts, filterRuleTunnelType=filterRuleTunnelType, filterGlobalMplsParsing=filterGlobalMplsParsing, UdfValueType=UdfValueType, filterstatsLastSampleDateTime=filterstatsLastSampleDateTime, filterstatsRowstatus=filterstatsRowstatus, filterRuleVset=filterRuleVset, filterRuleMplsFilterMode=filterRuleMplsFilterMode, IpProtocolType=IpProtocolType, FilterTosType=FilterTosType, filterRuleL4DstPortMask=filterRuleL4DstPortMask, filterRuleEnabled=filterRuleEnabled, filterRuleIp4Src=filterRuleIp4Src, filterstatsBytes=filterstatsBytes, filterRuleMplsPosition=filterRuleMplsPosition, FilterTunnelType=FilterTunnelType, filterexpandedRuleSubruleId=filterexpandedRuleSubruleId, filterRuleStatsAclUsed=filterRuleStatsAclUsed, filter=filter, filterfiltergroupsEntry=filterfiltergroupsEntry, filterRuleInnerL4DstPortMask=filterRuleInnerL4DstPortMask, filterRuleInnerIp4DstMask=filterRuleInnerIp4DstMask, filterRuleInnerIp4Src=filterRuleInnerIp4Src, filterRuleIpProtocol=filterRuleIpProtocol, FilterMplsLabelType=FilterMplsLabelType, HexList=HexList, filterRuleAction=filterRuleAction, FilterActionType=FilterActionType, filterRuleUdfValue=filterRuleUdfValue, PortMaskType=PortMaskType, filterRuleStatsExpandedRules=filterRuleStatsExpandedRules, FilterMplsLabelPositionType=FilterMplsLabelPositionType, filterexpandedRuleRuleId=filterexpandedRuleRuleId, filterRuleRowstatus=filterRuleRowstatus, filterexpandedRuleEntry=filterexpandedRuleEntry, FilterTeidType=FilterTeidType, filterstatsRatePeakBps=filterstatsRatePeakBps, filterstatsEntry=filterstatsEntry, filterRuleMacDst=filterRuleMacDst, UnsignedShort=UnsignedShort, filterRuleInnerIp4SrcMask=filterRuleInnerIp4SrcMask, filtergeneratedRuleRowstatus=filtergeneratedRuleRowstatus, filterRuleMplsMaxTags=filterRuleMplsMaxTags, filterRuleUdfMask=filterRuleUdfMask, filterRuleTos=filterRuleTos, FilterDscpType=FilterDscpType, filtergeneratedRuleEntry=filtergeneratedRuleEntry, filtergeneratedRuleBytes=filtergeneratedRuleBytes, filterRuleStatsCentiParamUtilization=filterRuleStatsCentiParamUtilization, filterRuleGreProtocolType=filterRuleGreProtocolType, FilterMplsEthertypeType=FilterMplsEthertypeType, filterRuleMacSrc=filterRuleMacSrc, filterRuleStatsMatchBytesUsed=filterRuleStatsMatchBytesUsed, filterRuleGtpPayload=filterRuleGtpPayload, FilterPrecedenceType=FilterPrecedenceType, VlanMaskType=VlanMaskType, filterRuleIp4DstMask=filterRuleIp4DstMask, FilterFragmentType=FilterFragmentType, filterRuleMplsLabel=filterRuleMplsLabel, filterRuleGroups=filterRuleGroups, filterRuleInnerIp4Dst=filterRuleInnerIp4Dst, filterRuleInnerL4SrcPortMask=filterRuleInnerL4SrcPortMask, filterRuleL4UdfValue=filterRuleL4UdfValue, FilterRangeNameType=FilterRangeNameType, filtergeneratedRuleIndex=filtergeneratedRuleIndex, filterRuleInnerL4SrcPort=filterRuleInnerL4SrcPort, filterRuleInnerL4DstPort=filterRuleInnerL4DstPort, filterRuleMacSrcMask=filterRuleMacSrcMask, filterRuleL4SrcPort=filterRuleL4SrcPort, filterRuleEthertype=filterRuleEthertype, filterRuleL4DstPortEnd=filterRuleL4DstPortEnd, filterRuleFragment=filterRuleFragment, filterGlobal=filterGlobal, nETOPTICS_XFAM_FILTER_MIB=nETOPTICS_XFAM_FILTER_MIB, filterRuleInnerIpProtocol=filterRuleInnerIpProtocol, FilterModeType=FilterModeType, filterRuleTcpFlags=filterRuleTcpFlags, String=String, filterRuleIp6DstMask=filterRuleIp6DstMask, filterstatsRatePeakTimestamp=filterstatsRatePeakTimestamp, filterRuleInPorts=filterRuleInPorts)
