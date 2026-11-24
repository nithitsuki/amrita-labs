# Review: CN endsem prep + answers

**Verdict:** Both files are largely accurate and the arithmetic is almost all sound, but there is one wrong header size that will be memorised (802.11), one wrong table row (count to infinity), and four places where the two files state the same fact differently — fix those before 09:30.

## Errors

| # | File | Line | Stated | Correct | Severity |
|---|------|------|--------|---------|----------|
| 1 | CN-endsem-answers.org | 1192 | "The header is 30 bytes without address 4 and 36 bytes with it." | 24 bytes without A4, 30 bytes with it (FC 2 + Dur 2 + A1 6 + A2 6 + A3 6 + Seq 2 = 24; +A4 6 = 30). The prep file (line 6151) has this right: "24 byte header, plus 6 bytes when A4 is present". This is literally CNE2 Q10 ("draw the frame format of 802.11"), so it will be written from memory. | high |
| 2 | CN-endsem-prep.org | 4650 | Count-to-infinity drill (c = 2 per hop), round 6 row: O says 16, P says 14 | Round 6 must be O = 14, P = 16. From round 5 (O 14, P 12): O = min(16, 2+12) = 14, P = min(16, 2+14) = 16. Stated row is unreachable from the row above it (O = 16 needs P = 14; P = 14 needs O = 12; neither exists). Round 7 (16, 16) is correct. | medium |
| 3 | CN-endsem-answers.org | 1180 | 802.11 diagram labels Address 4 as "(ad hoc)" | A4 is present only when **both** To DS and From DS are set (AP-to-AP over the distribution system). In an ad hoc / IBSS frame there are only three addresses. The answer's own text (line 1188) states the To DS / From DS rule correctly, so the label contradicts the paragraph next to it. | low |
| 4 | CN-endsem-prep.org | 1445 vs CN-endsem-answers.org 2743 | Prep: "Send a jam signal of 48 bits". Answers CNE2 Q15: "sends a 32-bit jam signal". Answers CNE5 Q9: "sends a 48-bit jam signal". | One value, one place. IEEE 802.3 specifies 32 bits; Tanenbaum says 48 bits; the Kurose slides (Ch. 6, "CSMA/CD") say only "send jam signal" with no length, so pick one and use it in all three places. IEEE 32 is the safer exam answer. | medium |
| 5 | CN-endsem-prep.org | 173, 376, 496-498 | Bandwidth-delay product = **R x RTT** (0.5 s), e.g. 4 Mbit/s x 90 ms = 360 000 bit | Kurose defines it as R x **propagation delay** (one way), so 4 Mbit/s x 45 ms = 180 000 bit. The answers file already uses the one-way form (line 57: `BDP = R x d(prop)`), so the two files disagree. The "frames to fill the pipe" use of R x RTT is fine as a window-sizing number, but do not label it the bandwidth-delay product. | medium |
| 6 | CN-endsem-prep.org | 5434 | "maximum segment length 2500 m worst case in 10BASE5" | A 10BASE5 segment is 500 m. 2500 m is the maximum **network / collision-domain diameter** (5 segments, 4 repeaters), which is what the 2500 m in the next sentence actually is. Change the row label, not the number. | low |
| 7 | CN-endsem-answers.org | 2253 | Class A "First octet 0 to 127" | 1 to 126. 0.x.x.x is "this network" and 127.0.0.0/8 is loopback; the answer itself says "126 networks" two lines later, and the prep file (line 3308) says 1-126. | low |
| 8 | CN-endsem-prep.org | 2301 | State table row: `ACK / CLOSE_WAIT -> LAST_ACK` | The move CLOSE_WAIT -> LAST_ACK is caused by sending a **FIN**, not an ACK. An ACK received in CLOSE_WAIT does not change state. | low |
| 9 | CN-endsem-prep.org | 6510-6514, 6527-6530, 6608, 6642 | Coverage map and triage cite CNE3 as "Q2a, Q2b, Q2c, Q3a, Q3b, Q4a, Q4b, Q5a, Q5b" | The actual CNE3 paper (and the paper bank at lines 6978-7064) numbers the questions Q1a, Q1b, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10. The sub-part labels exist nowhere, so a student cannot match the coverage map to the bank. Marks still add to 50 either way. | low |

## Suspicious — could not settle from the slides

| File | Line | Item | Why it is uncertain |
|------|------|------|---------------------|
| prep | 1804 | "A FIN with seq = u is followed by data starting at u + 1" | A FIN carries no data, so nothing follows it. The intended point is that the peer ACKs u+1. As written it can produce "data after the FIN". |
| answers | 2530 | Fast recovery: "sets cwnd = ssthresh" | The Ch. 3 slides only say the rate is "cut in half on triple duplicate ACK (TCP Reno)", which supports this. Kurose's text adds `cwnd = ssthresh + 3 MSS` (prep line 3034). Both are defensible; they just should not differ between the files. |
| prep | 5087-5093 | CRC "detects every double-bit error, as long as G has more than one term" | The slides give only "can detect all burst errors less than r+1 bits". The usual precise condition is that G does not divide x^k+1, or that G contains (x+1). Not contradicted, but unverified against the course material. |
| prep | 5093 | "A burst of r+1 bits or longer with probability 1 - 2^-r" | Exact for bursts longer than r+1; for a burst of exactly r+1 the escape probability is 2^-(r-1). Pedantic, and not in the slides. |
| prep | 4921 | 2D parity "detects any burst whose length is at most the number of columns" | Holds for this grid (I proved it case by case), but it is a Tanenbaum result, not a Kurose one; the slides stop at "detect and correct single bit errors". |
| prep | 435 | End-to-end over three links: "3 x (0.4 + 2 + 5) = 22.2 ms" | Processing delay is charged three times but only two routers sit on a three-link path. Arithmetically fine, conceptually loose. |
| prep | 1970 | MSL "typical value is 2 minutes" | Windows default is 2 min, Linux 60 s. Not in the slides. The arithmetic (2 x 120 s = 240 s = 4 min) is right. |

## Org syntax

No blocking problems. I checked mechanically, and the files will render:

- `#+begin_example` / `#+end_example` are balanced: 159/159 in the prep file, 118/118 in the answers file. No nesting, no orphan ends.
- No heading-level skips in either file (every level starts at 1 and increments by at most 1).
- Every table has a consistent cell count across its rows. The only "mismatches" a naive check reports are separator rows (`|---+---|`), which Org treats as horizontal rules — that is correct syntax.
- ASCII diagrams that contain `|` (answers line 2367-2378, the DSL drawing) are inside an example block, so they are literal text and will not be parsed as tables.

Cosmetic items only:

1. Markdown backticks used as inline code in 9 places render as literal backticks in Org. Use `=...=` instead.
   - prep: 4448, 4449, 5734, 6335, 6336
   - answers: 2403, 2405, 2407, 2409
2. prep line 6578-6583: the summary table has a second rule row between the mean row and the data rows. It renders, but two rules in one table looks like an editing accident.
3. Bold emphasis written as `*Working.*` at the start of a line is legal Org (a heading needs `*` plus a space), so it renders as bold. No action needed, but do not add a space after the asterisk.

## Verified correct (spot-check of what I recomputed or checked against the slides)

**Numerical, recomputed independently**
- UDP checksum worked example (prep 1335-1393): 0xB4C3+0x9E28 = 0x52EC after fold, +0x71D6 = 0xC4C2, +0x5A0F = 0x1ED2, +0xE12D = 0xFFFF. Two end-around carries. Bit-4 flip of W3 gives 0x1EC2 + 0xE12D = 0xFFEF. All correct.
- Checksum drill (prep 2486-2498): 0x1234+0x5678+0x9ABC+0xDEF0+0x1DA6 = 0xFFFF with one fold. Correct.
- CNE4 Q10 checksum (answers 3535-3562): 0x0050+0x0019+0x0014+0x6666+0x5555+0x8F0C = 0x14B44 -> 0x4B45, verdict "error", expected checksum 0x43C7 vs received 0x8F0C. I get exactly the same numbers. Verdict correct.
- CRC long division (prep 5027-5080, D=11010110, G=1011): remainder 111, step table self-consistent bit for bit, frame 11010110111 divides to 000. Correct.
- CRC drill (answers 6398-6421, D=10110110, G=1101): remainder 010, frame 10110110010. Correct.
- Two-dimensional parity main grid (prep 4811-4841): all five row parities and all four column parities recomputed; corner bit 1 agrees from both directions; 30 bits total, 10 bits overhead. Correct.
- Single-bit, two-bit and same-row-two-bit cases in the same section: every failing row and column I recomputed matches the text.
- Parity drill (prep 6352-6389): 4x4 grid parities and the received-grid failures {2,4} rows, {1,3} columns are all correct; the two real errors really are (2,3) and (4,1).
- CNE1 Q10 answer grid (answers 439-468): row parities 1,0,0,1, column parities all 0, corner 0. The r2c3 flip makes row 2 and column 3 odd. Correct.
- Fragmentation (prep 3765-3784): 2980 payload, 776 per fragment, 3 full + 652, lengths 796/796/796/672 = 3060 = 2980 + 4x20, offsets 0/97/194/291. All correct; 776 -> 97 is right.
- Fragmentation drill (prep 3969-3986): 576 per fragment, remainder 176, lengths 596x4 + 196 = 2580, offsets 0/72/144/216/288. Correct.
- Stop-and-wait and pipelining (prep 2613-2635): 12/62 = 0.1935, 60/62 = 0.968, N >= 62/12 = 5.17 -> 6. Correct.
- HTTP counting (prep 792-804): 210, 1470, 990, 590 ms; 880 ms saved = 60 percent. Correct.
- Caching delay (prep 899-912): 0.30 and 0.135 utilisation, 0.7255 s average, 54 percent saved. Correct.
- P2P distribution (prep 1105-1118): 400/133/800/160 s, 3x and 5x. Correct.
- RTO (prep 2155-2168): 105 ms, 19 ms, 181 ms. Correct.
- Windowed rate (prep 2892-2917): 25 ms, 525 ms cycle, 32 000 bit pipe, 20 frames, 24 381 bps, 38 percent. Correct.
- TCP throughput (prep 3055-3073): 157 437 B/s = 1.26 Mbps, and 0.75x12x1460/0.08 = 164 250 B/s. Correct, and the W = 12 MSS cross-check is consistent (W = 1.62/sqrt(p)).
- CNE3 Q7 pipelining (answers 2068-2100): 12 ms, pipe 4, U = 20/80/100 percent at N = 1/4/5. Correct.
- CNE3 Q8 GBN satellite (answers 2117-2176): 40 ms, 800 ms, pipe 20 frames, cycle 840 ms, 9 524 bps, 47.6 percent. The "do not add an extra Tt" note is right, and U = N/(1+2a) agrees.
- Drills: subnetting from prefix (prep 3919-3938), reverse subnetting (3943-3946), the six-question utilisation drill (3153-3162), the GBN trace (3168-3177), the SR legality drill (3180-3185), the cwnd trace (3188-3199) — all recomputed and correct, including ssthresh = 10 and the handover at 10.
- VLSM, three separate plans: prep five departments (3458-3483, free .188-.255 = 68), prep drill four (3951-3957, free 36), CNE5 six departments (3066-3142, 128 used, 116 usable, 12 spare), CNE4 five blocks (3574-3612, exactly 256), CNE6 three blocks (3990-4025, free 48). Every network address is aligned to its own block size, every broadcast is network + block - 1, every range is right.
- Delay chains: prep 9 ms nodal and 22.2 ms end to end; CNE5 Q1 12 us vs 15 ms (1250x) and 120 us vs 0.5 us (240x); CNE4 Q4 8 ms / 40 ms / 4 ms / 52 ms with 77 / 15 / 8 percent shares; CNE2 Q3 1.005 ms and 2.01 ms. All correct.
- CSMA/CD numbers: 2500 m -> 12.5 us -> 250 bits at 10 Mbps; 2000 m at 100 Mbps -> 2000 bits = 250 bytes; a = 0.1 -> 66.7 percent; 512 bit times = 51.2 us at 10 Mbps and 5.12 us at 100 Mbps; backoff maxima 512/1536/3584/523 776 bit times and 16 attempts. All correct. 1 Gbps needing 2500 bytes at that length is right.
- Distance vector ring (prep 4172-4200) and the four-router drill (4609-4636): every entry of every round recomputed, including "converged at round 1".
- Dijkstra traces (prep 4095-4119 and 4587-4606): every D(v), p(v) cell recomputed; the forwarding-table next hop is right in both, including F = 9 via B and T = 5 via A.
- Count to infinity with c = 1 (prep 4222-4237): all 15 rows correct.
- CO mark accounting: paper-level splits 22/20/8, 25/22/13/13/27, 10/20/20, 22/20/8, 20/15/20/25/20, 15/5/25/5/0 all match the CO tables printed on the OCR'd papers; the unit totals 112/102/101/68/67 and the 450 sum are correct; the mean row 22/19/16/21/22 is correct.

**Header field widths and sizes**
- UDP 8 bytes, four 16-bit fields, length includes the header; pseudo-header 32+32+8+8+16 = 96 bits = 12 bytes, protocol 17. Checksum optional in IPv4, mandatory in IPv6, 0x0000 means "not computed", computed zero must be sent as 0xFFFF. All correct.
- TCP fixed header 20 bytes, options to 40, data offset in 32-bit words (5 = 20 B, 15 = 60 B), five 32-bit rows = 160 bits. Pseudo-header 12 bytes, protocol 6. Correct. Reserved 3 + NS 1 in the prep file and reserved 4 (NS being the last bit) in the answers file both add to 16 for that row — consistent, not an error.
- IPv4: 4+4+8+16 / 16+3+13 / 8+8+16 / 32 / 32 = 160 bits = 20 bytes; hlen 4 bits so max 60 bytes; offset in 8-byte units; flags reserved/DF/MF. Correct.
- IPv6: 4+8+20 then 16+8+8 then 128+128 = 320 bits = 40 bytes exactly; no checksum, no base-header fragmentation. Correct.
- Ethernet: 7 preamble + 1 SFD + 6 + 6 + 2 + 46-1500 + 4; 64-byte minimum excludes the 8-byte preamble; 1518 maximum; 46-byte payload floor. Correct in both files.
- 802.1Q: 4 bytes, inserted after the source MAC, TPID 0x8100 + 3-bit priority + 1-bit CFI/DEI + 12-bit VID (0 and 4095 reserved), tagged frame max 1522. Correct in both files.
- ARP: 28 bytes with the field list 2+2+1+1+2+6+4+6+4, EtherType 0x0806. Correct.
- 802.11: 2/2/6/6/6/2(/6) field widths, A1 = receiver, A2 = transmitter, A3 = the DS-side address, A4 only for AP-to-AP; payload 0-2312; FCS 4. The widths and the address semantics are right in both files — only the total in the answers file is wrong (row 1 above).

**Protocol facts**
- RIP: distance vector, hop count, 15 valid / 16 = infinity, full table every 30 s, UDP 520, 180 s dead timer. Correct.
- OSPF: link state, Dijkstra, IP protocol 89, area 0 backbone, cost = reference bandwidth / interface bandwidth, five packet types, ABR/ASBR roles. Correct.
- BGP: path vector, TCP 179, AS-PATH / NEXT-HOP / LOCAL-PREF / MED, iBGP is not an IGP, policy beats path length. Correct.
- TCP flags: SYN, ACK, FIN, RST, PSH, URG, CWR, ECE with the right meanings; SYN and FIN each consume one sequence number; a pure ACK consumes none. Correct in both files.
- TCP close: FIN_WAIT_1 -> FIN_WAIT_2 -> TIME_WAIT = 2 x MSL; half-close; the ACK may be combined with the FIN. Correct apart from the one table row listed as error 8.
- ARP for an off-subnet destination: resolve the default gateway, never the final destination; the IP destination is unchanged end to end; request broadcast, reply unicast; ~20 min cache. Correct and repeated consistently in both files.
- ARP message size and fields, gratuitous ARP, proxy ARP, ARP spoofing. Correct.
- CSMA/CD minimum-frame reasoning: the sender must still be transmitting at 2 x t_prop, so L >= 2 x t_prop x R, hence 64 bytes at 10 Mbps and 2500 m. Correct.
- CSMA/CA and RTS/CTS ordering: RTS from sender, CTS from AP heard by the hidden node, DATA, ACK; SIFS shorter than DIFS; collision detection impossible on radio; ACK is mandatory, RTS/CTS optional. Correct.
- DHCP DORA with ports 67/68, 0.0.0.0 source, yiaddr, giaddr relay, 50 percent and 87.5 percent renewals. Correct.
- DNS: A, AAAA, CNAME, MX, NS; UDP 53 with TCP for large replies and zone transfers; 13 root servers; iterative referral vs recursive. Correct.
- FTP: 21 control persistent, 20 data in active mode, random port in passive, out-of-band control, stateful. Correct.
- NAT/NAPT: table keyed on address and port, source rewritten outbound, destination inbound, breaks end-to-end, STUN. Correct.
- Port table correct for all 14 entries; IP protocol numbers 1/6/17/41 correct; ICMP type/code list correct.
