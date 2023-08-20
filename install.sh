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

chmod +x pil.sh
ln -s "$(pwd)/pil.sh" /bin/pil
chmod +x pilprobe.sh
ln -s "$(pwd)/pilprobe.sh" /bin/pilprobe
pil --help