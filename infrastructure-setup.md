# Infrastructure Installation Guide

---

## Spin Up EC2 Instances

TODO: Describe how to spin up the EC2 instances.

## EC2 Instances Configuration - RHEL VMs

The following instructions apply to Red Hat Enterprise Linux servers.

### Update and Install Packages

Update yum repositories and upgrade packages.

```bash
yum update
yum upgrade
```

### Setup Docker
Docker is needed to run the application containers. 

### Setup GlusterFS
Gluster FS is needed to maintain FS consistency across the cluster. 

### Setup Traefik Proxy
Traefik is needed to route traffic to the application containers.

### Configure FirewallD

```bash```

## TO DO
1. Create high level concept designs
2. Test EC2 instances configuration
3. Test API gateway configurations
4. Design and build User Management Service API (NodeJS/Express)
5. Design and build Votes Calculation Service API (NodeJS/Express)

