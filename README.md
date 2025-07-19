# P2P-Chat
Peer to peer chat with file transfer option.
The chat is for one time use, so every chat will be erased after the chat is closed.
This add another layer of security, so the user can be sure that the chat is not stored on the server.

# Security
A connection will only be established if the user has a valid public key registered and connected to the discovery server.
Every connection with peer to peer will be verified by the "Discovery Server" using the public key of the user.
Each side of the p2p will need to prove his identity by signing a challenge with their public key.
The key exchange will go over the discovery server, so the discovery server will know the public key is connected to the right side.
The connection will include rate limiting to prevent abuse of ddos.

Messages will be encrypted with the AES encryption algorithm, the key exchange will be done with Diffie-Hellman key exchange algorithm.

File transfer will be done over the p2p connection, and the file will be encrypted with AES before sending and verified with hash.

# Features
- Peer to peer chat
- File transfer
- Discovery server
- Public key authentication
- AES encryption
- Rate limiting
- tkinter GUI
- Diffie-Hellman key exchange
- Hash verification for file transfer
- Challenge-response authentication
- Multi-threading for concurrent connections
- File virus scanning (virustotal API)
- Discovery Server Commend Line Interface (CLI)