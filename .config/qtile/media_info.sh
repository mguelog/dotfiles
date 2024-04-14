#!/bin/bash

notify-send 'Currently playing' "`playerctl metadata title` by `playerctl metadata artist`"
