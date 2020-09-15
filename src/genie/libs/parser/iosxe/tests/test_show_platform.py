#!/bin/env python
import unittest

from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
from genie.libs.parser.iosxe.show_platform import ShowPlatformIntegrity

class TestShowProcessesMemorySorted(unittest.TestCase):
    device = Device(name='aDevice')

    golden_parsed_output_c9300_xml = {
        'boot': {
            'loader': {
                'hash': '51CE6FB9AE606330810EBFFE99D71D56640FD48F780EDE0C19FB5A75E31EF2192A58A196D18B244ADF67D18BF6B3AA6A16229C66DCC03D8A900753760B252C57',
                'version': 'System Bootstrap, Version 16.10.1r[FC2], DEVELOPMENT SOFTWARE',
            },
            0: {
                'hash': '523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF',
                'version': 'F01144R16.216e68ad62019-02-13',
            },
        }, 
        'os_hashes': {
            'PCR0': 'BB33E3FE338B82635B1BD3F1401CF442ACC9BB12A405A424FBE0A5776569884E',
            'PCR8': '1C6B134C5932F40257F1CF4CADE48BC3E76B1F545EB9C659D3F5DC071D9A6CF6',
            'cat9k-cc_srdriver.2019-07-11_16.25_mzafar.SSA.pkg': '0DC44C89FF1D483AB74C8D0D1DE8B2BF08221B93DC6FED5EB9B2C9F064918DA41CBAB990652650BC1FA04EEF0A1DE75948B4D81CD1903BDD82B0628605CD8E48',
            'cat9k-espbase.2019-07-11_16.25_mzafar.SSA.pkg': 'FF3FAF589D0EE29663CDC29A4F04942B71240718373BB3F43778DF517740A7AF141A7B966B68CACAE2526804CE5B93B9D2B7A7410CB8B20797310779C78EFBE6',
            'cat9k-guestshell.2019-07-11_16.25_mzafar.SSA.pkg': '3AD2036AAF458CF57AC058B4025F70B44BCE3DDF231C9666BCD105FE5910DCF287D2B80F6953717B4CDDA3877B1D112386CB9BAC06D594950DDEC959B3265295',
            'cat9k-rpbase.2019-07-11_16.25_mzafar.SSA.pkg': '51C2AE55EE9FF671D37DE63994B9C97A9775E541D67304B6E5EFA10F76293863D9F890114F47C7C83D8BD5BA4A013CFC62F20726B1EC62F906681B0A6DE0E97F',
            'cat9k-sipbase.2019-07-11_16.25_mzafar.SSA.pkg': '5791879D1C6FC17F92DB77AAD53CD15D0EF51F490334B07D49A717DBB4861CD6FB1AF9B33B3AA40F0DDD84AE86DC1852A9EFF54549942D6D5CCA44843035A7F1',
            'cat9k-sipspa.2019-07-11_16.25_mzafar.SSA.pkg': 'AA925FAD9A5770C638B62E770513D6310CDE1491BCBB1323E31D8CADC8A752455C8323F702DE612EFCD21F5340D222A08A4CA2B7A933EE6E1C4D62E6C94FB39A',
            'cat9k-srdriver.2019-07-11_16.25_mzafar.SSA.pkg': 'A14599C664D858675990FB7CAC886E0AE0EC73E99B50C12E1704A91C50DB1BBF27CA55D18EF9800D6BC4E39B6952F3077B48394F4DFEF2B65B471A8E872C15CB',
            'cat9k-webui.2019-07-11_16.25_mzafar.SSA.pkg': 'D73DAE3793E6BE06EEC01DF677579227015DDFBE871C8922504E5A1A90D399D57D92834933508177433BD4AD05A4DA6B1DD6AFD458967D5DBED51FF0D2C902A2',
            'cat9k-wlc.2019-07-11_16.25_mzafar.SSA.pkg': '6E71EDFACE945DA86CE565F557B00CD9527198CDACC2F4EADB860712D141EE1378E1033882E2C22502A175428EA5EF5C777E5D81702055B9A4387E7EDEFAC448',
        },
        'os_version': '2019-07-11_16.25_mzafar',
        'platform': 'C9300-24U',
    }

    golden_output_c9300_xml = '''
        <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:4679c98c-647b-43fa-8349-de852d77b775">
            <data>
                <boot-integrity-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-boot-integrity-oper">
                <boot-integrity>
                    <platform>C9300-24U</platform>
                    <boot-ver>F01144R16.216e68ad62019-02-13</boot-ver>
                    <boot-loader-ver>System Bootstrap, Version 16.10.1r[FC2], DEVELOPMENT SOFTWARE</boot-loader-ver>
                    <os-version>2019-07-11_16.25_mzafar</os-version>
                    <boot-hash>523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF</boot-hash>
                    <boot-loader-hash>51CE6FB9AE606330810EBFFE99D71D56640FD48F780EDE0C19FB5A75E31EF2192A58A196D18B244ADF67D18BF6B3AA6A16229C66DCC03D8A900753760B252C57</boot-loader-hash>
                    <os-hash>F3D73D330E81CDF682FDB0A55510B48EEF2A1D3F79AD48736493C50B1DA58A32F794A3868D9706BBDE82883CE76A90A74CF458173A7B43CF21DC223D90E204C8</os-hash>
                    <package-count>9</package-count>
                    <pcr-register>
                    <index>0</index>
                    <pcr-content>BB33E3FE338B82635B1BD3F1401CF442ACC9BB12A405A424FBE0A5776569884E</pcr-content>
                    </pcr-register>
                    <pcr-register>
                    <index>8</index>
                    <pcr-content>1C6B134C5932F40257F1CF4CADE48BC3E76B1F545EB9C659D3F5DC071D9A6CF6</pcr-content>
                    </pcr-register>
                    <package-signature>
                    <name>cat9k-wlc.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>6E71EDFACE945DA86CE565F557B00CD9527198CDACC2F4EADB860712D141EE1378E1033882E2C22502A175428EA5EF5C777E5D81702055B9A4387E7EDEFAC448</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-webui.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>D73DAE3793E6BE06EEC01DF677579227015DDFBE871C8922504E5A1A90D399D57D92834933508177433BD4AD05A4DA6B1DD6AFD458967D5DBED51FF0D2C902A2</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-rpbase.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>51C2AE55EE9FF671D37DE63994B9C97A9775E541D67304B6E5EFA10F76293863D9F890114F47C7C83D8BD5BA4A013CFC62F20726B1EC62F906681B0A6DE0E97F</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-sipspa.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>AA925FAD9A5770C638B62E770513D6310CDE1491BCBB1323E31D8CADC8A752455C8323F702DE612EFCD21F5340D222A08A4CA2B7A933EE6E1C4D62E6C94FB39A</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-espbase.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>FF3FAF589D0EE29663CDC29A4F04942B71240718373BB3F43778DF517740A7AF141A7B966B68CACAE2526804CE5B93B9D2B7A7410CB8B20797310779C78EFBE6</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-sipbase.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>5791879D1C6FC17F92DB77AAD53CD15D0EF51F490334B07D49A717DBB4861CD6FB1AF9B33B3AA40F0DDD84AE86DC1852A9EFF54549942D6D5CCA44843035A7F1</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-srdriver.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>A14599C664D858675990FB7CAC886E0AE0EC73E99B50C12E1704A91C50DB1BBF27CA55D18EF9800D6BC4E39B6952F3077B48394F4DFEF2B65B471A8E872C15CB</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-guestshell.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>3AD2036AAF458CF57AC058B4025F70B44BCE3DDF231C9666BCD105FE5910DCF287D2B80F6953717B4CDDA3877B1D112386CB9BAC06D594950DDEC959B3265295</hash>
                    </package-signature>
                    <package-signature>
                    <name>cat9k-cc_srdriver.2019-07-11_16.25_mzafar.SSA.pkg</name>
                    <hash>0DC44C89FF1D483AB74C8D0D1DE8B2BF08221B93DC6FED5EB9B2C9F064918DA41CBAB990652650BC1FA04EEF0A1DE75948B4D81CD1903BDD82B0628605CD8E48</hash>
                    </package-signature>
                    <signature>138ABFFAC76AFBDB43C533601D29A5DA5163D47741D970F406E43CF7081DB0B3CFCDD4D54A059BF64A55B7FB9BFA363B2EEB43526DC7F01E19622A76349988196A16A40B5874658D125F6BE260823DDC485AD9666C88E1FB23DF22181C2BF19F59DA656C0C3064FFAE0522F3440D1C625D75B8474A265191D25BEA028202206B211DBE634CF6DA81871336F13CF4A4497ED34A35ACBACE9BD56193DB71393C3EB062E2C5DACB40D1B6FC7940B0DA9391AF99F8D645354F5AEBC5684401FE69914DF554C0F3233129E12215ECB8778F3BE7C854640CC60373A006174D8910CCF024196C9E7D7E622552DEFA4D2650128A94C3098B7CAF7097A4D6F3770E401488</signature>
                    <sig-version>1</sig-version>
                </boot-integrity>
                </boot-integrity-oper-data>
            </data>
            </rpc-reply>

        '''

    
    def test_golden_c9300_xml(self):
        self.maxDiff = None
        version_obj = ShowPlatformIntegrity(device=None)
        parsed_output = version_obj.yang(output=self.golden_output_c9300_xml)
        self.assertEqual(parsed_output, self.golden_parsed_output_c9300_xml)