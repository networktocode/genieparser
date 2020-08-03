import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_hw_module_status import Show_Hw_Module_Status


# =====================================
# Unit test for 'show_hw-module_status'
# =====================================
class test_show_hw_module_status(unittest.TestCase):
    """Unit test for 'show_hw-module_status'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
    "transceiver_status": {
        1: {
            1: {
                1: {
                    "status": "enabled",
                    "module_temperature": "+28.750",
                    "supply_voltage_mVolts": "3252.5",
                    "bias_current_uAmps": 6706,
                    "tx_power_dBm": "-2.7",
                    "optical_power_dBm": "-2.1"
                },
                2: {
                    "status": "disabled",
                    "module_temperature": "+28.625",
                    "supply_voltage_mVolts": "3252.5",
                    "bias_current_uAmps": 6706,
                    "tx_power_dBm": "-2.7",
                    "optical_power_dBm": "-2.1"
                }
            },
            2: {
                2: {
                    "status": "enabled",
                    "module_temperature": "+28.750",
                    "supply_voltage_mVolts": "3252.5",
                    "bias_current_uAmps": 6706,
                    "tx_power_dBm": "-2.7",
                    "optical_power_dBm": "-2.1"
                }
            }
        },
        2: {
            1: {
                1: {
                    "status": "disabled",
                    "module_temperature": "+28.625",
                    "supply_voltage_mVolts": "3252.5",
                    "bias_current_uAmps": 6706,
                    "tx_power_dBm": "-2.7",
                    "optical_power_dBm": "-2.1"
                }
            }
        }
    }
}

    golden_output1 = {'execute.return_value': '''
The Transceiver in slot 1 subslot 1 port 1 is enabled.
  Module temperature                        = +28.750 C
  Transceiver Tx supply voltage             = 3252.5 mVolts
  Transceiver Tx bias current               = 6706 uAmps
  Transceiver Tx power                      = -2.7 dBm
  Transceiver Rx optical power              = -2.1 dBm
The Transceiver in slot 1 subslot 1 port 2 is disabled.
  Module temperature                        = +28.625 C
  Transceiver Tx supply voltage             = 3252.5 mVolts
  Transceiver Tx bias current               = 6706 uAmps
  Transceiver Tx power                      = -2.7 dBm
  Transceiver Rx optical power              = -2.1 dBm
The Transceiver in slot 1 subslot 2 port 2 is enabled.
  Module temperature                        = +28.750 C
  Transceiver Tx supply voltage             = 3252.5 mVolts
  Transceiver Tx bias current               = 6706 uAmps
  Transceiver Tx power                      = -2.7 dBm
  Transceiver Rx optical power              = -2.1 dBm
The Transceiver in slot 2 subslot 1 port 1 is disabled.
  Module temperature                        = +28.625 C
  Transceiver Tx supply voltage             = 3252.5 mVolts
  Transceiver Tx bias current               = 6706 uAmps
  Transceiver Tx power                      = -2.7 dBm
  Transceiver Rx optical power              = -2.1 dBm      
    '''}

    def test_show_hw_module_status_full(self):
        self.device = Mock(**self.golden_output1)
        obj = Show_Hw_Module_Status(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_hw_module_status_empty(self):
        self.device = Mock(**self.empty_output)
        obj = Show_Hw_Module_Status(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()