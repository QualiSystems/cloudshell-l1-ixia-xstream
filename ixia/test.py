from unittest import TestCase
from cloudshell.core.logger.qs_logger import get_qs_logger
from ixia.ixia_xstream_driver_handler import IxiaXstreamDriverHandler


class IxiaUnittest(TestCase):
    def test_autoload(self):
        ixia_handler = IxiaXstreamDriverHandler().get_resource_description("192.168.73.76", get_qs_logger())

    def test_map_uni(self):
        ixia_handler = IxiaXstreamDriverHandler()
        ixia_handler.login("192.168.73.76", command_logger=get_qs_logger())
        ixia_handler.map_uni(src_port="1", dst_port="2")

