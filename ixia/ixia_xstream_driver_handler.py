#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import re

from common.configuration_parser import ConfigurationParser
from common.driver_handler_base import DriverHandlerBase
from common.resource_info import ResourceInfo
from cloudshell.snmp.quali_snmp import QualiSnmp, SNMPV3Parameters, SNMPV2Parameters, PySnmpError
from ixia.ixia_xstrem_autoload_helper import IxiaXstreamAutoloadHelper


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
        model_name = device_data["model"]
        self._resource_info.set_model_name(model_name)
        self._resource_info.set_serial_number(device_data["serial"])

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
        return self._resource_info.convert_to_xml()

    def map_uni(self, src_port, dst_port, command_logger=None):
        if self._service_mode.lower() == "ssh":
            pass
        elif self._service_mode.lower() == "snmp":
            self._add_snmp_filter(src_port, dst_port, command_logger)

    def map_tap(self, src_port, dst_port, command_logger=None):
        if self._service_mode.lower() == "ssh":
            pass
        elif self._service_mode.lower() == "snmp":
            self._add_snmp_filter(src_port, dst_port, command_logger)

    def map_bidi(self, src_port, dst_port, command_logger=None):
        if self._service_mode.lower() == "ssh":
            pass
        elif self._service_mode.lower() == "snmp":
            self._add_snmp_filter(src_port, dst_port, command_logger)
            self._add_snmp_filter(dst_port, src_port, command_logger)

    def _add_snmp_filter(self, src_port, dst_port, logger):
        src_in_port = src_port[-1]
        dst_out_port = dst_port[-1]
        existing_rules = self._get_filter(src_in_port)
        if existing_rules:
            logger.info(existing_rules)
            self._append_snmp_filter(existing_rules, dst_out_port, logger)
        else:
            rule_name_table = self._snmp_handler.get_table("NETOPTICS-XFAM-FILTER-MIB", "filterRuleName")
            index = self._incr_ctag()
            while index in rule_name_table.keys():
                index = self._incr_ctag()

            self._set_snmp_filter(src_in_port, dst_out_port, index)

    def _append_snmp_filter(self, existing_rules, dst_out_port, logger):
        for index in existing_rules:
            dst_port = self._snmp_handler.get_property("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRedirPorts", index)
            if dst_port:
                dst_out_port = "{0},{1}".format(dst_port, dst_out_port)
                logger.info(dst_out_port)
            try:
                self._snmp_handler.set([(("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRedirPorts", index), dst_out_port)])
            except PySnmpError as e:
                logger.error(e.args)
            if dst_out_port not in self._snmp_handler.get_property("NETOPTICS-XFAM-FILTER-MIB",
                                                                   "filterRuleRedirPorts", index):
                raise Exception(self.__class__.__name__, "Failed to append filter rule")

    def _set_snmp_filter(self, src_in_port, dst_out_port, index):
        try:
            self._snmp_handler.set([(("NETOPTICS-XFAM-FILTER-MIB", "filterRuleAction", index), 1),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleName", index),
                                     "{0} to {1}".format(src_in_port, dst_out_port)),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleInPorts", index), src_in_port),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRedirPorts", index), dst_out_port),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleEnabled", index), 1),
                                    (("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRowstatus", index), 4)])
        except PySnmpError:
            if not self._snmp_handler.get_property("NETOPTICS-XFAM-FILTER-MIB", "filterRuleName", index):
                raise

    def map_clear_to(self, src_port_path, src_port_paths, command_logger=None):
        self.map_clear(src_port_path, src_port_paths, command_logger, uni=True)

    def map_clear(self, src_port, dst_port, command_logger=None, uni=False):
        if self._service_mode.lower() == "ssh":
            pass
        elif self._service_mode.lower() == "snmp":
            src_in_port = src_port[-1]
            for index in self._get_filter(src_in_port):
                self._remove_filter(index)

    def _get_filter(self, src_port):
        result = []
        rule_name_table = self._snmp_handler.get_table("NETOPTICS-XFAM-FILTER-MIB", "filterRuleInPorts")
        for index, value in rule_name_table.iteritems():
            filter_port = value.get("filterRuleInPorts")
            if filter_port and int(src_port) == int(filter_port):
                result.append(index)
        return result

    def _remove_filter(self, index):
        self._snmp_handler.set([(("NETOPTICS-XFAM-FILTER-MIB", "filterRuleRowstatus", index), 6)])

    def set_speed_manual(self, command_logger=None):
        pass
