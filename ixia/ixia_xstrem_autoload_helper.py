import re


class IxiaXstreamAutoloadHelper(object):
    def __init__(self, logger):
        self._logger = logger
        self._mapping = False
        self._filtering = False

    def get_ssh_device_structure(self, session):
        pass

    def get_snmp_device_structure(self, snmp_handler):
        """

        :param QualiSnmp snmp_handler: snmp handler
        :return:
        """

        return {
            "vendor": "Ixia",
            "type": snmp_handler.get_property("SNMPv2-MIB", "sysDescr", 0),
            "version": snmp_handler.get_property("NETOPTICS-XFAM-IMAGE-MIB", "imageInfoRunningVersion", 0),
            "model": snmp_handler.get_property("NETOPTICS-XFAM-DEVICE-MIB", "deviceHwInventoryModelName", 0),
            "serial": snmp_handler.get_property("NETOPTICS-XFAM-DEVICE-MIB", "deviceHwInventorySerialNumber", 0),
            "model_name": snmp_handler.get_property("NETOPTICS-XFAM-DEVICE-MIB", "deviceHwInventoryModelNumber", 0),
            "ports": self.get_snmp_ports(snmp_handler)
        }

    def get_snmp_port_mapping(self, snmp_handler):
        port_mapping = {}
        mapping = snmp_handler.get_table("NETOPTICS-XFAM-MAP-MIB", "mapIdTable")
        if mapping:
            for key, value in mapping.iteritems():
                if value:
                    in_port = value["mapIdInPorts"]
                    out_port = value["mapIdOutPorts"]
                    if "-" in in_port or "-" in out_port:
                        continue
                    in_ports = in_port.split(",")
                    out_ports = out_port.split(",")
                    if len(in_ports) != len(out_ports):
                        continue

                    for port in in_ports:
                        port_mapping[port] = out_ports[in_ports.index(port)]
        else:
            filtering_table = snmp_handler.get_table(
                "NETOPTICS-XFAM-FILTER-MIB", "filterRuleAction").filter_by_column("ction", "'redir'")
            for key, value in filtering_table.iteritems():
                if value:
                    in_port = snmp_handler.get_property("NETOPTICS-XFAM-FILTER-MIB", "filterRuleInPorts", key)
                    out_port =snmp_handler.get_property("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRedirPorts", key)
                    if "-" in in_port or "-" in out_port:
                        continue

                    in_ports = in_port.split(",")
                    out_ports = out_port.split(",")
                    if len(in_ports) != len(out_ports):
                        continue

                    for port in in_ports:
                        port_mapping[port] = out_ports[in_ports.index(port)]

        return port_mapping

    def get_snmp_ports(self, snmp_handler):
        ports = {}
        port_mapping = self.get_snmp_port_mapping(snmp_handler)
        ports_table = snmp_handler.get_table("NETOPTICS-XFAM-PORTS-MIB", "portAdmin")
        for port_index, port_data in ports_table.iteritems():
            port_speed = "1 Gbps"
            port_speed_str = snmp_handler.get_property("NETOPTICS-XFAM-PORTS-MIB", "portLinkSpeed", port_index)
            port_speed_match = re.search(r"\d+", port_speed_str)
            if port_speed_match:
                port_speed_int = port_speed_match.group()
                if len(port_speed_int) > 4:
                    port_speed = "10 Gbps"

            ports[port_index] = {"state": port_data["portAdmin"].replace("'", "").title(),
                                 "speed": port_speed,
                                 "auto_neg": "on" in snmp_handler.get_property("NETOPTICS-XFAM-PORTS-MIB", "portAutoNegotiation",
                                                                       port_index).lower()}
            mapped_to = port_mapping.get(str(port_index))
            if mapped_to:
                ports[port_index]["mapped_to"] = mapped_to

        return ports
