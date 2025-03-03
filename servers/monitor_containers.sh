#!/bin/bash
LOG_FILE="monitoring.log"

echo "===== Docker Containers Status =====" > $LOG_FILE
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}\t{{.Ports}}" >> $LOG_FILE

echo -e "\n===== Resource Usage =====" >> $LOG_FILE
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}" >> $LOG_FILE

echo -e "\n===== DICOM Instance Counts =====" >> $LOG_FILE
for server in 8042 8043 8044; do
    count=$(curl -s -u orthanc:orthanc "http://localhost:$server/instances" | jq '. | length')
    echo "Orthanc Server on port $server has $count DICOM instances" >> $LOG_FILE
done

echo -e "\n===== Queue Depth (Pending Jobs) =====" >> $LOG_FILE
for server in 8042 8043 8044; do
    jobs=$(curl -s -u orthanc:orthanc "http://localhost:$server/queries" | jq '. | length')
    echo "Orthanc Server on port $server has $jobs pending jobs" >> $LOG_FILE
done

echo -e "\n===== Response Time =====" >> $LOG_FILE
for server in 8042 8043 8044; do
    time=$(curl -o /dev/null -s -w "%{time_total}\n" -u orthanc:orthanc "http://localhost:$server/")
    echo "Orthanc Server on port $server response time: $time seconds" >> $LOG_FILE
done

echo -e "\n===== Container Restarts =====" >> $LOG_FILE
docker ps --format "{{.Names}}: {{.RestartCount}} restarts" >> $LOG_FILE

echo -e "\n===== Logs for Orthanc Servers =====" >> $LOG_FILE
docker logs --tail 20 orthanc1 >> $LOG_FILE
docker logs --tail 20 orthanc2 >> $LOG_FILE
docker logs --tail 20 orthanc3 >> $LOG_FILE

echo "Monitoring complete. Data saved to $LOG_FILE"

