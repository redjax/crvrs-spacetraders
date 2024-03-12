import register_agent

import httpx

if __name__ == "__main__":
    print(
        f"Spacetraders register agent endpoint: {register_agent.SPACETRADERS_REGISTER_ENDPOINT}"
    )
    agent_name = register_agent.random_agentname()
    print(f"Random agent name: {agent_name}")

    register_agent_req = register_agent.build_register_agent_request(
        agent_symbol=agent_name
    )
    print(f"Register agent request: {register_agent_req}")

    print(f"Attempting to register agent '{agent_name}'")
    with httpx.Client(headers={"Content-Type": "application/json"}) as client:
        try:
            res = client.send(register_agent_req)
            assert res, ValueError("Register agent response should not have been None")

            if res.status_code not in [200, 201]:
                print(
                    f"Non-200 register agent response: [{res.status_code}: {res.reason_phrase}]: {res.text}"
                )
            else:
                print(
                    f"Register agent response: [{res.status_code}: {res.reason_phrase}]"
                )

        except Exception as exc:
            msg = Exception(
                f"Unhandled exception registering agent '{agent_name}'. Details: {exc}"
            )
            print(f"[ERROR] {msg}")

            raise msg

    print(f"Regsitered agent: {res.content}")
