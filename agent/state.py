from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    messages: List[str]
    intent: Optional[str]
    
    # Lead details
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]

    # Helper flags for the state machine
    name_captured: Optional[bool]
    email_captured: Optional[bool]
    platform_captured: Optional[bool]