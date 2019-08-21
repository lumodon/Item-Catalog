#!/bin/sh
rsync -r ./.env ./assets/.env
rsync -r ./static/favicon.ico ./assets/favicon.ico
tar -czvf ./syncs/assets.tar.gz ./assets
gdrive sync upload syncs --keep-local 1uBMXceRugdm_Zzg4onemoq7cuLHB9NWL