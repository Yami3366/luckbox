# Optional Challenge :LuckBox
- Write a program with two compilation errors, a runtime error and a logical error.
- Next to each error, add a comment that explains what type of error it is and why it occurs.
  
## LuckBox Data Work Flow

```mermaid
sequenceDiagram
    participant data_input
    participant data_process
    participant Lottery_results
    data_input->>data_process: user input prizes if not default value
    data_process->>Lottery_results: reay lottery show prizes 
    Lottery_results->>data_process: wait user click [enter]
    data_process->>data_input: input validate failed
    data_input->>data_process: validate input validate pass
    data_process->>data_process: Repeatedly verify data until ready for lottery.
    Lottery_results->>Lottery_results: Repeatedly lottery until without prize.
```

### LuckBox program Demo operation screen
<img width="567" alt="h1" 
    src="https://github.com/Yami3366/luckbox/assets/159643271/b2adb41b-83df-41ac-a165-43a7cd16882c">  


Start Welcome Luckbox  

<img width="567" alt="h2" src="https://github.com/Yami3366/luckbox/assets/159643271/fdc16dc0-e639-44d4-a163-b2fa0be7b079">  

Enter How many prizes :  
How many people participating in the lottery : 13  


<img width="567" alt="h3" src="https://github.com/Yami3366/luckbox/assets/159643271/143cebb3-cd3d-49ba-953c-00dbe8be2f55">  

User input below 5 items prizes.  
If no input is entered,the default value will be displayed.  

  
iPhone 15 Pro  
Apple iPad 10.9  
Xbox Series X  
KODAK Mini Portable Photo Printer  
Garmin Forerunner 255 GPS Watch 


<img width="567" alt="h4" src="https://github.com/Yami3366/luckbox/assets/159643271/86438b28-a244-48cd-9db6-e466a511a4c5">  

The draw has been prepared and the prizes and mumber of participants are displayed.  
Wait for the person to press enter to draw the prize.  

<img width="567" alt="h5" src="https://github.com/Yami3366/luckbox/assets/159643271/f99b63c2-b3aa-4c3a-80e8-6b54f26196b4">  

Press enter to draw the first prize  

<img width="567" alt="h6" src="https://github.com/Yami3366/luckbox/assets/159643271/f11309a5-1c5b-41ab-8139-77b9fde141d0">  

Press enter to draw the second prize  

<img width="567" alt="h7" src="https://github.com/Yami3366/luckbox/assets/159643271/f70ba06d-3d61-467b-8d45-0ecdc97da593">  

Press enter to draw the third prize  



<img width="567" alt="h8" src="https://github.com/Yami3366/luckbox/assets/159643271/c5cffadf-08da-4fb9-865a-e555e0a7a048">  

Press enter to draw the fourth prize  



<img width="567" alt="h9" src="https://github.com/Yami3366/luckbox/assets/159643271/6093c406-908d-42d1-92b0-def5d1f9e00a">  

Press enter to draw the fifth prize.

### LuckBox program Demo completed.





