# cloudshell-l1-ixia-xstream
<p align="center">
<img src="https://github.com/QualiSystems/devguide_source/raw/master/logo.png"></img>
</p>

# Ixia Xstream L1 Shell
Release date: Septemeber 2017
Shell version 1.0.0


# Overview
The Ixia Xstream L1 Shell provides CloudShell with the capability to communicate with switches that are part of the CloudShell inventory.
End users will be able to create routes, discover the Switch structure, configure port settings and read attribute values from the switch using the CloudShell Portal, Resource Manager client or the CloudShell API.

# The Ixia Xstream L1 Shell package includes:

|File name				|File description	| Version|
|---|---|---|
|`IxiaXstream.exe`|Ixia Driver Used by CloudShell Server|1.0.0|
|`ixia_xstream_runtime_configuration.json`|JSON file enabling additional configuration interface for the driver|1.0.0|
|`ixia_xstream_runtime_datamodel.xml`|An XML file holding all attribute and capabilities of the L1 switches|1.0.0|

# The Shell is compatible with the following CloudShell versions:
⦁	6.4 and above

# The driver has been certified with the following Ixia Xstream Software Version:
⦁	x10_060700_041216

# Installation
Follow the instructions in the link below for installation:
http://help.qualisystems.com/Online%20Help/7.0.0.0/Portal/Content/Admn/Cnct-Ctrl-L1-Swch.htm 

In step 7 at the above guide, you will need to copy only one exe file, and instead of the runtimeConfig.xml file please copy the 'ixia_xstream_runtime_configuration.json' file.

# Commands
|Commands|Description|
|---|---|
|`MapUni`|	Creates a uni-directional connection between two ports.|
|`MapTap`|	Creates one bi-directional connection between two ports and one uni-directional connection from first port to third port.|
|`MapBidi`|	Creates a bi-directional connection between two ports.|
|`MapClear`|	Clears any connection ending in this port.|
|`MapClearTo`|	Clears a uni-directional connection between two ports.|


# Bug fixes
No


# Known issues
Initial start	Python L1 driver getting refuse connection when driver starts for the first time. Once driver is running – everything works as expected.
This issue is resolved in CloudShell 7.0 patch 1 and above.

