#!/bin/sh
rsync -r ./.env assets/.env
rsync -r ./client_secrets.json assets/client_secrets.json
rsync -r ./static/favicon.ico assets/favicon.ico
tar -czvf ./syncs/assets.tar.gz ./assets
gdrive sync upload syncs --keep-local 1uBMXceRugdm_Zzg4onemoq7cuLHB9NWL
