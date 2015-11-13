#! /bin/bash

FILE=$1
TYPE=""
URLPATH=""
EXECAPP=""

while read LINE; do
    RESULT=$(echo $LINE | /bin/grep 'Type=Link')
    if [[ ${RESULT} != "" ]]; then
        TYPE="Link"
        continue
    fi
    
    RESULT=$(echo $LINE | /bin/grep 'URL\[$e\]=file://')
    if [[ ${RESULT} != "" ]]; then
        URLPATH=$LINE
        continue
    fi

    RESULT=$(echo $LINE | /bin/grep 'X-KDE-LastOpenedWith=')
    if [[ ${RESULT} != "" ]]; then
        EXECAPP=$LINE
        continue
    fi
done < ${FILE}

URLPATH=${URLPATH/'URL[$e]'/'URLXXX'}
URLVAR=${URLPATH%\=*}
eval "${URLPATH}"
URLPATH=${!URLVAR}
URLPATH=${URLPATH#*file://}

EXECAPP=${EXECAPP/'X-KDE-LastOpenedWith'/'XKDEOPENWIDTH'}
APPVAR=${EXECAPP%\=*}
eval "${EXECAPP}"
EXECAPP=${!APPVAR}

if [[ ${TYPE} == "Link" ]]; then
    /bin/${EXECAPP} ${URLPATH}
fi
