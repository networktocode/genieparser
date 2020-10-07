import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =======================================
# Schema for:
#  * 'show redundancy switchover history'
# =======================================
class ShowRedundancySwitchoverHistorySchema(MetaParser):
    """Schema for show redundancy switchover history."""

    schema = {
        
    }


# =======================================
# Parser for:
#  * 'show redundancy switchover history'
# =======================================
class ShowRedundancySwitchoverHistory(ShowRedundancySwitchoverHistorySchema):
    """Parser for show redundancy switchover history"""

    cli_command = ['show redundancy switchover history']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Index  Previous  Current  Switchover             Switchover
        #        active    active   reason                 time
        # -----  --------  -------  ----------             ----------
        #    1       1        2     Active lost GW         03:26:09 UTC Wed Sep 23 2020
        #    2       2        1     user forced            05:40:13 UTC Thu Oct 1 2020


        #    1       1        2     Active lost GW         03:26:09 UTC Wed Sep 23 2020
        switchover_history_capture = re.compile(
            # 1
            r"^(?P<index>\d+)\s+"
            # 1
            r"(?P<previous_active>\d+)\s+"
            # 2
            r"(?P<current_active>\d+)\s+"
            # Active lost GW
            r"(?P<switchover_reason>.+)\s+"
            # 03:26:09 UTC Wed Sep 23 2020
            r"(?P<switchover_time>\d+:\d+:\d+\sUTC\s\S+\s\S+\s\d+\s\d+)$"
        )

        redundancy_info_obj = {}

        for line in output.splitlines():
            line = line.strip()

            if switchover_history_capture.match(line):
                match = switchover_history_capture.match(line)
                group = match.groupdict()

                # cleanup dict
                for item in group:
                    # remove trailing spaces from regex capture
                    group[item] = group[item].strip()

                    # convert str to int
                    try:
                        group[item] = int(group[item])
                    except ValueError:
                        continue

                # pull a key from dict to use as new_key
                new_key = "index"
                info_dict = {group[new_key]: {}}

                # update then pop new_key from the dict
                info_dict[group[new_key]].update(group)
                info_dict[group[new_key]].pop(new_key)

                if not redundancy_info_obj.get(new_key):
                    # initialize the dict with new_key
                    redundancy_info_obj[new_key] = {}

                redundancy_info_obj[new_key].update(info_dict)

        return redundancy_info_obj