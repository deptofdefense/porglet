#!/bin/csh

# Get the control path
if ( ! ($?CONTROL_PATH) ) then
    set CONTROL_PATH=`python ../../scripts/getControlPath.py`
endif

if ( "$CONTROL_PATH" == "NOT_FOUND" ) then
    echo "WARNING: Cannot find path to control"
    exit 0
endif

foreach n ( `ls *.cc` )
  g++ -c -fPIC $n &
end
wait

set built_o_files = ""
foreach n ( `ls *.o` )
  set built_o_files = "$built_o_files $n"
end

if ( ! ($?CONTROL_PATH) ) then
    echo "WARNING: Define CONTROL_PATH to build C files"
else
    g++ $built_o_files -L$CONTROL_PATH/messages/c/ -lprotoc -lprotobuf -lpthread -shared -lcontrolmessages -o libfalconmessages.so
endif

