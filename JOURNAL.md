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
