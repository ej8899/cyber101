![BullDog Excavations Logo](lhl-bulldog-logo.png)

# Bulldog Excavations Security Monitoring and Data Management Plan

## Introduction

It is now crucial for businesses of every size to prioritize their cybersecurity  measures. Bulldog Excavations, which utilizes a mix of on site and cloud services needs a customized plan for monitoring and managing data to safeguard its infrastructure and ensure continuous business operations. This document outlines a method for collecting, storing and preserving data specifically designed for Bulldog Excavations distinct environment to safeguard business operations and maintain data reliability.

## 1. Prioritization of Devices, Services, and Data Types

To effectively secure the company infrastructure, it is essential to prioritize the various devices, services, and data types based on their importance to the business:

1. **Windows Server**: 
   - **Importance**: High
   - **Reasoning**: The Windows Server hosts the file shares, database, and Active Directory (AD) domain information. All which are critical to business operations, user management, and data integrity.

2. **Payment and Accounting Workstations**:
   - **Importance**: High
   - **Reasoning**: These workstations handle financial transactions and record management which are essential for the financial health and legal compliance of the company.

3. **Main Switch, Router, and Firewall**:
   - **Importance**: High
   - **Reasoning**: These devices manage network traffic, ensure connectivity, and protect the network perimeter from external threats.

4. **Project/Contract Planning Workstations**:
   - **Importance**: Medium
   - **Reasoning**: These workstations are essential for day-to-day operations, planning, and project management, though they are less critical than financial systems.

5. **Offsite Website and Analytics**:
   - **Importance**: Medium
   - **Reasoning**: Although hosted offsite, the website analytics provide valuable business insights but are not mission-critical in real-time operations.

6. **Online Email and Personal File Storage Service**:
   - **Importance**: Medium to Low
   - **Reasoning**: Critical for communication and personal file management, but given the cloud-based nature of it, this system may already have robust security and redundancy in place.  It should be evaluated for its security and redundancy.

## 2. Data Collection Recommendations

### Windows Server
   - **Logs to Collect**:
     - Active Directory logs (authentication, group changes, permissions changes)
     - File access logs
     - Database access and modification logs
   - **Network Traffic to Capture**:
     - Internal traffic related to database queries and file access
   - **Metadata to Capture**:
     - User access times, source IP addresses, changes in file permissions

### Payment and Accounting Workstations
   - **Logs to Collect**:
     - Transaction logs
     - Application logs (especially related to financial software)
   - **Network Traffic to Capture**:
     - Encrypted payment transaction traffic, ensuring no anomalies
   - **Metadata to Capture**:
     - Transaction timestamps, user actions, software usage patterns

### Main Switch, Router, and Firewall
   - **Logs to Collect**:
     - Firewall logs (blocked attempts, allowed traffic logs)
     - Router traffic logs
     - Geolocation of access origin attempts
   - **Network Traffic to Capture**:
     - Suspicious or high-volume traffic patterns
   - **Metadata to Capture**:
     - Source and destination IP addresses, port usage, protocol types

### Project/Contract Planning Workstations
   - **Logs to Collect**:
     - User activity logs
     - Application usage logs
   - **Network Traffic to Capture**:
     - File transfer traffic, remote access attempts
   - **Metadata to Capture**:
     - User login times, project file modification details

### Offsite Website and Analytics
   - **Logs to Collect**:
     - Access logs
     - User interaction logs (if accessible)
   - **Network Traffic to Capture**:
     - Traffic to and from analytics platforms
   - **Metadata to Capture**:
     - User IPs, session durations, geographic data

### Online Email and Personal File Storage Service
   - **Logs to Collect**:
     - Email access logs
     - File upload/download logs
   - **Network Traffic to Capture**:
     - Traffic related to file transfers
   - **Metadata to Capture**:
     - File timestamps, email metadata (sender, recipient, subject)

## 3. Data Storage Recommendations
For all data being saved, it is recommended to store it in a centralized location for easy access and management. This ensures that all logs and data are stored in a single, secure location.  Also recommended is full drive compression system to reduce storage requirements.
### Centralized Logging Server
   - **Location**: Dedicated network-attached storage or cloud-based, depending on the volume and access requirements.
   - **Security**: Encrypt all logs in transit and at rest. Implement strict access controls to the logging server.
   - **Retention**: Store critical logs (e.g., financial, AD logs) locally with backups in cloud storage.

### Network Traffic Data Storage
   - **Location**: Dedicated network-attached storage (NAS) or cloud storage with high redundancy.
   - **Security**: Use encryption and ensure segmented storage to protect sensitive data.
   - **Retention**: Store raw traffic data for a shorter period (e.g., 30-90 days), while metadata may be kept longer for trend analysis.

### Metadata Storage
   - **Location**: Integrated into the logging system, possibly within a SIEM (Security Information and Event Management) solution.
   - **Security**: Use encryption and role-based access controls.
   - **Retention**: Metadata can be stored longer (e.g., 1-2 years) as it requires less space and can be valuable for long-term analysis.

## 4. Data Retention Criteria

When determining the retention period for collected data, consider the following criteria:

1. **Compliance Requirements**:
   - Retain logs and data as required by industry regulations (e.g., financial records might need to be kept for 7 years).

2. **Business Needs**:
   - Logs crucial for business operations, like financial transactions and project management records, should be kept longer.

3. **Storage Costs**:
   - Balance between storage costs and the necessity of long-term data. Older data that is infrequently accessed might be archived in a cost-effective manner.
   - Compression techniques can help reduce storage requirements and therefore costs.

4. **Security Concerns**:
   - Retain data long enough to conduct thorough security investigations but not so long that it increases the risk of exposure or breaches.

5. **Operational Value**:
   - Determine the period during which logs and data are valuable for operational purposes, such as monitoring trends or performance analysis.

## Conclusion

The recommendations provided aim to improve Bulldog Excavations' security posture by implementing a prioritized approach to the monitoring, data collection, and storage of historical log data. 

By focusing on the most critical systems and ensuring that data is stored securely and retained according to business and regulatory needs, Bulldog Excavations can enhance its resilience against threats and maintain smooth operational continuity in the face of potential security incidents.