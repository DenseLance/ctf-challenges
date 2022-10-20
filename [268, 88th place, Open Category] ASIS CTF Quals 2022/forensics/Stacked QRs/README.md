# forensics/Stacked QRs

<p align = "center"><img src="challenge.JPG" alt="alt text" width="50%" height="50%" /></p>

All they give you is this:

<p align = "center"><img src="stacked_qrs.png" alt="alt text" width="50%" height="50%" /></p>

Each QR code must have 3 position markers (aka big squares) at the corners so that the QR scanner can determine the orientation of the QR code. Most of them in this picture only have 1 or 2, meaning to say we have to create the position markers and insert those at the correct position for them. After much searching, I found 3 QR codes that were not randomized strings.

The first one is at the centre and is second from the top:

<p align = "center"><img src="qr1.JPG" alt="alt text" width="25%" height="25%" /></p>

```
ASIS{7iM3_70_f
```

The second one is at the centre, with a blob that looks like <b>amogus</b>.

<p align = "center"><img src="qr2.JPG" alt="alt text" width="25%" height="25%" /></p>

```
ix_7Hi5_0ld_di
```

The last one is at the bottom right corner.

<p align = "center"><img src="qr3.JPG" alt="alt text" width="25%" height="25%" /></p>

```
R7y_PRin73R!!}
```

Combining all 3 parts gives the following flag:

```
ASIS{7iM3_70_fix_7Hi5_0ld_diR7y_PRin73R!!}
```