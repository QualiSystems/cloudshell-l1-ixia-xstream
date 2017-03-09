#
# PySNMP MIB module NETOPTICS-XFAM-IMAGE-MIB (http://pysnmp.sf.net)
# ASN.1 source file://C:\MIBS\text_mibs\NETOPTICS-XFAM-IMAGE-MIB.mib
# Produced by pysmi-0.0.6 at Tue Mar 07 21:53:37 2017
# On host ? platform ? version ? by user ?
# Using Python version 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)]
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, IpAddress, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "IpAddress", "Counter32")
( TruthValue, DisplayString, RowStatus, TextualConvention, DateAndTime, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention", "DateAndTime")
nETOPTICS_XFAM_IMAGE_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1)).setLabel("nETOPTICS-XFAM-IMAGE-MIB").setRevisions(("2016-02-03 00:00",))
class UnsignedShort(Unsigned32, TextualConvention):
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)

class ConfdString(OctetString, TextualConvention):
    displayHint = '1t'

class InetAddressIP(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),)
class String(OctetString, TextualConvention):
    displayHint = '1t'

class BankChecksumType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,63)

class RunningBankNumberType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,3)

class SwImageCommandType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3,)
    namedValues = NamedValues(("idle", 0), ("imageUpgrade", 1), ("imageSwitch", 2), ("downloadAbort", 3),)

class ImageEventDateType(OctetString, TextualConvention):
    displayHint = '1t'

class BankVersionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,63)

class BootVersionType(OctetString, TextualConvention):
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,63)

class NextBootBankNumberType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(1, 2,)
    namedValues = NamedValues(("a1", 1), ("a2", 2),)

class SwImageStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3,)
    namedValues = NamedValues(("na", 0), ("ok", 1), ("fail", 2), ("empty", 3),)

class SwImageCmdStatusType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 99,)
    namedValues = NamedValues(("idle", 0), ("ok", 1), ("fail", 2), ("aborted", 3), ("starting", 4), ("transferring", 5), ("uncompressing", 6), ("validating", 7), ("analyzing", 8), ("processing", 9), ("preInstall", 10), ("installing", 11), ("postInstall", 12), ("versionUpdate", 13), ("switching", 14), ("unconfiguring", 15), ("migrating", 16), ("rebooting", 99),)

class PercentType(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,100)

cdb = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 2))
cdbCdbPrevious = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 2, 1), String()).setMaxAccess("readonly")
cdbCdbCurrent = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 2, 2), String()).setMaxAccess("readonly")
cdbUpgradeDate = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 2, 3), String()).setMaxAccess("readonly")
cdbNumChanges = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 2, 4), Integer32()).setMaxAccess("readonly")
image = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1))
imageInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1))
imageInfoBank1Version = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1, 1), BankVersionType()).setMaxAccess("readonly")
imageInfoBank2Version = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1, 5), BankVersionType()).setMaxAccess("readonly")
imageInfoRunningBankNumber = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1, 9), RunningBankNumberType()).setMaxAccess("readonly")
imageInfoAltBankNumber = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1, 10), RunningBankNumberType()).setMaxAccess("readonly")
imageInfoNextBootBankNumber = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1, 11), RunningBankNumberType()).setMaxAccess("readonly")
imageInfoRunningVersion = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1, 16), String()).setMaxAccess("readonly")
imageInfoAltVersion = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 1, 17), String()).setMaxAccess("readonly")
imageBuildInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 3))
imageImageCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2))
imageImageCmdCommand = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 1), SwImageCommandType()).setMaxAccess("readwrite")
imageImageCmdSrvip = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 2), InetAddressIP()).setMaxAccess("readwrite")
imageImageCmdFilename = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 3), String().subtype(subtypeSpec=ValueSizeConstraint(0,1023))).setMaxAccess("readwrite")
imageImageCmdUser = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 4), String().subtype(subtypeSpec=ValueSizeConstraint(4,64))).setMaxAccess("readwrite")
imageImageCmdPw = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 5), ConfdString()).setMaxAccess("readwrite")
imageImageCmdUnconfig = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 6), TruthValue()).setMaxAccess("readwrite")
imageImageCmdFtpMode = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 7), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("passive", 1), ("active", 2),))).setMaxAccess("readwrite")
imageImageCmdProtocol = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 8), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2, 3,)).clone(namedValues=NamedValues(("ftp", 1), ("sftp", 2), ("scp", 3),))).setMaxAccess("readwrite")
imageImageCmdSshPort = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 9), UnsignedShort()).setMaxAccess("readwrite")
imageImageCmdStatus = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 20), SwImageCmdStatusType()).setMaxAccess("readonly")
imageImageCmdLockStatus = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 23), TruthValue()).setMaxAccess("readonly")
imageImageCmdPercentComplete = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 22), PercentType()).setMaxAccess("readonly")
imageImageCmdSeverity = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 21), Integer32().subtype(subtypeSpec=SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7,)).clone(namedValues=NamedValues(("recoveryAlert", 0), ("debugAlert", 1), ("infoAlert", 2), ("noticeAlert", 3), ("warnAlert", 4), ("minorAlert", 5), ("majorAlert", 6), ("criticalAlert", 7),))).setMaxAccess("readonly")
imageImageCmdStatusMessage = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 24), String()).setMaxAccess("readonly")
imageImageCmdStatusDateTime = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 25), ImageEventDateType()).setMaxAccess("readonly")
imageImageCmdFileSize = MibScalar((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 2, 26), Unsigned32()).setMaxAccess("readonly")
imageBuildInfoAttributeTable = MibTable((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 3, 1), )
imageBuildInfoAttributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 3, 1, 1), ).setIndexNames((1, "NETOPTICS-XFAM-IMAGE-MIB", "imageBuildInfoAttributeName"))
imageBuildInfoAttributeName = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 3, 1, 1, 1), String())
imageBuildInfoAttributeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 3, 1, 1, 2), String()).setMaxAccess("readonly")
imageBuildInfoAttributeDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 23022, 100, 14, 1, 1, 3, 1, 1, 3), String()).setMaxAccess("readonly")
mibBuilder.exportSymbols("NETOPTICS-XFAM-IMAGE-MIB", ConfdString=ConfdString, imageImageCmdPercentComplete=imageImageCmdPercentComplete, imageBuildInfoAttributeTable=imageBuildInfoAttributeTable, UnsignedShort=UnsignedShort, cdbNumChanges=cdbNumChanges, imageInfoRunningVersion=imageInfoRunningVersion, imageImageCmdSrvip=imageImageCmdSrvip, cdb=cdb, RunningBankNumberType=RunningBankNumberType, SwImageStatusType=SwImageStatusType, imageBuildInfoAttributeName=imageBuildInfoAttributeName, SwImageCommandType=SwImageCommandType, imageImageCmdStatusMessage=imageImageCmdStatusMessage, SwImageCmdStatusType=SwImageCmdStatusType, imageBuildInfoAttributeEntry=imageBuildInfoAttributeEntry, imageImageCmdStatus=imageImageCmdStatus, imageImageCmdStatusDateTime=imageImageCmdStatusDateTime, imageImageCmdLockStatus=imageImageCmdLockStatus, imageImageCmd=imageImageCmd, PercentType=PercentType, BankVersionType=BankVersionType, cdbUpgradeDate=cdbUpgradeDate, imageInfoBank2Version=imageInfoBank2Version, imageInfoAltBankNumber=imageInfoAltBankNumber, cdbCdbCurrent=cdbCdbCurrent, imageBuildInfoAttributeDescription=imageBuildInfoAttributeDescription, NextBootBankNumberType=NextBootBankNumberType, imageImageCmdCommand=imageImageCmdCommand, BankChecksumType=BankChecksumType, cdbCdbPrevious=cdbCdbPrevious, imageImageCmdFilename=imageImageCmdFilename, imageImageCmdUnconfig=imageImageCmdUnconfig, imageImageCmdFileSize=imageImageCmdFileSize, imageImageCmdPw=imageImageCmdPw, imageImageCmdSshPort=imageImageCmdSshPort, imageBuildInfoAttributeValue=imageBuildInfoAttributeValue, nETOPTICS_XFAM_IMAGE_MIB=nETOPTICS_XFAM_IMAGE_MIB, InetAddressIP=InetAddressIP, imageImageCmdProtocol=imageImageCmdProtocol, imageImageCmdFtpMode=imageImageCmdFtpMode, BootVersionType=BootVersionType, PYSNMP_MODULE_ID=nETOPTICS_XFAM_IMAGE_MIB, ImageEventDateType=ImageEventDateType, imageImageCmdSeverity=imageImageCmdSeverity, imageImageCmdUser=imageImageCmdUser, imageInfo=imageInfo, imageInfoRunningBankNumber=imageInfoRunningBankNumber, imageInfoAltVersion=imageInfoAltVersion, String=String, image=image, imageInfoBank1Version=imageInfoBank1Version, imageInfoNextBootBankNumber=imageInfoNextBootBankNumber, imageBuildInfo=imageBuildInfo)
