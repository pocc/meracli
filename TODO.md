# MeraCLI todo list
## v1.0: Program flow
### 1. Initial Entry
User enters their username and password when starting the CLI
   i.e. (meracli username password)

### 2. Overview Mode
MSP Portal - list of organizations are shown and user chooses one to 
enter.
    
### 3. Organization Mode

1. List of networks that can be accessed.
2. Organization settings are can be shown/edited per permissions.

### 4. Network Mode

1. List of devices that can be accessed are shown.
2. Network-wide settings are shown/edited per permissions.

### 5. Device Mode

1. Information about device displayed at top.
2. Live tools available.
3. Voluminous information about device should be available (i.e. a show 
command). This information should have documentation linked where possible.

### 6. Local Status Page

1. Login to local status page with a prompt for required info:
    * Local username
    * Local password
    * Address: type of network (setup.meraki.com can be used). IP address 
    can also be used.

## Ideas
* Text color of a device should be green/yellow/red depending on status.
* Make it so that all text is red if licensing is non-compliant.
