#!/bin/bash
cd ~/Desktop/Blast

osascript -e 'tell app "Terminal"
    do script "cd ~/Desktop/Blast && python3 wire.py"
    do script "cd ~/Desktop/Blast && python3 usalead.py"
    do script "cd ~/Desktop/Blast && python3 loan.py"
    do script "cd ~/Desktop/Blast && python3 debit.py"
    do script "cd ~/Desktop/Blast && python3 facebook.py"
    do script "cd ~/Desktop/Blast && python3 invoice.py"
end tell'
