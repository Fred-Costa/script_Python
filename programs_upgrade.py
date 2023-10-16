import subprocess

# Open cmd 
run_cmd = "runas /user:frede cmd"

# Execute 'winget upgrade'
winget_upgrade_cmd = "winget upgrade"

# Execute 'winget upgrade --all'
winget_upgrade_all_cmd = "winget upgrade --all"

# All in one string
full_cmd = f"{run_cmd} /K {winget_upgrade_cmd} & {winget_upgrade_all_cmd}"

# Execute
subprocess.run(full_cmd, shell=True)


