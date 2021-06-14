'''You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph;
then run the next two at 15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus?'''
MilesFromUni=4
VelocityBus=25
TimeTaken=((MilesFromUni/VelocityBus)*60)
# 2 minutes at each stop
StopTime=20
TotalTime=TimeTaken+StopTime
print(f'The total time taken by the bus is {TotalTime}')
Jog1=((1/7)*60)
Jog2=((2/15)*60)
Jog3=((1/7)*60)
TotalJogTime=Jog1+Jog2+Jog3
print(f'The total time taken by running is {TotalJogTime}')
if (TotalTime>TotalJogTime):
    print('Taking a bus is slower than running')
else:
    print('Taking a bus is faster than running')