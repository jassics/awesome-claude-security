# Reference: MITRE ATT&CK (Enterprise)

Stable taxonomy + frequently used techniques. ATT&CK is versioned — for any technique
not listed here, or to confirm sub-technique structure, check **attack.mitre.org**
(note the version you cite).

## Enterprise tactics (the "why", in kill-chain order)

| Tactic | ID | Adversary goal |
| --- | --- | --- |
| Reconnaissance | TA0043 | Gather info to plan the operation |
| Resource Development | TA0042 | Establish infrastructure/capabilities |
| Initial Access | TA0001 | Get into the network |
| Execution | TA0002 | Run malicious code |
| Persistence | TA0003 | Keep a foothold across reboots/creds |
| Privilege Escalation | TA0004 | Gain higher permissions |
| Defense Evasion | TA0005 | Avoid detection |
| Credential Access | TA0006 | Steal account credentials |
| Discovery | TA0007 | Learn the environment |
| Lateral Movement | TA0008 | Move through the environment |
| Collection | TA0009 | Gather data of interest |
| Command and Control | TA0011 | Communicate with compromised systems |
| Exfiltration | TA0010 | Steal data |
| Impact | TA0040 | Manipulate, interrupt, or destroy |

## Frequently used techniques (ID · name · tactic)

- **T1566** Phishing (Initial Access) — .001 Spearphishing Attachment, .002 Link
- **T1190** Exploit Public-Facing Application (Initial Access)
- **T1078** Valid Accounts (Initial Access / Persistence / Priv-Esc / Defense Evasion)
- **T1059** Command and Scripting Interpreter (Execution) — .001 PowerShell,
  .003 Windows Command Shell, .004 Unix Shell, .006 Python
- **T1053** Scheduled Task/Job (Execution / Persistence / Priv-Esc)
- **T1547** Boot or Logon Autostart Execution (Persistence / Priv-Esc)
- **T1543** Create or Modify System Process (Persistence / Priv-Esc)
- **T1068** Exploitation for Privilege Escalation (Priv-Esc)
- **T1055** Process Injection (Defense Evasion / Priv-Esc)
- **T1027** Obfuscated Files or Information (Defense Evasion)
- **T1070** Indicator Removal (Defense Evasion)
- **T1003** OS Credential Dumping (Credential Access) — .001 LSASS Memory
- **T1110** Brute Force (Credential Access)
- **T1552** Unsecured Credentials (Credential Access)
- **T1087** Account Discovery · **T1018** Remote System Discovery · **T1083**
  File and Directory Discovery · **T1057** Process Discovery (Discovery)
- **T1021** Remote Services (Lateral Movement) — .001 RDP, .002 SMB, .004 SSH
- **T1071** Application Layer Protocol (C2) · **T1573** Encrypted Channel (C2)
- **T1041** Exfiltration Over C2 Channel · **T1567** Exfil Over Web Service (Exfil)
- **T1486** Data Encrypted for Impact (Impact, ransomware) · **T1485** Data Destruction

## Cloud / container additions (Enterprise sub-matrices)

- **T1078.004** Valid Accounts: Cloud Accounts
- **T1530** Data from Cloud Storage
- **T1610** Deploy Container · **T1611** Escape to Host (containers/k8s)
- **T1552.005** Unsecured Credentials: Cloud Instance Metadata API

## Mapping tips

- Tactic = goal, technique = method, sub-technique = specific variant. Tag the most
  specific level the evidence supports.
- A single behavior can serve multiple tactics (e.g., Valid Accounts) — pick by intent
  in context.
- Pair with **D3FEND** for defensive countermeasure mapping and **CAR**/Sigma for
  analytics; route coverage analysis to `detection-engineering`.
