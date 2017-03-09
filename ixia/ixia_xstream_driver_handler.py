#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import re

from common.configuration_parser import ConfigurationParser
from common.driver_handler_base import DriverHandlerBase
from common.resource_info import ResourceInfo
from ixia.ixia_xstrem_autoload_helper import IxiaXstreamAutoloadHelper
from cloudshell.snmp.quali_snmp import QualiSnmp, SNMPV3Parameters, SNMPV2Parameters


class IxiaXstreamDriverHandler(DriverHandlerBase):
    def __init__(self):
        DriverHandlerBase.__init__(self)

        self._snmp_handler = None
        self._ctag = 1
        self._switch_name = ''
        self._switch_size = 0
        self._mapping_info = dict()

        self._resource_info = None

        self._service_mode = ConfigurationParser.get("driver_variable", "service_mode")
        self._port_logical_mode = ConfigurationParser.get("driver_variable", "port_mode")
        self._custom_port_pairing = ConfigurationParser.get("driver_variable", "custom_port_pairing")
        self._snmp_write_community = ConfigurationParser.get("driver_variable", "snmp_write_community")
        self._snmp_version = ConfigurationParser.get("driver_variable", "snmp_version")
        self._snmp_v3_user = ConfigurationParser.get("driver_variable", "snmp_write_community")
        self._snmp_v3_password = ConfigurationParser.get("driver_variable", "snmp_write_community")
        self._snmp_v3_private_key = ConfigurationParser.get("driver_variable", "snmp_write_community")

    def _incr_ctag(self):
        self._ctag += 1
        return self._ctag

    def login(self, address, username="", password="", command_logger=None):
        if self._service_mode.lower() == "snmp":
            self._snmp_handler = self.__get_snmp_handler(address, command_logger)
            command_result = self._snmp_handler.get_property("SNMPv2-MIB", "sysName", 0)
        elif self._service_mode.lower() == "ssh":
            command_result = ""
            try:
                self._session.connect(address, username, password, port=None)
                command_result = self._session.send_command("", re_string=self._prompt)
                command_logger.info('Login status: OK')
            except Exception as e:
                command_logger.info(e.args)
        else:
            raise Exception(self.__class__.__name__, "From service mode type (current mode: '" +
                            self._service_mode + "'!")

        match_result = re.search(r"(?<=(@)).*(?=(]))", command_result, re.DOTALL)
        if match_result:
            self._switch_name = match_result.group()

    def __get_snmp_handler(self, host, logger):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".", "mibs"))
        logger.info(host)
        logger.info(self._snmp_write_community)
        if "3" in self._snmp_version:
            if not self._snmp_v3_user or not self._snmp_v3_password or not self._snmp_v3_private_key:
                raise Exception(self.__class__.__name__, "Cannot create SNMP Version 3, Check configuration")
            snmp_params = SNMPV3Parameters(ip=host, snmp_user=self._snmp_v3_user, snmp_password=self._snmp_v3_password,
                                           snmp_private_key=self._snmp_v3_private_key)
            logger.info("SNMP V3 Created")
        else:
            if not self._snmp_write_community:
                raise Exception(self.__class__.__name__, "Cannot create SNMP Version 2, Check configuration")
            snmp_params = SNMPV2Parameters(ip=host, snmp_community=self._snmp_write_community)
            logger.info("SNMP V2 Created")
        snmp_handler = QualiSnmp(snmp_params, logger)
        snmp_handler.update_mib_sources(path)
        return snmp_handler

    def get_resource_description(self, address, command_logger=None):
        autoload_helper = IxiaXstreamAutoloadHelper(command_logger)
        if self._service_mode.lower() == "ssh":
            device_data = autoload_helper.get_ssh_device_structure(self._session)
        elif self._service_mode.lower() == "snmp":
            snmp_handler = self.__get_snmp_handler(address, command_logger)
            device_data = autoload_helper.get_snmp_device_structure(snmp_handler)
        else:
            if not self._service_mode.lower():
                raise Exception(self.__class__.__name__, "Service mode is empty")
            raise Exception(self.__class__.__name__,
                            "Service mode {0} is not supported".format(self._service_mode.lower()))

        address_prefix = address + "/"
        self._resource_info = ResourceInfo()
        self._resource_info.set_depth(0)
        self._resource_info.set_index(1)

        self._resource_info.set_address(address)
        self._resource_info.add_attribute("Vendor", device_data["vendor"])
        self._resource_info.add_attribute("Type", device_data["type"])
        self._resource_info.add_attribute("Version", device_data["version"])
        self._resource_info.add_attribute("Model", device_data["model"])
        self._resource_info.set_model_name(device_data["model"])
        self._resource_info.set_serial_number(device_data["serial"])
        model_name = device_data["model"]

        # if self._port_logical_mode.lower() == "logical":
        for port_id, port_data in device_data["ports"].iteritems():
            port_resource_info = ResourceInfo()
            port_resource_info.set_depth(1)
            port_resource_info.set_index(port_id)
            port_resource_info.set_model_name(model_name)
            mapped_to = port_data.get("mapped_to")
            if mapped_to:
                port_resource_info.set_mapping(address_prefix + mapped_to)
            port_resource_info.add_attribute("State", port_data['state'])
            port_resource_info.add_attribute("Protocol Type", 0)
            self._resource_info.add_child(port_id, port_resource_info)
        # else:
        #     for port_data in port_map_list:
        #         port_map_match = re.search(r"IPORTID=(?P<src_port>\d+).*IPORTNAME=(?P<src_port_name>\S+),IP.*" +
        #                                    "OPORTID=(?P<dst_port>\d+).*OPORTNAME=(?P<dst_port_name>\S+),OP.*",
        #                                    port_data, re.DOTALL)
        #         if port_map_match is not None:
        #             port_map_dict = port_map_match.groupdict()
        #             if int(port_map_dict['src_port']) > 0 and \
        #                             int(port_map_dict['dst_port']) > 0:
        #                 src_port = port_map_dict["src_port"]
        #                 dst_port = port_map_dict["dst_port"]
        #                 # self._mapping_info[dst_port] = src_port
        #                 self._mapping_info[src_port] = dst_port
        #     for port_data in port_list:
        #         port_info_match = re.search(r"PORTID=(?P<id>\d+).*PORTNAME=(?P<name>(IN|OUT)\d+)" +
        #                                     ".*PORTHEALTH=(?P<state>good|bad)", port_data, re.DOTALL)
        #         if port_info_match is not None:
        #             port_info_dict = port_info_match.groupdict()
        #             port_resource_info = ResourceInfo()
        #             port_resource_info.set_depth(1)
        #             port_id = port_info_dict["id"]
        #             port_resource_info.set_index(port_id)
        #             port_resource_info.set_model_name(model_name)
        #             # port_resource_info.set_name(port_info_dict["name"])
        #             if port_id in self._mapping_info:
        #                 port_resource_info.set_mapping(address_prefix + self._mapping_info[port_id])
        #             if port_info_dict["state"].lower() == "good":
        #                 port_resource_info.add_attribute("State", "Enable")
        #             else:
        #                 port_resource_info.add_attribute("State", "Disable")
        #             port_resource_info.add_attribute("Protocol Type", 0)
        #             self._resource_info.add_child(port_info_dict["id"], port_resource_info)
        return self._resource_info.convert_to_xml()

    def map_uni(self, src_port, dst_port, command_logger=None):
        if self._service_mode.lower() == "ssh":
            pass
        elif self._service_mode.lower() == "snmp":
            index = self._incr_ctag()
            self._snmp_handler.set([(("NETOPTICS-XFAM-FILTER-MIB", "filterRuleAction", index), 1),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleName", index),
                                     "{0} to {1}".format(src_port, dst_port)),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleInPorts", index), src_port),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRedirPorts", index), dst_port),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleEnabled", index), 1),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRowstatus", index), 4)])
            src_in_port = src_port

            dst_out_port = dst_port

            if self._port_logical_mode.lower() == "logical":
                src_in_port = str(10000 + int(src_in_port.split('-')[0]))
                dst_out_port = str(20000 + int(dst_out_port.split('-')[1]))

            command = "ent-crs-fiber::{0},{1}:{2};".format(src_in_port, dst_out_port, self._incr_ctag())
            command_result = self._session.send_command(command, re_string=self._prompt)
            command_logger.info(command_result)

    def map_bidi(self, src_port, dst_port, command_logger=None):
        if self._service_mode.lower() == "scpi":
            pass
        elif self._service_mode.lower() == "tl1":
            if self._port_logical_mode.lower() == "logical":
                source_port = str(src_port[1]).split('-')
                destination_port = str(dst_port[1]).split('-')
                src_in_port = str(10000 + int(source_port[0]))
                dst_in_port = str(10000 + int(destination_port[0]))
                src_out_port = str(20000 + int(source_port[1]))
                dst_out_port = str(20000 + int(destination_port[1]))

                command = "ent-crs-fiber::{0}&{1},{2}&{3}:{4};".format(src_in_port, dst_in_port, dst_out_port,
                                                                       src_out_port, self._incr_ctag())
                command_result = self._session.send_command(command, re_string=self._prompt)
                command_logger.info(command_result)
            else:
                raise Exception(self.__class__.__name__,
                                "Bidirectional port mapping could be done only in logical port_mode " +
                                "(current mode: '" + self._port_logical_mode + "'")

    def map_clear_to(self, src_port, dst_port, command_logger=None):
        if self._service_mode.lower() == "scpi":
            pass
        elif self._service_mode.lower() == "tl1":
            src_in_port = src_port[1]
            if self._port_logical_mode.lower() == "logical":
                source_port = src_port[1].split('-')
                src_in_port = str(10000 + int(source_port[0]))

            command = "dlt-crs-fiber::{0}:{1};".format(src_in_port, self._incr_ctag())

            self._session.send_command(command, re_string=self._prompt)

    def map_clear(self, src_port, dst_port, command_logger=None):
        if self._service_mode.lower() == "scpi":
            pass
        elif self._service_mode.lower() == "tl1":
            if self._port_logical_mode.lower() == "logical":
                source_port = src_port[1].split('-')
                destination_port = dst_port[1].split('-')
                src_in_port = str(10000 + int(source_port[0]))
                dst_in_port = str(10000 + int(destination_port[0]))

                command = "dlt-crs-fiber::{0}&{1}:{2};".format(src_in_port, dst_in_port, self._incr_ctag())

                self._session.send_command(command, re_string=self._prompt)
            else:
                self.map_clear_to(src_port, dst_port, command_logger)

    def set_speed_manual(self, command_logger=None):
        pass


if __name__ == '__main__':
    from cloudshell.core.logger.qs_logger import get_qs_logger

    gglass = IxiaXstreamDriverHandler()
    plogger = get_qs_logger('Autoload', 'GlimmerGlass', 'GlimmerGlass')
    gglass.login('192.168.2.41:10033', 'admin', 'password', plogger)
