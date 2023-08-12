#!/bin/bash

python3 -m venv env
env/bin/pip install -r requirements.txt

CUR_DIR=$(pwd)

echo "
#!/bin/bash
$CUR_DIR/env/bin/python main.py \$@
" > pil.sh

chmod +x pil.sh
ln -s "$(pwd)/pil.sh" /bin/pil
pil --help