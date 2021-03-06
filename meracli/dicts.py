# -*- coding: utf-8 -*-
"""Meraki CLI."""

user_mode_string = """
  * = Not implemented.

  *<1-99>      Session number to resume
  *connect     Open a terminal connection
  *disable     Turn off privileged commands
  *disconnect  Disconnect an existing network connection
  enable      Turn on privileged commands
  exit        Exit from the EXEC
  logout      Exit from the EXEC
  *ping        Send echo messages
  *resume      Resume an active network connection
  *show        Show running system information
  *ssh         Open a secure shell client connection
  *telnet      Open a telnet connection
  *terminal    Set terminal line parameters
  *traceroute  Trace route to destination
"""

priv_mode_string = """
  * = Not implemented.

  *<1-99>      Session number to resume
  *auto        Exec level Automation
  *clear       Reset functions
  *clock       Manage the system clock
  *configure   Enter configuration mode
  *connect     Open a terminal connection
  *copy        Copy from one file to another
  *debug       Debugging functions (see also 'undebug')
  *delete      Delete a file
  *dir         List files on a filesystem
  *disable     Turn off privileged commands
  *disconnect  Disconnect an existing network connection
  *enable      Turn on privileged commands
  *erase       Erase a filesystem
  exit        Exit from the EXEC
  logout      Exit from the EXEC
  *mkdir       Create new directory
  *more        Display the contents of a file
  *no          Disable debugging informations
  *ping        Send echo messages
  *reload      Halt and perform a cold restart
  *resume      Resume an active network connection
  *rmdir       Remove existing directory
  *send        Send a message to other tty lines
  *setup       Run the SETUP command facility
  *show        Show running system information
  *ssh         Open a secure shell client connection
  *telnet      Open a telnet connection
  *terminal    Set terminal line parameters
  *traceroute  Trace route to destination
  *undebug     Disable debugging functions (see also 'debug')
  *vlan        Configure VLAN parameters
  *write       Write running configuration to memory, network, or
"""

global_config_mode_string = """
Configure commands:
  * = Not implemented.

  *aaa                Authentication, Authorization and Accounting.
  *access-list        Add an access list entry
  *banner             Define a login banner
  *boot               Modify system boot parameters
  *cdp                Global CDP configuration subcommands
  *class-map          Configure Class Map
  *clock              Configure time-of-day clock
  *config-register    Define the configuration register
  *crypto             Encryption module
  *do                 To run exec commands in config mode
  *dot11              IEEE 802.11 config commands
  *enable             Modify enable password parameters
  end                Exit from configure mode
  exit               Exit from configure mode
  *flow               Global Flow configuration subcommands
  *hostname           Set system's network name
  *interface          Select an interface to configure
  *ip                 Global IP configuration subcommands
  *ipv6               Global IPv6 configuration commands
  *key                Key management
  *license            Configure license features
  *line               Configure a terminal line
  *lldp               Global LLDP configuration subcommands
  *logging            Modify message logging facilities
  *login              Enable secure login checking
  *mac-address-table  Configure the MAC address table
  *no                 Negate a command or set its defaults
  *ntp                Configure NTP
  *parser             Configure parser
  *policy-map         Configure QoS Policy Map
  *port-channel       EtherChannel configuration
  *priority-list      Build a priority list
  *privilege          Command privilege parameters
  *queue-list         Build a custom queue list
  *radius-server      Modify Radius query parameters
  *router             Enable a routing process
  *secure             Secure image and configuration archival commands
  *security           Infra Security CLIs
  *service            Modify use of network based services
  *snmp-server        Modify SNMP engine parameters
  *spanning-tree      Spanning Tree Subsystem
  *tacacs-server      Modify TACACS query parameters
  *username           Establish User Name Authentication
  *vpdn               Virtual Private Dialup Network
  *vpdn-group         VPDN group configuration
"""