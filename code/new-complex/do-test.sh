#!/bin/bash

wn=1
ns='--ns'

tr='trva.100.remap'
te='te.1.remap'
item='item'
imp='trva.model'

logs_pth='test-logs'
mkdir -p $logs_pth

task(){
t=100
k=8
l=128
w=0.000244140625

cmd='./train'
cmd="$cmd -k $k"
cmd="$cmd -l $l"
cmd="$cmd -t $t"
cmd="$cmd -w $w"
cmd="$cmd -c 5"
cmd="$cmd -wn ${wn}"
cmd="$cmd -imp ${imp}"
cmd="$cmd $ns"
cmd="$cmd -p ${te}"
cmd="$cmd ${item} ${tr}"
cmd="$cmd > $logs_pth/${tr}.${k}.${l}.${w}.$ns"
echo $cmd
}

task
#task | xargs -d '\n' -P $num_core -I {} sh -c {} &