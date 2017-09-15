#
# PySNMP MIB module NETOPTICS-XFAM-DEVICE-MIB (http://pysnmp.sf.net)
# ASN.1 source file://C:\MIBS\text_mibs\NETOPTICS-XFAM-DEVICE-MIB.mib
# Produced by pysmi-0.0.6 at Tue Mar 07 16:46:34 2017
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
nETOPTICS_XFAM_DEVICE_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3)).setLabel("nETOPTICS-XFAM-DEVICE-MIB").setRevisions(("2015-11-20 00:00",))
class UnsignedShort(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)

class ConfdString(OctetString, TextualConvention):
    displayHint = '1t'

class InetAddressIP(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),)
class String(OctetString, TextualConvention):
    displayHint = '1t'

class HexList(OctetString, TextualConvention):
    displayHint = '1x:'

class HwRevisionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class ModelNumberType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class Note1Type(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class Note2Type(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class Note3Type(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class MgmtPortSpeedStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 10, 100, 1000,)
    namedValues = NamedValues(("na", 0), ("a10Mbps", 10), ("a100Mbps", 100), ("a1000Mbps", 1000),)

class MgmtPortAutoNegCfgType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("off", 1), ("on", 2),)

class InstallationDateTimeType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,19)

class DeviceNtpstatReportType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,512)

class DeviceModelNameType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 4, 9, 11, 12, 13,)
    namedValues = NamedValues(("unknown", 0), ("directorxStream", 4), ("xBalancer", 9), ("iLinkAggxStream", 11), ("xStream", 12), ("xStream40", 13),)

class DeviceConsoleBaudrateType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,10)

class MgmtPortSpeedCfgType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(10, 100, 1000,)
    namedValues = NamedValues(("a10Mbps", 10), ("a100Mbps", 100), ("a1000Mbps", 1000),)

class ModelNameType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class ManufacturingDetailsType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class DeviceCurrentTimeDateType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,99)

class HwBuildDateType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class NtpServerStateCfgType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("enable", 1), ("disable", 2),)

class MgmtPortLinkStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1,)
    namedValues = NamedValues(("down", 0), ("up", 1),)

class CpldVersionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class FpgaVersionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class InstallerNameType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,32)

class DeviceTimeDateSourceType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("local", 1), ("fromNtp", 2),)

class CpuTypeType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class NtpKeyIdType(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,65534)

class NtpKeyValueType(OctetString, TextualConvention):
    displayHint = '1t'

class DeviceNtpRunstateType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,32)

class DevicePtpRunStateType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,32)

class MgmtPortDuplexCfgType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("half", 1), ("full", 2),)

class MgmtPortDuplexStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("none", 0), ("half", 1), ("full", 2),)

class DeviceTimezoneType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,128)

class HexByteType(OctetString, TextualConvention):
    displayHint = '1t'

class SerialNumberType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class MgmtPortAutoNegStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("none", 0), ("off", 1), ("on", 2),)

class HwModelNameType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,31)

class Time24hType(OctetString, TextualConvention):
    displayHint = '1t'

class DateMMDDYY2037Type(OctetString, TextualConvention):
    displayHint = '1t'

class Ipv6PrefixLenType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,128)

class NtpAuthType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1,)
    namedValues = NamedValues(("none", 0), ("symmetric-keys", 1),)

class NtpKeyDigestType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2,)
    namedValues = NamedValues(("md5", 0), ("sha", 1), ("sha1", 2),)

class NtpSrvIdType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,3)

class NtpAdminCfgType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("enable", 1), ("disable", 2),)

class PtpAdminCfgType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("enable", 1), ("disable", 2),)

class PtpInterfaceType(OctetString, TextualConvention):
    displayHint = '1t'

device = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1))
deviceTimeDate = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1))
deviceTimeDateCurrentTimeAndDate = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 1), DeviceCurrentTimeDateType()).setMaxAccess("readonly")
deviceTimeDateZone = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 2), DeviceTimezoneType()).setMaxAccess("readwrite")
deviceTimeDateNtp = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3))
deviceTimeDateNtpAdmin = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 1), NtpAdminCfgType()).setMaxAccess("readwrite")
deviceTimeDateNtpAuthType = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 4), NtpAuthType()).setMaxAccess("readwrite")
deviceTimeDateNtpNtpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 3))
deviceTimeDateNtpNtpStatusRunstate = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 3, 1), DeviceNtpRunstateType()).setMaxAccess("readonly")
deviceTimeDateNtpNtpStatusNtpstatReport = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 3, 2), DeviceNtpstatReportType()).setMaxAccess("readonly")
deviceTimeDatePtp = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5))
deviceTimeDatePtpAdmin = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 1), PtpAdminCfgType()).setMaxAccess("readwrite")
deviceTimeDatePtpPtpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2))
deviceTimeDatePtpPtpStatusRunState = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2, 1), DevicePtpRunStateType()).setMaxAccess("readonly")
deviceTimeDatePtpPtpStatusMasterIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2, 2), IpAddress()).setMaxAccess("readonly")
deviceTimeDatePtpPtpStatusMasterMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2, 3), String()).setMaxAccess("readonly")
deviceTimeDatePtpPtpStatusCurrentOffset = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2, 4), ConfdString()).setMaxAccess("readonly")
deviceTimeDatePtpPtpStatusCurrentPathDelay = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2, 5), ConfdString()).setMaxAccess("readonly")
deviceTimeDatePtpPtpStatusLastValidSyncTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2, 6), ConfdString()).setMaxAccess("readonly")
deviceTimeDatePtpPtpStatusLastValidSyncDateTime = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 5, 2, 7), String()).setMaxAccess("readonly")
deviceMgmtPort = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2))
deviceMgmtPortSpeed = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 1), MgmtPortSpeedCfgType()).setMaxAccess("readwrite")
deviceMgmtPortDuplex = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 2), MgmtPortDuplexCfgType()).setMaxAccess("readwrite")
deviceMgmtPortStats = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 3))
deviceMgmtPortStatsRxTotal = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 3, 1), ConfdString()).setMaxAccess("readonly")
deviceMgmtPortStatsRxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 3, 2), ConfdString()).setMaxAccess("readonly")
deviceMgmtPortStatsRxOtherErrors = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 3, 3), ConfdString()).setMaxAccess("readonly")
deviceMgmtPortStatsTxTotal = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 3, 4), ConfdString()).setMaxAccess("readonly")
deviceMgmtPortStatsTxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 3, 5), ConfdString()).setMaxAccess("readonly")
deviceMgmtPortStatsTxOtherErrors = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 3, 6), ConfdString()).setMaxAccess("readonly")
deviceMgmtPortStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 4))
deviceMgmtPortStatusSpeed = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 4, 1), MgmtPortSpeedStatusType()).setMaxAccess("readonly")
deviceMgmtPortStatusDuplex = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 4, 2), MgmtPortDuplexStatusType()).setMaxAccess("readonly")
deviceMgmtPortStatusAutoNeg = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 2, 4, 3), MgmtPortAutoNegStatusType()).setMaxAccess("readonly")
deviceSysIp = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 3))
deviceSysIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 3, 1), IpAddress()).setMaxAccess("readonly")
deviceSysIpNetMask = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 3, 2), IpAddress()).setMaxAccess("readonly")
deviceSysIpGateway = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 3, 3), IpAddress()).setMaxAccess("readonly")
deviceSysIpIp6Address = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 3, 4), Ipv6Address()).setMaxAccess("readonly")
deviceSysIpIp6PrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 3, 5), Ipv6PrefixLenType()).setMaxAccess("readonly")
deviceSysIpMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 3, 6), HexList()).setMaxAccess("readonly")
deviceHwInventory = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6))
deviceHwInventoryMfgModelName = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 11), HwModelNameType()).setMaxAccess("readonly")
deviceHwInventoryModelName = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 1), HwModelNameType()).setMaxAccess("readonly")
deviceHwInventoryModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 2), ModelNumberType()).setMaxAccess("readonly")
deviceHwInventorySerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 3), SerialNumberType()).setMaxAccess("readonly")
deviceHwInventoryHwBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 4), HwBuildDateType()).setMaxAccess("readonly")
deviceHwInventoryHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 5), HwRevisionType()).setMaxAccess("readonly")
deviceHwInventoryFpgaVersion = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 6), FpgaVersionType()).setMaxAccess("readonly")
deviceHwInventoryCpldVersion = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 7), CpldVersionType()).setMaxAccess("readonly")
deviceHwInventoryCpuType = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 10), CpuTypeType()).setMaxAccess("readonly")
deviceHwInventoryManufacturingDetails = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 8), ManufacturingDetailsType()).setMaxAccess("readonly")
deviceHwInventoryNumFans = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 6, 9), Unsigned32()).setMaxAccess("readonly")
deviceHwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8))
deviceHwStatusMemUsage = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 4))
deviceHwStatusMemUsageTotalMem = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 4, 1), Unsigned32()).setMaxAccess("readonly")
deviceHwStatusMemUsageUsedMem = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 4, 2), Unsigned32()).setMaxAccess("readonly")
deviceHwStatusMemUsageFreeMem = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 4, 3), Unsigned32()).setMaxAccess("readonly")
deviceInstallation = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 7))
deviceInstallationInstallerName = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 7, 1), InstallerNameType()).setMaxAccess("readwrite")
deviceInstallationInstallationDateTime = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 7, 2), InstallationDateTimeType()).setMaxAccess("readwrite")
deviceInstallationNote1 = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 7, 3), Note1Type()).setMaxAccess("readwrite")
deviceInstallationNote2 = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 7, 4), Note2Type()).setMaxAccess("readwrite")
deviceInstallationNote3 = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 7, 5), Note3Type()).setMaxAccess("readwrite")
deviceSfp = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4))
deviceSsh = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 5))
deviceSshExtraSSHEnabled = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 5, 2), TruthValue()).setMaxAccess("readwrite")
deviceSshExtraSSHPort = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 5, 1), UnsignedShort()).setMaxAccess("readwrite")
deviceSshExtraSSHCiphers = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 5, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1,)).clone(namedValues=NamedValues(("all", 0), ("fips140-2", 1),))).setMaxAccess("readwrite")
deviceSshExtraSSHMacs = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 5, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1,)).clone(namedValues=NamedValues(("all", 0), ("fips140-2", 1),))).setMaxAccess("readwrite")
deviceConsolePort = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 9))
deviceConsolePortBaudrate = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 9, 1), DeviceConsoleBaudrateType()).setMaxAccess("readwrite")
deviceConsolePortCurrentBaudrate = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 9, 2), DeviceConsoleBaudrateType()).setMaxAccess("readonly")
devicePlatformInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 10))
deviceTimedateZoneListTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 4), )
deviceTimedateZoneListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 4, 1), ).setIndexNames((0, "NETOPTICS-XFAM-DEVICE-MIB", "deviceTimedateZoneListZoneindex"))
deviceTimedateZoneListZoneindex = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
deviceTimedateZoneListZoneFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 4, 1, 2), DeviceTimezoneType()).setMaxAccess("readonly")
deviceNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2), )
deviceNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1), ).setIndexNames((0, "NETOPTICS-XFAM-DEVICE-MIB", "deviceNtpServerId"))
deviceNtpServerId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 1), NtpSrvIdType())
deviceNtpServerIpaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 2), InetAddressIP()).setMaxAccess("readcreate")
deviceNtpServerPolling = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 3), NtpServerStateCfgType().clone('enable')).setMaxAccess("readcreate")
deviceNtpServerKey = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 4), TruthValue()).setMaxAccess("readcreate")
deviceNtpServerKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 6), NtpKeyDigestType()).setMaxAccess("readcreate")
deviceNtpServerKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 5), NtpKeyIdType()).setMaxAccess("readcreate")
deviceNtpServerKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 7), NtpKeyValueType()).setMaxAccess("readcreate")
deviceNtpServerRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 1, 3, 2, 1, 99), RowStatus()).setMaxAccess("readcreate")
deviceInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11), )
deviceInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1), ).setIndexNames((1, "NETOPTICS-XFAM-DEVICE-MIB", "deviceInterfaceIfName"))
deviceInterfaceIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 1), String().subtype(subtypeSpec=ValueSizeConstraint(4,7)))
deviceInterfaceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 2), String().subtype(subtypeSpec=ValueSizeConstraint(0,255))).setMaxAccess("readcreate")
deviceInterfaceEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 3), TruthValue()).setMaxAccess("readcreate")
deviceInterfaceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 4), IpAddress()).setMaxAccess("readcreate")
deviceInterfaceNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 5), IpAddress()).setMaxAccess("readcreate")
deviceInterfaceGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 6), IpAddress()).setMaxAccess("readcreate")
deviceInterfaceIp6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 7), Ipv6Address()).setMaxAccess("readcreate")
deviceInterfaceIp6PrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 8), Ipv6PrefixLenType()).setMaxAccess("readcreate")
deviceInterfaceRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 11, 1, 99), RowStatus()).setMaxAccess("readcreate")
deviceFanTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1), )
deviceFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-DEVICE-MIB", "deviceFanFanNum"))
deviceFanFanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1, 1, 1), Unsigned32())
deviceFanDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1, 1, 2), String()).setMaxAccess("readonly")
deviceFanRpm = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1, 1, 3), Integer32()).setMaxAccess("readonly")
deviceFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2, 3,)).clone(namedValues=NamedValues(("na", 0), ("empty", 1), ("ok", 2), ("alarm", 3),))).setMaxAccess("readonly")
deviceFanLastFailureDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1, 1, 5), String()).setMaxAccess("readonly")
deviceFanRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
devicePsuTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2), )
devicePsuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1), ).setIndexNames((0, "NETOPTICS-XFAM-DEVICE-MIB", "devicePsuPsuNum"))
devicePsuPsuNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 1), Unsigned32())
devicePsuDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 2), String()).setMaxAccess("readonly")
devicePsuVoltageMilliVolts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 3), Integer32()).setMaxAccess("readonly")
devicePsuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2, 3,)).clone(namedValues=NamedValues(("psuNa", 0), ("empty", 1), ("ok", 2), ("alarm", 3),))).setMaxAccess("readonly")
devicePsuLastFailureDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 5), String()).setMaxAccess("readonly")
devicePsuLowThresholdMilliVolts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 6), Integer32()).setMaxAccess("readonly")
devicePsuHighThresholdMilliVolts = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 7), Integer32()).setMaxAccess("readonly")
devicePsuRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
deviceTempSensorTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3), )
deviceTempSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1), ).setIndexNames((0, "NETOPTICS-XFAM-DEVICE-MIB", "deviceTempSensorSensorNum"))
deviceTempSensorSensorNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 1), Unsigned32())
deviceTempSensorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 2), String()).setMaxAccess("readonly")
deviceTempSensorTemperatureMilliDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 3), Integer32()).setMaxAccess("readonly")
deviceTempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 4), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2, 3,)).clone(namedValues=NamedValues(("na", 0), ("empty", 1), ("ok", 2), ("alarm", 3),))).setMaxAccess("readonly")
deviceTempSensorLastFailureDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 5), String()).setMaxAccess("readonly")
deviceTempSensorLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 6), Integer32()).setMaxAccess("readonly")
deviceTempSensorHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 7), Integer32()).setMaxAccess("readonly")
deviceTempSensorRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
deviceCpuUsageTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5), )
deviceCpuUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1), ).setIndexNames((0, "NETOPTICS-XFAM-DEVICE-MIB", "deviceCpuUsageIndex"))
deviceCpuUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
deviceCpuUsageCpuId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1, 2), String()).setMaxAccess("readonly")
deviceCpuUsageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1, 3), String()).setMaxAccess("readonly")
deviceCpuUsageUserCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1, 4), ConfdString()).setMaxAccess("readonly")
deviceCpuUsageSystemCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1, 5), ConfdString()).setMaxAccess("readonly")
deviceCpuUsageIdleCpu = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1, 6), ConfdString()).setMaxAccess("readonly")
deviceCpuUsageRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 8, 5, 1, 99), RowStatus()).setMaxAccess("readcreate")
deviceSfpTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1), )
deviceSfpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1), ).setIndexNames((0, "NETOPTICS-XFAM-DEVICE-MIB", "deviceSfpPortNum"))
deviceSfpPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,64)))
deviceSfpSfpState = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2,)).clone(namedValues=NamedValues(("not-connected", 0), ("sfp-connected", 1), ("qsfp-connected", 2),))).setMaxAccess("readonly")
deviceSfpLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2, 3,)).clone(namedValues=NamedValues(("na", 0), ("linkUp", 1), ("linkDown", 2), ("linkRxDown", 3),))).setMaxAccess("readonly")
deviceSfpSfpTrxId = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpLength50um = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 7), UnsignedShort()).setMaxAccess("readonly")
deviceSfpSfpLength625um = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 8), UnsignedShort()).setMaxAccess("readonly")
deviceSfpSfpLengthOM3 = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 9), UnsignedShort()).setMaxAccess("readonly")
deviceSfpSfpVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 10), String().subtype(subtypeSpec=ValueSizeConstraint(0,16))).setMaxAccess("readonly")
deviceSfpSfpVendorOui = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 11), String().subtype(subtypeSpec=ValueSizeConstraint(0,16))).setMaxAccess("readonly")
deviceSfpSfpVendorPN = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 12), String().subtype(subtypeSpec=ValueSizeConstraint(0,16))).setMaxAccess("readonly")
deviceSfpSfpPartRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 13), String().subtype(subtypeSpec=ValueSizeConstraint(0,16))).setMaxAccess("readonly")
deviceSfpSfpVendorSN = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 14), String().subtype(subtypeSpec=ValueSizeConstraint(0,16))).setMaxAccess("readonly")
deviceSfpSfpDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 15), String().subtype(subtypeSpec=ValueSizeConstraint(0,16))).setMaxAccess("readonly")
deviceSfpSfpSFF8472Rev = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 16), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpRtAlarmFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 17), String().subtype(subtypeSpec=ValueSizeConstraint(0,256))).setMaxAccess("readonly")
deviceSfpSfpRtWarningFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 18), String().subtype(subtypeSpec=ValueSizeConstraint(0,256))).setMaxAccess("readonly")
deviceSfpSfpDiagMonitorType = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 19), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpRtTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 20), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpRtVcc = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 21), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpRtTxBiasCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 22), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpRtTxOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 23), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpRtRxInputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 24), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpTrx10GEnetCompliance = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 25), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpTrxEnetCompliance = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 26), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpTrxFibreLinkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 27), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpTrxFibreTechnology = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 28), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpTrxSfpCableTechnology = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 29), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpTrxFibreTxMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 30), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpTrxFibreSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 31), String().subtype(subtypeSpec=ValueSizeConstraint(0,100))).setMaxAccess("readonly")
deviceSfpSfpRtTemperatureMilliDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 32), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtVccMilliVolt = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 33), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtTxBiasCurrentMilliMA = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 34), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtTxBiasCurrent2MilliMA = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 35), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtTxBiasCurrent3MilliMA = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 36), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtTxBiasCurrent4MilliMA = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 37), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtTxOutputPowerCentiDBm = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 38), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtRxInputPowerCentiDBm = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 39), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtRxInputPower2CentiDBm = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 40), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtRxInputPower3CentiDBm = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 41), Integer32()).setMaxAccess("readonly")
deviceSfpSfpRtRxInputPower4CentiDBm = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 42), Integer32()).setMaxAccess("readonly")
deviceSfpRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 4, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
devicePlatformInfoAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 10, 1), )
devicePlatformInfoAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 10, 1, 1), ).setIndexNames((1, "NETOPTICS-XFAM-DEVICE-MIB", "devicePlatformInfoAttributeName"))
devicePlatformInfoAttributeName = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 10, 1, 1, 1), String())
devicePlatformInfoAttributeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 10, 1, 1, 2), String()).setMaxAccess("readonly")
devicePlatformInfoAttributeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 2, 3, 1, 10, 1, 1, 3), String()).setMaxAccess("readonly")
mibBuilder.exportSymbols("NETOPTICS-XFAM-DEVICE-MIB", HwRevisionType=HwRevisionType, HexByteType=HexByteType, deviceTempSensorRowstatus=deviceTempSensorRowstatus, deviceSfpSfpTrxSfpCableTechnology=deviceSfpSfpTrxSfpCableTechnology, deviceInterfaceTable=deviceInterfaceTable, deviceSysIpGateway=deviceSysIpGateway, HexList=HexList, deviceSfpSfpLengthOM3=deviceSfpSfpLengthOM3, deviceNtpServerTable=deviceNtpServerTable, deviceSfpSfpRtTxBiasCurrent2MilliMA=deviceSfpSfpRtTxBiasCurrent2MilliMA, deviceCpuUsageRowstatus=deviceCpuUsageRowstatus, deviceHwInventory=deviceHwInventory, deviceSfpSfpTrxFibreLinkLength=deviceSfpSfpTrxFibreLinkLength, deviceMgmtPortStatus=deviceMgmtPortStatus, deviceHwInventoryCpldVersion=deviceHwInventoryCpldVersion, deviceFanTable=deviceFanTable, devicePsuTable=devicePsuTable, deviceSfpPortNum=deviceSfpPortNum, deviceNtpServerId=deviceNtpServerId, FpgaVersionType=FpgaVersionType, deviceSfpSfpRtRxInputPower=deviceSfpSfpRtRxInputPower, deviceTimeDateNtpAuthType=deviceTimeDateNtpAuthType, deviceTimeDateNtpAdmin=deviceTimeDateNtpAdmin, deviceHwStatus=deviceHwStatus, deviceSfpSfpRtTemperature=deviceSfpSfpRtTemperature, deviceTimeDateNtp=deviceTimeDateNtp, deviceFanRowstatus=deviceFanRowstatus, NtpKeyIdType=NtpKeyIdType, deviceInterfaceDescription=deviceInterfaceDescription, deviceTimeDatePtpPtpStatusLastValidSyncDateTime=deviceTimeDatePtpPtpStatusLastValidSyncDateTime, deviceHwStatusMemUsageUsedMem=deviceHwStatusMemUsageUsedMem, devicePsuLastFailureDateTime=devicePsuLastFailureDateTime, deviceInterfaceNetMask=deviceInterfaceNetMask, DeviceConsoleBaudrateType=DeviceConsoleBaudrateType, deviceSfpSfpTrxEnetCompliance=deviceSfpSfpTrxEnetCompliance, deviceInstallationNote1=deviceInstallationNote1, deviceHwInventoryMfgModelName=deviceHwInventoryMfgModelName, MgmtPortAutoNegCfgType=MgmtPortAutoNegCfgType, MgmtPortSpeedCfgType=MgmtPortSpeedCfgType, devicePsuStatus=devicePsuStatus, Note2Type=Note2Type, ConfdString=ConfdString, deviceInterfaceIfName=deviceInterfaceIfName, deviceCpuUsageIndex=deviceCpuUsageIndex, deviceMgmtPortStatsRxTotal=deviceMgmtPortStatsRxTotal, deviceSysIpAddress=deviceSysIpAddress, deviceSfpSfpRtRxInputPower4CentiDBm=deviceSfpSfpRtRxInputPower4CentiDBm, deviceSfpSfpTrxFibreTxMedia=deviceSfpSfpTrxFibreTxMedia, deviceTimeDateCurrentTimeAndDate=deviceTimeDateCurrentTimeAndDate, deviceSfpSfpSFF8472Rev=deviceSfpSfpSFF8472Rev, deviceInterfaceEntry=deviceInterfaceEntry, deviceFanEntry=deviceFanEntry, deviceConsolePort=deviceConsolePort, deviceHwStatusMemUsageTotalMem=deviceHwStatusMemUsageTotalMem, deviceTimeDate=deviceTimeDate, deviceHwInventoryManufacturingDetails=deviceHwInventoryManufacturingDetails, deviceNtpServerKeyId=deviceNtpServerKeyId, deviceTimeDatePtpPtpStatusMasterMacAddr=deviceTimeDatePtpPtpStatusMasterMacAddr, deviceSfpSfpRtTxBiasCurrent=deviceSfpSfpRtTxBiasCurrent, deviceInstallationInstallationDateTime=deviceInstallationInstallationDateTime, deviceHwInventoryNumFans=deviceHwInventoryNumFans, deviceSfpSfpRtTxBiasCurrent4MilliMA=deviceSfpSfpRtTxBiasCurrent4MilliMA, deviceFanStatus=deviceFanStatus, deviceSshExtraSSHMacs=deviceSshExtraSSHMacs, deviceHwInventoryFpgaVersion=deviceHwInventoryFpgaVersion, deviceSysIpNetMask=deviceSysIpNetMask, deviceSfpSfpVendorPN=deviceSfpSfpVendorPN, deviceInstallationInstallerName=deviceInstallationInstallerName, devicePlatformInfoAttributeName=devicePlatformInfoAttributeName, deviceSfpSfpVendorOui=deviceSfpSfpVendorOui, deviceSfpSfpRtTxBiasCurrentMilliMA=deviceSfpSfpRtTxBiasCurrentMilliMA, deviceCpuUsageEntry=deviceCpuUsageEntry, deviceSfpSfpState=deviceSfpSfpState, deviceTimeDatePtpPtpStatus=deviceTimeDatePtpPtpStatus, InstallationDateTimeType=InstallationDateTimeType, deviceCpuUsageIdleCpu=deviceCpuUsageIdleCpu, deviceSfpSfpDiagMonitorType=deviceSfpSfpDiagMonitorType, deviceMgmtPortStatsTxCrcErrors=deviceMgmtPortStatsTxCrcErrors, DeviceTimeDateSourceType=DeviceTimeDateSourceType, deviceSshExtraSSHPort=deviceSshExtraSSHPort, deviceSfpSfpTrx10GEnetCompliance=deviceSfpSfpTrx10GEnetCompliance, deviceMgmtPortStatsTxOtherErrors=deviceMgmtPortStatsTxOtherErrors, devicePsuLowThresholdMilliVolts=devicePsuLowThresholdMilliVolts, NtpKeyValueType=NtpKeyValueType, devicePsuDescription=devicePsuDescription, deviceHwStatusMemUsage=deviceHwStatusMemUsage, deviceNtpServerIpaddr=deviceNtpServerIpaddr, deviceHwInventoryHwBuildDate=deviceHwInventoryHwBuildDate, devicePlatformInfoAttributeTable=devicePlatformInfoAttributeTable, deviceSfpSfpRtTxOutputPowerCentiDBm=deviceSfpSfpRtTxOutputPowerCentiDBm, NtpSrvIdType=NtpSrvIdType, deviceSfpSfpRtWarningFlags=deviceSfpSfpRtWarningFlags, deviceMgmtPortStatsRxOtherErrors=deviceMgmtPortStatsRxOtherErrors, Note1Type=Note1Type, deviceSfpSfpPartRevision=deviceSfpSfpPartRevision, deviceSfpSfpRtRxInputPowerCentiDBm=deviceSfpSfpRtRxInputPowerCentiDBm, deviceMgmtPortStatusAutoNeg=deviceMgmtPortStatusAutoNeg, CpldVersionType=CpldVersionType, deviceInstallationNote3=deviceInstallationNote3, deviceTimeDatePtpPtpStatusMasterIpAddr=deviceTimeDatePtpPtpStatusMasterIpAddr, deviceTimeDatePtp=deviceTimeDatePtp, deviceSfpSfpRtVcc=deviceSfpSfpRtVcc, deviceFanLastFailureDateTime=deviceFanLastFailureDateTime, deviceMgmtPortStatusDuplex=deviceMgmtPortStatusDuplex, deviceTempSensorStatus=deviceTempSensorStatus, deviceSfpSfpRtRxInputPower3CentiDBm=deviceSfpSfpRtRxInputPower3CentiDBm, deviceMgmtPortDuplex=deviceMgmtPortDuplex, deviceInstallation=deviceInstallation, deviceTimedateZoneListTable=deviceTimedateZoneListTable, deviceSfpSfpRtTxBiasCurrent3MilliMA=deviceSfpSfpRtTxBiasCurrent3MilliMA, HwBuildDateType=HwBuildDateType, deviceSshExtraSSHEnabled=deviceSshExtraSSHEnabled, deviceHwInventoryModelNumber=deviceHwInventoryModelNumber, deviceTimedateZoneListZoneindex=deviceTimedateZoneListZoneindex, deviceTempSensorHighThreshold=deviceTempSensorHighThreshold, deviceSfpSfpRtVccMilliVolt=deviceSfpSfpRtVccMilliVolt, DateMMDDYY2037Type=DateMMDDYY2037Type, deviceCpuUsageCpuId=deviceCpuUsageCpuId, deviceFanFanNum=deviceFanFanNum, deviceSysIpIp6Address=deviceSysIpIp6Address, deviceSfpSfpVendorName=deviceSfpSfpVendorName, deviceMgmtPortStatusSpeed=deviceMgmtPortStatusSpeed, MgmtPortDuplexCfgType=MgmtPortDuplexCfgType, deviceInterfaceGateway=deviceInterfaceGateway, deviceCpuUsageSystemCpu=deviceCpuUsageSystemCpu, InstallerNameType=InstallerNameType, deviceInterfaceIp6Address=deviceInterfaceIp6Address, deviceSfpSfpLength625um=deviceSfpSfpLength625um, deviceMgmtPortStats=deviceMgmtPortStats, DeviceNtpRunstateType=DeviceNtpRunstateType, devicePsuVoltageMilliVolts=devicePsuVoltageMilliVolts, PtpInterfaceType=PtpInterfaceType, deviceNtpServerKeyValue=deviceNtpServerKeyValue, Note3Type=Note3Type, nETOPTICS_XFAM_DEVICE_MIB=nETOPTICS_XFAM_DEVICE_MIB, MgmtPortLinkStatusType=MgmtPortLinkStatusType, devicePsuRowstatus=devicePsuRowstatus, deviceInterfaceRowstatus=deviceInterfaceRowstatus, NtpAuthType=NtpAuthType, deviceSfpSfpRtTxOutputPower=deviceSfpSfpRtTxOutputPower, DeviceModelNameType=DeviceModelNameType, PYSNMP_MODULE_ID=nETOPTICS_XFAM_DEVICE_MIB, deviceTimeDateNtpNtpStatusNtpstatReport=deviceTimeDateNtpNtpStatusNtpstatReport, deviceInstallationNote2=deviceInstallationNote2, deviceSysIp=deviceSysIp, deviceSfpSfpRtRxInputPower2CentiDBm=deviceSfpSfpRtRxInputPower2CentiDBm, deviceTempSensorTable=deviceTempSensorTable, deviceSfpSfpRtAlarmFlags=deviceSfpSfpRtAlarmFlags, deviceNtpServerPolling=deviceNtpServerPolling, deviceSfpSfpLength50um=deviceSfpSfpLength50um, deviceHwInventorySerialNumber=deviceHwInventorySerialNumber, deviceSfpSfpVendorSN=deviceSfpSfpVendorSN, deviceNtpServerEntry=deviceNtpServerEntry, InetAddressIP=InetAddressIP, deviceTimedateZoneListEntry=deviceTimedateZoneListEntry, deviceTimeDateZone=deviceTimeDateZone, devicePsuEntry=devicePsuEntry, NtpServerStateCfgType=NtpServerStateCfgType, deviceTempSensorDescription=deviceTempSensorDescription, devicePsuPsuNum=devicePsuPsuNum, deviceCpuUsageTable=deviceCpuUsageTable, Time24hType=Time24hType, deviceSfpSfpTrxFibreSpeed=deviceSfpSfpTrxFibreSpeed, devicePlatformInfoAttributeDescription=devicePlatformInfoAttributeDescription, deviceSfpSfpTrxFibreTechnology=deviceSfpSfpTrxFibreTechnology, deviceTimeDatePtpPtpStatusCurrentOffset=deviceTimeDatePtpPtpStatusCurrentOffset, deviceSfpEntry=deviceSfpEntry, CpuTypeType=CpuTypeType, HwModelNameType=HwModelNameType, deviceNtpServerKey=deviceNtpServerKey, deviceSfpRowstatus=deviceSfpRowstatus, deviceSfpSfpTrxId=deviceSfpSfpTrxId, deviceSysIpMacAddress=deviceSysIpMacAddress, deviceTempSensorTemperatureMilliDegC=deviceTempSensorTemperatureMilliDegC, DeviceTimezoneType=DeviceTimezoneType, UnsignedShort=UnsignedShort, deviceHwInventoryCpuType=deviceHwInventoryCpuType, deviceInterfaceIp6PrefixLen=deviceInterfaceIp6PrefixLen, DevicePtpRunStateType=DevicePtpRunStateType, deviceFanDescription=deviceFanDescription, deviceConsolePortBaudrate=deviceConsolePortBaudrate, devicePsuHighThresholdMilliVolts=devicePsuHighThresholdMilliVolts, deviceSsh=deviceSsh, deviceInterfaceEnabled=deviceInterfaceEnabled, deviceTimeDateNtpNtpStatus=deviceTimeDateNtpNtpStatus, deviceTimeDatePtpAdmin=deviceTimeDatePtpAdmin, deviceInterfaceAddress=deviceInterfaceAddress, deviceHwStatusMemUsageFreeMem=deviceHwStatusMemUsageFreeMem, deviceTempSensorEntry=deviceTempSensorEntry, deviceMgmtPortStatsTxTotal=deviceMgmtPortStatsTxTotal, MgmtPortSpeedStatusType=MgmtPortSpeedStatusType, deviceSfpSfpDateCode=deviceSfpSfpDateCode, MgmtPortDuplexStatusType=MgmtPortDuplexStatusType, DeviceCurrentTimeDateType=DeviceCurrentTimeDateType, deviceConsolePortCurrentBaudrate=deviceConsolePortCurrentBaudrate, deviceTimeDateNtpNtpStatusRunstate=deviceTimeDateNtpNtpStatusRunstate, deviceTimedateZoneListZoneFilename=deviceTimedateZoneListZoneFilename, deviceHwInventoryHwRevision=deviceHwInventoryHwRevision, deviceSfpSfpEncoding=deviceSfpSfpEncoding, deviceTimeDatePtpPtpStatusLastValidSyncTimestamp=deviceTimeDatePtpPtpStatusLastValidSyncTimestamp, deviceMgmtPortStatsRxCrcErrors=deviceMgmtPortStatsRxCrcErrors, DeviceNtpstatReportType=DeviceNtpstatReportType, NtpKeyDigestType=NtpKeyDigestType, ModelNumberType=ModelNumberType, deviceSshExtraSSHCiphers=deviceSshExtraSSHCiphers, deviceSfpTable=deviceSfpTable, NtpAdminCfgType=NtpAdminCfgType, deviceCpuUsageUserCpu=deviceCpuUsageUserCpu, deviceHwInventoryModelName=deviceHwInventoryModelName, devicePlatformInfo=devicePlatformInfo, devicePlatformInfoAttributeValue=devicePlatformInfoAttributeValue, Ipv6PrefixLenType=Ipv6PrefixLenType, deviceNtpServerKeyType=deviceNtpServerKeyType, deviceSysIpIp6PrefixLen=deviceSysIpIp6PrefixLen, deviceFanRpm=deviceFanRpm, deviceMgmtPortSpeed=deviceMgmtPortSpeed, device=device, SerialNumberType=SerialNumberType, MgmtPortAutoNegStatusType=MgmtPortAutoNegStatusType, deviceSfpSfpRtTemperatureMilliDegC=deviceSfpSfpRtTemperatureMilliDegC, deviceSfpSfpConnector=deviceSfpSfpConnector, deviceTempSensorSensorNum=deviceTempSensorSensorNum, deviceTempSensorLowThreshold=deviceTempSensorLowThreshold, ManufacturingDetailsType=ManufacturingDetailsType, deviceSfp=deviceSfp, PtpAdminCfgType=PtpAdminCfgType, deviceSfpLinkStatus=deviceSfpLinkStatus, deviceTimeDatePtpPtpStatusRunState=deviceTimeDatePtpPtpStatusRunState, deviceMgmtPort=deviceMgmtPort, deviceTempSensorLastFailureDateTime=deviceTempSensorLastFailureDateTime, String=String, deviceTimeDatePtpPtpStatusCurrentPathDelay=deviceTimeDatePtpPtpStatusCurrentPathDelay, devicePlatformInfoAttributeEntry=devicePlatformInfoAttributeEntry, deviceNtpServerRowstatus=deviceNtpServerRowstatus, ModelNameType=ModelNameType, deviceCpuUsageDescription=deviceCpuUsageDescription)
