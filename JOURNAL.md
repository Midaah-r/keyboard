---
title: keyboard
author: Midaah
description: a keyboard that keyboard's
created_at: 2025-7-28
---

# keyboard 

### 27th July (day 1): reasearch and brainstorming

😭i was busy with exams and kept this project on a hold. This is my first time doing a project of this complexity and i didnt know anyhting about the workings of a mechanical keyboard and i have never owned one but.

I spent the ENTIRE (around 4 hours) day researching keyboard jargon, engineering, stabilizers, switches, parts, layouts etc... I found a few keebs for inspo

That sums up my day along with simultaneously working on my macropad (slickopad :) ) which also helped my understand the working and workflow better.

<image src="assets_journal/notion.jpg" width="400">

Suuuuper professional research notes:

<image src="assets_journal/notes.jpg" width="400">

**Time Spent:** 4 hours

---

### 29th July (day 2): design, schematic and pcb

I FORGOT TO ENTER MY PREVIOUS DAY cos i had to attend a family event :( but here goes 

spent the previous day and today finalizing the layout, i wanted a cute, compact keyboard so i decided to go with a 65% keyboard layout, the top right key replaced with a RE:

<image src="assets_journal/layout.png" width="400">

for the MCU i decided to go for a raspberry pi pico, cos its simple, fairly cheap and readily available. 

This is my first pcb of this scale so it took quite a bit of research (the macropad helped tons). i decided to go for a 15x5 key matrix with diodes to prevent ghosting coming to a total of 66 keys and 1 RE. here is the schematic (took me less time than i expected me to) i came up with:

<image src="assets_journal/schematic.png" width="400">

I HATE ROUTING, while making my macropad i rerouted a couple hundered of times. but THIS TIME I HAD A FIXED LAYOUT IN MIND and as a result i didnt have to reroute much. Im sooo happy that my routing went smoothly. i had to use 2-3 vias but i tried to make do without. here is the pcb:

<image src="assets_journal/pcb.png" width="400">

finally here's a 3d render of the pcb (LOOKS REALLY COOOOOL!!!)

<image src="assets_journal/pcb_3d.png" width="400">

Im really happy with the progress ive made although i wasted quite a bit of time finding the right footprints and models and figuring out (googling) other teeny tiny issues but now i can do stuff without tutorials now and im proud of that.

I'll start designing the case tomorrow!! (3d modelling is nightmare fuel)

**Time Spent:**  4.5 hours

---

### 30th July (day 3): CAD - case

_wheeeeezeee_

I truly hate fusion navigation controls, controlling a 3d space with a 2d cursor is hard, anyhow....

I COMPLETELY LOCKED IN TODAY! 

After researching about keyboard mounts, i wanted to go for a gasket mount or gummy-o-ring mount, but both of those sounded a bit complex and i didnt know if i could find the gaskets separately, sooo, i chose to go for a top mount design as i read its a good balance and is reallly popular.

Im using heatset inserts this time and i want to conceal the screws so i kept that in mind.

This is what i came up with, although i might need to tweak it a bit tomorrow:

bottom case:

<image src="assets_journal/bottom_case.jpg" width="400">

plate: 

<image src="assets_journal/plate.jpg" width="400">

top case:

<image src="assets_journal/top_case.jpg" width="400">

final assembled look: 

<image src="assets_journal/assembled.jpg" width="400">

Although im happy with how it turned out, i dont like the massive 40mm unused space on the top, i wanted to make a minimal keyboard and this goes completely against, the only solution i found feasible was to use solder pads and then use wires to link the pcb to the MCU, but this is my first time with something like this and i thought its better not to experiment too much, moreover, i have a deadline, ie, tomorrow!

Ill do the finishing touches and fix up any errors tomorrow and get my repo ready tomorrow hopefully!

BTW!!! My macropad got approved today!! YIPPEEE!

**Time spent:** 8 hours
