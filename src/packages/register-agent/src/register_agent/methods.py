import typing as t

import uuid
import json

import httpx

from .constants import SPACETRADERS_REGISTER_ENDPOINT


def random_agentname(char_limit: int = 14) -> str:
    ## Get a UUID string & remove '-' characters
    _uuid: str = str(uuid.uuid4()).replace("-", "")

    if len(_uuid) > char_limit:
        ## Strip UUID string to char_limit
        agent_name: str = _uuid[:char_limit]

    return agent_name


def build_register_agent_request(
    url: str = SPACETRADERS_REGISTER_ENDPOINT,
    agent_symbol: str = None,
    agent_faction: str = "COSMIC",
) -> httpx.Request:
    assert agent_symbol, ValueError("Missing agent_symbol")
    assert isinstance(agent_symbol, str), TypeError(
        f"Expected agent_symbol to be a str. Got type: ({type(agent_symbol)})"
    )
    assert len(agent_symbol) <= 14, ValueError(
        f"agent_symbol must be 14 characters or less. agent_symbol was {len(agent_symbol)} character(s)."
    )

    assert agent_faction, ValueError("Missing agent_faction")
    assert isinstance(agent_faction, str), TypeError(
        f"Expected agent_faction to be a str. Got type: ({type(agent_faction)})"
    )

    json_data: dict = {"symbol": agent_symbol, "faction": agent_faction.upper()}

    try:
        req: httpx.Request = httpx.Request(
            method="POST",
            url=url,
            json=json_data,
        )

        return req
    except Exception as exc:
        msg = Exception(
            f"Unhandled exception building register agent request. Details: {exc}"
        )

        raise msg
