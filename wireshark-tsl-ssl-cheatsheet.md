Useful Wireshark filter for analysis of TSL/SSL Traffic.
replace tsl with ssl as needed

Client Hello:
tsl.handshake.type == 1

Server Hello:
tsl.handshake.type == 2

NewSessionTicket:
tsl.handshake.type == 4

Certificate:
tsl.handshake.type == 11

CertificateRequest
tsl.handshake.type == 13

ServerHelloDone:
tsl.handshake.type == 14

Cipher Suites:
tsl.handshake.ciphersuite