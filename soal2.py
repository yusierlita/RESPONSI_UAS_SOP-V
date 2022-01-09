print("RESPONSI SOP - V")
print("5200411094 - Yusi Erlita")
print("________________________")
print("SOAL NO. 2")

def Waiting_Time(proses, jumlah, burst_time, waiting_time, quantum):
    ram_bursttime = [0] * jumlah
    for y in range(jumlah):
        ram_bursttime[y] = burst_time[y]
    t = 0 
    while(1):
        selesai = True
        for y in range(jumlah):
            if (ram_bursttime[y] > 0) :
                selesai = False 
                if (ram_bursttime[y] > quantum) :
                    t += quantum
                    ram_bursttime[y] -= quantum
                else:
                    t = t + ram_bursttime[y]
                    waiting_time[y] = t - burst_time[y]
                    ram_bursttime[y] = 0
        if (selesai == True):break
            
def TurnAround_Time(proses, jumlah, burst_time, waiting_time, taroundtime):
    for y in range(jumlah):
        taroundtime[y] = burst_time[y] + waiting_time[y]

def Average_Time(proses, jumlah, burst_time, quantum):
    Waiting_time = [0] * jumlah
    taround_time = [0] * jumlah
    Waiting_Time(proses, jumlah, burst_time, Waiting_time, quantum)
    TurnAround_Time(proses, jumlah, burst_time, Waiting_time, taround_time)
    print("Proses Burst Time Waiting", "Turn Around Time")
    total_waitingtime = 0
    total_taroundtime = 0
    for y in range(jumlah):
        total_waitingtime = total_waitingtime + Waiting_time[y]
        total_taroundtime = total_taroundtime + taround_time[y]
        print(" ", y + 1, "\t\t", burst_time[y],
            "\t\t", Waiting_time[y], "\t\t", taround_time[y])
    print("\nAverage waiting time = %.5f "%(total_waitingtime /jumlah) )
    print("Average turn around time = %.5f "% (total_taroundtime / jumlah))
    
if __name__ =="__main__":   
    proses = [1, 2, 3]
    jumlah = 3
    burst_time = [7, 17, 3]
    quantum = 2;
    Average_Time(proses, jumlah, burst_time, quantum)
