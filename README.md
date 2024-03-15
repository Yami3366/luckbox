# Optional Challenge :Luckbox
- Write a program with two compilation errors, a runtime error and a logical error.
- Next to each error, add a comment that explains what type of error it is and why it occurs.
## Data Flow

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
