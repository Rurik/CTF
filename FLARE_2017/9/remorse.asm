
remorse.ino.hex:     file format ihex


Disassembly of section .sec1:

00000000 <.sec1>:
       0:	0c 94 62 00 	jmp	0xc4	;  0xc4
       4:	0c 94 8a 00 	jmp	0x114	;  0x114
       8:	0c 94 8a 00 	jmp	0x114	;  0x114
       c:	0c 94 8a 00 	jmp	0x114	;  0x114
      10:	0c 94 8a 00 	jmp	0x114	;  0x114
      14:	0c 94 8a 00 	jmp	0x114	;  0x114
      18:	0c 94 8a 00 	jmp	0x114	;  0x114
      1c:	0c 94 8a 00 	jmp	0x114	;  0x114
      20:	0c 94 8a 00 	jmp	0x114	;  0x114
      24:	0c 94 8a 00 	jmp	0x114	;  0x114
      28:	0c 94 8a 00 	jmp	0x114	;  0x114
      2c:	0c 94 8a 00 	jmp	0x114	;  0x114
      30:	0c 94 8a 00 	jmp	0x114	;  0x114
      34:	0c 94 8a 00 	jmp	0x114	;  0x114
      38:	0c 94 8a 00 	jmp	0x114	;  0x114
      3c:	0c 94 8a 00 	jmp	0x114	;  0x114
      40:	0c 94 f5 03 	jmp	0x7ea	;  0x7ea
      44:	0c 94 8a 00 	jmp	0x114	;  0x114
      48:	0c 94 c3 03 	jmp	0x786	;  0x786
      4c:	0c 94 9d 03 	jmp	0x73a	;  0x73a
      50:	0c 94 8a 00 	jmp	0x114	;  0x114
      54:	0c 94 8a 00 	jmp	0x114	;  0x114
      58:	0c 94 8a 00 	jmp	0x114	;  0x114
      5c:	0c 94 8a 00 	jmp	0x114	;  0x114
      60:	0c 94 8a 00 	jmp	0x114	;  0x114
      64:	0c 94 8a 00 	jmp	0x114	;  0x114
      68:	00 00       	nop
      6a:	00 00       	nop
      6c:	24 00       	.word	0x0024	; ????
      6e:	27 00       	.word	0x0027	; ????
      70:	2a 00       	.word	0x002a	; ????
      72:	00 00       	nop
      74:	00 00       	nop
      76:	25 00       	.word	0x0025	; ????
      78:	28 00       	.word	0x0028	; ????
      7a:	2b 00       	.word	0x002b	; ????
      7c:	00 00       	nop
      7e:	00 00       	nop
      80:	23 00       	.word	0x0023	; ????
      82:	26 00       	.word	0x0026	; ????
      84:	29 00       	.word	0x0029	; ????
      86:	04 04       	cpc	r0, r4
      88:	04 04       	cpc	r0, r4
      8a:	04 04       	cpc	r0, r4
      8c:	04 04       	cpc	r0, r4
      8e:	02 02       	muls	r16, r18
      90:	02 02       	muls	r16, r18
      92:	02 02       	muls	r16, r18
      94:	03 03       	mulsu	r16, r19
      96:	03 03       	mulsu	r16, r19
      98:	03 03       	mulsu	r16, r19
      9a:	01 02       	muls	r16, r17
      9c:	04 08       	sbc	r0, r4
      9e:	10 20       	and	r1, r0
      a0:	40 80       	ld	r4, Z
      a2:	01 02       	muls	r16, r17
      a4:	04 08       	sbc	r0, r4
      a6:	10 20       	and	r1, r0
      a8:	01 02       	muls	r16, r17
      aa:	04 08       	sbc	r0, r4
      ac:	10 20       	and	r1, r0
      ae:	00 00       	nop
      b0:	00 08       	sbc	r0, r0
      b2:	00 02       	muls	r16, r16
      b4:	01 00       	.word	0x0001	; ????
      b6:	00 03       	mulsu	r16, r16
      b8:	04 07       	cpc	r16, r20
	...
      c2:	cf 05       	cpc	r28, r15
      c4:	11 24       	eor	r1, r1
      c6:	1f be       	out	0x3f, r1	; 63
      c8:	cf ef       	ldi	r28, 0xFF	; 255
      ca:	d8 e0       	ldi	r29, 0x08	; 8
      cc:	de bf       	out	0x3e, r29	; 62
      ce:	cd bf       	out	0x3d, r28	; 61
      d0:	15 e0       	ldi	r17, 0x05	; 5
      d2:	a0 e0       	ldi	r26, 0x00	; 0
      d4:	b1 e0       	ldi	r27, 0x01	; 1
      d6:	ea ee       	ldi	r30, 0xEA	; 234
      d8:	fc e0       	ldi	r31, 0x0C	; 12
      da:	02 c0       	rjmp	.+4      	;  0xe0
      dc:	05 90       	lpm	r0, Z+
      de:	0d 92       	st	X+, r0
      e0:	ac 36       	cpi	r26, 0x6C	; 108
      e2:	b1 07       	cpc	r27, r17
      e4:	d9 f7       	brne	.-10     	;  0xdc
      e6:	26 e0       	ldi	r18, 0x06	; 6
      e8:	ac e6       	ldi	r26, 0x6C	; 108
      ea:	b5 e0       	ldi	r27, 0x05	; 5
      ec:	01 c0       	rjmp	.+2      	;  0xf0
      ee:	1d 92       	st	X+, r1
      f0:	ac 32       	cpi	r26, 0x2C	; 44
      f2:	b2 07       	cpc	r27, r18
      f4:	e1 f7       	brne	.-8      	;  0xee
      f6:	10 e0       	ldi	r17, 0x00	; 0
      f8:	c2 e6       	ldi	r28, 0x62	; 98
      fa:	d0 e0       	ldi	r29, 0x00	; 0
      fc:	04 c0       	rjmp	.+8      	;  0x106
      fe:	21 97       	sbiw	r28, 0x01	; 1
     100:	fe 01       	movw	r30, r28
     102:	0e 94 68 06 	call	0xcd0	;  0xcd0
     106:	c1 36       	cpi	r28, 0x61	; 97
     108:	d1 07       	cpc	r29, r17
     10a:	c9 f7       	brne	.-14     	;  0xfe
     10c:	0e 94 fc 05 	call	0xbf8	;  0xbf8
     110:	0c 94 73 06 	jmp	0xce6	;  0xce6
     114:	0c 94 00 00 	jmp	0	;  0x0
     118:	cf 92       	push	r12
     11a:	df 92       	push	r13
     11c:	ef 92       	push	r14
     11e:	ff 92       	push	r15
     120:	0f 93       	push	r16
     122:	1f 93       	push	r17
     124:	cf 93       	push	r28
     126:	df 93       	push	r29
     128:	6c 01       	movw	r12, r24
     12a:	7a 01       	movw	r14, r20
     12c:	8b 01       	movw	r16, r22
     12e:	c0 e0       	ldi	r28, 0x00	; 0
     130:	d0 e0       	ldi	r29, 0x00	; 0
     132:	ce 15       	cp	r28, r14
     134:	df 05       	cpc	r29, r15
     136:	89 f0       	breq	.+34     	;  0x15a
     138:	d8 01       	movw	r26, r16
     13a:	6d 91       	ld	r22, X+
     13c:	8d 01       	movw	r16, r26
     13e:	d6 01       	movw	r26, r12
     140:	ed 91       	ld	r30, X+
     142:	fc 91       	ld	r31, X
     144:	01 90       	ld	r0, Z+
     146:	f0 81       	ld	r31, Z
     148:	e0 2d       	mov	r30, r0
     14a:	c6 01       	movw	r24, r12
     14c:	09 95       	icall
     14e:	89 2b       	or	r24, r25
     150:	11 f4       	brne	.+4      	;  0x156
     152:	7e 01       	movw	r14, r28
     154:	02 c0       	rjmp	.+4      	;  0x15a
     156:	21 96       	adiw	r28, 0x01	; 1
     158:	ec cf       	rjmp	.-40     	;  0x132
     15a:	c7 01       	movw	r24, r14
     15c:	df 91       	pop	r29
     15e:	cf 91       	pop	r28
     160:	1f 91       	pop	r17
     162:	0f 91       	pop	r16
     164:	ff 90       	pop	r15
     166:	ef 90       	pop	r14
     168:	df 90       	pop	r13
     16a:	cf 90       	pop	r12
     16c:	08 95       	ret
     16e:	08 95       	ret
     170:	80 e0       	ldi	r24, 0x00	; 0
     172:	90 e0       	ldi	r25, 0x00	; 0
     174:	08 95       	ret
     176:	fc 01       	movw	r30, r24
     178:	53 8d       	ldd	r21, Z+27	; 0x1b
     17a:	44 8d       	ldd	r20, Z+28	; 0x1c
     17c:	25 2f       	mov	r18, r21
     17e:	30 e0       	ldi	r19, 0x00	; 0
     180:	84 2f       	mov	r24, r20
     182:	90 e0       	ldi	r25, 0x00	; 0
     184:	82 1b       	sub	r24, r18
     186:	93 0b       	sbc	r25, r19
     188:	54 17       	cp	r21, r20
     18a:	10 f0       	brcs	.+4      	;  0x190
     18c:	cf 96       	adiw	r24, 0x3f	; 63
     18e:	08 95       	ret
     190:	01 97       	sbiw	r24, 0x01	; 1
     192:	08 95       	ret
     194:	fc 01       	movw	r30, r24
     196:	91 8d       	ldd	r25, Z+25	; 0x19
     198:	82 8d       	ldd	r24, Z+26	; 0x1a
     19a:	98 17       	cp	r25, r24
     19c:	61 f0       	breq	.+24     	;  0x1b6
     19e:	82 8d       	ldd	r24, Z+26	; 0x1a
     1a0:	df 01       	movw	r26, r30
     1a2:	a8 0f       	add	r26, r24
     1a4:	b1 1d       	adc	r27, r1
     1a6:	5d 96       	adiw	r26, 0x1d	; 29
     1a8:	8c 91       	ld	r24, X
     1aa:	92 8d       	ldd	r25, Z+26	; 0x1a
     1ac:	9f 5f       	subi	r25, 0xFF	; 255
     1ae:	9f 73       	andi	r25, 0x3F	; 63
     1b0:	92 8f       	std	Z+26, r25	; 0x1a
     1b2:	90 e0       	ldi	r25, 0x00	; 0
     1b4:	08 95       	ret
     1b6:	8f ef       	ldi	r24, 0xFF	; 255
     1b8:	9f ef       	ldi	r25, 0xFF	; 255
     1ba:	08 95       	ret
     1bc:	fc 01       	movw	r30, r24
     1be:	91 8d       	ldd	r25, Z+25	; 0x19
     1c0:	82 8d       	ldd	r24, Z+26	; 0x1a
     1c2:	98 17       	cp	r25, r24
     1c4:	31 f0       	breq	.+12     	;  0x1d2
     1c6:	82 8d       	ldd	r24, Z+26	; 0x1a
     1c8:	e8 0f       	add	r30, r24
     1ca:	f1 1d       	adc	r31, r1
     1cc:	85 8d       	ldd	r24, Z+29	; 0x1d
     1ce:	90 e0       	ldi	r25, 0x00	; 0
     1d0:	08 95       	ret
     1d2:	8f ef       	ldi	r24, 0xFF	; 255
     1d4:	9f ef       	ldi	r25, 0xFF	; 255
     1d6:	08 95       	ret
     1d8:	fc 01       	movw	r30, r24
     1da:	91 8d       	ldd	r25, Z+25	; 0x19
     1dc:	22 8d       	ldd	r18, Z+26	; 0x1a
     1de:	89 2f       	mov	r24, r25
     1e0:	90 e0       	ldi	r25, 0x00	; 0
     1e2:	80 5c       	subi	r24, 0xC0	; 192
     1e4:	9f 4f       	sbci	r25, 0xFF	; 255
     1e6:	82 1b       	sub	r24, r18
     1e8:	91 09       	sbc	r25, r1
     1ea:	8f 73       	andi	r24, 0x3F	; 63
     1ec:	99 27       	eor	r25, r25
     1ee:	08 95       	ret
     1f0:	8f e8       	ldi	r24, 0x8F	; 143
     1f2:	95 e0       	ldi	r25, 0x05	; 5
     1f4:	0e 94 ec 00 	call	0x1d8	;  0x1d8
     1f8:	21 e0       	ldi	r18, 0x01	; 1
     1fa:	89 2b       	or	r24, r25
     1fc:	09 f4       	brne	.+2      	;  0x200
     1fe:	20 e0       	ldi	r18, 0x00	; 0
     200:	82 2f       	mov	r24, r18
     202:	08 95       	ret
     204:	cf 92       	push	r12
     206:	df 92       	push	r13
     208:	ef 92       	push	r14
     20a:	ff 92       	push	r15
     20c:	1f 93       	push	r17
     20e:	cf 93       	push	r28
     210:	df 93       	push	r29
     212:	ec 01       	movw	r28, r24
     214:	6a 01       	movw	r12, r20
     216:	7b 01       	movw	r14, r22
     218:	12 2f       	mov	r17, r18
     21a:	e8 89       	ldd	r30, Y+16	; 0x10
     21c:	f9 89       	ldd	r31, Y+17	; 0x11
     21e:	82 e0       	ldi	r24, 0x02	; 2
     220:	80 83       	st	Z, r24
     222:	41 15       	cp	r20, r1
     224:	51 4e       	sbci	r21, 0xE1	; 225
     226:	61 05       	cpc	r22, r1
     228:	71 05       	cpc	r23, r1
     22a:	b1 f0       	breq	.+44     	;  0x258
     22c:	60 e0       	ldi	r22, 0x00	; 0
     22e:	79 e0       	ldi	r23, 0x09	; 9
     230:	8d e3       	ldi	r24, 0x3D	; 61
     232:	90 e0       	ldi	r25, 0x00	; 0
     234:	a7 01       	movw	r20, r14
     236:	96 01       	movw	r18, r12
     238:	0e 94 46 06 	call	0xc8c	;  0xc8c
     23c:	da 01       	movw	r26, r20
     23e:	c9 01       	movw	r24, r18
     240:	01 97       	sbiw	r24, 0x01	; 1
     242:	a1 09       	sbc	r26, r1
     244:	b1 09       	sbc	r27, r1
     246:	b6 95       	lsr	r27
     248:	a7 95       	ror	r26
     24a:	97 95       	ror	r25
     24c:	87 95       	ror	r24
     24e:	ac 01       	movw	r20, r24
     250:	41 15       	cp	r20, r1
     252:	80 e1       	ldi	r24, 0x10	; 16
     254:	58 07       	cpc	r21, r24
     256:	a8 f0       	brcs	.+42     	;  0x282
     258:	e8 89       	ldd	r30, Y+16	; 0x10
     25a:	f9 89       	ldd	r31, Y+17	; 0x11
     25c:	10 82       	st	Z, r1
     25e:	60 e8       	ldi	r22, 0x80	; 128
     260:	74 e8       	ldi	r23, 0x84	; 132
     262:	8e e1       	ldi	r24, 0x1E	; 30
     264:	90 e0       	ldi	r25, 0x00	; 0
     266:	a7 01       	movw	r20, r14
     268:	96 01       	movw	r18, r12
     26a:	0e 94 46 06 	call	0xc8c	;  0xc8c
     26e:	ba 01       	movw	r22, r20
     270:	a9 01       	movw	r20, r18
     272:	41 50       	subi	r20, 0x01	; 1
     274:	51 09       	sbc	r21, r1
     276:	61 09       	sbc	r22, r1
     278:	71 09       	sbc	r23, r1
     27a:	76 95       	lsr	r23
     27c:	67 95       	ror	r22
     27e:	57 95       	ror	r21
     280:	47 95       	ror	r20
     282:	ec 85       	ldd	r30, Y+12	; 0x0c
     284:	fd 85       	ldd	r31, Y+13	; 0x0d
     286:	50 83       	st	Z, r21
     288:	ee 85       	ldd	r30, Y+14	; 0x0e
     28a:	ff 85       	ldd	r31, Y+15	; 0x0f
     28c:	40 83       	st	Z, r20
     28e:	18 8e       	std	Y+24, r1	; 0x18
     290:	ec 89       	ldd	r30, Y+20	; 0x14
     292:	fd 89       	ldd	r31, Y+21	; 0x15
     294:	10 83       	st	Z, r17
     296:	ea 89       	ldd	r30, Y+18	; 0x12
     298:	fb 89       	ldd	r31, Y+19	; 0x13
     29a:	80 81       	ld	r24, Z
     29c:	80 61       	ori	r24, 0x10	; 16
     29e:	80 83       	st	Z, r24
     2a0:	ea 89       	ldd	r30, Y+18	; 0x12
     2a2:	fb 89       	ldd	r31, Y+19	; 0x13
     2a4:	80 81       	ld	r24, Z
     2a6:	88 60       	ori	r24, 0x08	; 8
     2a8:	80 83       	st	Z, r24
     2aa:	ea 89       	ldd	r30, Y+18	; 0x12
     2ac:	fb 89       	ldd	r31, Y+19	; 0x13
     2ae:	80 81       	ld	r24, Z
     2b0:	80 68       	ori	r24, 0x80	; 128
     2b2:	80 83       	st	Z, r24
     2b4:	ea 89       	ldd	r30, Y+18	; 0x12
     2b6:	fb 89       	ldd	r31, Y+19	; 0x13
     2b8:	80 81       	ld	r24, Z
     2ba:	8f 7d       	andi	r24, 0xDF	; 223
     2bc:	80 83       	st	Z, r24
     2be:	df 91       	pop	r29
     2c0:	cf 91       	pop	r28
     2c2:	1f 91       	pop	r17
     2c4:	ff 90       	pop	r15
     2c6:	ef 90       	pop	r14
     2c8:	df 90       	pop	r13
     2ca:	cf 90       	pop	r12
     2cc:	08 95       	ret
     2ce:	fc 01       	movw	r30, r24
     2d0:	84 8d       	ldd	r24, Z+28	; 0x1c
     2d2:	df 01       	movw	r26, r30
     2d4:	a8 0f       	add	r26, r24
     2d6:	b1 1d       	adc	r27, r1
     2d8:	a3 5a       	subi	r26, 0xA3	; 163
     2da:	bf 4f       	sbci	r27, 0xFF	; 255
     2dc:	2c 91       	ld	r18, X
     2de:	84 8d       	ldd	r24, Z+28	; 0x1c
     2e0:	90 e0       	ldi	r25, 0x00	; 0
     2e2:	01 96       	adiw	r24, 0x01	; 1
     2e4:	8f 73       	andi	r24, 0x3F	; 63
     2e6:	99 27       	eor	r25, r25
     2e8:	84 8f       	std	Z+28, r24	; 0x1c
     2ea:	a6 89       	ldd	r26, Z+22	; 0x16
     2ec:	b7 89       	ldd	r27, Z+23	; 0x17
     2ee:	2c 93       	st	X, r18
     2f0:	a0 89       	ldd	r26, Z+16	; 0x10
     2f2:	b1 89       	ldd	r27, Z+17	; 0x11
     2f4:	8c 91       	ld	r24, X
     2f6:	80 64       	ori	r24, 0x40	; 64
     2f8:	8c 93       	st	X, r24
     2fa:	93 8d       	ldd	r25, Z+27	; 0x1b
     2fc:	84 8d       	ldd	r24, Z+28	; 0x1c
     2fe:	98 13       	cpse	r25, r24
     300:	06 c0       	rjmp	.+12     	;  0x30e
     302:	02 88       	ldd	r0, Z+18	; 0x12
     304:	f3 89       	ldd	r31, Z+19	; 0x13
     306:	e0 2d       	mov	r30, r0
     308:	80 81       	ld	r24, Z
     30a:	8f 7d       	andi	r24, 0xDF	; 223
     30c:	80 83       	st	Z, r24
     30e:	08 95       	ret
     310:	ef 92       	push	r14
     312:	ff 92       	push	r15
     314:	0f 93       	push	r16
     316:	1f 93       	push	r17
     318:	cf 93       	push	r28
     31a:	df 93       	push	r29
     31c:	ec 01       	movw	r28, r24
     31e:	81 e0       	ldi	r24, 0x01	; 1
     320:	88 8f       	std	Y+24, r24	; 0x18
     322:	9b 8d       	ldd	r25, Y+27	; 0x1b
     324:	8c 8d       	ldd	r24, Y+28	; 0x1c
     326:	98 13       	cpse	r25, r24
     328:	05 c0       	rjmp	.+10     	;  0x334
     32a:	e8 89       	ldd	r30, Y+16	; 0x10
     32c:	f9 89       	ldd	r31, Y+17	; 0x11
     32e:	80 81       	ld	r24, Z
     330:	85 fd       	sbrc	r24, 5
     332:	24 c0       	rjmp	.+72     	;  0x37c
     334:	f6 2e       	mov	r15, r22
     336:	0b 8d       	ldd	r16, Y+27	; 0x1b
     338:	10 e0       	ldi	r17, 0x00	; 0
     33a:	0f 5f       	subi	r16, 0xFF	; 255
     33c:	1f 4f       	sbci	r17, 0xFF	; 255
     33e:	0f 73       	andi	r16, 0x3F	; 63
     340:	11 27       	eor	r17, r17
     342:	e0 2e       	mov	r14, r16
     344:	8c 8d       	ldd	r24, Y+28	; 0x1c
     346:	e8 12       	cpse	r14, r24
     348:	0c c0       	rjmp	.+24     	;  0x362
     34a:	0f b6       	in	r0, 0x3f	; 63
     34c:	07 fc       	sbrc	r0, 7
     34e:	fa cf       	rjmp	.-12     	;  0x344
     350:	e8 89       	ldd	r30, Y+16	; 0x10
     352:	f9 89       	ldd	r31, Y+17	; 0x11
     354:	80 81       	ld	r24, Z
     356:	85 ff       	sbrs	r24, 5
     358:	f5 cf       	rjmp	.-22     	;  0x344
     35a:	ce 01       	movw	r24, r28
     35c:	0e 94 67 01 	call	0x2ce	;  0x2ce
     360:	f1 cf       	rjmp	.-30     	;  0x344
     362:	8b 8d       	ldd	r24, Y+27	; 0x1b
     364:	fe 01       	movw	r30, r28
     366:	e8 0f       	add	r30, r24
     368:	f1 1d       	adc	r31, r1
     36a:	e3 5a       	subi	r30, 0xA3	; 163
     36c:	ff 4f       	sbci	r31, 0xFF	; 255
     36e:	f0 82       	st	Z, r15
     370:	0b 8f       	std	Y+27, r16	; 0x1b
     372:	ea 89       	ldd	r30, Y+18	; 0x12
     374:	fb 89       	ldd	r31, Y+19	; 0x13
     376:	80 81       	ld	r24, Z
     378:	80 62       	ori	r24, 0x20	; 32
     37a:	07 c0       	rjmp	.+14     	;  0x38a
     37c:	ee 89       	ldd	r30, Y+22	; 0x16
     37e:	ff 89       	ldd	r31, Y+23	; 0x17
     380:	60 83       	st	Z, r22
     382:	e8 89       	ldd	r30, Y+16	; 0x10
     384:	f9 89       	ldd	r31, Y+17	; 0x11
     386:	80 81       	ld	r24, Z
     388:	80 64       	ori	r24, 0x40	; 64
     38a:	80 83       	st	Z, r24
     38c:	81 e0       	ldi	r24, 0x01	; 1
     38e:	90 e0       	ldi	r25, 0x00	; 0
     390:	df 91       	pop	r29
     392:	cf 91       	pop	r28
     394:	1f 91       	pop	r17
     396:	0f 91       	pop	r16
     398:	ff 90       	pop	r15
     39a:	ef 90       	pop	r14
     39c:	08 95       	ret
     39e:	cf 93       	push	r28
     3a0:	df 93       	push	r29
     3a2:	ec 01       	movw	r28, r24
     3a4:	88 8d       	ldd	r24, Y+24	; 0x18
     3a6:	88 23       	and	r24, r24
     3a8:	c9 f0       	breq	.+50     	;  0x3dc
     3aa:	ea 89       	ldd	r30, Y+18	; 0x12
     3ac:	fb 89       	ldd	r31, Y+19	; 0x13
     3ae:	80 81       	ld	r24, Z
     3b0:	85 fd       	sbrc	r24, 5
     3b2:	05 c0       	rjmp	.+10     	;  0x3be
     3b4:	a8 89       	ldd	r26, Y+16	; 0x10
     3b6:	b9 89       	ldd	r27, Y+17	; 0x11
     3b8:	8c 91       	ld	r24, X
     3ba:	86 fd       	sbrc	r24, 6
     3bc:	0f c0       	rjmp	.+30     	;  0x3dc
     3be:	0f b6       	in	r0, 0x3f	; 63
     3c0:	07 fc       	sbrc	r0, 7
     3c2:	f5 cf       	rjmp	.-22     	;  0x3ae
     3c4:	80 81       	ld	r24, Z
     3c6:	85 ff       	sbrs	r24, 5
     3c8:	f2 cf       	rjmp	.-28     	;  0x3ae
     3ca:	a8 89       	ldd	r26, Y+16	; 0x10
     3cc:	b9 89       	ldd	r27, Y+17	; 0x11
     3ce:	8c 91       	ld	r24, X
     3d0:	85 ff       	sbrs	r24, 5
     3d2:	ed cf       	rjmp	.-38     	;  0x3ae
     3d4:	ce 01       	movw	r24, r28
     3d6:	0e 94 67 01 	call	0x2ce	;  0x2ce
     3da:	e7 cf       	rjmp	.-50     	;  0x3aa
     3dc:	df 91       	pop	r29
     3de:	cf 91       	pop	r28
     3e0:	08 95       	ret
     3e2:	80 e0       	ldi	r24, 0x00	; 0
     3e4:	90 e0       	ldi	r25, 0x00	; 0
     3e6:	89 2b       	or	r24, r25
     3e8:	29 f0       	breq	.+10     	;  0x3f4
     3ea:	0e 94 f8 00 	call	0x1f0	;  0x1f0
     3ee:	81 11       	cpse	r24, r1
     3f0:	0c 94 00 00 	jmp	0	;  0x0
     3f4:	08 95       	ret
     3f6:	83 30       	cpi	r24, 0x03	; 3
     3f8:	81 f0       	breq	.+32     	;  0x41a
     3fa:	28 f4       	brcc	.+10     	;  0x406
     3fc:	81 30       	cpi	r24, 0x01	; 1
     3fe:	99 f0       	breq	.+38     	;  0x426
     400:	82 30       	cpi	r24, 0x02	; 2
     402:	a1 f0       	breq	.+40     	;  0x42c
     404:	08 95       	ret
     406:	87 30       	cpi	r24, 0x07	; 7
     408:	a9 f0       	breq	.+42     	;  0x434
     40a:	88 30       	cpi	r24, 0x08	; 8
     40c:	b9 f0       	breq	.+46     	;  0x43c
     40e:	84 30       	cpi	r24, 0x04	; 4
     410:	d1 f4       	brne	.+52     	;  0x446
     412:	80 91 80 00 	lds	r24, 0x0080	;  0x800080
     416:	8f 7d       	andi	r24, 0xDF	; 223
     418:	03 c0       	rjmp	.+6      	;  0x420
     41a:	80 91 80 00 	lds	r24, 0x0080	;  0x800080
     41e:	8f 77       	andi	r24, 0x7F	; 127
     420:	80 93 80 00 	sts	0x0080, r24	;  0x800080
     424:	08 95       	ret
     426:	84 b5       	in	r24, 0x24	; 36
     428:	8f 77       	andi	r24, 0x7F	; 127
     42a:	02 c0       	rjmp	.+4      	;  0x430
     42c:	84 b5       	in	r24, 0x24	; 36
     42e:	8f 7d       	andi	r24, 0xDF	; 223
     430:	84 bd       	out	0x24, r24	; 36
     432:	08 95       	ret
     434:	80 91 b0 00 	lds	r24, 0x00B0	;  0x8000b0
     438:	8f 77       	andi	r24, 0x7F	; 127
     43a:	03 c0       	rjmp	.+6      	;  0x442
     43c:	80 91 b0 00 	lds	r24, 0x00B0	;  0x8000b0
     440:	8f 7d       	andi	r24, 0xDF	; 223
     442:	80 93 b0 00 	sts	0x00B0, r24	;  0x8000b0
     446:	08 95       	ret
     448:	cf 93       	push	r28
     44a:	df 93       	push	r29
     44c:	28 2f       	mov	r18, r24
     44e:	30 e0       	ldi	r19, 0x00	; 0
     450:	f9 01       	movw	r30, r18
     452:	e2 55       	subi	r30, 0x52	; 82
     454:	ff 4f       	sbci	r31, 0xFF	; 255
     456:	84 91       	lpm	r24, Z
     458:	f9 01       	movw	r30, r18
     45a:	e6 56       	subi	r30, 0x66	; 102
     45c:	ff 4f       	sbci	r31, 0xFF	; 255
     45e:	d4 91       	lpm	r29, Z
     460:	f9 01       	movw	r30, r18
     462:	ea 57       	subi	r30, 0x7A	; 122
     464:	ff 4f       	sbci	r31, 0xFF	; 255
     466:	c4 91       	lpm	r28, Z
     468:	cc 23       	and	r28, r28
     46a:	91 f0       	breq	.+36     	;  0x490
     46c:	81 11       	cpse	r24, r1
     46e:	0e 94 fb 01 	call	0x3f6	;  0x3f6
     472:	ec 2f       	mov	r30, r28
     474:	f0 e0       	ldi	r31, 0x00	; 0
     476:	ee 0f       	add	r30, r30
     478:	ff 1f       	adc	r31, r31
     47a:	e4 58       	subi	r30, 0x84	; 132
     47c:	ff 4f       	sbci	r31, 0xFF	; 255
     47e:	a5 91       	lpm	r26, Z+
     480:	b4 91       	lpm	r27, Z
     482:	ec 91       	ld	r30, X
     484:	ed 23       	and	r30, r29
     486:	81 e0       	ldi	r24, 0x01	; 1
     488:	90 e0       	ldi	r25, 0x00	; 0
     48a:	21 f4       	brne	.+8      	;  0x494
     48c:	80 e0       	ldi	r24, 0x00	; 0
     48e:	02 c0       	rjmp	.+4      	;  0x494
     490:	80 e0       	ldi	r24, 0x00	; 0
     492:	90 e0       	ldi	r25, 0x00	; 0
     494:	df 91       	pop	r29
     496:	cf 91       	pop	r28
     498:	08 95       	ret
     49a:	1f 93       	push	r17
     49c:	cf 93       	push	r28
     49e:	df 93       	push	r29
     4a0:	28 2f       	mov	r18, r24
     4a2:	30 e0       	ldi	r19, 0x00	; 0
     4a4:	f9 01       	movw	r30, r18
     4a6:	e2 55       	subi	r30, 0x52	; 82
     4a8:	ff 4f       	sbci	r31, 0xFF	; 255
     4aa:	84 91       	lpm	r24, Z
     4ac:	f9 01       	movw	r30, r18
     4ae:	e6 56       	subi	r30, 0x66	; 102
     4b0:	ff 4f       	sbci	r31, 0xFF	; 255
     4b2:	d4 91       	lpm	r29, Z
     4b4:	f9 01       	movw	r30, r18
     4b6:	ea 57       	subi	r30, 0x7A	; 122
     4b8:	ff 4f       	sbci	r31, 0xFF	; 255
     4ba:	c4 91       	lpm	r28, Z
     4bc:	cc 23       	and	r28, r28
     4be:	c9 f0       	breq	.+50     	;  0x4f2
     4c0:	16 2f       	mov	r17, r22
     4c2:	81 11       	cpse	r24, r1
     4c4:	0e 94 fb 01 	call	0x3f6	;  0x3f6
     4c8:	ec 2f       	mov	r30, r28
     4ca:	f0 e0       	ldi	r31, 0x00	; 0
     4cc:	ee 0f       	add	r30, r30
     4ce:	ff 1f       	adc	r31, r31
     4d0:	ee 58       	subi	r30, 0x8E	; 142
     4d2:	ff 4f       	sbci	r31, 0xFF	; 255
     4d4:	a5 91       	lpm	r26, Z+
     4d6:	b4 91       	lpm	r27, Z
     4d8:	8f b7       	in	r24, 0x3f	; 63
     4da:	f8 94       	cli
     4dc:	11 11       	cpse	r17, r1
     4de:	05 c0       	rjmp	.+10     	;  0x4ea
     4e0:	9c 91       	ld	r25, X
     4e2:	ed 2f       	mov	r30, r29
     4e4:	e0 95       	com	r30
     4e6:	e9 23       	and	r30, r25
     4e8:	02 c0       	rjmp	.+4      	;  0x4ee
     4ea:	ec 91       	ld	r30, X
     4ec:	ed 2b       	or	r30, r29
     4ee:	ec 93       	st	X, r30
     4f0:	8f bf       	out	0x3f, r24	; 63
     4f2:	df 91       	pop	r29
     4f4:	cf 91       	pop	r28
     4f6:	1f 91       	pop	r17
     4f8:	08 95       	ret
     4fa:	cf 93       	push	r28
     4fc:	df 93       	push	r29
     4fe:	90 e0       	ldi	r25, 0x00	; 0
     500:	fc 01       	movw	r30, r24
     502:	e6 56       	subi	r30, 0x66	; 102
     504:	ff 4f       	sbci	r31, 0xFF	; 255
     506:	24 91       	lpm	r18, Z
     508:	fc 01       	movw	r30, r24
     50a:	ea 57       	subi	r30, 0x7A	; 122
     50c:	ff 4f       	sbci	r31, 0xFF	; 255
     50e:	84 91       	lpm	r24, Z
     510:	88 23       	and	r24, r24
     512:	61 f1       	breq	.+88     	;  0x56c
     514:	90 e0       	ldi	r25, 0x00	; 0
     516:	88 0f       	add	r24, r24
     518:	99 1f       	adc	r25, r25
     51a:	fc 01       	movw	r30, r24
     51c:	e8 59       	subi	r30, 0x98	; 152
     51e:	ff 4f       	sbci	r31, 0xFF	; 255
     520:	c5 91       	lpm	r28, Z+
     522:	d4 91       	lpm	r29, Z
     524:	fc 01       	movw	r30, r24
     526:	ee 58       	subi	r30, 0x8E	; 142
     528:	ff 4f       	sbci	r31, 0xFF	; 255
     52a:	a5 91       	lpm	r26, Z+
     52c:	b4 91       	lpm	r27, Z
     52e:	61 11       	cpse	r22, r1
     530:	09 c0       	rjmp	.+18     	;  0x544
     532:	9f b7       	in	r25, 0x3f	; 63
     534:	f8 94       	cli
     536:	88 81       	ld	r24, Y
     538:	20 95       	com	r18
     53a:	82 23       	and	r24, r18
     53c:	88 83       	st	Y, r24
     53e:	ec 91       	ld	r30, X
     540:	2e 23       	and	r18, r30
     542:	0b c0       	rjmp	.+22     	;  0x55a
     544:	62 30       	cpi	r22, 0x02	; 2
     546:	61 f4       	brne	.+24     	;  0x560
     548:	9f b7       	in	r25, 0x3f	; 63
     54a:	f8 94       	cli
     54c:	38 81       	ld	r19, Y
     54e:	82 2f       	mov	r24, r18
     550:	80 95       	com	r24
     552:	83 23       	and	r24, r19
     554:	88 83       	st	Y, r24
     556:	ec 91       	ld	r30, X
     558:	2e 2b       	or	r18, r30
     55a:	2c 93       	st	X, r18
     55c:	9f bf       	out	0x3f, r25	; 63
     55e:	06 c0       	rjmp	.+12     	;  0x56c
     560:	8f b7       	in	r24, 0x3f	; 63
     562:	f8 94       	cli
     564:	e8 81       	ld	r30, Y
     566:	2e 2b       	or	r18, r30
     568:	28 83       	st	Y, r18
     56a:	8f bf       	out	0x3f, r24	; 63
     56c:	df 91       	pop	r29
     56e:	cf 91       	pop	r28
     570:	08 95       	ret
     572:	3f b7       	in	r19, 0x3f	; 63
     574:	f8 94       	cli
     576:	80 91 8b 05 	lds	r24, 0x058B	;  0x80058b
     57a:	90 91 8c 05 	lds	r25, 0x058C	;  0x80058c
     57e:	a0 91 8d 05 	lds	r26, 0x058D	;  0x80058d
     582:	b0 91 8e 05 	lds	r27, 0x058E	;  0x80058e
     586:	26 b5       	in	r18, 0x26	; 38
     588:	a8 9b       	sbis	0x15, 0	; 21
     58a:	05 c0       	rjmp	.+10     	;  0x596
     58c:	2f 3f       	cpi	r18, 0xFF	; 255
     58e:	19 f0       	breq	.+6      	;  0x596
     590:	01 96       	adiw	r24, 0x01	; 1
     592:	a1 1d       	adc	r26, r1
     594:	b1 1d       	adc	r27, r1
     596:	3f bf       	out	0x3f, r19	; 63
     598:	ba 2f       	mov	r27, r26
     59a:	a9 2f       	mov	r26, r25
     59c:	98 2f       	mov	r25, r24
     59e:	88 27       	eor	r24, r24
     5a0:	82 0f       	add	r24, r18
     5a2:	91 1d       	adc	r25, r1
     5a4:	a1 1d       	adc	r26, r1
     5a6:	b1 1d       	adc	r27, r1
     5a8:	bc 01       	movw	r22, r24
     5aa:	cd 01       	movw	r24, r26
     5ac:	42 e0       	ldi	r20, 0x02	; 2
     5ae:	66 0f       	add	r22, r22
     5b0:	77 1f       	adc	r23, r23
     5b2:	88 1f       	adc	r24, r24
     5b4:	99 1f       	adc	r25, r25
     5b6:	4a 95       	dec	r20
     5b8:	d1 f7       	brne	.-12     	;  0x5ae
     5ba:	08 95       	ret
     5bc:	8f 92       	push	r8
     5be:	9f 92       	push	r9
     5c0:	af 92       	push	r10
     5c2:	bf 92       	push	r11
     5c4:	cf 92       	push	r12
     5c6:	df 92       	push	r13
     5c8:	ef 92       	push	r14
     5ca:	ff 92       	push	r15
     5cc:	6b 01       	movw	r12, r22
     5ce:	7c 01       	movw	r14, r24
     5d0:	0e 94 b9 02 	call	0x572	;  0x572
     5d4:	4b 01       	movw	r8, r22
     5d6:	5c 01       	movw	r10, r24
     5d8:	c1 14       	cp	r12, r1
     5da:	d1 04       	cpc	r13, r1
     5dc:	e1 04       	cpc	r14, r1
     5de:	f1 04       	cpc	r15, r1
     5e0:	f1 f0       	breq	.+60     	;  0x61e
     5e2:	0e 94 b9 02 	call	0x572	;  0x572
     5e6:	dc 01       	movw	r26, r24
     5e8:	cb 01       	movw	r24, r22
     5ea:	88 19       	sub	r24, r8
     5ec:	99 09       	sbc	r25, r9
     5ee:	aa 09       	sbc	r26, r10
     5f0:	bb 09       	sbc	r27, r11
     5f2:	88 3e       	cpi	r24, 0xE8	; 232
     5f4:	93 40       	sbci	r25, 0x03	; 3
     5f6:	a1 05       	cpc	r26, r1
     5f8:	b1 05       	cpc	r27, r1
     5fa:	70 f3       	brcs	.-36     	;  0x5d8
     5fc:	21 e0       	ldi	r18, 0x01	; 1
     5fe:	c2 1a       	sub	r12, r18
     600:	d1 08       	sbc	r13, r1
     602:	e1 08       	sbc	r14, r1
     604:	f1 08       	sbc	r15, r1
     606:	88 ee       	ldi	r24, 0xE8	; 232
     608:	88 0e       	add	r8, r24
     60a:	83 e0       	ldi	r24, 0x03	; 3
     60c:	98 1e       	adc	r9, r24
     60e:	a1 1c       	adc	r10, r1
     610:	b1 1c       	adc	r11, r1
     612:	c1 14       	cp	r12, r1
     614:	d1 04       	cpc	r13, r1
     616:	e1 04       	cpc	r14, r1
     618:	f1 04       	cpc	r15, r1
     61a:	19 f7       	brne	.-58     	;  0x5e2
     61c:	dd cf       	rjmp	.-70     	;  0x5d8
     61e:	ff 90       	pop	r15
     620:	ef 90       	pop	r14
     622:	df 90       	pop	r13
     624:	cf 90       	pop	r12
     626:	bf 90       	pop	r11
     628:	af 90       	pop	r10
     62a:	9f 90       	pop	r9
     62c:	8f 90       	pop	r8
     62e:	08 95       	ret
     630:	26 e0       	ldi	r18, 0x06	; 6
     632:	0c 94 02 01 	jmp	0x204	;  0x204
     636:	0e 94 6e 06 	call	0xcdc	;  0xcdc
     63a:	61 15       	cp	r22, r1
     63c:	71 05       	cpc	r23, r1
     63e:	79 f0       	breq	.+30     	;  0x65e
     640:	fb 01       	movw	r30, r22
     642:	01 90       	ld	r0, Z+
     644:	00 20       	and	r0, r0
     646:	e9 f7       	brne	.-6      	;  0x642
     648:	31 97       	sbiw	r30, 0x01	; 1
     64a:	af 01       	movw	r20, r30
     64c:	46 1b       	sub	r20, r22
     64e:	57 0b       	sbc	r21, r23
     650:	dc 01       	movw	r26, r24
     652:	ed 91       	ld	r30, X+
     654:	fc 91       	ld	r31, X
     656:	02 80       	ldd	r0, Z+2	; 0x02
     658:	f3 81       	ldd	r31, Z+3	; 0x03
     65a:	e0 2d       	mov	r30, r0
     65c:	09 94       	ijmp
     65e:	80 e0       	ldi	r24, 0x00	; 0
     660:	90 e0       	ldi	r25, 0x00	; 0
     662:	08 95       	ret
     664:	0f 93       	push	r16
     666:	1f 93       	push	r17
     668:	cf 93       	push	r28
     66a:	df 93       	push	r29
     66c:	ec 01       	movw	r28, r24
     66e:	0e 94 1d 03 	call	0x63a	;  0x63a
     672:	8c 01       	movw	r16, r24
     674:	62 e2       	ldi	r22, 0x22	; 34
     676:	75 e0       	ldi	r23, 0x05	; 5
     678:	ce 01       	movw	r24, r28
     67a:	0e 94 1d 03 	call	0x63a	;  0x63a
     67e:	80 0f       	add	r24, r16
     680:	91 1f       	adc	r25, r17
     682:	df 91       	pop	r29
     684:	cf 91       	pop	r28
     686:	1f 91       	pop	r17
     688:	0f 91       	pop	r16
     68a:	08 95       	ret
     68c:	af 92       	push	r10
     68e:	bf 92       	push	r11
     690:	cf 92       	push	r12
     692:	df 92       	push	r13
     694:	ef 92       	push	r14
     696:	ff 92       	push	r15
     698:	0f 93       	push	r16
     69a:	1f 93       	push	r17
     69c:	cf 93       	push	r28
     69e:	df 93       	push	r29
     6a0:	cd b7       	in	r28, 0x3d	; 61
     6a2:	de b7       	in	r29, 0x3e	; 62
     6a4:	a1 97       	sbiw	r28, 0x21	; 33
     6a6:	0f b6       	in	r0, 0x3f	; 63
     6a8:	f8 94       	cli
     6aa:	de bf       	out	0x3e, r29	; 62
     6ac:	0f be       	out	0x3f, r0	; 63
     6ae:	cd bf       	out	0x3d, r28	; 61
     6b0:	5c 01       	movw	r10, r24
     6b2:	41 15       	cp	r20, r1
     6b4:	51 05       	cpc	r21, r1
     6b6:	41 f4       	brne	.+16     	;  0x6c8
     6b8:	dc 01       	movw	r26, r24
     6ba:	ed 91       	ld	r30, X+
     6bc:	fc 91       	ld	r31, X
     6be:	01 90       	ld	r0, Z+
     6c0:	f0 81       	ld	r31, Z
     6c2:	e0 2d       	mov	r30, r0
     6c4:	09 95       	icall
     6c6:	26 c0       	rjmp	.+76     	;  0x714
     6c8:	19 a2       	std	Y+33, r1	; 0x21
     6ca:	42 30       	cpi	r20, 0x02	; 2
     6cc:	08 f4       	brcc	.+2      	;  0x6d0
     6ce:	4a e0       	ldi	r20, 0x0A	; 10
     6d0:	70 e0       	ldi	r23, 0x00	; 0
     6d2:	80 e0       	ldi	r24, 0x00	; 0
     6d4:	90 e0       	ldi	r25, 0x00	; 0
     6d6:	8e 01       	movw	r16, r28
     6d8:	0f 5d       	subi	r16, 0xDF	; 223
     6da:	1f 4f       	sbci	r17, 0xFF	; 255
     6dc:	c4 2e       	mov	r12, r20
     6de:	d1 2c       	mov	r13, r1
     6e0:	e1 2c       	mov	r14, r1
     6e2:	f1 2c       	mov	r15, r1
     6e4:	a7 01       	movw	r20, r14
     6e6:	96 01       	movw	r18, r12
     6e8:	0e 94 46 06 	call	0xc8c	;  0xc8c
     6ec:	e6 2f       	mov	r30, r22
     6ee:	ca 01       	movw	r24, r20
     6f0:	b9 01       	movw	r22, r18
     6f2:	01 50       	subi	r16, 0x01	; 1
     6f4:	11 09       	sbc	r17, r1
     6f6:	ea 30       	cpi	r30, 0x0A	; 10
     6f8:	14 f4       	brge	.+4      	;  0x6fe
     6fa:	e0 5d       	subi	r30, 0xD0	; 208
     6fc:	01 c0       	rjmp	.+2      	;  0x700
     6fe:	e9 5c       	subi	r30, 0xC9	; 201
     700:	d8 01       	movw	r26, r16
     702:	ec 93       	st	X, r30
     704:	23 2b       	or	r18, r19
     706:	24 2b       	or	r18, r20
     708:	25 2b       	or	r18, r21
     70a:	61 f7       	brne	.-40     	;  0x6e4
     70c:	b8 01       	movw	r22, r16
     70e:	c5 01       	movw	r24, r10
     710:	0e 94 1d 03 	call	0x63a	;  0x63a
     714:	a1 96       	adiw	r28, 0x21	; 33
     716:	0f b6       	in	r0, 0x3f	; 63
     718:	f8 94       	cli
     71a:	de bf       	out	0x3e, r29	; 62
     71c:	0f be       	out	0x3f, r0	; 63
     71e:	cd bf       	out	0x3d, r28	; 61
     720:	df 91       	pop	r29
     722:	cf 91       	pop	r28
     724:	1f 91       	pop	r17
     726:	0f 91       	pop	r16
     728:	ff 90       	pop	r15
     72a:	ef 90       	pop	r14
     72c:	df 90       	pop	r13
     72e:	cf 90       	pop	r12
     730:	bf 90       	pop	r11
     732:	af 90       	pop	r10
     734:	08 95       	ret
     736:	0c 94 1d 03 	jmp	0x63a	;  0x63a
     73a:	1f 92       	push	r1
     73c:	0f 92       	push	r0
     73e:	0f b6       	in	r0, 0x3f	; 63
     740:	0f 92       	push	r0
     742:	11 24       	eor	r1, r1
     744:	2f 93       	push	r18
     746:	3f 93       	push	r19
     748:	4f 93       	push	r20
     74a:	5f 93       	push	r21
     74c:	6f 93       	push	r22
     74e:	7f 93       	push	r23
     750:	8f 93       	push	r24
     752:	9f 93       	push	r25
     754:	af 93       	push	r26
     756:	bf 93       	push	r27
     758:	ef 93       	push	r30
     75a:	ff 93       	push	r31
     75c:	8f e8       	ldi	r24, 0x8F	; 143
     75e:	95 e0       	ldi	r25, 0x05	; 5
     760:	0e 94 67 01 	call	0x2ce	;  0x2ce
     764:	ff 91       	pop	r31
     766:	ef 91       	pop	r30
     768:	bf 91       	pop	r27
     76a:	af 91       	pop	r26
     76c:	9f 91       	pop	r25
     76e:	8f 91       	pop	r24
     770:	7f 91       	pop	r23
     772:	6f 91       	pop	r22
     774:	5f 91       	pop	r21
     776:	4f 91       	pop	r20
     778:	3f 91       	pop	r19
     77a:	2f 91       	pop	r18
     77c:	0f 90       	pop	r0
     77e:	0f be       	out	0x3f, r0	; 63
     780:	0f 90       	pop	r0
     782:	1f 90       	pop	r1
     784:	18 95       	reti
     786:	1f 92       	push	r1
     788:	0f 92       	push	r0
     78a:	0f b6       	in	r0, 0x3f	; 63
     78c:	0f 92       	push	r0
     78e:	11 24       	eor	r1, r1
     790:	2f 93       	push	r18
     792:	8f 93       	push	r24
     794:	9f 93       	push	r25
     796:	ef 93       	push	r30
     798:	ff 93       	push	r31
     79a:	e0 91 9f 05 	lds	r30, 0x059F	;  0x80059f
     79e:	f0 91 a0 05 	lds	r31, 0x05A0	;  0x8005a0
     7a2:	80 81       	ld	r24, Z
     7a4:	e0 91 a5 05 	lds	r30, 0x05A5	;  0x8005a5
     7a8:	f0 91 a6 05 	lds	r31, 0x05A6	;  0x8005a6
     7ac:	82 fd       	sbrc	r24, 2
     7ae:	12 c0       	rjmp	.+36     	;  0x7d4
     7b0:	90 81       	ld	r25, Z
     7b2:	80 91 a8 05 	lds	r24, 0x05A8	;  0x8005a8
     7b6:	8f 5f       	subi	r24, 0xFF	; 255
     7b8:	8f 73       	andi	r24, 0x3F	; 63
     7ba:	20 91 a9 05 	lds	r18, 0x05A9	;  0x8005a9
     7be:	82 17       	cp	r24, r18
     7c0:	51 f0       	breq	.+20     	;  0x7d6
     7c2:	e0 91 a8 05 	lds	r30, 0x05A8	;  0x8005a8
     7c6:	f0 e0       	ldi	r31, 0x00	; 0
     7c8:	e1 57       	subi	r30, 0x71	; 113
     7ca:	fa 4f       	sbci	r31, 0xFA	; 250
     7cc:	95 8f       	std	Z+29, r25	; 0x1d
     7ce:	80 93 a8 05 	sts	0x05A8, r24	;  0x8005a8
     7d2:	01 c0       	rjmp	.+2      	;  0x7d6
     7d4:	80 81       	ld	r24, Z
     7d6:	ff 91       	pop	r31
     7d8:	ef 91       	pop	r30
     7da:	9f 91       	pop	r25
     7dc:	8f 91       	pop	r24
     7de:	2f 91       	pop	r18
     7e0:	0f 90       	pop	r0
     7e2:	0f be       	out	0x3f, r0	; 63
     7e4:	0f 90       	pop	r0
     7e6:	1f 90       	pop	r1
     7e8:	18 95       	reti
     7ea:	1f 92       	push	r1
     7ec:	0f 92       	push	r0
     7ee:	0f b6       	in	r0, 0x3f	; 63
     7f0:	0f 92       	push	r0
     7f2:	11 24       	eor	r1, r1
     7f4:	2f 93       	push	r18
     7f6:	3f 93       	push	r19
     7f8:	8f 93       	push	r24
     7fa:	9f 93       	push	r25
     7fc:	af 93       	push	r26
     7fe:	bf 93       	push	r27
     800:	80 91 87 05 	lds	r24, 0x0587	;  0x800587
     804:	90 91 88 05 	lds	r25, 0x0588	;  0x800588
     808:	a0 91 89 05 	lds	r26, 0x0589	;  0x800589
     80c:	b0 91 8a 05 	lds	r27, 0x058A	;  0x80058a
     810:	30 91 86 05 	lds	r19, 0x0586	;  0x800586
     814:	23 e0       	ldi	r18, 0x03	; 3
     816:	23 0f       	add	r18, r19
     818:	2d 37       	cpi	r18, 0x7D	; 125
     81a:	20 f4       	brcc	.+8      	;  0x824
     81c:	01 96       	adiw	r24, 0x01	; 1
     81e:	a1 1d       	adc	r26, r1
     820:	b1 1d       	adc	r27, r1
     822:	05 c0       	rjmp	.+10     	;  0x82e
     824:	26 e8       	ldi	r18, 0x86	; 134
     826:	23 0f       	add	r18, r19
     828:	02 96       	adiw	r24, 0x02	; 2
     82a:	a1 1d       	adc	r26, r1
     82c:	b1 1d       	adc	r27, r1
     82e:	20 93 86 05 	sts	0x0586, r18	;  0x800586
     832:	80 93 87 05 	sts	0x0587, r24	;  0x800587
     836:	90 93 88 05 	sts	0x0588, r25	;  0x800588
     83a:	a0 93 89 05 	sts	0x0589, r26	;  0x800589
     83e:	b0 93 8a 05 	sts	0x058A, r27	;  0x80058a
     842:	80 91 8b 05 	lds	r24, 0x058B	;  0x80058b
     846:	90 91 8c 05 	lds	r25, 0x058C	;  0x80058c
     84a:	a0 91 8d 05 	lds	r26, 0x058D	;  0x80058d
     84e:	b0 91 8e 05 	lds	r27, 0x058E	;  0x80058e
     852:	01 96       	adiw	r24, 0x01	; 1
     854:	a1 1d       	adc	r26, r1
     856:	b1 1d       	adc	r27, r1
     858:	80 93 8b 05 	sts	0x058B, r24	;  0x80058b
     85c:	90 93 8c 05 	sts	0x058C, r25	;  0x80058c
     860:	a0 93 8d 05 	sts	0x058D, r26	;  0x80058d
     864:	b0 93 8e 05 	sts	0x058E, r27	;  0x80058e
     868:	bf 91       	pop	r27
     86a:	af 91       	pop	r26
     86c:	9f 91       	pop	r25
     86e:	8f 91       	pop	r24
     870:	3f 91       	pop	r19
     872:	2f 91       	pop	r18
     874:	0f 90       	pop	r0
     876:	0f be       	out	0x3f, r0	; 63
     878:	0f 90       	pop	r0
     87a:	1f 90       	pop	r1
     87c:	18 95       	reti
     87e:	1f 93       	push	r17
     880:	cf 93       	push	r28
     882:	df 93       	push	r29
     884:	c0 e0       	ldi	r28, 0x00	; 0
     886:	d0 e0       	ldi	r29, 0x00	; 0
     888:	8c 2f       	mov	r24, r28
     88a:	0e 94 24 02 	call	0x448	;  0x448
     88e:	0c 2e       	mov	r0, r28
     890:	01 c0       	rjmp	.+2      	;  0x894
     892:	88 0f       	add	r24, r24
     894:	0a 94       	dec	r0
     896:	ea f7       	brpl	.-6      	;  0x892
     898:	81 2b       	or	r24, r17
     89a:	18 2f       	mov	r17, r24
     89c:	21 96       	adiw	r28, 0x01	; 1
     89e:	c8 30       	cpi	r28, 0x08	; 8
     8a0:	d1 05       	cpc	r29, r1
     8a2:	91 f7       	brne	.-28     	;  0x888
     8a4:	df 91       	pop	r29
     8a6:	cf 91       	pop	r28
     8a8:	1f 91       	pop	r17
     8aa:	08 95       	ret
     8ac:	cf 93       	push	r28
     8ae:	c0 e0       	ldi	r28, 0x00	; 0
     8b0:	60 e0       	ldi	r22, 0x00	; 0
     8b2:	8c 2f       	mov	r24, r28
     8b4:	0e 94 7d 02 	call	0x4fa	;  0x4fa
     8b8:	61 e0       	ldi	r22, 0x01	; 1
     8ba:	8c 2f       	mov	r24, r28
     8bc:	0e 94 4d 02 	call	0x49a	;  0x49a
     8c0:	cf 5f       	subi	r28, 0xFF	; 255
     8c2:	c8 30       	cpi	r28, 0x08	; 8
     8c4:	a9 f7       	brne	.-22     	;  0x8b0
     8c6:	61 e0       	ldi	r22, 0x01	; 1
     8c8:	8d e0       	ldi	r24, 0x0D	; 13
     8ca:	0e 94 7d 02 	call	0x4fa	;  0x4fa
     8ce:	40 e8       	ldi	r20, 0x80	; 128
     8d0:	55 e2       	ldi	r21, 0x25	; 37
     8d2:	60 e0       	ldi	r22, 0x00	; 0
     8d4:	70 e0       	ldi	r23, 0x00	; 0
     8d6:	8f e8       	ldi	r24, 0x8F	; 143
     8d8:	95 e0       	ldi	r25, 0x05	; 5
     8da:	0e 94 18 03 	call	0x630	;  0x630
     8de:	10 92 85 05 	sts	0x0585, r1	;  0x800585
     8e2:	cf 91       	pop	r28
     8e4:	08 95       	ret
     8e6:	8f 92       	push	r8
     8e8:	9f 92       	push	r9
     8ea:	af 92       	push	r10
     8ec:	bf 92       	push	r11
     8ee:	cf 92       	push	r12
     8f0:	df 92       	push	r13
     8f2:	ef 92       	push	r14
     8f4:	ff 92       	push	r15
     8f6:	0f 93       	push	r16
     8f8:	1f 93       	push	r17
     8fa:	cf 93       	push	r28
     8fc:	df 93       	push	r29
     8fe:	24 e0       	ldi	r18, 0x04	; 4
     900:	82 02       	muls	r24, r18
     902:	c0 01       	movw	r24, r0
     904:	11 24       	eor	r1, r1
     906:	fc 01       	movw	r30, r24
     908:	e0 50       	subi	r30, 0x00	; 0
     90a:	ff 4f       	sbci	r31, 0xFF	; 255
     90c:	c0 80       	ld	r12, Z
     90e:	d1 80       	ldd	r13, Z+1	; 0x01
     910:	e2 80       	ldd	r14, Z+2	; 0x02
     912:	f3 80       	ldd	r15, Z+3	; 0x03
     914:	c1 14       	cp	r12, r1
     916:	d1 04       	cpc	r13, r1
     918:	e1 04       	cpc	r14, r1
     91a:	f1 04       	cpc	r15, r1
     91c:	09 f4       	brne	.+2      	;  0x920
     91e:	4d c0       	rjmp	.+154    	;  0x9ba
     920:	c0 e0       	ldi	r28, 0x00	; 0
     922:	d0 e0       	ldi	r29, 0x00	; 0
     924:	02 e0       	ldi	r16, 0x02	; 2
     926:	81 2c       	mov	r8, r1
     928:	91 2c       	mov	r9, r1
     92a:	54 01       	movw	r10, r8
     92c:	83 94       	inc	r8
     92e:	d5 01       	movw	r26, r10
     930:	c4 01       	movw	r24, r8
     932:	0c 2e       	mov	r0, r28
     934:	04 c0       	rjmp	.+8      	;  0x93e
     936:	88 0f       	add	r24, r24
     938:	99 1f       	adc	r25, r25
     93a:	aa 1f       	adc	r26, r26
     93c:	bb 1f       	adc	r27, r27
     93e:	0a 94       	dec	r0
     940:	d2 f7       	brpl	.-12     	;  0x936
     942:	8c 21       	and	r24, r12
     944:	9d 21       	and	r25, r13
     946:	ae 21       	and	r26, r14
     948:	bf 21       	and	r27, r15
     94a:	89 2b       	or	r24, r25
     94c:	8a 2b       	or	r24, r26
     94e:	8b 2b       	or	r24, r27
     950:	39 f0       	breq	.+14     	;  0x960
     952:	61 e0       	ldi	r22, 0x01	; 1
     954:	8d e0       	ldi	r24, 0x0D	; 13
     956:	0e 94 4d 02 	call	0x49a	;  0x49a
     95a:	1f 5f       	subi	r17, 0xFF	; 255
     95c:	01 e0       	ldi	r16, 0x01	; 1
     95e:	10 c0       	rjmp	.+32     	;  0x980
     960:	00 23       	and	r16, r16
     962:	c1 f0       	breq	.+48     	;  0x994
     964:	60 e0       	ldi	r22, 0x00	; 0
     966:	8d e0       	ldi	r24, 0x0D	; 13
     968:	0e 94 4d 02 	call	0x49a	;  0x49a
     96c:	13 30       	cpi	r17, 0x03	; 3
     96e:	41 f5       	brne	.+80     	;  0x9c0
     970:	65 e2       	ldi	r22, 0x25	; 37
     972:	75 e0       	ldi	r23, 0x05	; 5
     974:	8f e8       	ldi	r24, 0x8F	; 143
     976:	95 e0       	ldi	r25, 0x05	; 5
     978:	0e 94 9b 03 	call	0x736	;  0x736
     97c:	00 e0       	ldi	r16, 0x00	; 0
     97e:	10 e0       	ldi	r17, 0x00	; 0
     980:	6a ef       	ldi	r22, 0xFA	; 250
     982:	70 e0       	ldi	r23, 0x00	; 0
     984:	80 e0       	ldi	r24, 0x00	; 0
     986:	90 e0       	ldi	r25, 0x00	; 0
     988:	0e 94 de 02 	call	0x5bc	;  0x5bc
     98c:	21 96       	adiw	r28, 0x01	; 1
     98e:	c0 32       	cpi	r28, 0x20	; 32
     990:	d1 05       	cpc	r29, r1
     992:	69 f6       	brne	.-102    	;  0x92e
     994:	60 e0       	ldi	r22, 0x00	; 0
     996:	8d e0       	ldi	r24, 0x0D	; 13
     998:	0e 94 4d 02 	call	0x49a	;  0x49a
     99c:	6e ee       	ldi	r22, 0xEE	; 238
     99e:	72 e0       	ldi	r23, 0x02	; 2
     9a0:	80 e0       	ldi	r24, 0x00	; 0
     9a2:	90 e0       	ldi	r25, 0x00	; 0
     9a4:	0e 94 de 02 	call	0x5bc	;  0x5bc
     9a8:	69 e2       	ldi	r22, 0x29	; 41
     9aa:	75 e0       	ldi	r23, 0x05	; 5
     9ac:	8f e8       	ldi	r24, 0x8F	; 143
     9ae:	95 e0       	ldi	r25, 0x05	; 5
     9b0:	0e 94 9b 03 	call	0x736	;  0x736
     9b4:	81 e0       	ldi	r24, 0x01	; 1
     9b6:	90 e0       	ldi	r25, 0x00	; 0
     9b8:	06 c0       	rjmp	.+12     	;  0x9c6
     9ba:	8f ef       	ldi	r24, 0xFF	; 255
     9bc:	9f ef       	ldi	r25, 0xFF	; 255
     9be:	03 c0       	rjmp	.+6      	;  0x9c6
     9c0:	67 e2       	ldi	r22, 0x27	; 39
     9c2:	75 e0       	ldi	r23, 0x05	; 5
     9c4:	d7 cf       	rjmp	.-82     	;  0x974
     9c6:	df 91       	pop	r29
     9c8:	cf 91       	pop	r28
     9ca:	1f 91       	pop	r17
     9cc:	0f 91       	pop	r16
     9ce:	ff 90       	pop	r15
     9d0:	ef 90       	pop	r14
     9d2:	df 90       	pop	r13
     9d4:	cf 90       	pop	r12
     9d6:	bf 90       	pop	r11
     9d8:	af 90       	pop	r10
     9da:	9f 90       	pop	r9
     9dc:	8f 90       	pop	r8
     9de:	08 95       	ret
     9e0:	ff 92       	push	r15
     9e2:	0f 93       	push	r16
     9e4:	1f 93       	push	r17
     9e6:	cf 93       	push	r28
     9e8:	df 93       	push	r29
     9ea:	18 2f       	mov	r17, r24
     9ec:	f9 2e       	mov	r15, r25
     9ee:	06 2f       	mov	r16, r22
     9f0:	6e ee       	ldi	r22, 0xEE	; 238
     9f2:	72 e0       	ldi	r23, 0x02	; 2
     9f4:	80 e0       	ldi	r24, 0x00	; 0
     9f6:	90 e0       	ldi	r25, 0x00	; 0
     9f8:	0e 94 de 02 	call	0x5bc	;  0x5bc
     9fc:	c1 2f       	mov	r28, r17
     9fe:	df 2d       	mov	r29, r15
     a00:	e1 2f       	mov	r30, r17
     a02:	ff 2d       	mov	r31, r15
     a04:	f1 2e       	mov	r15, r17
     a06:	8e 2f       	mov	r24, r30
     a08:	81 1b       	sub	r24, r17
     a0a:	80 17       	cp	r24, r16
     a0c:	98 f4       	brcc	.+38     	;  0xa34
     a0e:	a1 91       	ld	r26, Z+
     a10:	84 e0       	ldi	r24, 0x04	; 4
     a12:	a8 02       	muls	r26, r24
     a14:	d0 01       	movw	r26, r0
     a16:	11 24       	eor	r1, r1
     a18:	a0 50       	subi	r26, 0x00	; 0
     a1a:	bf 4f       	sbci	r27, 0xFF	; 255
     a1c:	8d 91       	ld	r24, X+
     a1e:	9d 91       	ld	r25, X+
     a20:	0d 90       	ld	r0, X+
     a22:	bc 91       	ld	r27, X
     a24:	a0 2d       	mov	r26, r0
     a26:	89 2b       	or	r24, r25
     a28:	8a 2b       	or	r24, r26
     a2a:	8b 2b       	or	r24, r27
     a2c:	61 f7       	brne	.-40     	;  0xa06
     a2e:	8f ef       	ldi	r24, 0xFF	; 255
     a30:	9f ef       	ldi	r25, 0xFF	; 255
     a32:	16 c0       	rjmp	.+44     	;  0xa60
     a34:	8c 2f       	mov	r24, r28
     a36:	8f 19       	sub	r24, r15
     a38:	80 17       	cp	r24, r16
     a3a:	20 f4       	brcc	.+8      	;  0xa44
     a3c:	89 91       	ld	r24, Y+
     a3e:	0e 94 73 04 	call	0x8e6	;  0x8e6
     a42:	f8 cf       	rjmp	.-16     	;  0xa34
     a44:	68 ee       	ldi	r22, 0xE8	; 232
     a46:	73 e0       	ldi	r23, 0x03	; 3
     a48:	80 e0       	ldi	r24, 0x00	; 0
     a4a:	90 e0       	ldi	r25, 0x00	; 0
     a4c:	0e 94 de 02 	call	0x5bc	;  0x5bc
     a50:	64 e2       	ldi	r22, 0x24	; 36
     a52:	75 e0       	ldi	r23, 0x05	; 5
     a54:	8f e8       	ldi	r24, 0x8F	; 143
     a56:	95 e0       	ldi	r25, 0x05	; 5
     a58:	0e 94 32 03 	call	0x664	;  0x664
     a5c:	81 e0       	ldi	r24, 0x01	; 1
     a5e:	90 e0       	ldi	r25, 0x00	; 0
     a60:	df 91       	pop	r29
     a62:	cf 91       	pop	r28
     a64:	1f 91       	pop	r17
     a66:	0f 91       	pop	r16
     a68:	ff 90       	pop	r15
     a6a:	08 95       	ret
     a6c:	cf 93       	push	r28
     a6e:	df 93       	push	r29
     a70:	cd b7       	in	r28, 0x3d	; 61
     a72:	de b7       	in	r29, 0x3e	; 62
     a74:	da 95       	dec	r29
     a76:	0f b6       	in	r0, 0x3f	; 63
     a78:	f8 94       	cli
     a7a:	de bf       	out	0x3e, r29	; 62
     a7c:	0f be       	out	0x3f, r0	; 63
     a7e:	cd bf       	out	0x3d, r28	; 61
     a80:	fe 01       	movw	r30, r28
     a82:	31 96       	adiw	r30, 0x01	; 1
     a84:	df 01       	movw	r26, r30
     a86:	9f ef       	ldi	r25, 0xFF	; 255
     a88:	9e 0f       	add	r25, r30
     a8a:	1d 92       	st	X+, r1
     a8c:	9a 13       	cpse	r25, r26
     a8e:	fd cf       	rjmp	.-6      	;  0xa8a
     a90:	95 eb       	ldi	r25, 0xB5	; 181
     a92:	99 83       	std	Y+1, r25	; 0x01
     a94:	9a 83       	std	Y+2, r25	; 0x02
     a96:	96 e8       	ldi	r25, 0x86	; 134
     a98:	9b 83       	std	Y+3, r25	; 0x03
     a9a:	94 eb       	ldi	r25, 0xB4	; 180
     a9c:	9c 83       	std	Y+4, r25	; 0x04
     a9e:	94 ef       	ldi	r25, 0xF4	; 244
     aa0:	9d 83       	std	Y+5, r25	; 0x05
     aa2:	93 eb       	ldi	r25, 0xB3	; 179
     aa4:	9e 83       	std	Y+6, r25	; 0x06
     aa6:	91 ef       	ldi	r25, 0xF1	; 241
     aa8:	9f 83       	std	Y+7, r25	; 0x07
     aaa:	20 eb       	ldi	r18, 0xB0	; 176
     aac:	28 87       	std	Y+8, r18	; 0x08
     aae:	29 87       	std	Y+9, r18	; 0x09
     ab0:	9a 87       	std	Y+10, r25	; 0x0a
     ab2:	9d ee       	ldi	r25, 0xED	; 237
     ab4:	9b 87       	std	Y+11, r25	; 0x0b
     ab6:	90 e8       	ldi	r25, 0x80	; 128
     ab8:	9c 87       	std	Y+12, r25	; 0x0c
     aba:	9b eb       	ldi	r25, 0xBB	; 187
     abc:	9d 87       	std	Y+13, r25	; 0x0d
     abe:	9f e8       	ldi	r25, 0x8F	; 143
     ac0:	9e 87       	std	Y+14, r25	; 0x0e
     ac2:	9f eb       	ldi	r25, 0xBF	; 191
     ac4:	9f 87       	std	Y+15, r25	; 0x0f
     ac6:	9d e8       	ldi	r25, 0x8D	; 141
     ac8:	98 8b       	std	Y+16, r25	; 0x10
     aca:	96 ec       	ldi	r25, 0xC6	; 198
     acc:	99 8b       	std	Y+17, r25	; 0x11
     ace:	95 e8       	ldi	r25, 0x85	; 133
     ad0:	9a 8b       	std	Y+18, r25	; 0x12
     ad2:	97 e8       	ldi	r25, 0x87	; 135
     ad4:	9b 8b       	std	Y+19, r25	; 0x13
     ad6:	90 ec       	ldi	r25, 0xC0	; 192
     ad8:	9c 8b       	std	Y+20, r25	; 0x14
     ada:	94 e9       	ldi	r25, 0x94	; 148
     adc:	9d 8b       	std	Y+21, r25	; 0x15
     ade:	91 e8       	ldi	r25, 0x81	; 129
     ae0:	9e 8b       	std	Y+22, r25	; 0x16
     ae2:	9c e8       	ldi	r25, 0x8C	; 140
     ae4:	9f 8b       	std	Y+23, r25	; 0x17
     ae6:	ac e6       	ldi	r26, 0x6C	; 108
     ae8:	b5 e0       	ldi	r27, 0x05	; 5
     aea:	20 e0       	ldi	r18, 0x00	; 0
     aec:	91 91       	ld	r25, Z+
     aee:	98 27       	eor	r25, r24
     af0:	92 0f       	add	r25, r18
     af2:	9d 93       	st	X+, r25
     af4:	2f 5f       	subi	r18, 0xFF	; 255
     af6:	27 31       	cpi	r18, 0x17	; 23
     af8:	c9 f7       	brne	.-14     	;  0xaec
     afa:	80 91 76 05 	lds	r24, 0x0576	;  0x800576
     afe:	80 34       	cpi	r24, 0x40	; 64
     b00:	a1 f4       	brne	.+40     	;  0xb2a
     b02:	6b e2       	ldi	r22, 0x2B	; 43
     b04:	75 e0       	ldi	r23, 0x05	; 5
     b06:	8f e8       	ldi	r24, 0x8F	; 143
     b08:	95 e0       	ldi	r25, 0x05	; 5
     b0a:	0e 94 32 03 	call	0x664	;  0x664
     b0e:	67 e1       	ldi	r22, 0x17	; 23
     b10:	8c e6       	ldi	r24, 0x6C	; 108
     b12:	95 e0       	ldi	r25, 0x05	; 5
     b14:	0e 94 f0 04 	call	0x9e0	;  0x9e0
     b18:	6c e6       	ldi	r22, 0x6C	; 108
     b1a:	75 e0       	ldi	r23, 0x05	; 5
     b1c:	8f e8       	ldi	r24, 0x8F	; 143
     b1e:	95 e0       	ldi	r25, 0x05	; 5
     b20:	0e 94 32 03 	call	0x664	;  0x664
     b24:	81 e0       	ldi	r24, 0x01	; 1
     b26:	90 e0       	ldi	r25, 0x00	; 0
     b28:	02 c0       	rjmp	.+4      	;  0xb2e
     b2a:	80 e0       	ldi	r24, 0x00	; 0
     b2c:	90 e0       	ldi	r25, 0x00	; 0
     b2e:	d3 95       	inc	r29
     b30:	0f b6       	in	r0, 0x3f	; 63
     b32:	f8 94       	cli
     b34:	de bf       	out	0x3e, r29	; 62
     b36:	0f be       	out	0x3f, r0	; 63
     b38:	cd bf       	out	0x3d, r28	; 61
     b3a:	df 91       	pop	r29
     b3c:	cf 91       	pop	r28
     b3e:	08 95       	ret
     b40:	cf 93       	push	r28
     b42:	0e 94 3f 04 	call	0x87e	;  0x87e
     b46:	c8 2f       	mov	r28, r24
     b48:	80 91 85 05 	lds	r24, 0x0585	;  0x800585
     b4c:	c8 17       	cp	r28, r24
     b4e:	01 f1       	breq	.+64     	;  0xb90
     b50:	60 91 00 05 	lds	r22, 0x0500	;  0x800500
     b54:	70 91 01 05 	lds	r23, 0x0501	;  0x800501
     b58:	8f e8       	ldi	r24, 0x8F	; 143
     b5a:	95 e0       	ldi	r25, 0x05	; 5
     b5c:	0e 94 9b 03 	call	0x736	;  0x736
     b60:	42 e0       	ldi	r20, 0x02	; 2
     b62:	50 e0       	ldi	r21, 0x00	; 0
     b64:	6c 2f       	mov	r22, r28
     b66:	8f e8       	ldi	r24, 0x8F	; 143
     b68:	95 e0       	ldi	r25, 0x05	; 5
     b6a:	0e 94 46 03 	call	0x68c	;  0x68c
     b6e:	64 e2       	ldi	r22, 0x24	; 36
     b70:	75 e0       	ldi	r23, 0x05	; 5
     b72:	8f e8       	ldi	r24, 0x8F	; 143
     b74:	95 e0       	ldi	r25, 0x05	; 5
     b76:	0e 94 32 03 	call	0x664	;  0x664
     b7a:	8c 2f       	mov	r24, r28
     b7c:	0e 94 36 05 	call	0xa6c	;  0xa6c
     b80:	01 97       	sbiw	r24, 0x01	; 1
     b82:	21 f0       	breq	.+8      	;  0xb8c
     b84:	60 e0       	ldi	r22, 0x00	; 0
     b86:	8d e0       	ldi	r24, 0x0D	; 13
     b88:	0e 94 4d 02 	call	0x49a	;  0x49a
     b8c:	c0 93 85 05 	sts	0x0585, r28	;  0x800585
     b90:	68 ee       	ldi	r22, 0xE8	; 232
     b92:	73 e0       	ldi	r23, 0x03	; 3
     b94:	80 e0       	ldi	r24, 0x00	; 0
     b96:	90 e0       	ldi	r25, 0x00	; 0
     b98:	cf 91       	pop	r28
     b9a:	0c 94 de 02 	jmp	0x5bc	;  0x5bc
     b9e:	ef e8       	ldi	r30, 0x8F	; 143
     ba0:	f5 e0       	ldi	r31, 0x05	; 5
     ba2:	13 82       	std	Z+3, r1	; 0x03
     ba4:	12 82       	std	Z+2, r1	; 0x02
     ba6:	88 ee       	ldi	r24, 0xE8	; 232
     ba8:	93 e0       	ldi	r25, 0x03	; 3
     baa:	a0 e0       	ldi	r26, 0x00	; 0
     bac:	b0 e0       	ldi	r27, 0x00	; 0
     bae:	84 83       	std	Z+4, r24	; 0x04
     bb0:	95 83       	std	Z+5, r25	; 0x05
     bb2:	a6 83       	std	Z+6, r26	; 0x06
     bb4:	b7 83       	std	Z+7, r27	; 0x07
     bb6:	84 e1       	ldi	r24, 0x14	; 20
     bb8:	95 e0       	ldi	r25, 0x05	; 5
     bba:	91 83       	std	Z+1, r25	; 0x01
     bbc:	80 83       	st	Z, r24
     bbe:	85 ec       	ldi	r24, 0xC5	; 197
     bc0:	90 e0       	ldi	r25, 0x00	; 0
     bc2:	95 87       	std	Z+13, r25	; 0x0d
     bc4:	84 87       	std	Z+12, r24	; 0x0c
     bc6:	84 ec       	ldi	r24, 0xC4	; 196
     bc8:	90 e0       	ldi	r25, 0x00	; 0
     bca:	97 87       	std	Z+15, r25	; 0x0f
     bcc:	86 87       	std	Z+14, r24	; 0x0e
     bce:	80 ec       	ldi	r24, 0xC0	; 192
     bd0:	90 e0       	ldi	r25, 0x00	; 0
     bd2:	91 8b       	std	Z+17, r25	; 0x11
     bd4:	80 8b       	std	Z+16, r24	; 0x10
     bd6:	81 ec       	ldi	r24, 0xC1	; 193
     bd8:	90 e0       	ldi	r25, 0x00	; 0
     bda:	93 8b       	std	Z+19, r25	; 0x13
     bdc:	82 8b       	std	Z+18, r24	; 0x12
     bde:	82 ec       	ldi	r24, 0xC2	; 194
     be0:	90 e0       	ldi	r25, 0x00	; 0
     be2:	95 8b       	std	Z+21, r25	; 0x15
     be4:	84 8b       	std	Z+20, r24	; 0x14
     be6:	86 ec       	ldi	r24, 0xC6	; 198
     be8:	90 e0       	ldi	r25, 0x00	; 0
     bea:	97 8b       	std	Z+23, r25	; 0x17
     bec:	86 8b       	std	Z+22, r24	; 0x16
     bee:	11 8e       	std	Z+25, r1	; 0x19
     bf0:	12 8e       	std	Z+26, r1	; 0x1a
     bf2:	13 8e       	std	Z+27, r1	; 0x1b
     bf4:	14 8e       	std	Z+28, r1	; 0x1c
     bf6:	08 95       	ret
     bf8:	78 94       	sei
     bfa:	84 b5       	in	r24, 0x24	; 36
     bfc:	82 60       	ori	r24, 0x02	; 2
     bfe:	84 bd       	out	0x24, r24	; 36
     c00:	84 b5       	in	r24, 0x24	; 36
     c02:	81 60       	ori	r24, 0x01	; 1
     c04:	84 bd       	out	0x24, r24	; 36
     c06:	85 b5       	in	r24, 0x25	; 37
     c08:	82 60       	ori	r24, 0x02	; 2
     c0a:	85 bd       	out	0x25, r24	; 37
     c0c:	85 b5       	in	r24, 0x25	; 37
     c0e:	81 60       	ori	r24, 0x01	; 1
     c10:	85 bd       	out	0x25, r24	; 37
     c12:	80 91 6e 00 	lds	r24, 0x006E	;  0x80006e
     c16:	81 60       	ori	r24, 0x01	; 1
     c18:	80 93 6e 00 	sts	0x006E, r24	;  0x80006e
     c1c:	10 92 81 00 	sts	0x0081, r1	;  0x800081
     c20:	80 91 81 00 	lds	r24, 0x0081	;  0x800081
     c24:	82 60       	ori	r24, 0x02	; 2
     c26:	80 93 81 00 	sts	0x0081, r24	;  0x800081
     c2a:	80 91 81 00 	lds	r24, 0x0081	;  0x800081
     c2e:	81 60       	ori	r24, 0x01	; 1
     c30:	80 93 81 00 	sts	0x0081, r24	;  0x800081
     c34:	80 91 80 00 	lds	r24, 0x0080	;  0x800080
     c38:	81 60       	ori	r24, 0x01	; 1
     c3a:	80 93 80 00 	sts	0x0080, r24	;  0x800080
     c3e:	80 91 b1 00 	lds	r24, 0x00B1	;  0x8000b1
     c42:	84 60       	ori	r24, 0x04	; 4
     c44:	80 93 b1 00 	sts	0x00B1, r24	;  0x8000b1
     c48:	80 91 b0 00 	lds	r24, 0x00B0	;  0x8000b0
     c4c:	81 60       	ori	r24, 0x01	; 1
     c4e:	80 93 b0 00 	sts	0x00B0, r24	;  0x8000b0
     c52:	80 91 7a 00 	lds	r24, 0x007A	;  0x80007a
     c56:	84 60       	ori	r24, 0x04	; 4
     c58:	80 93 7a 00 	sts	0x007A, r24	;  0x80007a
     c5c:	80 91 7a 00 	lds	r24, 0x007A	;  0x80007a
     c60:	82 60       	ori	r24, 0x02	; 2
     c62:	80 93 7a 00 	sts	0x007A, r24	;  0x80007a
     c66:	80 91 7a 00 	lds	r24, 0x007A	;  0x80007a
     c6a:	81 60       	ori	r24, 0x01	; 1
     c6c:	80 93 7a 00 	sts	0x007A, r24	;  0x80007a
     c70:	80 91 7a 00 	lds	r24, 0x007A	;  0x80007a
     c74:	80 68       	ori	r24, 0x80	; 128
     c76:	80 93 7a 00 	sts	0x007A, r24	;  0x80007a
     c7a:	10 92 c1 00 	sts	0x00C1, r1	;  0x8000c1
     c7e:	0e 94 56 04 	call	0x8ac	;  0x8ac
     c82:	0e 94 a0 05 	call	0xb40	;  0xb40
     c86:	0e 94 f1 01 	call	0x3e2	;  0x3e2
     c8a:	fb cf       	rjmp	.-10     	;  0xc82
     c8c:	a1 e2       	ldi	r26, 0x21	; 33
     c8e:	1a 2e       	mov	r1, r26
     c90:	aa 1b       	sub	r26, r26
     c92:	bb 1b       	sub	r27, r27
     c94:	fd 01       	movw	r30, r26
     c96:	0d c0       	rjmp	.+26     	;  0xcb2
     c98:	aa 1f       	adc	r26, r26
     c9a:	bb 1f       	adc	r27, r27
     c9c:	ee 1f       	adc	r30, r30
     c9e:	ff 1f       	adc	r31, r31
     ca0:	a2 17       	cp	r26, r18
     ca2:	b3 07       	cpc	r27, r19
     ca4:	e4 07       	cpc	r30, r20
     ca6:	f5 07       	cpc	r31, r21
     ca8:	20 f0       	brcs	.+8      	;  0xcb2
     caa:	a2 1b       	sub	r26, r18
     cac:	b3 0b       	sbc	r27, r19
     cae:	e4 0b       	sbc	r30, r20
     cb0:	f5 0b       	sbc	r31, r21
     cb2:	66 1f       	adc	r22, r22
     cb4:	77 1f       	adc	r23, r23
     cb6:	88 1f       	adc	r24, r24
     cb8:	99 1f       	adc	r25, r25
     cba:	1a 94       	dec	r1
     cbc:	69 f7       	brne	.-38     	;  0xc98
     cbe:	60 95       	com	r22
     cc0:	70 95       	com	r23
     cc2:	80 95       	com	r24
     cc4:	90 95       	com	r25
     cc6:	9b 01       	movw	r18, r22
     cc8:	ac 01       	movw	r20, r24
     cca:	bd 01       	movw	r22, r26
     ccc:	cf 01       	movw	r24, r30
     cce:	08 95       	ret
     cd0:	ee 0f       	add	r30, r30
     cd2:	ff 1f       	adc	r31, r31
     cd4:	05 90       	lpm	r0, Z+
     cd6:	f4 91       	lpm	r31, Z
     cd8:	e0 2d       	mov	r30, r0
     cda:	09 94       	ijmp
     cdc:	81 e0       	ldi	r24, 0x01	; 1
     cde:	90 e0       	ldi	r25, 0x00	; 0
     ce0:	f8 94       	cli
     ce2:	0c 94 73 06 	jmp	0xce6	;  0xce6
     ce6:	f8 94       	cli
     ce8:	ff cf       	rjmp	.-2      	;  0xce8
	...
     d6e:	d7 75       	andi	r29, 0x57	; 87
     d70:	07 00       	.word	0x0007	; ????
     d72:	5d 5d       	subi	r21, 0xDD	; 221
     d74:	00 00       	nop
     d76:	00 00       	nop
     d78:	00 00       	nop
     d7a:	d5 d5       	rcall	.+2986   	;  0x1926
     d7c:	01 00       	.word	0x0001	; ????
     d7e:	00 00       	nop
     d80:	00 00       	nop
     d82:	5d 05       	cpc	r21, r13
     d84:	00 00       	nop
     d86:	dd dd       	rcall	.-1094   	;  0x942
     d88:	05 00       	.word	0x0005	; ????
     d8a:	d7 5d       	subi	r29, 0xD7	; 215
     d8c:	00 00       	nop
     d8e:	d7 5d       	subi	r29, 0xD7	; 215
     d90:	07 00       	.word	0x0007	; ????
     d92:	00 00       	nop
     d94:	00 00       	nop
     d96:	5d 17       	cp	r21, r29
     d98:	00 00       	nop
     d9a:	77 75       	andi	r23, 0x57	; 87
     d9c:	07 00       	.word	0x0007	; ????
     d9e:	57 75       	andi	r21, 0x57	; 87
     da0:	00 00       	nop
     da2:	5d d7       	rcall	.+3770   	;  0x1c5e
     da4:	01 00       	.word	0x0001	; ????
     da6:	57 17       	cp	r21, r23
     da8:	00 00       	nop
     daa:	77 77       	andi	r23, 0x77	; 119
     dac:	07 00       	.word	0x0007	; ????
     dae:	dd dd       	rcall	.-1094   	;  0x96a
     db0:	01 00       	.word	0x0001	; ????
     db2:	75 77       	andi	r23, 0x75	; 117
     db4:	00 00       	nop
     db6:	d5 1d       	adc	r29, r5
     db8:	00 00       	nop
     dba:	55 07       	cpc	r21, r21
     dbc:	00 00       	nop
     dbe:	55 01       	movw	r10, r10
     dc0:	00 00       	nop
     dc2:	57 05       	cpc	r21, r7
     dc4:	00 00       	nop
     dc6:	77 15       	cp	r23, r7
     dc8:	00 00       	nop
     dca:	77 57       	subi	r23, 0x77	; 119
     dcc:	00 00       	nop
     dce:	77 77       	andi	r23, 0x77	; 119
     dd0:	01 00       	.word	0x0001	; ????
     dd2:	77 57       	subi	r23, 0x77	; 119
     dd4:	01 00       	.word	0x0001	; ????
     dd6:	d7 75       	andi	r29, 0x57	; 87
     dd8:	01 00       	.word	0x0001	; ????
     dda:	00 00       	nop
     ddc:	00 00       	nop
     dde:	57 1d       	adc	r21, r7
     de0:	00 00       	nop
     de2:	00 00       	nop
     de4:	00 00       	nop
     de6:	75 57       	subi	r23, 0x75	; 117
     de8:	00 00       	nop
     dea:	dd 75       	andi	r29, 0x5D	; 93
     dec:	01 00       	.word	0x0001	; ????
     dee:	1d 00       	.word	0x001d	; ????
     df0:	00 00       	nop
     df2:	57 01       	movw	r10, r14
     df4:	00 00       	nop
     df6:	d7 05       	cpc	r29, r7
     df8:	00 00       	nop
     dfa:	57 00       	.word	0x0057	; ????
     dfc:	00 00       	nop
     dfe:	01 00       	.word	0x0001	; ????
     e00:	00 00       	nop
     e02:	75 01       	movw	r14, r10
     e04:	00 00       	nop
     e06:	77 01       	movw	r14, r14
     e08:	00 00       	nop
     e0a:	55 00       	.word	0x0055	; ????
     e0c:	00 00       	nop
     e0e:	05 00       	.word	0x0005	; ????
     e10:	00 00       	nop
     e12:	dd 1d       	adc	r29, r13
     e14:	00 00       	nop
     e16:	d7 01       	movw	r26, r14
     e18:	00 00       	nop
     e1a:	5d 01       	movw	r10, r26
     e1c:	00 00       	nop
     e1e:	77 00       	.word	0x0077	; ????
     e20:	00 00       	nop
     e22:	17 00       	.word	0x0017	; ????
     e24:	00 00       	nop
     e26:	77 07       	cpc	r23, r23
     e28:	00 00       	nop
     e2a:	dd 05       	cpc	r29, r13
     e2c:	00 00       	nop
     e2e:	77 1d       	adc	r23, r7
     e30:	00 00       	nop
     e32:	5d 00       	.word	0x005d	; ????
     e34:	00 00       	nop
     e36:	15 00       	.word	0x0015	; ????
     e38:	00 00       	nop
     e3a:	07 00       	.word	0x0007	; ????
     e3c:	00 00       	nop
     e3e:	75 00       	.word	0x0075	; ????
     e40:	00 00       	nop
     e42:	d5 01       	movw	r26, r10
     e44:	00 00       	nop
     e46:	dd 01       	movw	r26, r26
     e48:	00 00       	nop
     e4a:	57 07       	cpc	r21, r23
     e4c:	00 00       	nop
     e4e:	d7 1d       	adc	r29, r7
     e50:	00 00       	nop
     e52:	77 05       	cpc	r23, r7
	...
     e64:	00 00       	nop
     e66:	75 d7       	rcall	.+3818   	;  0x1d52
     e68:	01 00       	.word	0x0001	; ????
     e6a:	00 00       	nop
     e6c:	00 00       	nop
     e6e:	1d 00       	.word	0x001d	; ????
     e70:	00 00       	nop
     e72:	57 01       	movw	r10, r14
     e74:	00 00       	nop
     e76:	d7 05       	cpc	r29, r7
     e78:	00 00       	nop
     e7a:	57 00       	.word	0x0057	; ????
     e7c:	00 00       	nop
     e7e:	01 00       	.word	0x0001	; ????
     e80:	00 00       	nop
     e82:	75 01       	movw	r14, r10
     e84:	00 00       	nop
     e86:	77 01       	movw	r14, r14
     e88:	00 00       	nop
     e8a:	55 00       	.word	0x0055	; ????
     e8c:	00 00       	nop
     e8e:	05 00       	.word	0x0005	; ????
     e90:	00 00       	nop
     e92:	dd 1d       	adc	r29, r13
     e94:	00 00       	nop
     e96:	d7 01       	movw	r26, r14
     e98:	00 00       	nop
     e9a:	5d 01       	movw	r10, r26
     e9c:	00 00       	nop
     e9e:	77 00       	.word	0x0077	; ????
     ea0:	00 00       	nop
     ea2:	17 00       	.word	0x0017	; ????
     ea4:	00 00       	nop
     ea6:	77 07       	cpc	r23, r23
     ea8:	00 00       	nop
     eaa:	dd 05       	cpc	r29, r13
     eac:	00 00       	nop
     eae:	77 1d       	adc	r23, r7
     eb0:	00 00       	nop
     eb2:	5d 00       	.word	0x005d	; ????
     eb4:	00 00       	nop
     eb6:	15 00       	.word	0x0015	; ????
     eb8:	00 00       	nop
     eba:	07 00       	.word	0x0007	; ????
     ebc:	00 00       	nop
     ebe:	75 00       	.word	0x0075	; ????
     ec0:	00 00       	nop
     ec2:	d5 01       	movw	r26, r10
     ec4:	00 00       	nop
     ec6:	dd 01       	movw	r26, r26
     ec8:	00 00       	nop
     eca:	57 07       	cpc	r21, r23
     ecc:	00 00       	nop
     ece:	d7 1d       	adc	r29, r7
     ed0:	00 00       	nop
     ed2:	77 05       	cpc	r23, r7
	...
    10e8:	00 00       	nop
    10ea:	3e 05       	cpc	r19, r14
    10ec:	15 14       	cp	r1, r5
    10ee:	13 12       	cpse	r1, r19
    10f0:	11 10       	cpse	r1, r1
    10f2:	0f 0e       	add	r0, r31
    10f4:	13 12       	cpse	r1, r19
    10f6:	0d 0c       	add	r0, r13
    10f8:	0b 0a       	sbc	r0, r27
    10fa:	00 00       	nop
    10fc:	00 00       	nop
    10fe:	88 01       	movw	r16, r16
    1100:	8c 00       	.word	0x008c	; ????
    1102:	bb 00       	.word	0x00bb	; ????
    1104:	cf 01       	movw	r24, r30
    1106:	ec 00       	.word	0x00ec	; ????
    1108:	ca 00       	.word	0x00ca	; ????
    110a:	de 00       	.word	0x00de	; ????
    110c:	0d 0a       	sbc	r0, r29
    110e:	00 2d       	mov	r16, r0
    1110:	00 2e       	mov	r0, r16
    1112:	00 20       	and	r0, r0
    1114:	00 43       	sbci	r16, 0x30	; 48
    1116:	6f 72       	andi	r22, 0x2F	; 47
    1118:	72 65       	ori	r23, 0x52	; 82
    111a:	63 74       	andi	r22, 0x43	; 67
    111c:	20 50       	subi	r18, 0x00	; 0
    111e:	69 6e       	ori	r22, 0xE9	; 233
    1120:	20 53       	subi	r18, 0x30	; 48
    1122:	74 61       	ori	r23, 0x14	; 20
    1124:	74 65       	ori	r23, 0x54	; 84
    1126:	3a 00       	.word	0x003a	; ????
    1128:	46 6c       	ori	r20, 0xC6	; 198
    112a:	61 72       	andi	r22, 0x21	; 33
    112c:	65 2d       	mov	r22, r5
    112e:	4f 6e       	ori	r20, 0xEF	; 239
    1130:	20 32       	cpi	r18, 0x20	; 32
    1132:	30 31       	cpi	r19, 0x10	; 16
    1134:	37 20       	and	r3, r7
    1136:	41 64       	ori	r20, 0x41	; 65
    1138:	72 75       	andi	r23, 0x52	; 82
    113a:	69 6e       	ori	r22, 0xE9	; 233
    113c:	6f 20       	and	r6, r15
    113e:	55 4e       	sbci	r21, 0xE5	; 229
    1140:	4f 20       	and	r4, r15
    1142:	44 69       	ori	r20, 0x94	; 148
    1144:	67 69       	ori	r22, 0x97	; 151
    1146:	74 61       	ori	r23, 0x14	; 20
    1148:	6c 20       	and	r6, r12
    114a:	50 69       	ori	r21, 0x90	; 144
    114c:	6e 20       	and	r6, r14
    114e:	73 74       	andi	r23, 0x43	; 67
    1150:	61 74       	andi	r22, 0x41	; 65
    1152:	65 3a       	cpi	r22, 0xA5	; 165
	...
