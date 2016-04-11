rm -rf design.py*

for i in "$@"
do
case $i in
    -u=*|--ui=*)
    FILE_UI="${i#*=}"

    ;;
    -m=*|--main=*)
    FILE_MAIN="${i#*=}"

    ;;
    *)

    ;;
esac
done

pyuic4 -x ${FILE_UI}.ui -o ${FILE_UI}.py

if [ "${FILE_MAIN}" != "" ]; then
    python ${FILE_MAIN}.py
else
    python ${FILE_UI}.py
fi
