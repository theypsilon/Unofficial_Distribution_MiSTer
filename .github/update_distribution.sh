#!/usr/bin/env bash
# Copyright (c) 2021 José Manuel Barroso Galindo <theypsilon@gmail.com>

set -euo pipefail

curl -o /tmp/update_distribution.source "https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/develop/.github/update_distribution.sh"

source /tmp/update_distribution.source
rm /tmp/update_distribution.source

curl -o /tmp/calculate_db.py "https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/develop/.github/calculate_db.py"
chmod +x /tmp/calculate_db.py

update_distribution() {
    local OUTPUT_FOLDER="${1}"
    local PUSH_COMMAND="${2:-}"

    process_url "https://github.com/Kyp069/zx48-MiSTer" _Computer "${OUTPUT_FOLDER}"
    process_url "https://github.com/MrX-8B/MiSTer-Arcade-PenguinKunWars" _Arcade "${OUTPUT_FOLDER}"
    process_url "https://github.com/va7deo/zerowing" _Arcade "${OUTPUT_FOLDER}"
    process_url "https://github.com/va7deo/zerowing" "user-content-mra-alternatives-under-releases" "${OUTPUT_FOLDER}"
    process_url "https://github.com/va7deo/TerraCresta" _Arcade "${OUTPUT_FOLDER}"
    process_url "https://github.com/va7deo/TerraCresta" "user-content-mra-alternatives-under-releases" "${OUTPUT_FOLDER}"
    process_url "https://github.com/va7deo/ArmedF" _Arcade "${OUTPUT_FOLDER}"
    process_url "https://github.com/va7deo/ArmedF" "user-content-mra-alternatives-under-releases" "${OUTPUT_FOLDER}"
    process_url "https://github.com/GX400-Friends/gx400-bin" _Arcade "${OUTPUT_FOLDER}"
    process_url "https://github.com/GX400-Friends/gx400-bin" "user-content-mra-alternatives-under-releases" "${OUTPUT_FOLDER}"
    process_url "https://github.com/atrac17/Toaplan2" _Arcade "${OUTPUT_FOLDER}"

    if [[ "${PUSH_COMMAND}" != "--push" ]] ; then
        return
    fi

    git checkout -f develop -b main
    echo "Running detox"
    detox -v -s utf_8-only -r *
    echo "Detox done"
    git add "${OUTPUT_FOLDER}"
    git commit -m "-"
    git fetch origin main || true
    echo "Calculating db..."
    /tmp/calculate_db.py
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]] ; then
    update_distribution "${1}" "${2:-}"
fi
