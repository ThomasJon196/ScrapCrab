# Monitoring

Grafana Credentials:

user: admin
pw  : ****


__Grafana create dashboard__


Query for CPU usage in %

```sql
100 - (avg(irate(node_cpu_seconds_total{mode="idle"}[30m])) * 100)
```