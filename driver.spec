# -*- mode: python -*-
block_cipher = None

import os
import PyInstaller.utils.hooks

CS_L1_NETCORE = "../cloudshell-L1-networking-core"

def add_data_files(related_path, root_path="."):

    path = os.path.join(root_path, related_path)
    templates = []
    for resp_temp_file in os.listdir(path):
        templates.append((os.path.join(related_path, resp_temp_file),
                          os.path.join(path, resp_temp_file),
                          "DATA"))
    return templates

a = Analysis(['main.py'],
             # pathex=[".", "../cloudshell-core", CS_L1_NETCORE],
             pathex=[".", CS_L1_NETCORE],
             binaries=None,
             datas=PyInstaller.utils.hooks.collect_data_files('pysnmp') + \
             PyInstaller.utils.hooks.collect_data_files('cloudshell.snmp.mibs') + \
             PyInstaller.utils.hooks.collect_data_files('ixia'),
             hiddenimports=PyInstaller.utils.hooks.collect_submodules('pysmi') + \
             PyInstaller.utils.hooks.collect_submodules('ply') + \
             PyInstaller.utils.hooks.collect_submodules('pyasn1') + \
             PyInstaller.utils.hooks.collect_submodules('pysnmp') + [
                "pysnmp.smi.exval",
                "pysnmp.cache",
                "common.cli.tcp_session",
                "common.cli.telnet_session",
                "common.cli.console_session",
                "cloudshell.snmp.*",
                "common.cli.ssh_session",
                "ixia.ixia_xstream_driver_handler"
             ] + PyInstaller.utils.hooks.collect_submodules('cloudshell'),
             hookspath=["..\cloudshell-snmp\."],
             runtime_hooks=None,
             excludes=["cloudshell.cli", "cloudshell.shell", "cloudshell.networking"],
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries + add_data_files("configuration") + add_data_files("common/response_template", CS_L1_NETCORE) ,
          a.zipfiles,
          a.datas,
          name='IxiaXstream',
          debug=False,
          strip=None,
          upx=True,
          console=True,
          version='version.txt',
          icon=os.path.join(CS_L1_NETCORE, "img/icon.ico")
          )
