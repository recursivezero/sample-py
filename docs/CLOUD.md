# Cloud Deployment

- Install python v 3.12, streamlit and poetry using pip

```sh
sudo apt install python3-pip python3-venv
pip install streamlit
curl -sSL https://install.python-poetry.org | python3.12 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
# install additional required packages
sudo apt install -y libglib2.0-0 libsm6 libxrender1 libxext6
sudo apt install -y libgl1
```

config poetry and virtual environment

```sh
poetry config --global virtualenvs.prefer-active-python true
sudo mkdir -p /opt/venv
sudo chown $USER:$USER /opt/venv
echo 'export POETRY_VIRTUALENVS_PATH=/opt/venv' >> ~/.bashrc
source ~/.bashrc
poetry config virtualenvs.in-project false
poetry config virtualenvs.path /opt/venv
poetry env info

```

- copy tz-script repo in a folder
- copy `.env` and `.streamlit/config.toml` to that folder
- go to folder and install package dependencies

```sh
poetry lock --no-cache
poetry install --all-extras --with dev
```

## run python app standalone ( not recommended )

```sh
nohup poetry run sample dev > sample.log 2>&1 &

# check log

tail -f sample.log
```

here we have to stop and start again manually checking port `lsof -ti:8501 | xargs kill -9` and many other manual work

so better use system service method as below

## run app using system service

- create service file

### /etc/systemd/system/sample.service

```sh
[Unit]
Description=ThreadZip App (via Poetry)
After=network.target

[Service]
User=root
WorkingDirectory=/opt/project/path/tz-script
Environment="HOME=/root"
Environment="PYTHONUNBUFFERED=1"
Environment="PATH=/root/.local/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=/root/.local/bin/poetry run sample dev
Restart=always
RestartSec=5

# Optional: persistent logs
StandardOutput=append:/var/log/sample.log
StandardError=append:/var/log/sample-error.log

[Install]
WantedBy=multi-user.target

```

now start the service using

```sh
sudo systemctl daemon-reload
sudo systemctl restart sample
```

to stop/disable

```sh
sudo systemctl disable sample
# to check status
sudo systemctl status sample
```

to check running logs

```sh

tail -f /var/log/sample-error.log

```
