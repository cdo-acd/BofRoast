from typing import List, Tuple

from outflank_stage1.task.base_bof_task import BaseBOFTask
from outflank_stage1.task.enums import BOFArgumentEncoding


class BofRoastBOF(BaseBOFTask):
    def __init__(self):
        super().__init__("BofRoast", base_binary_name="kerberoast")

        self.parser.description = (
            "Kerberoast a given Service Principal"
        )
        self.parser.epilog = "Usage: BofRoast <spn>"

        self.parser.add_argument(
            "spn",
            help=f"SPN to kerberoast"        
        )

    def _encode_arguments_bof(
        self, arguments: List[str]
    ) -> List[Tuple[BOFArgumentEncoding, str]]:
        parser_arguments = self.parser.parse_args(arguments)

        return [(BOFArgumentEncoding.WSTR, parser_arguments.spn)]