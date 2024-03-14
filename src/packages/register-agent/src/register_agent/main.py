from constants import SPACETRADERS_REGISTER_ENDPOINT
from methods import random_agentname

import httpx


def register_agent(agent_name: str = None) -> httpx.Response:
    client: httpx.Client = httpx.Client(headers={"Content-Type": "application/json"})

    params: dict = {"symbol": agent_name, "faction": "COSMIC"}

    with client as c:
        try:
            res = c.post(url=SPACETRADERS_REGISTER_ENDPOINT, json=params)
            print(f"[{res.status_code}: {res.reason_phrase}] Register agent response")
            if res.status_code not in [200, 201]:
                print(
                    f"Non-200 status code [{res.status_code}] received. Response text: {res.text}"
                )
        except Exception as exc:
            msg = Exception(f"Unhandled exception registering agent. Details: {exc}")
            print(msg)

            raise msg

    return res


if __name__ == "__main__":
    print(f"Register agent URL: {SPACETRADERS_REGISTER_ENDPOINT}")
    agent_name = random_agentname()
    print(f"Agent name: {agent_name}")

    register_agent_res: httpx.Response = register_agent(agent_name=agent_name)
    print(f"Registered agent: {register_agent_res.text}")
