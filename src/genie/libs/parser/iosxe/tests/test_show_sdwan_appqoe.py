import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxe.show_sdwan_appqoe import (
    ShowSdwanAppqoeTcpoptStatus,
    ShowSdwanAppqoeNatStatistics,
    ShowSdwanAppqoeRmResources)


# ============================================
# unittest for 'show sdwan appqoe tcpopt status'
# ============================================
class TestShowSdwanAppqoeTcpoptStatus(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                        TCP-OPT Status
        ==========================================================

        Status
        ------
        TCP OPT Operational State      : RUNNING
        TCP Proxy Operational State    : RUNNING
        '''
        }

    golden_parsed_output = {
        'status': {
            'tcp_opt_operational_state': 'RUNNING',
            'tcp_proxy_operational_state': 'RUNNING'
            }
        }
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanAppqoeTcpoptStatus(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanAppqoeTcpoptStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


# ============================================
# unittest for 'show sdwan appqoe nat-statistics'
# ============================================
class TestShowSdwanAppqoeNatStatistics(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                    NAT Statistics
        ==========================================================
        Insert Success      : 518181
        Delete Success      : 518181
        Duplicate Entries   : 5
        Allocation Failures : 0
        Port Alloc Success  : 0
        Port Alloc Failures : 0
        Port Free Success   : 0
        Port Free Failures  : 0
        '''
        }

    golden_parsed_output = {
        'nat_statistics': {
            'insert_success': 518181,
            'delete_success': 518181,
            'duplicate_entries': 5,
            'allocation_failures': 0,
            'port_alloc_success': 0,
            'port_alloc_failures': 0,
            'port_free_success': 0,
            'port_free_failures': 0
            }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanAppqoeNatStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanAppqoeNatStatistics(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
