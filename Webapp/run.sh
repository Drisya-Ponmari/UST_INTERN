#!/bin/bash

python backend.py &

gnome-terminal --tab -- bash -c "streamlit run frontend.py" &
