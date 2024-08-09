SNMP (Simple Network Management Protocol):
SNMP is a protocol used for network management and monitoring of devices like routers, switches, servers, and more. It allows network administrators to manage network performance, find and solve network problems, and plan for network growth. SNMP operates by sending messages, called protocol data units (PDUs), to different parts of a network. It consists of three key components: managed devices, agents, and network management systems (NMS).

Impact on CIA Triad:
Confidentiality: SNMP can impact confidentiality if improperly configured or if communication is intercepted. For example, SNMPv1 and SNMPv2c use community strings for authentication, which are sent in plaintext, making them vulnerable to eavesdropping.
Integrity: SNMP can affect integrity if data is modified in transit. Without proper security measures, data integrity can be compromised, allowing attackers to manipulate SNMP messages.
Availability: Availability can be impacted by SNMP through denial-of-service (DoS) attacks. Attackers can flood the network with SNMP requests, overwhelming devices and causing network disruptions.
IoCs (Indicators of Compromise):
IoCs are forensic artifacts observed on a network or in an operating system that indicate potential malicious activities or security breaches. These can include IP addresses, domain names, file hashes, URLs, registry keys, and more. IoCs are crucial for detecting and responding to cybersecurity incidents, allowing security teams to identify compromised systems and mitigate further damage.

Impact on CIA Triad:
Confidentiality: IoCs can help maintain confidentiality by identifying potential breaches early. By detecting unauthorized access or data exfiltration IoCs contribute to preserving confidentiality.
Integrity: IoCs support integrity by identifying changes in system files or configurations that indicate tampering or compromise. This allows for timely response to prevent further integrity violations.
Availability: IoCs assist in maintaining availability by enabling rapid detection and mitigation of attacks targeting availability, such as DDoS attacks or malware designed to disrupt services.
In summary, SNMP facilitates network management but must be secured to protect the CIA triad. IoCs play a critical role in cybersecurity by enabling detection and response to threats, thereby safeguarding confidentiality, integrity, and availability of systems and data.