"""
ACL Configuration Generator using Ollama
The Tech-E LLC - Ollama for Network Engineers Lab 4
"""

import ollama


class ACLConfigGenerator:
    """Generate Cisco ACL configurations using the neteng model."""
    
    def __init__(self, model: str = "neteng"):
        self.model = model
    
    def generate(self, acl_name: str, action: str, 
                 protocol: str, source_network: str, 
                 ports: list[int]) -> str:
        """
        Generate an ACL configuration.
        
        Args:
            acl_name: Name for the ACL (e.g., "BLOCK-SSH")
            action: "deny" or "permit"
            protocol: "tcp", "udp", or "ip"
            source_network: Source in CIDR (e.g., "192.168.100.0/24")
            ports: List of ports to match (e.g., [22, 23])
        """
        ports_str = ", ".join(str(p) for p in ports)
        prompt = (f"Create ACL named {acl_name} to {action} {protocol} "
                  f"ports {ports_str} from {source_network}")
        
        response = ollama.generate(
            model=self.model,
            prompt=prompt
        )
        return response["response"]


if __name__ == "__main__":
    gen = ACLConfigGenerator()
    
    print("--- Block SSH/Telnet from Guest Network ---")
    print(gen.generate(
        acl_name="BLOCK-GUEST-MGMT",
        action="deny",
        protocol="tcp",
        source_network="192.168.100.0/24",
        ports=[22, 23]
    ))
    
    print("\n--- Block SQL from DMZ ---")
    print(gen.generate(
        acl_name="BLOCK-DMZ-SQL",
        action="deny", 
        protocol="tcp",
        source_network="10.10.10.0/24",
        ports=[1433, 3306]
    ))


