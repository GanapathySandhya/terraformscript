
Given below are sample for code for the following customizations 
that can be done for a guest vm created by terraform.

1. Time Zone
2. dns_suffix
3. admin_password change
4. ssh using private key
5. Joining a windows vm to a domain.

------------------
Time Zone in Linux
------------------

"time_zone" : "America/New_York"

Verify by timedatectl|grep TimeZone


-------------------
dns_suffix in Linux
-------------------

"dns_suffixes": ["hpelab.local", "hpelab.remote"]

Verify by checking /etc/resolv.conf

---------------------
ssh using private key
---------------------


"provisioner": {
                   "file": {
                     "source" : "<path to public key in local machine>",
                     "destination":  “<temporary path to store the public key in remote vm>",
                     "connection": {
                         "type": "ssh",
                         "user": "<username>",
                         "password": "<password>"
                     }
                }
            },
"provisioner": {
                  "remote-exec": {
                      "inline" : [
                          "mkdir -p /home/<user>/.ssh/",
                          "mv <temporary path> /home/<user>/.ssh/authorized_keys"
                       ],
                       "connection": {
                         "type": "ssh",
                         "user": "<username>",
                         "password": "<password>"
                     }
                  }
            }

Verified by ssh –i <path to private key> user@<ip address>
Logs in without asking for password.


-------------------------
admin_password in Windows
-------------------------

“windows_opt_config”: {
                      “admin_password”: “test”
}

Verify by logging into the windows vm using password "test"


------------------------------
Joining windows_vm to a domain
------------------------------


"network_interface": {
                    "label": "Backbone",
                    "ipv4_address": "<static IPV4 address>",
                    "ipv4_prefix_length": "<subnet_mask prefix length",
                    "ipv4_gateway": "<gateway>"
                },
"dns_servers": "<IP Address of domain name server>",

"windows_opt_config": {
                    "domain": "<domain name>",
                    "domain_user": "<domain user name>",
                    "domain_user_password": "<domain user password>"
                }
----------------------------------------------------------------------------------------------------------------------------------
