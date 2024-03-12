import typing as t

import uuid
import json


def random_agentname(char_limit: int = 14) -> str:
    ## Get a UUID string & remove '-' characters
    _uuid: str = str(uuid.uuid4()).replace("-", "")

    if len(_uuid) > char_limit:
        ## Strip UUID string to char_limit
        agent_name: str = _uuid[:char_limit]

    return agent_name
