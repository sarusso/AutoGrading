#!/bin/bash

# Exit on any error. More advanced logics could be applied in future
# (see https://stackoverflow.com/questions/4381618/exit-a-script-on-error)
set -e

echo ""
echo "[INFO] Executing entrypoint..."

#---------------------
#   Save env
#---------------------
echo "[INFO] Dumping env"
env | \
while read env_var; do
  if [[ $env_var == HOME\=* ]]; then
      : # Skip HOME var
  elif [[ $env_var == PWD\=* ]]; then
      : # Skip PWD var
  else
      echo "export $env_var" >> /env.sh
  fi
done

#---------------------
#  Entrypoint command
#---------------------
if [[ "x$@" == "x" ]] ; then
    ENTRYPOINT_COMMAND="sudo -u ubuntu /run.sh"
else
    ENTRYPOINT_COMMAND=$@
fi
echo -n "[INFO] Executing entrypoint command: "
echo $ENTRYPOINT_COMMAND
exec $ENTRYPOINT_COMMAND
