#!/bin/bash

python3 -m venv env
env/bin/pip install -r requirements.txt

CUR_DIR=$(pwd)

echo "
#!/bin/bash
$CUR_DIR/env/bin/python $CUR_DIR/main.py \$@
" > pil.sh

echo "
#!/bin/bash
$CUR_DIR/env/bin/python $CUR_DIR/probe.py \$@
" > pilprobe.sh

add_permissions()
{
chmod +x pil.sh
chmod +x pilprobe.sh
}

install_on_linux()
{
ln -s "$(pwd)/pil.sh" /usr/bin/pil
ln -s "$(pwd)/pilprobe.sh" /usr/bin/pilprobe
}

install_on_mac()
{
ln -s "$(pwd)/pil.sh" ~/bin/pil
ln -s "$(pwd)/pilprobe.sh" ~/bin/pilprobe
}

add_permissions

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)
        install_on_linux
    ;;
    Darwin*)
        install_on_mac
    ;;
esac
