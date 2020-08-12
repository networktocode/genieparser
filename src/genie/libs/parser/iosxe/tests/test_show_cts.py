import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_cts import ShowCtsSxpConnectionsVrfBr


# ====================================================
# Unit test for 'show cts sxp connections vrf {vrf} br'
# ====================================================
class TestShowCtsSxpConnectionsVrfBr(unittest.TestCase):
    """Unit test for 'show cts sxp connections vrf {vrf} br'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "sxp_connections": {
            "status": {
                "sxp_status": "Enabled",
                "highest_version": 4,
                "default_pw": "Set",
                "key_chain": "Not Set",
                "key_chain_name": "Not Applicable",
                "source_ip": "Not Set",
                "conn_retry": 120,
                "reconcile_secs": 120,
                "retry_timer": "running",
                "seq_export": "Not Set",
                "seq_import": "Not Set"
            },
            "sxp_peers": {
                "10.1.100.110": {
                    "source_ip": "10.1.20.6",
                    "conn_status": "Off",
                    "duration": "0:00:17:33"
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
 SXP              : Enabled
 Highest Version Supported: 4
 Default Password : Set
 Default Key-Chain: Not Set
 Default Key-Chain Name: Not Applicable
 Default Source IP: Not Set
Connection retry open period: 120 secs
Reconcile period: 120 secs
Retry open timer is running
Peer-Sequence traverse limit for export: Not Set
Peer-Sequence traverse limit for import: Not Set

----------------------------------------------------------------------------------------------------------------------------------
Peer_IP          Source_IP        Conn Status                                          Duration 
----------------------------------------------------------------------------------------------------------------------------------
10.1.100.110   10.1.20.6   Off                                                  0:00:17:33 (dd:hr:mm:sec)

Total num of SXP Connections = 1        
    '''}

    def test_show_cts_sxp_connections_vrf_br_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowCtsSxpConnectionsVrfBr(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_cts_sxp_connections_vrf_br_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCtsSxpConnectionsVrfBr(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
