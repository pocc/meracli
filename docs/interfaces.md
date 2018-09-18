# Cisco IOS interfaces
## Exec >?
    <1-99>      Session number to resume
    connect     Open a terminal connection
    disable     Turn off privileged commands
    disconnect  Disconnect an existing network connection
    enable      Turn on privileged commands
    exit        Exit from the EXEC
    logout      Exit from the EXEC
    ping        Send echo messages
    resume      Resume an active network connection
    show        Show running system information
    ssh         Open a secure shell client connection
    telnet      Open a telnet connection
    terminal    Set terminal line parameters
    traceroute  Trace route to destination

### show run
    Building configuration...
    
    Current configuration : 607 bytes
    !
    version 15.1
    no service timestamps log datetime msec
    no service timestamps debug datetime msec
    no service password-encryption
    !
    hostname Router
    !
    !
    !
    !
    !
    !
    !
    !
    ip cef
    no ipv6 cef
    !
    !
    !
    !
    license udi pid CISCO2901/K9 sn FTX152417TA
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    spanning-tree mode pvst
    !
    !
    !
    !
    !
    !
    interface GigabitEthernet0/0
     no ip address
     duplex auto
     speed auto
     shutdown
    !
    interface GigabitEthernet0/1
     no ip address
     duplex auto
     speed auto
     shutdown
    !
    interface Vlan1
     no ip address
     shutdown
    !
    ip classless
    !
    ip flow-export version 9
    !
    !
    !
    !
    !
    !
    !
    line con 0
    !
    line aux 0
    !
    line vty 0 4
     login
    !
    !
    !
    end

## Privileged Exec #?
    <1-99>      Session number to resume
    auto        Exec level Automation
    clear       Reset functions
    clock       Manage the system clock
    configure   Enter configuration mode
    connect     Open a terminal connection
    copy        Copy from one file to another
    debug       Debugging functions (see also 'undebug')
    delete      Delete a file
    dir         List files on a filesystem
    disable     Turn off privileged commands
    disconnect  Disconnect an existing network connection
    enable      Turn on privileged commands
    erase       Erase a filesystem
    exit        Exit from the EXEC
    logout      Exit from the EXEC
    mkdir       Create new directory
    more        Display the contents of a file
    no          Disable debugging informations
    ping        Send echo messages
    reload      Halt and perform a cold restart
    resume      Resume an active network connection
    rmdir       Remove existing directory
    send        Send a message to other tty lines
    setup       Run the SETUP command facility
    show        Show running system information
    ssh         Open a secure shell client connection
    telnet      Open a telnet connection
    terminal    Set terminal line parameters
    traceroute  Trace route to destination
    undebug     Disable debugging functions (see also 'debug')
    vlan        Configure VLAN parameters
    write       Write running configuration to memory, network, or
    
